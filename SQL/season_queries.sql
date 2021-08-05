/* Spring movies */
WITH movie_test AS
(SELECT * FROM netflix_spring)
SELECT "TOTAL", COUNT(show_id)
FROM movie_test
UNION 
SELECT "TV", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%TV%"
UNION 
SELECT "Movies", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Movies%"
UNION 
SELECT "Action & Adventure", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Action & Adventure%"
UNION 
SELECT "Dramas", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Dramas%"
UNION
SELECT "International", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%International%"
UNION
SELECT "Sci-Fi & Fantasy", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Sci-Fi & Fantasy%"
UNION
SELECT "Horror", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Horror%"
UNION
SELECT "Thriller", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Thriller%"
UNION
SELECT "Crime", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Crime%"
UNION
SELECT "Sports", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Sports%"
UNION
SELECT "Documentaries/docuseries", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Documentaries%"
    OR listed_in LIKE "%Docuseries%"
UNION
SELECT "Independent", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Independent%"
UNION
SELECT "Comedies", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Comedies%"
UNION
SELECT "Anime", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Anime%"
UNION
SELECT "Reality TV", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Reality TV%"
UNION
SELECT "Romantic", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Romantic%"
UNION
SELECT "Science & Nature", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Science & Nature%"
UNION
SELECT "Mysteries", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Mysteries%"
UNION
SELECT "Music & Musicals", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Music & Musicals%"
UNION
SELECT "For kids", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Kids%"
    OR listed_in LIKE "%Children"
UNION
SELECT "LGBTQ", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%LGBTQ%"
UNION
SELECT "Teen", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Teen%"
UNION
SELECT "Cult", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Cult%"
UNION
SELECT "Stand-Up Comedy", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Stand-Up Comedy%";

/* Summer movies */
WITH movie_test AS
(SELECT * FROM netflix_summer)
SELECT "TOTAL", COUNT(show_id)
FROM movie_test
UNION 
SELECT "TV", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%TV%"
UNION 
SELECT "Movies", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Movies%"
UNION 
SELECT "Action & Adventure", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Action & Adventure%"
UNION 
SELECT "Dramas", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Dramas%"
UNION
SELECT "International", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%International%"
UNION
SELECT "Sci-Fi & Fantasy", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Sci-Fi & Fantasy%"
UNION
SELECT "Horror", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Horror%"
UNION
SELECT "Thriller", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Thriller%"
UNION
SELECT "Crime", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Crime%"
UNION
SELECT "Sports", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Sports%"
UNION
SELECT "Documentaries/docuseries", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Documentaries%"
    OR listed_in LIKE "%Docuseries%"
UNION
SELECT "Independent", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Independent%"
UNION
SELECT "Comedies", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Comedies%"
UNION
SELECT "Anime", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Anime%"
UNION
SELECT "Reality TV", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Reality TV%"
UNION
SELECT "Romantic", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Romantic%"
UNION
SELECT "Science & Nature", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Science & Nature%"
UNION
SELECT "Mysteries", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Mysteries%"
UNION
SELECT "Music & Musicals", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Music & Musicals%"
UNION
SELECT "For kids", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Kids%"
    OR listed_in LIKE "%Children"
UNION
SELECT "LGBTQ", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%LGBTQ%"
UNION
SELECT "Teen", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Teen%"
UNION
SELECT "Cult", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Cult%"
UNION
SELECT "Stand-Up Comedy", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Stand-Up Comedy%";

/* Fall movies */
WITH movie_test AS
(SELECT * FROM netflix_fall)
SELECT "TOTAL", COUNT(show_id)
FROM movie_test
UNION 
SELECT "TV", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%TV%"
UNION 
SELECT "Movies", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Movies%"
UNION 
SELECT "Action & Adventure", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Action & Adventure%"
UNION 
SELECT "Dramas", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Dramas%"
UNION
SELECT "International", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%International%"
UNION
SELECT "Sci-Fi & Fantasy", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Sci-Fi & Fantasy%"
UNION
SELECT "Horror", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Horror%"
UNION
SELECT "Thriller", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Thriller%"
UNION
SELECT "Crime", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Crime%"
UNION
SELECT "Sports", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Sports%"
UNION
SELECT "Documentaries/docuseries", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Documentaries%"
    OR listed_in LIKE "%Docuseries%"
UNION
SELECT "Independent", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Independent%"
UNION
SELECT "Comedies", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Comedies%"
UNION
SELECT "Anime", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Anime%"
UNION
SELECT "Reality TV", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Reality TV%"
UNION
SELECT "Romantic", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Romantic%"
UNION
SELECT "Science & Nature", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Science & Nature%"
UNION
SELECT "Mysteries", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Mysteries%"
UNION
SELECT "Music & Musicals", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Music & Musicals%"
UNION
SELECT "For kids", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Kids%"
    OR listed_in LIKE "%Children"
UNION
SELECT "LGBTQ", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%LGBTQ%"
UNION
SELECT "Teen", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Teen%"
UNION
SELECT "Cult", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Cult%"
UNION
SELECT "Stand-Up Comedy", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Stand-Up Comedy%";

/* Winter movies */
WITH movie_test AS
(SELECT * FROM netflix_winter)
SELECT "TOTAL", COUNT(show_id)
FROM movie_test
UNION 
SELECT "TV", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%TV%"
UNION 
SELECT "Movies", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Movies%"
UNION 
SELECT "Action & Adventure", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Action & Adventure%"
UNION 
SELECT "Dramas", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Dramas%"
UNION
SELECT "International", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%International%"
UNION
SELECT "Sci-Fi & Fantasy", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Sci-Fi & Fantasy%"
UNION
SELECT "Horror", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Horror%"
UNION
SELECT "Thriller", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Thriller%"
UNION
SELECT "Crime", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Crime%"
UNION
SELECT "Sports", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Sports%"
UNION
SELECT "Documentaries/docuseries", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Documentaries%"
    OR listed_in LIKE "%Docuseries%"
UNION
SELECT "Independent", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Independent%"
UNION
SELECT "Comedies", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Comedies%"
UNION
SELECT "Anime", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Anime%"
UNION
SELECT "Reality TV", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Reality TV%"
UNION
SELECT "Romantic", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Romantic%"
UNION
SELECT "Science & Nature", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Science & Nature%"
UNION
SELECT "Mysteries", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Mysteries%"
UNION
SELECT "Music & Musicals", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Music & Musicals%"
UNION
SELECT "For kids", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Kids%"
    OR listed_in LIKE "%Children"
UNION
SELECT "LGBTQ", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%LGBTQ%"
UNION
SELECT "Teen", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Teen%"
UNION
SELECT "Cult", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Cult%"
UNION
SELECT "Stand-Up Comedy", COUNT(show_id)
FROM movie_test
WHERE listed_in LIKE "%Stand-Up Comedy%";