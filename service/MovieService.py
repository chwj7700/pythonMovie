from service.BaseService import BaseService
from repository.MovieRepository import MovieRepository

class MovieService(BaseService):
    
    def retrieveMoviePosterPathWithPaging(self, offset, limit):
        movieRepository = MovieRepository()
        movies = movieRepository.findAllWithPaging(offset, limit)
        moviePosterPaths = []
        for movie in movies:
            moviePosterPaths.append(movie.posterPath)
        return moviePosterPaths
    
    def retrieveMovieNameWithPaging(self, offset, limit):
        movieRepository = MovieRepository()
        movies = movieRepository.findAllWithPaging(offset, limit)
        movieNames = []
        for movie in movies:
            movieNames.append(movie.name)
        return movieNames
    
    def retriveMovieWithPaging(self, offset, limit):
        movieRepository = MovieRepository()
        movies = movieRepository.findAllWithPaging(offset, limit)
        return movies