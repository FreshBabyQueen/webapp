SELECT 
    movies.id AS movie_id,
    movies.title,
    movies.year,
    movies.director,
    movies.writers,
    movies.stars,
    movies.image_path,
    movies.trailer_url,
    movies.genre,
    movies.attribution,
    movies.user_id,
    users.username AS user_name
FROM 
    movies
JOIN 
    users
ON 
    movies.user_id = users.id;
