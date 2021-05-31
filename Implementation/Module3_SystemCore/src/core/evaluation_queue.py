#라이브러리에 있는 Queue해서 enqueue랑 dequeue 함수 생성
#pop 함수가 queue가 empty한 상태여도 프로그램 에러 안나고 계속 돌아가려나..?
#get() : 큐에서 항목을 제거하고 반환합니다. 
# 선택적 인자 block이 참이고 timeout이 None(기본값)이면
# 항목이 사용 가능할 때까지 필요하면 블록합니다. 이라는 설명이 있어
# get에 인자로 True를 전달함

from queue import Queue
from .evaluation_request import *


class evaluationQueue(evaluationRequest):
    def __init__(self):
        self.que = Queue()
        self.evalReq = evaluationRequest()

    def enqueue(self):
        self.que.put(self.evalReq)

    def dequeue(self):
        self.evalReq = self.que.get(True)