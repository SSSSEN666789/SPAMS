import os
import platform

from .test_strategy import TestStrategy
from .evaluation_request import EvaluationRequest

class PythonTestStrategy(TestStrategy):
    def executeTest(self, request: EvaluationRequest):
        # 채점 요청에서 필요한 파일명 가져옴
        tcName = request.testCase

        # pytest 실행
        os.system(f"pytest test_dir/{tcName} --report-log=test_dir/test_result.json > test_dir/cmd_output.txt")

        # pytest 결과 읽어 들이기
        # json파일에 json object가 하나가 아니라 라인마다 object 하나임에 유의
        result_f = open("test_dir/test_result.json", mode='r')
        result_str = result_f.read()
        result_f.close()

        # 기본적으로 결과 출력 결과에서 제공하지 않는 실행환경, raw ouput 붙여서 반환
        return self._get_env() + "\n" + result_str + self._get_output()

    # 실행 환경 json object를 string으로 반환
    # 실제 환경에서는 보안 이슈 있을 수도? 지금은 데모 환경이므로 일단 두자.
    def _get_env(self):
        platform_str = platform.platform() # 운영체제 정보
        py_impl = platform.python_implementation() # 파이썬 구현체
        py_ver = platform.python_version() # 파이썬 버전
        return f"{{\"platform\": \"{platform_str}\", \"python_version\": \"{py_impl}-{py_ver}\", \"$report_type\": \"Environment\"}}"

    def _get_output(self):
        return f"{{\"cmd_output_file\": \"test_dir/cmd_output.txt\", \"$report_type\": \"RawOutput\"}}"