menu = "You can add a movie (a), list all movies (l), search for a title (s), or quit (q):"

def get_selection():
    user_selection = input(menu)
    if user_selection == "a":
      print("add movie")
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

get_selection()