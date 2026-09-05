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
