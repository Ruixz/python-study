import fresh_tomatoes
import media

inglourious_basterds = media.Movie("Inglourious Basterds", "A story in WWII",
                                   "http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                                   "https://www.youtube.com/watch?v=6AtLlVNsuAc")

pulp_fiction = media.Movie("Pulp Fiction", "Several stories happened in LA",
                           "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/watch?v=wZBfmBvvotE")

kill_bill = media.Movie("Kill Bill", "A revenge story",
                        "http://upload.wikimedia.org/wikipedia/en/4/46/Kill_bill_vol_two_ver.jpg",
                        "https://www.youtube.com/watch?v=NSR7xRGBnOE")

django_unchained = media.Movie("Django Unchained", "A story in deep south of US",
                               "http://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")

reservoir_dogs = media.Movie("Reservoir Dogs", "A crime story",
                             "http://upload.wikimedia.org/wikipedia/en/f/f6/Reservoir_dogs_ver1.jpg",
                             "https://www.youtube.com/watch?v=QvoKT481EmU")

sin_city = media.Movie("Sin City", "A comic-like story",
                       "http://upload.wikimedia.org/wikipedia/en/d/da/Sin_City_Hard_Goodbye.jpg",
                       "https://www.youtube.com/watch?v=nqRRF5y94uE")

movies = [inglourious_basterds, pulp_fiction, kill_bill, django_unchained, reservoir_dogs, sin_city]
fresh_tomatoes.open_movies_page(movies)
