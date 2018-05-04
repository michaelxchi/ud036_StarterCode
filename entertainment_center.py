import fresh_tomatoes
import media

la_la_land = media.Movie(
    "La La Land",
    "Sebastian and Mia are drawn together \
    their common desire to do what they love",
    "https://bit.ly/2rm9lGh", #noqa
    "https://www.youtube.com/watch?v=0pdqf4P9MB8") #noqa

gone_with_the_wind = media.Movie(
    "Gone with the Wind",
    "Epic Civil War drama focuses on the life \
     of petulant southern belle Scarlett O'Hara",
    "https://bit.ly/2rnp0oJ", #noqa
    "https://www.youtube.com/watch?v=0X94oZgJis4") #noqa

stripes = media.Movie(
    "Stripes",
    "Two friends who are dissatisfied with their jobs \
      decide to join the army for a bit of fun",
    "https://bit.ly/2HU3I9g", #noqa
    "https://www.youtube.com/watch?v=n-alQs9WZn4") #noqa

platoon = media.Movie(
    "Platoon",
    "Chris Taylor leaves his university studies to \
     enlist in combat duty in Vietnam in 1967",
    "https://bit.ly/2FL8KTn", #noqa
    "https://www.youtube.com/watch?v=KztP7SKe0uk") #noqa

crouching_tiger = media.Movie(
    "Crouching Tiger Hidden Dragon",
    "The story of finding stolen sword",
    "https://bit.ly/2rmdaLA", #noqa
    "https://www.youtube.com/watch?v=gLpZ_5bHmo8") #noqa 

some_like_it_hot = media.Movie(
    "Some Like It Hot",
    "After witnessing a Mafia murder, slick saxophone player Joe \
     and his long-suffering buddy,improvise a quick plan to \
     escape from Chicago with their lives",
    "https://bit.ly/2rnSjHs", #noqa
    "https://www.youtube.com/watch?v=rI_lUHOCcbc") #noqa

# list of movies to be render on the web page
movies = (la_la_land, stripes, platoon, crouching_tiger, 
         some_like_it_hot, gone_with_the_wind)

# generate an HTML file
fresh_tomatoes.open_movies_page(movies)  
