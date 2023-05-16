from repository.BaseRepository import BaseRepository
from repository.MovieRepository import MovieRepository
from repository.CinemaRepository import CinemaRepository

class ScheduleRepository(BaseRepository):
    
    def isValidated(self, cls):
        movieRepository = MovieRepository()
        movie = movieRepository.findById(cls.movieId)
        if not movie:
            print('해당하는 영화가 없습니다.')
            return False
    
        cinemaRepository = CinemaRepository()
        cinema = cinemaRepository.findById(cls.cinemaId)
        if not cinema:
            print('해당하는 영화관이 없습니다.')
            return False
        
        return True