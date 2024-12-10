SELECT 
    u.username, 
    m.*
FROM 
    users u
JOIN 
    movies m
ON 
    u.id = m.user_id
WHERE 
    u.username = 'Latia M';
