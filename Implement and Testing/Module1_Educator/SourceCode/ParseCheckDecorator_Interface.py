from abc import *

class ParseCheckDecoratorMeta(metaclass=ABCMeta):
    
    def set_decorator_chain(self, prev, next):
        self.prev = prev
        self.next = next

    def get_outcast(self):
        res = self
        while res.prev: res = res.prev
        return res

    @abstractmethod
    def createPage(self, param):
        pass
