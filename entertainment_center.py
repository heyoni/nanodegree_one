from fresh_tomatoes import create_movie_tiles_content, open_movies_page
from media import movies



#Instantiating each movies object with details regarding the movie
snatch = movies("https://www.youtube.com/watch?v=ni4tEtuTccc", "Snatch",
                "http://blog.wlingua.com/learn-english/wp-content/uploads/sites/11/2015/10/snatch-5215c14f11168.jpg")


one_flew = movies("https://www.youtube.com/watch?v=2WSyJgydTsA", "One Flew Over the Cuckoo's Nest",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BYmJkODkwOTItZThjZC00MTE0LWIxNzQtYTM3MmQwMGI1OWFiXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg")  # noqa


apocalypse = movies("https://www.youtube.com/watch?v=snDR7XsSkB4", "Apocalypse Now",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BYWNjNjZjYmMtOTRjOC00ZGIwLWI2YzEtMjkxNTAzODkzZDRlXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg")  # noqa


Inglourious = movies("https://www.youtube.com/watch?v=KnrRy6kSFF0", "Inglourious Basterds",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BOTJiNDEzOWYtMTVjOC00ZjlmLWE0NGMtZmE1OWVmZDQ2OWJhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_SX675_AL_.jpg")  # noqa


howls = movies("https://www.youtube.com/watch?v=iwROgK94zcM", "Howl's Moving Castle",
               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY1OTg0MjE3MV5BMl5BanBnXkFtZTcwNTUxMTkyMQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg")  # noqa


donnie = movies("https://www.youtube.com/watch?v=ZZyBaFYFySk", "Donnie Darko",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMGIwNTc0NmMtZTFlZC00ZmY4LWE1NDItODhkZGJkMzFjZjg1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg")  # noqa


Serenity = movies("https://www.youtube.com/watch?v=JY3u7bB7dZk", "Serenity",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI0NTY1MzY4NV5BMl5BanBnXkFtZTcwNTczODAzMQ@@._V1_.jpg")  # noqa

films = [snatch, one_flew, apocalypse, Inglourious, howls, donnie, Serenity]

page = open_movies_page(films)