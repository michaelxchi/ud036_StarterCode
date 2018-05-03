import fresh_tomatoes
import media

la_la_land = media.Movie("La La Land",
                         "Sebastian and Mia are drawn together by their common desire to do what they love",
                         "https://upload.wikimedia.org/wikipedia/sco/a/ab/La_La_Land_%28film%29.png",
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")

gone_with_the_wind = media.Movie("Gone with the Wind",
                                 "Epic Civil War drama focuses on the life of petulant southern belle Scarlett O'Hara",
                                 "https://upload.wikimedia.org/wikipedia/commons/2/27/Poster_-_Gone_With_the_Wind_01.jpg",
                                 "https://www.youtube.com/watch?v=0X94oZgJis4")

stripes = media.Movie("Stripes",
                      "Two friends who are dissatisfied with their jobs decide to join the army for a bit of fun",
                      "https://upload.wikimedia.org/wikipedia/en/3/3e/Stripesposter.jpg",
                      "https://www.youtube.com/watch?v=n-alQs9WZn4")

platoon = media.Movie("Platoon",
                      "Chris Taylor leaves his university studies to enlist in combat duty in Vietnam in 1967",
                      "https://upload.wikimedia.org/wikipedia/en/a/a9/Platoon_posters_86.jpg",
                      "https://www.youtube.com/watch?v=KztP7SKe0uk")

crouching_tiger = media.Movie("Crouching Tiger Hidden Dragon",
                              "The story of finding stolen sword",
                              "https://upload.wikimedia.org/wikipedia/en/9/97/Crouching_tiger_hidden_dragon_poster.jpg",
                              "https://www.youtube.com/watch?v=gLpZ_5bHmo8")

some_like_it_hot = media.Movie("Some Like It Hot",
                               "After witnessing a Mafia murder, slick saxophone player Joe and his long-suffering buddy,improvise a quick plan to escape from Chicago with their lives",
                               "https://upload.wikimedia.org/wikipedia/en/b/b4/Some_Like_It_Hot_poster.jpg",
                               "https://www.youtube.com/watch?v=rI_lUHOCcbc")

#list of movies to be render on the web page
movies = (la_la_land, stripes, platoon, crouching_tiger, some_like_it_hot, gone_with_the_wind)

#generate an HTML file
fresh_tomatoes.open_movies_page(movies)
