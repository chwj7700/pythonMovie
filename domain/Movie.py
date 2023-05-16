class Movie:

    def __init__(self):
        self.id = None
        self.name = None
        self.description = None
        self.startDate = None
        self.nation = None
        self.director = None
        self.runningTime = None
        self.posterPath = None
        self.genre = None
    
    def __str__(self):
        return 'Movie : {' + '\n' \
               + '\t' + 'id : ' + self.id + '\n' \
               + '\t' + 'name : ' + self.name + '\n' \
               + '\t' + 'description : ' + self.description + '\n' \
               + '\t' + 'startDate : ' + self.startDate + '\n' \
               + '\t' + 'nation : ' + self.nation + '\n' \
               + '\t' + 'director : ' + self.director + '\n' \
               + '\t' + 'runningTime : ' + self.runningTime + '\n' \
               + '\t' + 'posterPath : ' + self.posterPath + '\n' \
               + '\t' + 'genre : ' + self.genre + '\n' \
               + '\t' + 'totalSeat : ' + self.totalSeat + '\n' \
               + '}'

    @staticmethod
    class Builder:

        def id(self, id):
            self.id = id
            return self
        
        def name(self, name):
            self.name = name
            return self
        
        def description(self, description):
            self.description = description
            return self
        
        def startDate(self, startDate):
            self.startDate = startDate
            return self
        
        def nation(self, nation):
            self.nation = nation
            return self
        
        def director(self, director):
            self.director = director
            return self
        
        def runningTime(self, runningTime):
            self.runningTime = runningTime
            return self
        
        def posterPath(self, posterPath):
            self.posterPath = posterPath
            return self
        
        def genre(self, genre):
            self.genre = genre
            return self
        
        def totalSeat(self, totalSeat):
            self.totalSeat = totalSeat
            return self

        def build(self):
            moive = Movie()
            moive.id = self.id
            moive.name = self.name
            moive.description = self.description 
            moive.startDate = self.startDate
            moive.nation = self.nation 
            moive.director = self.director
            moive.runningTime = self.runningTime
            moive.posterPath = self.posterPath
            moive.genre = self.genre
            moive.totalSeat = self.totalSeat
            return moive