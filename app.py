from flask import Flask, request, redirect, url_for, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "mysecretkey123"

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
        welcome = f"<span class='text-warning'>Welcome, {user}!</span>"
        logout_btn = '<a class="nav-link text-white" href="/logout">Logout</a>'
    else:
        welcome = ""
        logout_btn = ""

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AnimeHub - Anime, Manga & Manhwa</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #0f0f1a; color: white; }}
            .navbar {{ background-color: #1a1a2e !important; }}
            .hero {{
                background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                            url('https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1200') center/cover;
                padding: 100px 0;
                text-align: center;
            }
            .card {{
                background-color: #1a1a2e;
                border: none;
                transition: transform 0.3s;
            }
            .card:hover {{ transform: translateY(-10px); }}
            .section-title {{ color: #e94560; margin-bottom: 30px; }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand fw-bold" href="/">AnimeHub</a>
                <div class="d-flex gap-3">
                    <a class="nav-link text-white" href="/">Home</a>
                    <a class="nav-link text-white" href="/anime">Anime</a>
                    <a class="nav-link text-white" href="/manga">Manga</a>
                    <a class="nav-link text-white" href="/manhwa">Manhwa</a>
                    <a class="nav-link text-white" href="/contact">Contact</a>
                    <a class="nav-link text-white" href="/login">Login</a>
                    <a class="nav-link text-white" href="/signup">Signup</a>
                    {logout_btn}
                </div>
            </div>
        </nav>

        <div class="hero">
            <div class="container">
                <h1 class="display-3 fw-bold">Welcome to AnimeHub</h1>
                <p class="lead">Your ultimate destination for Anime, Manga & Manhwa</p>
                {welcome}
                <div class="mt-4">
                    <a href="/anime" class="btn btn-danger btn-lg me-2">Explore Anime</a>
                    <a href="/manga" class="btn btn-outline-light btn-lg">Explore Manga</a>
                </div>
            </div>
        </div>

        <div class="container my-5">
            <h2 class="text-center section-title">Popular Categories</h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card text-white h-100">
                        <div class="card-body text-center p-4">
                            <h3>Anime</h3>
                            <p>Watch and discover the best anime series and movies.</p>
                            <a href="/anime" class="btn btn-danger">View Anime</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white h-100">
                        <div class="card-body text-center p-4">
                            <h3>Manga</h3>
                            <p>Read popular Japanese manga online.</p>
                            <a href="/manga" class="btn btn-danger">View Manga</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white h-100">
                        <div class="card-body text-center p-4">
                            <h3>Manhwa</h3>
                            <p>Explore Korean manhwa and webtoons.</p>
                            <a href="/manhwa" class="btn btn-danger">View Manhwa</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/anime')
def anime():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Anime - AnimeHub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>body { background-color: #0f0f1a; color: white; } .navbar { background-color: #1a1a2e !important; }</style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand fw-bold" href="/">AnimeHub</a>
                <div class="d-flex gap-3">
                    <a class="nav-link text-white" href="/">Home</a>
                    <a class="nav-link text-white" href="/anime">Anime</a>
                    <a class="nav-link text-white" href="/manga">Manga</a>
                    <a class="nav-link text-white" href="/manhwa">Manhwa</a>
                </div>
            </div>
        </nav>
        <div class="container my-5 text-center">
            <h1 class="text-danger">Anime Section</h1>
            <p class="lead">Yahaan aap popular anime list add kar sakte hain.</p>
            <p>(Abhi basic page hai. Baad mein cards aur details add karenge.)</p>
            <a href="/" class="btn btn-outline-light mt-3">Back to Home</a>
        </div>
    </body>
    </html>
    """

@app.route('/manga')
def manga():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Manga - AnimeHub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>body { background-color: #0f0f1a; color: white; } .navbar { background-color: #1a1a2e !important; }</style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand fw-bold" href="/">AnimeHub</a>
                <div class="d-flex gap-3">
                    <a class="nav-link text-white" href="/">Home</a>
                    <a class="nav-link text-white" href="/anime">Anime</a>
                    <a class="nav-link text-white" href="/manga">Manga</a>
                    <a class="nav-link text-white" href="/manhwa">Manhwa</a>
                </div>
            </div>
        </nav>
        <div class="container my-5 text-center">
            <h1 class="text-danger">Manga Section</h1>
            <p class="lead">Yahaan popular manga list aayegi.</p>
            <a href="/" class="btn btn-outline-light mt-3">Back to Home</a>
        </div>
    </body>
    </html>
    """

@app.route('/manhwa')
def manhwa():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Manhwa - AnimeHub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>body { background-color: #0f0f1a; color: white; } .navbar { background-color: #1a1a2e !important; }</style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand fw-bold" href="/">AnimeHub</a>
                <div class="d-flex gap-3">
                    <a class="nav-link text-white" href="/">Home</a>
                    <a class="nav-link text-white" href="/anime">Anime</a>
                    <a class="nav-link text-white" href="/manga">Manga</a>
                    <a class="nav-link text-white" href="/manhwa">Manhwa</a>
                </div>
            </div>
        </nav>
        <div class="container my-5 text-center">
            <h1 class="text-danger">Manhwa Section</h1>
            <p class="lead">Yahaan Korean Manhwa aur Webtoons aayenge.</p>
            <a href="/" class="btn btn-outline-light mt-3">Back to Home</a>
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
            f.write(f"Time: {datetime.now()}\nName: {name}\nMessage: {message}\n{'-'*40}\n")
        return f"""
        <div style="background:#0f0f1a;color:white;min-height:100vh;text-align:center;padding-top:100px;">
            <h2>Thank You {name}!</h2>
            <p>Aapka message save ho gaya.</p>
            <a href="/" style="color:#e94560;">Home par wapas jayein</a>
        </div>
        """
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contact - AnimeHub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>body{background:#0f0f1a;color:white;} .navbar{background:#1a1a2e!important;}</style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand fw-bold" href="/">AnimeHub</a>
            </div>
        </nav>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card bg-dark text-white">
                        <div class="card-body">
                            <h3 class="text-center">Contact Us</h3>
                            <form method="POST">
                                <input type="text" name="name" class="form-control mb-3" placeholder="Aapka Naam" required>
                                <textarea name="message" class="form-control mb-3" rows="4" placeholder="Message" required></textarea>
                                <button class="btn btn-danger w-100">Submit</button>
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
        <title>Signup - AnimeHub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>body{{background:#0f0f1a;color:white;}}</style>
    </head>
    <body>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-5">
                    <div class="card bg-dark text-white">
                        <div class="card-body">
                            <h3 class="text-center">Signup</h3>
                            {message}
                            <form method="POST">
                                <input type="text" name="username" class="form-control mb-3" placeholder="Username" required>
                                <input type="password" name="password" class="form-control mb-3" placeholder="Password" required>
                                <button class="btn btn-danger w-100">Signup</button>
                            </form>
                            <p class="mt-3 text-center">Already have account? <a href="/login" class="text-warning">Login</a></p>
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
        <title>Login - AnimeHub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>body{{background:#0f0f1a;color:white;}}</style>
    </head>
    <body>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-5">
                    <div class="card bg-dark text-white">
                        <div class="card-body">
                            <h3 class="text-center">Login</h3>
                            {message}
                            <form method="POST">
                                <input type="text" name="username" class="form-control mb-3" placeholder="Username" required>
                                <input type="password" name="password" class="form-control mb-3" placeholder="Password" required>
                                <button class="btn btn-danger w-100">Login</button>
                            </form>
                            <p class="mt-3 text-center">New user? <a href="/signup" class="text-warning">Signup</a></p>
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
