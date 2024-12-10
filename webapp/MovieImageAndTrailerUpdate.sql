Use movie_app;

SET SQL_SAFE_UPDATES = 0;

UPDATE movies SET image_path = 'uploads/Friday The 13th.jpg' WHERE title = 'Friday The 13th';
UPDATE movies SET image_path = 'uploads/Halloween-1978.jpg' WHERE title = 'Halloween';
UPDATE movies SET image_path = 'uploads/Dr Strange.jpg' WHERE title = 'Dr Strange Multiverse of Madness';
UPDATE movies SET image_path = 'uploads/Moonfall.jpg' WHERE title = 'Moonfall';
UPDATE movies SET image_path = 'uploads/Death on the Nile.jpg' WHERE title = 'Death on the Nile';
UPDATE movies SET image_path = 'uploads/Norbit.jpg' WHERE title = 'Norbit';
UPDATE movies SET image_path = 'uploads/The Jacksons.jpeg' WHERE title = 'The Jacksons: An American Dream';
UPDATE movies SET image_path = 'uploads/True Lies.jpeg' WHERE title = 'True Lies';
UPDATE movies SET image_path = 'uploads/The Lion King.jpg' WHERE title = 'The Lion King';

-- Update image paths and trailer URLs for movies
UPDATE movies
SET 
    image_path = 'uploads/Friday The 13th.jpg',
    trailer_url = 'https://www.youtube.com/embed/aDrOvFtzyPQ?t=7s'
WHERE title = 'Friday The 13th';

UPDATE movies
SET 
    image_path = 'uploads/Halloween-1978.jpg',
    trailer_url = 'https://www.youtube.com/embed/oVgtguYmNBg'
WHERE title = 'Halloween';

UPDATE movies
SET 
    image_path = 'uploads/The Jacksons.jpeg',
    trailer_url = 'https://www.youtube.com/embed/Cq5qoF14P-8?t=50s'
WHERE title = 'The Jacksons: An American Dream';

UPDATE movies
SET 
    image_path = 'uploads/Norbit.jpg',
    trailer_url = 'https://www.youtube.com/embed/HFIdZpc2L6w?t=10s'
WHERE title = 'Norbit';

UPDATE movies
SET 
    image_path = 'uploads/True Lies.jpeg',
    trailer_url = 'https://www.youtube.com/embed/Qw4hz62r-Kk?t=19s'
WHERE title = 'True Lies';

UPDATE movies
SET 
    image_path = 'uploads/The Lion King.jpg',
    trailer_url = 'https://www.youtube.com/embed/eHcZlPpNt0Q'
WHERE title = 'The Lion King';

UPDATE movies
SET 
    image_path = 'uploads/Dr Strange.jpg',
    trailer_url = 'https://www.youtube.com/embed/aWzlQ2N6qqg'
WHERE title = 'Dr Strange Multiverse of Madness';

UPDATE movies
SET 
    image_path = 'uploads/Moonfall.jpg',
    trailer_url = 'https://www.youtube.com/embed/V4F-8cSirJA'
WHERE title = 'Moonfall';

UPDATE movies
SET 
    image_path = 'uploads/Death on the Nile.jpg',
    trailer_url = 'https://www.youtube.com/embed/dZRqB0JLizw'
WHERE title = 'Death on the Nile';

-- Attributes
UPDATE movies
SET attribution = 'https://cdn.seat42f.com/wp-content/uploads/2022/06/02134631/Doctor-Strange-in-the-Multiverse-of-Madness-Disney-Poster.jpg; https://www.youtube.com/embed/awzlQ2N6qqg'
WHERE title = 'Dr Strange Multiverse of Madness';

UPDATE movies
SET attribution = 'https://lionsgate.brightspotcdn.com/99/bb/7a9190fb4a88887c221a242af617/moonfall-bg-own.jpg; https://www.youtube.com/embed/V4F-8cSirJA'
WHERE title = 'Moonfall';

UPDATE movies
SET attribution = 'https://www.themoviedb.org/t/p/original/oq35ZpGaOcaYbl2APAW1ivElM2s.jpg; https://www.youtube.com/embed/dZRqB0JLizw'
WHERE title = 'Death on the Nile';

SET SQL_SAFE_UPDATES = 1;
