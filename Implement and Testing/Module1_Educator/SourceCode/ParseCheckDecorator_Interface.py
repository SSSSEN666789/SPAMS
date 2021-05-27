from abc import *
from typing_extensions import ParamSpecKwargs

class ParseCheckDecoratorMeta(metaclass=ABCMeta):
    
    def set_decorator_chain(self, prev, next):
        self.prev = prev
        self.next = next

    def get_outcast(self):
        res = self
        while res.prev: res = res.prev
        return res

    @abstractmethod
    def createAssignmentEditor(self, param):
        pass

    @abstractmethod
    def createAssignmentList(self, param):
        pass

    @abstractmethod
    def createAssignmentCont(self, param):
        pass

    @abstractclassmethod
    def createAssignmentObject(self, param):
        pass

    @abstractclassmethod
    def modifyAssignmentObject(self, param):
        pass

    @abstractclassmethod
    def createSubList(self, param):
        pass

    @abstractclassmethod
    def createSubCont(self, param):
        pass

