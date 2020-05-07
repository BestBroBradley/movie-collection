menu = "You can add a movie (a), list all movies (l), search for a title (s), or quit (q): "

user_library = []

def query_user():
    user_selection = input(menu)
    if user_selection == "a":
      add_movie()
      query_user()
    elif user_selection == "l":
      view_all()
      query_user()
    elif user_selection == "s":
      search()
      query_user()
    elif user_selection == "q":
      print("Thank you for using our movie service.")
    else:
      print("You must select a valid option.")
      query_user()


def get_gen_rating(new_title):
    genre = input(f"What genre is {new_title}? ")
    rating = input(f"What rating would you like to give {new_title}? (?/10) ")
    verify_gen_rating(new_title, genre, rating)


def verify_title(new_title):
    verify_query = input(f"Would you like to add {new_title} to your library? (y/n) ")
    if verify_query == "y":
        get_gen_rating(new_title)
    elif verify_query == "n":
        add_movie()
    else:
        print("You must type either 'y' or 'n'.")
        verify_title(new_title)

def add_to_library(new_title, genre, rating):
    user_library.append({"title": new_title, "genre": genre, "rating": rating + "/10"})
    query_user()

def verify_gen_rating(new_title, genre, rating):
    verify_final = input(f"Would you like to add {new_title} with a genre of {genre} and a rating of {rating}/10 to your library? (y/n) ")
    if verify_final == "y":
        add_to_library(new_title, genre, rating)
    elif verify_final == "n":
        get_gen_rating(new_title)
    else:
        print("You must type either 'y' or 'n'.")
        verify_gen_rating(new_title, genre, rating)


def add_movie():
    new_title = input("What is the title of the movie you would like to add? ")
    verify_title(new_title)


def view_all():
    if len(user_library) > 0:
        print("Your library:")
        for movie in user_library:
            title = movie["title"]
            genre = movie["genre"]
            rating = movie["rating"]
            print(f"{title} | {genre} | {rating}")
        query_user()
    else:
        print("There are no titles in your library.")
        query_user()

def search():
    search_term = input("What title would you like to search for? ")
    for movie in user_library:
        if movie["title"].lower() == search_term.lower():
            title = movie["title"]
            genre = movie["genre"]
            rating = movie["rating"]
            print("Movie Details:")
            print(f"{title} | {genre} | {rating}")
            break
    else:
        print("Looks like that title isn't in your library.")
    query_user()
query_user()
