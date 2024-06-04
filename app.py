from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['username'] = username
            session['firstname'] = user['firstname']
            return redirect(url_for('welcome'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password, firstname) VALUES (?, ?, ?)', (username, password, firstname))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        firstname = session['firstname']
        return render_template('welcome.html', firstname=firstname)
    return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    session.pop('firstname', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
