#!/usr/bin/env python3
"""
Telegram Notifier for Taskboard
Sends DM notifications to agents when tasks are assigned
"""

import requests
import json
import os
from datetime import datetime

# Bot tokens for each agent (from existing configuration)
AGENT_BOTS = {
    'product-architect': os.getenv('PRODUCT_ARCHITECT_BOT_TOKEN', ''),
    'backend-architect': os.getenv('BACKEND_ARCHITECT_BOT_TOKEN', ''),
    'frontend-architect': os.getenv('FRONTEND_ARCHITECT_BOT_TOKEN', ''),
    'builder-modules': os.getenv('BUILDER_MODULES_BOT_TOKEN', ''),
    'builder-mobile': os.getenv('BUILDER_MOBILE_BOT_TOKEN', ''),
    'reviewer-all': os.getenv('REVIEWER_ALL_BOT_TOKEN', ''),
    'operations-all': os.getenv('OPERATIONS_ALL_BOT_TOKEN', ''),
    'specialists-all': os.getenv('SPECIALISTS_ALL_BOT_TOKEN', '')
}

# Owner Telegram ID for notifications
OWNER_CHAT_ID = os.getenv('OWNER_CHAT_ID', '310970306')

# Webhook URL for callbacks
WEBHOOK_BASE_URL = os.getenv('WEBHOOK_BASE_URL', 'https://your-domain.com/webhook')

class TelegramNotifier:
    def __init__(self):
        self.api_base = "https://api.telegram.org/bot{token}"
    
    def send_task_notification(self, agent_key, task, action='new'):
        """Send task notification to agent"""
        token = AGENT_BOTS.get(agent_key)
        if not token:
            print(f"❌ No bot token for agent: {agent_key}")
            return False
        
        # Get agent info
        agent_name = task.get('agent_name', agent_key.replace('-', ' ').title())
        
        # Build message
        if action == 'new':
            message = self._build_new_task_message(task, agent_name)
        elif action == 'reminder':
            message = self._build_reminder_message(task, agent_name)
        else:
            return False
        
        # Send message with inline keyboard
        return self._send_message(token, task.get('agent_chat_id'), message, task['id'])
    
    def send_completion_notification(self, task, agent_key):
        """Notify owner when task is completed"""
        token = AGENT_BOTS.get('product-architect')  # Use Product-Architect bot
        if not token:
            return False
        
        agent_name = task.get('agent_name', agent_key.replace('-', ' ').title())
        message = f"""✅ *Task Completed*

*Task:* {task['id']} - {task['title']}
*Completed by:* {agent_name}
*Project:* {task.get('project', 'N/A')}

Great work team! 🎉"""
        
        return self._send_simple_message(token, OWNER_CHAT_ID, message)
    
    def _build_new_task_message(self, task, agent_name):
        """Build message for new task notification"""
        priority_emoji = {
            'critical': '🔴',
            'high': '🟠',
            'medium': '🟡',
            'low': '🟢'
        }.get(task.get('priority', 'medium'), '🟡')
        
        description = task.get('description', 'No description')[:100]  # Limit to 100 chars
        if len(task.get('description', '')) > 100:
            description += '...'
        
        return f"""🎯 *New Task Assigned*

*{task['id']}*: {task['title']}

{priority_emoji} *Priority:* {task.get('priority', 'medium').upper()}
📋 *Description:* {description}

Tap "Start Task" to begin working on this task."""
    
    def _build_reminder_message(self, task, agent_name):
        """Build reminder message"""
        return f"""⏰ *Task Reminder*

*{task['id']}*: {task['title']}

This task is still waiting in your queue. 
Please start working on it when ready."""
    
    def _send_message(self, token, chat_id, message, task_id):
        """Send message with inline keyboard"""
        url = f"{self.api_base.format(token=token)}/sendMessage"
        
        # Inline keyboard with actions
        keyboard = {
            "inline_keyboard": [
                [
                    {"text": "🔵 Start Task", "callback_data": f"start:{task_id}"},
                    {"text": "❌ Refuse", "callback_data": f"refuse:{task_id}"}
                ],
                [
                    {"text": "📊 View in Dashboard", "url": f"http://localhost:5000"}
                ]
            ]
        }
        
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
            "reply_markup": json.dumps(keyboard)
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ Notification sent to {chat_id}")
                return True
            else:
                print(f"❌ Failed to send: {response.text}")
                return False
        except Exception as e:
            print(f"❌ Error sending notification: {e}")
            return False
    
    def _send_simple_message(self, token, chat_id, message):
        """Send simple message without keyboard"""
        url = f"{self.api_base.format(token=token)}/sendMessage"
        
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def answer_callback(self, token, callback_query_id, text=None):
        """Answer callback query (button press)"""
        url = f"{self.api_base.format(token=token)}/answerCallbackQuery"
        
        payload = {
            "callback_query_id": callback_query_id
        }
        if text:
            payload["text"] = text
            payload["show_alert"] = False
        
        try:
            requests.post(url, json=payload, timeout=5)
            return True
        except:
            return False

# Singleton instance
notifier = TelegramNotifier()

if __name__ == '__main__':
    # Test
    test_task = {
        'id': 'TASK-001',
        'title': 'Test Task',
        'description': 'This is a test notification',
        'priority': 'high',
        'project': 'quickdelivery',
        'agent_name': 'Backend-Architect',
        'agent_chat_id': OWNER_CHAT_ID  # Use owner for testing
    }
    
    print("Testing Telegram Notifier...")
    result = notifier.send_task_notification('backend-architect', test_task)
    print(f"Result: {result}")
