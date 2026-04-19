#!/bin/bash
# Start taskboard server
cd /workspace/shared
python3 -m http.server 8080 &
echo "🚀 Taskboard server started on http://localhost:8080"
echo "📊 Open: http://localhost:8080/taskboard.html"
echo "💾 Data: /workspace/shared/taskboard/data.json"
echo ""
echo "To stop: kill %1"