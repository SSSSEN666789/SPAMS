#처음에는 evalReq 만들 때 넣을 데이터 같이 넣어서 이렇게 초기화 시키기

class EvaluationRequest:

    def __init__(self, id: int, sourceCode: str, testCase: str, timeLimit: int, memoryLimit: int, language: str):
        self.id = id
        self.sourceCode = sourceCode
        self.testCase = testCase
        self.timeLimit = timeLimit 
        self.memoryLimit = memoryLimit
        self.language = language

    