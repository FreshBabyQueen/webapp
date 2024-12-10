USE movie_app;

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user'
);

-- Movies Table
CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    director VARCHAR(255) NOT NULL,
    writers VARCHAR(255),
    stars VARCHAR(255),
    image_path VARCHAR(255),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Add the columns back
-- ALTER TABLE movies ADD COLUMN trailer_url VARCHAR(255);
-- ALTER TABLE movies ADD COLUMN genre VARCHAR(50) NOT NULL;
-- ALTER TABLE movies ADD COLUMN attribution VARCHAR(255);
-- ALTER TABLE movies ADD COLUMN user_id INT NOT NULL;




