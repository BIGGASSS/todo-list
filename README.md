# Todo List Web App

A simple todo list web application built with Python Flask that stores data persistently in a JSON file.

## Features

- ✅ Add new todos
- ✅ Mark todos as complete/incomplete
- ✅ Delete todos
- ✅ Persistent storage using JSON file
- ✅ Clean and responsive web interface
- ✅ Real-time statistics (total, completed, remaining)

## Installation

1. **Install Python** (3.7 or higher)
2. **Install Flask**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Using the application**:
   - Type a new todo in the input field and click "Add" or press Enter
   - Check/uncheck the checkbox to mark todos as complete/incomplete
   - Click "Delete" to remove a todo

## File Structure

```
todo-list/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # HTML template
├── requirements.txt    # Python dependencies
├── todos.json          # Data storage (created automatically)
└── README.md          # This file
```

## Technical Details

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, Jinja2 templates
- **Data Storage**: JSON file (todos.json)
- **Port**: 5000 (configurable)

## Data Format

Todos are stored in `todos.json` with the following structure:
```json
[
  {
    "id": 1,
    "text": "Buy groceries",
    "completed": false,
    "created_at": "2025-08-01T22:56:45.123456",
    "updated_at": "2025-08-01T22:56:45.123456"
  }
]
```

## Development

To run in development mode with debug enabled:
```bash
python app.py
```

The server will automatically restart when you make changes to the code.

## Production Deployment

For production deployment, use a proper WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
