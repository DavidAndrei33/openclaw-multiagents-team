#!/bin/bash
# Script pentru a crea repo-ul openclaw-multiagents-team pe GitHub

REPO_NAME="openclaw-multiagents-team"
REPO_DESC="OpenClaw Multi-Agent Team Configuration - 9 AI agents for QuickDelivery project"

echo "🚀 Creare repository GitHub: $REPO_NAME"
echo ""

# Verifică dacă există gh CLI
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI (gh) detectat"
    
    # Creare repo
    gh repo create "$REPO_NAME" --public --description "$REPO_DESC" --source=. --remote=origin --push
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Repository creat cu succes!"
        echo "🌐 URL: https://github.com/david3366/$REPO_NAME"
    else
        echo "❌ Eroare la crearea repository-ului"
        exit 1
    fi
else
    echo "⚠️  GitHub CLI (gh) nu este instalat"
    echo ""
    echo "Te rog să creezi manual repository-ul:"
    echo "1. Mergi pe https://github.com/new"
    echo "2. Numele repository-ului: $REPO_NAME"
    echo "3. Descriere: $REPO_DESC"
    echo "4. Alege 'Public' sau 'Private'"
    echo "5. Click 'Create repository'"
    echo ""
    echo "După ce creezi repo-ul, rulează:"
    echo "  cd /tmp/openclaw-multiagents-team"
    echo "  git remote add origin https://github.com/david3366/$REPO_NAME.git"
    echo "  git branch -M main"
    echo "  git push -u origin main"
fi
