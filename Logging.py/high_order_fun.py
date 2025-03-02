movies = [
    {"name": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994},
    {"name": "The Godfather", "director": "Francis Ford Coppola", "year": 1972},
    {"name": "The Dark Knight", "director": "Christopher Nolan", "year": 2008},

]
def find_movie(expected, finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie
    
find_by = input("What property are you searching by? ")
looking_for = input("What are you searching for? ")
movie = find_movie(looking_for, lambda movie: movie[find_by])
print(movie or 'No movies found.')
#The lambda function is a small anonymous function.
    