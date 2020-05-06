menu = "You can add a movie (a), list all movies (l), search for a title (s), or quit (q):"

user_library = []

def query_user():
    user_selection = input(menu)
    if user_selection == "a":
      add_movie()
      get_selection()
    elif user_selection == "l":
      print("see all")
      get_selection()
    elif user_selection == "s":
      print("search for a title")
      get_selection()
    elif user_selection == "q":
      print("Thank you for using our movie service")
    else:
      print("You must select a valid option.")
      get_selection()

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
        print("You must type either 'y' or 'n'.)
        verify_title(new_title)

def verify_gen_rating(new_title, genre, rating):
    verify_final = input(f"Would you like to add {new_title} with a genre of {genre} and a rating of {rating} to your library?")

def add_movie():
    new_title = input("What is the title of the movie you would like to add? ")
    verify_title(new_title)

def see_all():

def search():

query_user()

