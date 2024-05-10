# Please write a function named find_movies(database: list,
# search_term: str), which processes the movie database created in the
# previous exercise. The function should formulate a new list, which contains only
# the movies whose title includes the word searched for. Capitalisation is irrelevant
# here. A search for ana should return a list containing both Anaconda and Management.

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database.append({"name": name, "director": director, "year": year, "runtime": runtime})


def find_movies(database: list, search_term: str):
    search_result = []
    for movie in database:
        if search_term in movie["name"].lower():
            search_result.append(movie)
    return search_result
