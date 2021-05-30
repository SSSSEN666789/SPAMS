#라이브러리에 있는 Queue해서 enqueue랑 dequeue 함수 생성
#pop 함수가 queue가 empty한 상태여도 프로그램 에러 안나고 계속 돌아가려나..?
from queue import Queue
from .evaluation_request import *


class evaluationQueue(evaluationRequest):
    def __init__(self):
        self.que = Queue()
        self.evalReq = evaluationRequest()

    def enqueue(self):
        self.que.put(self.evalReq)

    def dequeue(self):
        self.evalReq = self.que.get()