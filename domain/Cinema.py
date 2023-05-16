class Cinema:

    def __init__(self):
        self.id = None
        self.totalSeat = None
        self.amount = None
    
    def __str__(self):
        return 'Cinema : {' + '\n' \
               + '\t' + 'id : ' + self.id + '\n' \
               + '\t' + 'totalSeat : ' + self.totalSeat + '\n' \
               + '\t' + 'amount : ' + str(self.amount) + '\n' \
               + '}'

    @staticmethod
    class Builder:

        def id(self, id):
            self.id = id
            return self
        
        def totalSeat(self, totalSeat):
            self.totalSeat = totalSeat
            return self
        
        def amount(self, amount):
            self.amount = amount
            return self
        
        def build(self):
            cinema = Cinema()
            cinema.id = self.id
            cinema.totalSeat = self.totalSeat
            cinema.amount = self.amount 
            return cinema