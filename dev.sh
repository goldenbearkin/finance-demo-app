#!/bin/bash

# Function to handle cleanup
cleanup() {
    echo "Cleaning up..."
    kill $FRONTEND_PID $BACKEND_PID 2>/dev/null
    exit 0
}

# Set up trap to catch Ctrl+C
trap cleanup SIGINT

# Start backend
echo "Starting backend..."
cd backend
rm -rf ./sqlite.db
uv run fastapi dev &
BACKEND_PID=$!

# Start frontend
echo "Starting frontend..."
cd ../frontend
npm run dev &
FRONTEND_PID=$!

echo "Development servers started!"
echo "Frontend: http://localhost:5173"
echo "Backend: http://localhost:8000"
echo "Swagger UI: http://localhost:8000/docs"
echo "Press Ctrl+C to stop both servers"

# Wait for both processes
wait $FRONTEND_PID $BACKEND_PID 