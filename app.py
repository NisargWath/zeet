from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)




conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the "users" table if it does not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL,
                   description TEXT NOT NULL)''')

conn.commit()
cursor.close()
conn.close()



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    # Extract form data
    name = request.form['name']
    email = request.form['email']
    description = request.form['description']

    # Insert data into database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, description) VALUES (?, ?, ?)", (name, email, description))
    conn.commit()
    cursor.close()
    conn.close()
    
    
    


    # Return success message
    return render_template('index.html')
    

@app.route('/event') 
def events():
    return render_template('blogs.html')

@app.route('/team')
def gallery():
    return render_template('gallery.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/send', methods=['POST'])
def login_form():
    # Extract form data
    
    
    admin = request.form['admin']
    password = request.form['password']
    
    if admin  == "admin1234":
        if password == "admin@123##":
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return render_template('admin.html',rows=rows)
        
        
        
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")