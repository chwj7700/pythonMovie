class Schedule:
    
    def __init__(self):
        self.id = None
        self.movieId = None
        self.cinemaId = None
        self.startTime = None
        self.endTime = None
        self.remainSeat = None

    def __str__(self):
        return 'Schedule : {' + '\n' \
               + '\t' + 'id : ' + self.id + '\n' \
               + '\t' + 'movieId : ' + self.movieId + '\n' \
               + '\t' + 'cinemaId : ' + self.cinemaId + '\n' \
               + '\t' + 'startTime : ' + self.startTime + '\n' \
               + '\t' + 'endTime : ' + self.endTime + '\n' \
               + '\t' + 'remainSeat : ' + self.remainSeat + '\n' \
               + '}'

    @staticmethod
    class Builder:

        def id(self, id):
            self.id = id
            return self
        
        def movieId(self, movieId):
            self.movieId = movieId
            return self
        
        def cinemaId(self, cinemaId):
            self.cinemaId = cinemaId
            return self
        
        def startTime(self, startTime):
            self.startTime = startTime
            return self
        
        def endTime(self, endTime):
            self.endTime = endTime
            return self
        
        def remainSeat(self, remainSeat):
            self.remainSeat = remainSeat
            return self

        def build(self):
            schedule = Schedule()
            schedule.id = self.id
            schedule.movieId = self.movieId
            schedule.cinemaId = self.cinemaId
            schedule.startTime = self.startTime 
            schedule.endTime = self.endTime
            schedule.remainSeat = self.remainSeat
            return schedule