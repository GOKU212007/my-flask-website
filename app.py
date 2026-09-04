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
            body {{ background-color: #0b0b13; color: white; font-family: 'Segoe UI', sans-serif; }}
            .navbar {{ background-color: #12121f !important; }}
            .hero {{
                background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
                            url('https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1400') center/cover;
                padding: 110px 0;
                text-align: center;
            }}
            .card {{
                background-color: #16162a;
                border: none;
                border-radius: 14px;
                transition: all 0.3s ease;
            }}
            .card:hover {{
                transform: translateY(-8px);
                box-shadow: 0 12px 25px rgba(233, 69, 96, 0.25);
            }}
            .section-title {{ color: #e94560; margin-bottom: 30px; font-weight: 600; }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand fw-bold fs-4" href="/">AnimeHub</a>
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
                <h1 class="display-3 fw-bold mb-3">Welcome to AnimeHub</h1>
                <p class="lead mb-4">Your ultimate destination for Anime, Manga & Manhwa</p>
                {welcome}
                <div class="mt-3">
                    <a href="/anime" class="btn btn-danger btn-lg me-2 px-4">Explore Anime</a>
                    <a href="/manga" class="btn btn-outline-light btn-lg px-4">Explore Manga</a>
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
                            <p class="text-secondary">Watch and discover the best anime series and movies.</p>
                            <a href="/anime" class="btn btn-danger mt-2">View Anime</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white h-100">
                        <div class="card-body text-center p-4">
                            <h3>Manga</h3>
                            <p class="text-secondary">Read popular Japanese manga online.</p>
                            <a href="/manga" class="btn btn-danger mt-2">View Manga</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white h-100">
                        <div class="card-body text-center p-4">
                            <h3>Manhwa</h3>
                            <p class="text-secondary">Explore Korean manhwa and webtoons.</p>
                            <a href="/manhwa" class="btn btn-danger mt-2">View Manhwa</a>
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
        <style>
            body {
                background-color: #0b0b13;
                color: white;
                font-family: 'Segoe UI', sans-serif;
            }
            .navbar {
                background-color: #12121f !important;
            }
            .anime-card {
                background-color: #16162a;
                border-radius: 14px;
                overflow: hidden;
                transition: all 0.3s ease;
                height: 100%;
            }
            .anime-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(233, 69, 96, 0.3);
            }
            .anime-img {
                height: 320px;
                width: 100%;
                object-fit: cover;
            }
            .anime-info {
                padding: 16px;
            }
            .anime-title {
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 4px;
            }
            .anime-genre {
                font-size: 0.85rem;
                color: #aaa;
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand fw-bold fs-4" href="/">AnimeHub</a>
                <div class="d-flex gap-3">
                    <a class="nav-link text-white" href="/">Home</a>
                    <a class="nav-link text-white" href="/anime">Anime</a>
                    <a class="nav-link text-white" href="/manga">Manga</a>
                    <a class="nav-link text-white" href="/manhwa">Manhwa</a>
                </div>
            </div>
        </nav>

        <div class="container my-5">
            <h1 class="text-center mb-5" style="color: #e94560; font-weight: 700;">Popular Anime</h1>
            
            <div class="row g-4">

                <div class="col-6 col-md-3">
                    <div class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/13/17405.jpg" class="anime-img" alt="Death Note">
                        <div class="anime-info">
                            <div class="anime-title">Death Note</div>
                            <div class="anime-genre">Mystery • Thriller</div>
                        </div>
                    </div>
                </div>

                <div class="col-6 col-md-3">
                    <div class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/10/47347.jpg" class="anime-img" alt="Naruto">
                        <div class="anime-info">
                            <div class="anime-title">Naruto</div>
                            <div class="anime-genre">Action • Adventure</div>
                        </div>
                    </div>
                </div>

                <div class="col-6 col-md-3">
                    <div class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/1208/94745.jpg" class="anime-img" alt="One Piece">
                        <div class="anime-info">
                            <div class="anime-title">One Piece</div>
                            <div class="anime-genre">Adventure • Fantasy</div>
                        </div>
                    </div>
                </div>

                <div class="col-6 col-md-3">
                    <div class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/1286/99889.jpg" class="anime-img" alt="Jujutsu Kaisen">
                        <div class="anime-info">
                            <div class="anime-title">Jujutsu Kaisen</div>
                            <div class="anime-genre">Action • Dark Fantasy</div>
                        </div>
                    </div>
                </div>

                <div class="col-6 col-md-3">
                    <div class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/1517/100633.jpg" class="anime-img" alt="Demon Slayer">
                        <div class="anime-info">
                            <div class="anime-title">Demon Slayer</div>
                            <div class="anime-genre">Action • Supernatural</div>
                        </div>
                    </div>
                </div>

                <div class="col-6 col-md-3">
                    <div class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/5/73199.jpg" class="anime-img" alt="Attack on Titan">
                        <div class="anime-info">
                            <div class="anime-title">Attack on Titan</div>
                            <div class="anime-genre">Action • Drama</div>
                        </div>
                    </div>
                </div>

                <div class="col-6 col-md-3">
                    <div class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/11/39717.jpg" class="anime-img" alt="Hunter x Hunter">
                        <div class="anime-info">
                            <div class="anime-title">Hunter x Hunter</div>
                            <div class="anime-genre">Adventure • Fantasy</div>
                        </div>
                    </div>
                </div>

                <div class="col-6 col-md-3">
                    <div class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/3/72046.jpg" class="anime-img" alt="Tokyo Ghoul">
                        <div class="anime-info">
                            <div class="anime-title">Tokyo Ghoul</div>
                            <div class="anime-genre">Action • Horror</div>
                        </div>
                    </div>
                </div>

            </div>
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
        <style>
            body { background-color: #0b0b13; color: white; }
            .navbar { background-color: #12121f !important; }
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
                </div>
            </div>
        </nav>
        <div class="container my-5 text-center">
            <h1 style="color:#e94560;">Manga Section</h1>
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
        <style>
            body { background-color: #0b0b13; color: white; }
            .navbar { background-color: #12121f !important; }
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
                </div>
            </div>
        </nav>
        <div class="container my-5 text-center">
            <h1 style="color:#e94560;">Manhwa Section</h1>
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
        <div style="background:#0b0b13;color:white;min-height:100vh;text-align:center;padding-top:100px;">
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
        <style>
            body { background-color: #0b0b13; color: white; }
            .navbar { background-color: #12121f !important; }
        </style>
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
        <style>
            body {{ background-color: #0b0b13; color: white; }}
        </style>
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
        <style>
            body {{ background-color: #0b0b13; color: white; }}
        </style>
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
