MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title : ")
    director = input("Enter the movie director : ")
    year = input("Enter the movie release year : ")

    movies.append({
        "title":title,
        "director":director,
        "year":year
    })


def list_movies():
    for movie in movies:
        print(f"\nMovie Title: {movie['title']}\nMovie Director:{movie['director']}\nMovie release year: {movie['year']}")


def search_movie():
    title = input("\nEnter Movie Title: ")
    for movie in movies:
        if movie["title"] == title:
            print(
                f"\nMovie Title: {movie['title']}\nMovie Director:{movie['director']}\nMovie release year: {movie['year']}")


selection = ""

while selection != "q":
    selection = input(MENU_PROMPT)
    if selection == "a":
        add_movie()
    elif selection == "l":
        list_movies()
    else:
        print("Unknown command. Try again!")