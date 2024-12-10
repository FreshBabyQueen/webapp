from flask import Flask, render_template, request, redirect, session, url_for
from database import DatabaseConnection

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong random secret key

# Database connection
db = DatabaseConnection()

@app.before_request
def clear_session_on_restart():
    """
    Clears session on every new browser session to ensure the user is always
    directed to the home page when reopening the website.
    """
    if not session.get('session_initialized'):
        session.clear()
        session['session_initialized'] = True

@app.route('/')
def index():
    # Always redirect to the register page on visiting the home route
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return "Username and password are required", 400

        try:
            existing_user = db.fetch_one("SELECT * FROM users WHERE username = %s", (username,))
            if existing_user:
                return "Username already exists", 409

            db.execute_query("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            print(f"User {username} successfully registered")
            return redirect(url_for('login'))
        except Exception as e:
            print(f"Registration error: {e}")
            return f"Registration failed: {str(e)}", 500

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            user = db.fetch_one("SELECT * FROM users WHERE username = %s", (username,))
            if user and user['password'] == password:
                session['username'] = user['username']
                session['user_id'] = user['id']
                print(f"User {username} logged in successfully")
                return redirect(url_for('movies'))
            elif user:
                return "Invalid password", 401
            else:
                return "User not found", 404
        except Exception as e:
            print(f"Login error: {e}")
            return f"Login failed: {str(e)}", 500

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    print("User logged out")
    return redirect(url_for('register'))

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    username = session.get('username')
    user_id = session.get('user_id')

    if not username:
        return redirect(url_for('login'))

    selected_genre = request.form.get('genre', 'All')  # Default to 'All'
    try:
        if selected_genre == 'All':
            # Fetch all movies for the user
            movies = db.fetch_all("SELECT * FROM movies WHERE user_id = %s", (user_id,))
        else:
            # Fetch movies filtered by the selected genre
            movies = db.fetch_all("SELECT * FROM movies WHERE user_id = %s AND genre = %s", (user_id, selected_genre))

        for movie in movies:
            movie['image_path'] = movie.get('image_path') or 'uploads/placeholder.png'
            movie['trailer_url'] = movie.get('trailer_url', None)
            movie['genre'] = movie.get('genre', 'Unknown')
            print(f"Image Path: {movie['image_path']} for Movie: {movie['title']}")

    except Exception as e:
        print(f"Error fetching movies: {e}")
        movies = []

    return render_template('movies.html', movies=movies, username=username, selected_genre=selected_genre)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            title = request.form['title']
            year = request.form['year']
            director = request.form['director']
            writers = request.form['writers']
            stars = request.form['stars']
            genre = request.form['genre']
            user_id = session.get('user_id')

            print(f"Received data: {title}, {year}, {director}, {writers}, {stars}, {genre}, {user_id}")

            if not all([title, year, director, writers, stars, genre]):
                return "All fields are required", 400

            db.execute_query(
                """
                INSERT INTO movies (title, year, director, writers, stars, genre, user_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (title, year, director, writers, stars, genre, user_id),
            )
            print(f"Movie '{title}' added successfully")
            return redirect(url_for('movies'))
        except Exception as e:
            print(f"Error adding movie: {e}")
            return f"Failed to add movie: {str(e)}", 500

    return render_template('addmovie.html')



@app.route('/edit_movie/<int:movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    try:
        movie = db.fetch_one("SELECT * FROM movies WHERE id = %s AND user_id = %s", 
                             (movie_id, session['user_id']))
        if not movie:
            return "Movie not found", 404

        if request.method == 'POST':
            title = request.form['title']
            year = request.form['year']
            director = request.form['director']
            writers = request.form['writers']
            stars = request.form['stars']
            trailer_url = request.form.get('trailer_url', None)
            genre = request.form['genre']  # Genre field

            db.execute_query("""
                UPDATE movies
                SET title = %s, year = %s, director = %s, writers = %s, stars = %s, trailer_url = %s, genre = %s
                WHERE id = %s AND user_id = %s
            """, (title, year, director, writers, stars, trailer_url, genre, movie_id, session['user_id']))
            return redirect(url_for('movies'))

        return render_template('editmovie.html', movie=movie)
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    try:
        db.execute_query("DELETE FROM movies WHERE id = %s AND user_id = %s", 
                         (movie_id, session['user_id']))
        return redirect(url_for('movies'))
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
