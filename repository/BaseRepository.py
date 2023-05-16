from util.Singleton import Singleton
from copy import *

class BaseRepository(Singleton):

    def __init__(self):
        if not hasattr(self, "init_"):    
            self.init_ = True
            self.__list = []

    def findAll(self):
        return self.__list
    
    def findById(self, id):
        for e in self.__list:
            if e.id == id:
                return e
        return None
    
    def findAllWithPaging(self, offset, limit):
        return self.__list[offset:limit]
    
    def __retrieveMaxId(self):
        maxId = 0
        for e in self.__list:
            id = int(e.id)
            if id > maxId:
                maxId = id
        return maxId
    
    def insert(self, cls):
        if not self.isValidated(cls): return None
        
        copyCls = deepcopy(cls)
        copyCls.id = str(int(self.__retrieveMaxId()) + 1)
        self.__list.append(copyCls)
        return copyCls

    
    def update(self, cls):
        if not self.isValidated(cls):  return None
        
        for e in self.__list:
            if e.id == cls.id:
                e = cls
                return cls
        
        print('해당하는 id가 없습니다.')
        return False
    
    def isValidated(self, cls):
        return True