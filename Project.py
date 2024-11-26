MENU_PROMPT= "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, 'q' to quit:"
movie=[]
def add_movie():
    title = input("Enter the movie title:")
    director= input("enter the movie director:")
    year= input("enter the movie release year:")


    movie.append({
    'title': title,
    'director':director,
    'year':year
    })
def show_movie():
    for m in movie:
        print_movie(m)

def print_movie(movie):
    print(f"title:{movie['title']}")
    print(f"Director:{movie['director']}")
    print(f"year:{movie['year']}")

def find_movie():
    search_title=("enter movie title you are looking for")
    for movie in movie:
        if movie["title"]== search_title:
            print_movie(movie)
def menu():
    selection= input(MENU_PROMPT)
    while selection!='q':
        if selection=="a":
           add_movie()
        elif selection=="l":
            show_movie()
        elif selection=="f":
            find_movie()
        else:
            print('unknown command. please try again.')

        selection= input(MENU_PROMPT) 

menu()
    