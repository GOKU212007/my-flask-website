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
@app.route('/')
@app.route('/')
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
            body {{
                background-color: #0b0b13;
                color: white;
                font-family: 'Segoe UI', sans-serif;
            }}
            .navbar {{
                background-color: #12121f !important;
            }}
            .hero {{
                background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
                            url('https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1400') center/cover;
                padding: 110px 0;
                text-align: center;
            }}
            .hero h1 {{
                font-size: 3rem;
                font-weight: 700;
                margin-bottom: 15px;
            }}
            .hero p {{
                font-size: 1.15rem;
                color: #ccc;
                margin-bottom: 25px;
            }}
            .search-box {{
                max-width: 500px;
                margin: 0 auto 25px auto;
            }}
            .search-box input {{
                background-color: #1a1a2e;
                border: 1px solid #333;
                color: white;
                padding: 12px 18px;
                border-radius: 8px 0 0 8px;
            }}
            .search-box input::placeholder {{
                color: #888;
            }}
            .search-box button {{
                background-color: #e94560;
                border: none;
                color: white;
                padding: 12px 20px;
                border-radius: 0 8px 8px 0;
            }}
            .card {{
                background-color: #16162a;
                border: none;
                border-radius: 16px;
                transition: all 0.3s ease;
                height: 100%;
            }}
            .card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(233, 69, 96, 0.3);
            }}
            .section-title {{
                color: #e94560;
                font-weight: 700;
                margin-bottom: 40px;
            }}
            .btn-danger {{
                background-color: #e94560;
                border: none;
            }}
            .btn-danger:hover {{
                background-color: #d63850;
            }}
            footer {{
                background-color: #12121f;
                padding: 30px 0;
                margin-top: 60px;
                text-align: center;
                color: #aaa;
                font-size: 0.9rem;
            }}
            footer a {{
                color: #e94560;
                text-decoration: none;
                margin: 0 10px;
            }}
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
                <h1>Welcome to AnimeHub</h1>
                <p>Your ultimate destination for Anime, Manga & Manhwa</p>
                {welcome}

                <div class="search-box">
                    <form action="/search" method="GET" class="d-flex">
                        <input type="text" name="q" class="form-control" placeholder="Search Anime, Manga, Manhwa..." required>
                        <button type="submit" class="btn">Search</button>
                    </form>
                </div>

                <div class="mt-2">
                    <a href="/anime" class="btn btn-danger btn-lg me-2 px-4">Explore Anime</a>
                    <a href="/manga" class="btn btn-outline-light btn-lg px-4">Explore Manga</a>
                </div>
            </div>
        </div>

        <div class="container my-5">
            <h2 class="text-center section-title">Popular Categories</h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card text-white">
                        <div class="card-body text-center p-5">
                            <h3 class="mb-3">Anime</h3>
                            <p class="text-secondary mb-4">Watch and discover the best anime series and movies from Japan.</p>
                            <a href="/anime" class="btn btn-danger px-4">View Anime</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white">
                        <div class="card-body text-center p-5">
                            <h3 class="mb-3">Manga</h3>
                            <p class="text-secondary mb-4">Read popular Japanese manga online. Classic and new titles.</p>
                            <a href="/manga" class="btn btn-danger px-4">View Manga</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white">
                        <div class="card-body text-center p-5">
                            <h3 class="mb-3">Manhwa</h3>
                            <p class="text-secondary mb-4">Explore Korean manhwa and webtoons with amazing stories.</p>
                            <a href="/manhwa" class="btn btn-danger px-4">View Manhwa</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer>
            <div class="container">
                <p class="mb-2">© 2026 AnimeHub. All rights reserved.</p>
                <div>
                    <a href="/">Home</a>
                    <a href="/anime">Anime</a>
                    <a href="/manga">Manga</a>
                    <a href="/manhwa">Manhwa</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """
@app.route('/anime')
@app.route('/anime')
@app.route('/anime')
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
                text-decoration: none;
                color: white;
                display: block;
            }
            .anime-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(233, 69, 96, 0.3);
                color: white;
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
            footer {
                background-color: #12121f;
                padding: 30px 0;
                margin-top: 60px;
                text-align: center;
                color: #aaa;
                font-size: 0.9rem;
            }
            footer a {
                color: #e94560;
                text-decoration: none;
                margin: 0 10px;
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
                    <a href="/details/Naruto" class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/10/47347.jpg" class="anime-img" alt="Naruto">
                        <div class="anime-info">
                            <div class="anime-title">Naruto</div>
                            <div class="anime-genre">Action • Adventure</div>
                        </div>
                    </a>
                </div>
                <div class="col-6 col-md-3">
                    <a href="/details/One Piece" class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/6/73245.jpg" class="anime-img" alt="One Piece">
                        <div class="anime-info">
                            <div class="anime-title">One Piece</div>
                            <div class="anime-genre">Adventure • Fantasy</div>
                        </div>
                    </a>
                </div>
                <div class="col-6 col-md-3">
                    <a href="/details/Demon Slayer" class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/1286/99889.jpg" class="anime-img" alt="DemonSlayer">
                        <div class="anime-info">
                            <div class="anime-title">DemonSlayer</div>
                            <div class="anime-genre">Action • Supernatural</div>
                        </div>
                    </a>
                </div>
                <div class="col-6 col-md-3">
                    <a href="/details/Jujutsu Kaisen" class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/1171/109222.jpg" class="anime-img" alt="Jujutsu Kaisen">
                        <div class="anime-info">
                            <div class="anime-title">Jujutsu Kaisen</div>
                            <div class="anime-genre">Action • Dark Fantasy</div>
                        </div>
                    </a>
                </div>
                <div class="col-6 col-md-3">
                    <a href="/details/Attack on Titan" class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/5/73199.jpg" class="anime-img" alt="Attack on Titan">
                        <div class="anime-info">
                            <div class="anime-title">Attack on Titan</div>
                            <div class="anime-genre">Action • Drama</div>
                        </div>
                    </a>
                </div>
                <div class="col-6 col-md-3">
                    <a href="/details/Death Note" class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/9/9453.jpg" class="anime-img" alt="Death Note">
                        <div class="anime-info">
                            <div class="anime-title">Death Note</div>
                            <div class="anime-genre">Mystery • Thriller</div>
                        </div>
                    </a>
                </div>
                <div class="col-6 col-md-3">
                    <a href="/details/Hunter x Hunter" class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/1337/99013.jpg" class="anime-img" alt="Hunter x Hunter">
                        <div class="anime-info">
                            <div class="anime-title">Hunter x Hunter</div>
                            <div class="anime-genre">Adventure • Fantasy</div>
                        </div>
                    </a>
                </div>
                <div class="col-6 col-md-3">
                    <a href="/details/Tokyo Ghoul" class="anime-card">
                        <img src="https://cdn.myanimelist.net/images/anime/5/64449.jpg" class="anime-img" alt="Tokyo Ghoul">
                        <div class="anime-info">
                            <div class="anime-title">Tokyo Ghoul</div>
                            <div class="anime-genre">Action • Horror</div>
                        </div>
                    </a>
                </div>
            </div>
        </div>

        <footer>
            <div class="container">
                <p class="mb-2">© 2026 AnimeHub. All rights reserved.</p>
                <div>
                    <a href="/">Home</a>
                    <a href="/anime">Anime</a>
                    <a href="/manga">Manga</a>
                    <a href="/manhwa">Manhwa</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """
