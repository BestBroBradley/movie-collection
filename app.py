menu = "You can add a movie (a), list all movies (l), search for a title (s), or quit (q)."
user_selection = input(menu)

if user_selection == "a":
    print("add movie")
    input(menu)
elif user_selection == "l":
    print("see all")
    input(menu)
elif user_selection == "s":
    print("search for a title")
    input(menu)
elif user_selection == "q":
    print("Thank you for using our movie service")
else:
    print("You must select a valid option.")
    print(menu)