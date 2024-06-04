# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3  # Import sqlite3 for database operations

# Create a Flask application instance
app = Flask(__name__)
# Set a secret key for securely signing the session cookie
app.secret_key = 'your_secret_key'

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')  # Connect to the 'users.db' SQLite database
    conn.row_factory = sqlite3.Row  # Enable accessing rows as dictionaries
    return conn  # Return the connection object

# Route for the root URL
@app.route('/')
def index():
    return redirect(url_for('login'))  # Redirect to the login page

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # If the request method is POST, handle the form submission
        username = request.form['username']  # Get the username from the form
        password = request.form['password']  # Get the password from the form
        conn = get_db_connection()  # Get a database connection
        # Query the database for a user with the given username and password
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()  # Close the database connection
        if user:  # If a matching user is found
            session['username'] = username  # Store the username in the session
            session['firstname'] = user['firstname']  # Store the user's first name in the session
            return redirect(url_for('dashboard'))  # Redirect to the dashboard page
        else:
            return 'Invalid username or password'  # Return an error message if login fails
    return render_template('login.html')  # Render the login template for GET requests

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  # If the request method is POST, handle the form submission
        username = request.form['username']  # Get the username from the form
        password = request.form['password']  # Get the password from the form
        firstname = request.form['firstname']  # Get the first name from the form
        conn = get_db_connection()  # Get a database connection
        # Insert the new user into the database
        conn.execute('INSERT INTO users (username, password, firstname) VALUES (?, ?, ?)', (username, password, firstname))
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection
        return redirect(url_for('login'))  # Redirect to the login page
    return render_template('register.html')  # Render the register template for GET requests

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    if 'username' in session:  # Check if the user is logged in
        return render_template('dashboard.html', firstname=session['firstname'])  # Render the dashboard template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the sessions page
@app.route('/sessions')
def sessions():
    if 'username' in session:  # Check if the user is logged in
        return render_template('sessions.html', firstname=session['firstname'])  # Render the sessions template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the profile page
@app.route('/profile')
def profile():
    if 'username' in session:  # Check if the user is logged in
        return render_template('profile.html', firstname=session['firstname'])  # Render the profile template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the analytics page
@app.route('/analytics')
def analytics():
    if 'username' in session:  # Check if the user is logged in
        return render_template('analytics.html', firstname=session['firstname'])  # Render the analytics template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the questionnaire page
@app.route('/questionnaire')
def questionnaire():
    if 'username' in session:  # Check if the user is logged in
        return render_template('questionnaire.html', firstname=session['firstname'])  # Render the questionnaire template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the integrations page
@app.route('/integrations')
def integrations():
    if 'username' in session:  # Check if the user is logged in
        return render_template('integrations.html', firstname=session['firstname'])  # Render the integrations template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the settings page
@app.route('/settings')
def settings():
    if 'username' in session:  # Check if the user is logged in
        return render_template('settings.html', firstname=session['firstname'])  # Render the settings template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the FAQs page
@app.route('/faqs')
def faqs():
    if 'username' in session:  # Check if the user is logged in
        return render_template('faqs.html', firstname=session['firstname'])  # Render the FAQs template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the support page
@app.route('/support')
def support():
    if 'username' in session:  # Check if the user is logged in
        return render_template('support.html', firstname=session['firstname'])  # Render the support template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for the feedback page
@app.route('/feedback')
def feedback():
    if 'username' in session:  # Check if the user is logged in
        return render_template('feedback.html', firstname=session['firstname'])  # Render the feedback template
    return redirect(url_for('login'))  # Redirect to the login page if not logged in

# Route for logging out
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)  # Remove the username from the session
    session.pop('firstname', None)  # Remove the first name from the session
    return redirect(url_for('login'))  # Redirect to the login page

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask application on all network interfaces (0.0.0.0) and port 5000