@app.route('/manga')
@app.route('/manga')
def manga():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Manga - AnimeHub</title>
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
            .manga-card {
                background-color: #16162a;
                border-radius: 14px;
                overflow: hidden;
                transition: all 0.3s ease;
                height: 100%;
            }
            .manga-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(233, 69, 96, 0.3);
            }
            .manga-img {
                height: 320px;
                width: 100%;
                object-fit: cover;
            }
            .manga-info {
                padding: 16px;
            }
            .manga-title {
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 4px;
            }
            .manga-genre {
                font-size: 0.85rem;
                color: #aaa;
            }
            footer {
                background-color: #12121f;
                padding: 30px 0;
                margin-top: 60px;
                text-align: center;
                color: #aaa;
                font-size: 0.9rem;
            }
            footer a {
                color: #e94560;
                text-decoration: none;
                margin: 0 10px;
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
            <h1 class="text-center mb-5" style="color: #e94560; font-weight: 700;">Popular Manga</h1>
            
            <div class="row g-4">
                <div class="col-6 col-md-3">
                    <div class="manga-card">
                        <img src="https://cdn.myanimelist.net/images/manga/3/55539.jpg" class="manga-img" alt="One Piece">
                        <div class="manga-info">
                            <div class="manga-title">One Piece</div>
                            <div class="manga-genre">Adventure • Fantasy</div>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3">
                    <div class="manga-card">
                        <img src="https://cdn.myanimelist.net/images/manga/2/253146.jpg" class="manga-img" alt="Naruto">
                        <div class="manga-info">
                            <div class="manga-title">Naruto</div>
                            <div class="manga-genre">Action • Adventure</div>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3">
                    <div class="manga-card">
                        <img src="https://cdn.myanimelist.net/images/manga/3/180031.jpg" class="manga-img" alt="Attack on Titan">
                        <div class="manga-info">
                            <div class="manga-title">Attack on Titan</div>
                            <div class="manga-genre">Action • Drama</div>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3">
                    <div class="manga-card">
                        <img src="https://cdn.myanimelist.net/images/manga/1/157931.jpg" class="manga-img" alt="Death Note">
                        <div class="manga-info">
                            <div class="manga-title">Death Note</div>
                            <div class="manga-genre">Mystery • Thriller</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer>
            <div class="container">
                <p class="mb-2">© 2026 AnimeHub. All rights reserved.</p>
                <div>
                    <a href="/">Home</a>
                    <a href="/anime">Anime</a>
                    <a href="/manga">Manga</a>
                    <a href="/manhwa">Manhwa</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """

@app.route('/manhwa')
@app.route('/manhwa')
def manhwa():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Manhwa - AnimeHub</title>
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
            .manhwa-card {
                background-color: #16162a;
                border-radius: 14px;
                overflow: hidden;
                transition: all 0.3s ease;
                height: 100%;
            }
            .manhwa-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(233, 69, 96, 0.3);
            }
            .manhwa-img {
                height: 320px;
                width: 100%;
                object-fit: cover;
            }
            .manhwa-info {
                padding: 16px;
            }
            .manhwa-title {
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 4px;
            }
            .manhwa-genre {
                font-size: 0.85rem;
                color: #aaa;
            }
            footer {
                background-color: #12121f;
                padding: 30px 0;
                margin-top: 60px;
                text-align: center;
                color: #aaa;
                font-size: 0.9rem;
            }
            footer a {
                color: #e94560;
                text-decoration: none;
                margin: 0 10px;
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
            <h1 class="text-center mb-5" style="color: #e94560; font-weight: 700;">Popular Manhwa</h1>
            
            <div class="row g-4">
                <div class="col-6 col-md-3">
                    <div class="manhwa-card">
                        <img src="https://cdn.myanimelist.net/images/manga/3/218851.jpg" class="manhwa-img" alt="Solo Leveling">
                        <div class="manhwa-info">
                            <div class="manhwa-title">Solo Leveling</div>
                            <div class="manhwa-genre">Action • Fantasy</div>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3">
                    <div class="manhwa-card">
                        <img src="https://cdn.myanimelist.net/images/manga/1/157897.jpg" class="manhwa-img" alt="Tower of God">
                        <div class="manhwa-info">
                            <div class="manhwa-title">Tower of God</div>
                            <div class="manhwa-genre">Action • Adventure</div>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3">
                    <div class="manhwa-card">
                        <img src="https://cdn.myanimelist.net/images/manga/2/253146.jpg" class="manhwa-img" alt="The God of High School">
                        <div class="manhwa-info">
                            <div class="manhwa-title">The God of High School</div>
                            <div class="manhwa-genre">Action • Martial Arts</div>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3">
                    <div class="manhwa-card">
                        <img src="https://cdn.myanimelist.net/images/manga/3/180031.jpg" class="manhwa-img" alt="Noblesse">
                        <div class="manhwa-info">
                            <div class="manhwa-title">Noblesse</div>
                            <div class="manhwa-genre">Action • Supernatural</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer>
            <div class="container">
                <p class="mb-2">© 2026 AnimeHub. All rights reserved.</p>
                <div>
                    <a href="/">Home</a>
                    <a href="/anime">Anime</a>
                    <a href="/manga">Manga</a>
                    <a href="/manhwa">Manhwa</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </footer>
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
        <style>body {{ background-color: #0b0b13; color: white; }}</style>
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
        <style>body {{ background-color: #0b0b13; color: white; }}</style>
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
@app.route('/search')
@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    
    all_items = [
        {"title": "Naruto", "type": "Anime", "genre": "Action • Adventure", "img": "https://cdn.myanimelist.net/images/anime/10/47347.jpg"},
        {"title": "One Piece", "type": "Anime", "genre": "Adventure • Fantasy", "img": "https://cdn.myanimelist.net/images/anime/6/73245.jpg"},
        {"title": "Demon Slayer", "type": "Anime", "genre": "Action • Supernatural", "img": "https://cdn.myanimelist.net/images/anime/1286/99889.jpg"},
        {"title": "Jujutsu Kaisen", "type": "Anime", "genre": "Action • Dark Fantasy", "img": "https://cdn.myanimelist.net/images/anime/1171/109222.jpg"},
        {"title": "Attack on Titan", "type": "Anime", "genre": "Action • Drama", "img": "https://cdn.myanimelist.net/images/anime/5/73199.jpg"},
        {"title": "Death Note", "type": "Anime", "genre": "Mystery • Thriller", "img": "https://cdn.myanimelist.net/images/anime/9/9453.jpg"},
        {"title": "Solo Leveling", "type": "Manhwa", "genre": "Action • Fantasy", "img": "https://cdn.myanimelist.net/images/manga/3/218851.jpg"},
        {"title": "Tower of God", "type": "Manhwa", "genre": "Action • Adventure", "img": "https://cdn.myanimelist.net/images/manga/1/157897.jpg"},
        {"title": "One Piece", "type": "Manga", "genre": "Adventure • Fantasy", "img": "https://cdn.myanimelist.net/images/manga/3/55539.jpg"},
        {"title": "Naruto", "type": "Manga", "genre": "Action • Adventure", "img": "https://cdn.myanimelist.net/images/manga/2/253146.jpg"},
    ]
    
    results = [item for item in all_items if query in item["title"].lower()]
    
    results_html = ""
    if results:
        for item in results:
            results_html += f"""
            <div class="col-6 col-md-3 mb-4">
                <div class="card h-100" style="background:#16162a; border:none; border-radius:12px; overflow:hidden;">
                    <img src="{item['img']}" class="card-img-top" style="height:280px; object-fit:cover;" alt="{item['title']}">
                    <div class="card-body">
                        <h6 class="card-title mb-1">{item['title']}</h6>
                        <p class="card-text text-secondary small">{item['type']} • {item['genre']}</p>
                    </div>
                </div>
            </div>
            """
    else:
        results_html = f"<p class='text-center text-secondary'>No results found for '<strong>{query}</strong>'</p>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Search Results - AnimeHub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #0b0b13; color: white; font-family: 'Segoe UI', sans-serif; }}
            .navbar {{ background-color: #12121f !important; }}
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

        <div class="container my-5">
            <h2 class="mb-4" style="color:#e94560;">Search Results for "{query}"</h2>
            <div class="row">
                {results_html}
            </div>
            <div class="text-center mt-4">
                <a href="/" class="btn btn-outline-light">Back to Home</a>
            </div>
        </div>
    </body>
    </html>
    """
@app.route('/details/<name>')
def details(name):
    data = {
        "Naruto": {
            "title": "Naruto",
            "genre": "Action • Adventure",
            "img": "https://cdn.myanimelist.net/images/anime/10/47347.jpg",
            "description": "Naruto Uzumaki is a young ninja who seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village."
        },
        "One Piece": {
            "title": "One Piece",
            "genre": "Adventure • Fantasy",
            "img": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
            "description": "Monkey D. Luffy sets off on an adventure with his pirate crew in search of the One Piece, the greatest treasure in the world."
        },
        "Demon Slayer": {
            "title": "Demon Slayer",
            "genre": "Action • Supernatural",
            "img": "https://cdn.myanimelist.net/images/anime/1286/99889.jpg",
            "description": "Tanjiro Kamado becomes a demon slayer after his family is slaughtered and his sister is turned into a demon."
        },
        "Jujutsu Kaisen": {
            "title": "Jujutsu Kaisen",
            "genre": "Action • Dark Fantasy",
            "img": "https://cdn.myanimelist.net/images/anime/1171/109222.jpg",
            "description": "Yuji Itadori joins a secret organization of Jujutsu Sorcerers to eliminate a powerful Curse named Ryomen Sukuna."
        },
        "Attack on Titan": {
            "title": "Attack on Titan",
            "genre": "Action • Drama",
            "img": "https://cdn.myanimelist.net/images/anime/5/73199.jpg",
            "description": "Humanity lives inside cities surrounded by enormous walls due to the Titans, gigantic humanoid creatures who devour humans."
        },
        "Death Note": {
            "title": "Death Note",
            "genre": "Mystery • Thriller",
            "img": "https://cdn.myanimelist.net/images/anime/9/9453.jpg",
            "description": "A high school student discovers a supernatural notebook that allows him to kill anyone by writing the victim's name."
        },
        "Hunter x Hunter": {
            "title": "Hunter x Hunter",
            "genre": "Adventure • Fantasy",
            "img": "https://cdn.myanimelist.net/images/anime/1337/99013.jpg",
            "description": "Gon Freecss aspires to become a Hunter like his father and embarks on a journey full of challenges and friends."
        },
        "Tokyo Ghoul": {
            "title": "Tokyo Ghoul",
            "genre": "Action • Horror",
            "img": "https://cdn.myanimelist.net/images/anime/5/64449.jpg",
            "description": "Ken Kaneki is transformed into a half-ghoul after an encounter with one, and must learn to live between two worlds."
        }
    }

    item = data.get(name, {
        "title": name,
        "genre": "Unknown",
        "img": "https://via.placeholder.com/300x400?text=No+Image",
        "description": "Details not available."
    })

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{item['title']} - AnimeHub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #0b0b13;
                color: white;
                font-family: 'Segoe UI', sans-serif;
            }}
            .navbar {{
                background-color: #12121f !important;
            }}
            .detail-img {{
                max-height: 450px;
                border-radius: 12px;
                object-fit: cover;
            }}
            footer {{
                background-color: #12121f;
                padding: 30px 0;
                margin-top: 60px;
                text-align: center;
                color: #aaa;
                font-size: 0.9rem;
            }}
            footer a {{
                color: #e94560;
                text-decoration: none;
                margin: 0 10px;
            }}
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
            <div class="row align-items-center">
                <div class="col-md-4 text-center mb-4">
                    <img src="{item['img']}" class="detail-img img-fluid" alt="{item['title']}">
                </div>
                <div class="col-md-8">
                    <h1 style="color:#e94560;">{item['title']}</h1>
                    <p class="text-secondary mb-3">{item['genre']}</p>
                    <p style="font-size:1.1rem; line-height:1.7;">{item['description']}</p>
                    <a href="/anime" class="btn btn-outline-light mt-3">← Back to Anime</a>
                </div>
            </div>
        </div>

        <footer>
            <div class="container">
                <p class="mb-2">© 2026 AnimeHub. All rights reserved.</p>
                <div>
                    <a href="/">Home</a>
                    <a href="/anime">Anime</a>
                    <a href="/manga">Manga</a>
                    <a href="/manhwa">Manhwa</a>
                    <a href="/contact">Contact</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """
