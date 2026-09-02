from flask import Flask, request, redirect, url_for, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "mysecretkey123"   # Session ke liye zaroori

# Users ko store karne ke liye simple file
USERS_FILE = "users.txt"

def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if "|" in line:
                    username, password = line.strip().split("|")
                    users[username] = password
    return users

def save_user(username, password):
    with open(USERS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username}|{password}\n")

@app.route('/')
def home():
    if "username" in session:
        user = session["username"]
        welcome = f"<h4 class='text-success'>Welcome, {user}!</h4>"
        logout_btn = '<a href="/logout" class="btn btn-danger btn-sm">Logout</a>'
    else:
        welcome = ""
        logout_btn = ""

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Website</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container">
                <a class="navbar-brand" href="/">My Website</a>
                <div>
                    <a class="nav-link text-white d-inline" href="/">Home</a>
                    <a class="nav-link text-white d-inline" href="/about">About</a>
                    <a class="nav-link text-white d-inline" href="/contact">Contact</a>
                    <a class="nav-link text-white d-inline" href="/login">Login</a>
                    <a class="nav-link text-white d-inline" href="/signup">Signup</a>
                    {logout_btn}
                </div>
            </div>
        </nav>

        <div class="container text-center mt-5">
            {welcome}
            <h1 class="display-4 text-primary">Welcome to My First Website</h1>
            <p class="lead">Yeh website Python Flask + Bootstrap se bani hai.</p>
            <a href="/about" class="btn btn-primary btn-lg m-2">About Page</a>
            <a href="/contact" class="btn btn-success btn-lg m-2">Contact Form</a>
        </div>
    </body>
    </html>
    """

@app.route('/about')
def about():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Us</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container">
                <a class="navbar-brand" href="/">My Website</a>
                <div>
                    <a class="nav-link text-white d-inline" href="/">Home</a>
                    <a class="nav-link text-white d-inline" href="/about">About</a>
                    <a class="nav-link text-white d-inline" href="/contact">Contact</a>
                    <a class="nav-link text-white d-inline" href="/login">Login</a>
                    <a class="nav-link text-white d-inline" href="/signup">Signup</a>
                </div>
            </div>
        </nav>

        <div class="container text-center mt-5">
            <h1 class="text-danger">About Us</h1>
            <p class="lead">Yeh mera pehla Python website hai. Main yahaan se web development seekh raha hoon.</p>
            <a href="/" class="btn btn-outline-primary">Home Page par wapas jayein</a>
        </div>
    </body>
    </html>
    """

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        
        with open('messages.txt', 'a', encoding='utf-8') as f:
            f.write(f"Time: {datetime.now()}\n")
            f.write(f"Name: {name}\n")
            f.write(f"Message: {message}\n")
            f.write("-" * 40 + "\n")
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Thank You</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="bg-light">
            <div class="container text-center mt-5">
                <h2 class="text-success">Thank You {name}!</h2>
                <p>Aapka message mil gaya aur save ho gaya.</p>
                <a href="/" class="btn btn-primary">Home Page par wapas jayein</a>
            </div>
        </body>
        </html>
        """
    
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contact Us</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container">
                <a class="navbar-brand" href="/">My Website</a>
                <div>
                    <a class="nav-link text-white d-inline" href="/">Home</a>
                    <a class="nav-link text-white d-inline" href="/about">About</a>
                    <a class="nav-link text-white d-inline" href="/contact">Contact</a>
                    <a class="nav-link text-white d-inline" href="/login">Login</a>
                    <a class="nav-link text-white d-inline" href="/signup">Signup</a>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card shadow">
                        <div class="card-body">
                            <h3 class="card-title text-center">Contact Form</h3>
                            <form method="POST">
                                <div class="mb-3">
                                    <input type="text" name="name" class="form-control" placeholder="Aapka Naam" required>
                                </div>
                                <div class="mb-3">
                                    <textarea name="message" class="form-control" rows="4" placeholder="Aapka Message" required></textarea>
                                </div>
                                <button type="submit" class="btn btn-success w-100">Submit</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = load_users()
        
        if username in users:
            message = "<div class='alert alert-danger'>Username already exists!</div>"
        else:
            save_user(username, password)
            message = "<div class='alert alert-success'>Signup successful! Ab Login karein.</div>"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Signup</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-5">
                    <div class="card shadow">
                        <div class="card-body">
                            <h3 class="card-title text-center">Signup</h3>
                            {message}
                            <form method="POST">
                                <div class="mb-3">
                                    <input type="text" name="username" class="form-control" placeholder="Username" required>
                                </div>
                                <div class="mb-3">
                                    <input type="password" name="password" class="form-control" placeholder="Password" required>
                                </div>
                                <button type="submit" class="btn btn-primary w-100">Signup</button>
                            </form>
                            <p class="mt-3 text-center">Already have account? <a href="/login">Login</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = load_users()
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            message = "<div class='alert alert-danger'>Invalid username or password!</div>"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-5">
                    <div class="card shadow">
                        <div class="card-body">
                            <h3 class="card-title text-center">Login</h3>
                            {message}
                            <form method="POST">
                                <div class="mb-3">
                                    <input type="text" name="username" class="form-control" placeholder="Username" required>
                                </div>
                                <div class="mb-3">
                                    <input type="password" name="password" class="form-control" placeholder="Password" required>
                                </div>
                                <button type="submit" class="btn btn-success w-100">Login</button>
                            </form>
                            <p class="mt-3 text-center">New user? <a href="/signup">Signup</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)