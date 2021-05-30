#처음에는 evalReq 만들 때 넣을 데이터 같이 넣어서 이렇게 초기화 시키기

class evaluationRequest:

    def __init__(self, data):
        self.id = data.id;
        self.sourceCode = data.sourceCode
        self.testCase = data.testCase
        self.timeLimit = data.timeLimit 
        self.memoryLimit = data.memoryLimit
        self.language = data.language

    