from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# File to store todos
TODOS_FILE = 'todos.json'

def load_todos():
    """Load todos from JSON file"""
    if os.path.exists(TODOS_FILE):
        try:
            with open(TODOS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_todos(todos):
    """Save todos to JSON file"""
    with open(TODOS_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

@app.route('/')
def index():
    """Main page showing all todos"""
    todos = load_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    """Add a new todo"""
    text = request.form.get('text', '').strip()
    
    if not text:
        return redirect(url_for('index'))
    
    todos = load_todos()
    
    new_todo = {
        'id': len(todos) + 1,
        'text': text,
        'completed': False,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    todos.append(new_todo)
    save_todos(todos)
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    """Toggle todo completion status"""
    todos = load_todos()
    
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            todo['updated_at'] = datetime.now().isoformat()
            save_todos(todos)
            break
    
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Delete a todo"""
    todos = load_todos()
    
    todos = [todo for todo in todos if todo['id'] != todo_id]
    
    # Reassign IDs to maintain sequential numbering
    for i, todo in enumerate(todos, 1):
        todo['id'] = i
    
    save_todos(todos)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
