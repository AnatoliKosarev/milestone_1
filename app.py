movies = []
MENU_MESSAGE = "'a' to add movie to collection \n'l' to display all movies from collection\n" \
               "'f' to find a specific movie info by its title\n'q' to quit the program\nPlease enter: "
movie_entry_info_message = "Please enter the {movie_parameter}: "
movie_display_template = "Movie title: {movie_title} ({movie_year}), by {movie_director}"


def enter_movie_info():
    movie_title = input(movie_entry_info_message.format(movie_parameter="movie title"))
    movie_year = input(movie_entry_info_message.format(movie_parameter="movie year"))
    movie_director = input(movie_entry_info_message.format(movie_parameter="movie director"))
    return movie_title, movie_year, movie_director


def add_movie_to_collection():
    movie_title, movie_year, movie_director = enter_movie_info()
    if movie_title and movie_year and movie_director:
        movies.append({
            "title": movie_title.title(),
            "year": movie_year,
            "director": movie_director.title()
        })
    else:
        print("Not all movie data was entered. PLease try again.")


def iterate_and_print_movies(movie_collection):
    for movie in movie_collection:
        print(movie_display_template.format(movie_title=movie.get("title"), movie_year=movie.get("year"),
                                            movie_director=movie.get("director")))


def display_movie_collection():
    iterate_and_print_movies(movies)


def search_for_movie():
    query_param = input("Please enter movie search parameter (title, year, director): ")
    if query_param == "title" or query_param == "year" or query_param == "director":
        query_value = input("Please enter movie search value: ")
        query_movies = []
        for movie in movies:
            if movie.get(query_param).lower() == query_value.lower():
                query_movies.append(movie)
                if query_param == "title":
                    break
        if query_movies:
            iterate_and_print_movies(query_movies)
        else:
            print(f"Movie with {query_param}: {query_value} was not found in your collection")
    else:
        print("Entered movie search parameter is incorrect. Please try again.")


user_options = {
    "a": add_movie_to_collection,
    "l": display_movie_collection,
    "f": search_for_movie
}


def start_menu():
    user_selection = input(MENU_MESSAGE)
    while user_selection != "q":  # if selection == "q" - program ends
        if user_selection in user_options:
            selected_function = user_options[user_selection]
            if (user_selection == "l" or user_selection == "f") and not movies:
                print("Your movie collection is empty. PLease add movies to collection first.")
            else:
                selected_function()
        else:
            print("Invalid selection. Please try again.")

        user_selection = input(MENU_MESSAGE)


start_menu()
