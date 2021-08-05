from chiSquareMain import *

genreList = ["TV", "Movies", "Action & Adventure", "Dramas", "International", "Sci-Fi & Fantasy", "Horror", "Thriller", "Crime", 
            "Sports", ("Documentaries", "Docuseries"), "Independent", "Comedies", "Anime", "Reality TV", "Romantic", "Science & Nature", 
            "Mysteries", "Music & Musicals", ("Kids", "Children"), "LGBTQ", "Teen", "Cult", "Stand-Up Comedy"]

# Makes the enders for genre
def makeQueryEndersGenre():
    params = genreList
    constTuple = ("listed_in LIKE '%", "%'")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)