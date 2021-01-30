import imdb

data = imdb.IMDb()
movie_name = input("Enter the movie name:")
movies = data.search_movie(movie_name)
index = movies[0].getID()
movie = data.get_movie(index)
print(movie.keys())
title = movie['title']
year = movie['year']
genres = movie['genres']
language = movie['languages']
box_office = movie['box office']
rating = movie['rating']
director = movie['directors']
producers = movie['producers']
composers = movie['composers']
writers = movie['writer']
cast = movie['cast']
list_of_cast = ','.join(map(str,cast))
print(title)
print(year)
print(genres)
print(language[0])
print(box_office['Budget'])
print(rating)
print(list_of_cast)