from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='testdb'
    )

# Create table if not exists
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL
        )
    ''')
    # Insert sample data
    cursor.execute("INSERT IGNORE INTO users (username, password) VALUES ('admin', 'admin123')")
    cursor.execute("INSERT IGNORE INTO users (username, password) VALUES ('user1', 'password1')")
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # VULNERABLE CODE - Direct string concatenation
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # This is vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if user:
        return f"Welcome {user[1]}! Login successful."
    else:
        return "Invalid credentials!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)