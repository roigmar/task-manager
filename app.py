from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_connection, init_db

app = Flask(__name__)
app.secret_key = 'clave-secreta-cambiar-en-produccion'

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('tasks'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        conn = get_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                (username, email, password_hash)
            )
            conn.commit()
            flash('Cuenta creada exitosamente. Iniciá sesión.', 'success')
            return redirect(url_for('login'))
        except Exception:
            flash('El usuario o email ya existe.', 'error')
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('tasks'))
        else:
            flash('Email o contraseña incorrectos.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/tasks')
def tasks():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_connection()
    user_tasks = conn.execute(
        'SELECT * FROM tasks WHERE user_id = ? ORDER BY created_at DESC',
        (session['user_id'],)
    ).fetchall()
    conn.close()

    return render_template('tasks.html', username=session['username'], tasks=user_tasks)


@app.route('/tasks/new', methods=['GET', 'POST'])
def new_task():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']

        conn = get_connection()
        conn.execute(
            'INSERT INTO tasks (user_id, title, description, priority) VALUES (?, ?, ?, ?)',
            (session['user_id'], title, description, priority)
        )
        conn.commit()
        conn.close()
        flash('Tarea creada.', 'success')
        return redirect(url_for('tasks'))

    return render_template('new_task.html')


@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_connection()
    task = conn.execute(
        'SELECT * FROM tasks WHERE id = ? AND user_id = ?',
        (task_id, session['user_id'])
    ).fetchone()

    if task:
        new_status = 0 if task['completed'] else 1
        conn.execute(
            'UPDATE tasks SET completed = ? WHERE id = ?',
            (new_status, task_id)
        )
        conn.commit()
    conn.close()
    return redirect(url_for('tasks'))


@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_connection()
    conn.execute(
        'DELETE FROM tasks WHERE id = ? AND user_id = ?',
        (task_id, session['user_id'])
    )
    conn.commit()
    conn.close()
    flash('Tarea eliminada.', 'success')
    return redirect(url_for('tasks'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

