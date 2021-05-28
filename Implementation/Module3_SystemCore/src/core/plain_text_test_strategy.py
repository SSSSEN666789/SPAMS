import json

from .test_strategy import TestStrategy

class PlainTextTestStrategy(TestStrategy):

    def executeTest(self):
        # 응답 파싱
        # 응답은 한 줄에 하나씩이라 가정
        res_f = open('test_dir/example.txt', 'r')
        res_str = res_f.read()
        responses = res_str.split('\n')

        # 정답 파싱
        # 정답은 한 줄에 하나씩이라 가정
        ans_f = open('test_dir/example_test.txt', 'r')
        ans_str = ans_f.read()
        answers = ans_str.split('\n')

        # JSON object 생성
        result = []
        for i in range(0, len(answers)):
            response = responses[i]
            answer = answers[i]
            result.append({"response": response, "isCorrect": response == answer})
        json_str = json.dumps(result)
        
        return json_str