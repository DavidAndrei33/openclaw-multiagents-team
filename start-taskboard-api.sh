#!/bin/bash
# Start Taskboard Backend API
cd "$(dirname "$0")/taskboard"
echo "🚀 Starting Taskboard Backend API..."
echo "📊 Dashboard: http://localhost:5000"
echo "📁 API Docs: http://localhost:5000/api/data"
echo ""
echo "Press Ctrl+C to stop"
echo ""
python3 api.py