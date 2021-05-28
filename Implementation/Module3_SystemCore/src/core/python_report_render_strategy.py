import json

from .report_render_strategy import ReportRenderStrategy

class PythonReportRenderStrategy(ReportRenderStrategy):

    def render(self, test_result: str):
        # JSON 파싱
        json_strs = test_result.split('\n')
        json_objs = list(map(lambda str: json.loads(str), json_strs))

        # 필요한 정보 추출
        env = list(filter(lambda obj: obj['$report_type'] == 'Environment', json_objs))[0]
        pytest_ver = list(filter(lambda obj: obj['$report_type'] == 'SessionStart', json_objs))[0]['pytest_version']

        tc_results = list(filter(lambda obj: obj['$report_type'] == 'TestReport' and obj['when'] == 'call', json_objs))
        exit_code = int(list(filter(lambda obj: obj['$report_type'] == 'SessionFinish', json_objs))[0]['exitstatus'])

        cmd_output_file_name = list(filter(lambda obj: obj['$report_type'] == "RawOutput", json_objs))[0]['cmd_output_file']
        cmd_output = None
        if cmd_output_file_name is not None:
            f = open(cmd_output_file_name, 'r')
            cmd_output = f.read()
            f.close()
            cmd_output = cmd_output.replace('\n', '<br>')
        
        # HTML 렌더링
        html = """
        <html>
        <head>
        <meta charset="UTF-8">
        </head>
        <body>
        <h1>자동채점 리포트</h1>
        """

        if env is not None:
            html += f"""
            <h2>환경</h2>
            <table border="1">
                <tr>
                    <td>플랫폼</td>
                    <td>{env['platform']}</td>
                </tr>
                <tr>
                    <td>Python 버전</td>
                    <td>{env['python_version']}</td>
                </tr>
            """
            if pytest_ver is not None:
                html += f"""
                <tr>
                    <td>PyTest 버전</td>
                    <td>{pytest_ver}</td>
                </tr>
                """
            html += "</table>"
        
        if len(tc_results) > 0:
            tc_cnt = len(tc_results)
            passed_cnt = len(list(filter(lambda r: r['outcome'] == 'passed', tc_results)))
            failed_cnt = len(list(filter(lambda r: r['outcome'] == 'failed', tc_results)))
            other_cnt = tc_cnt - passed_cnt - failed_cnt
            html += f"""
            <h2>채점 결과</h2>
            <p>총 {len(tc_results)}개의 채점 항목 중 <span style="color: green;">통과: {passed_cnt}개, </span><span style="color: red;">실패: {failed_cnt}개, </span><span style="color: orange;">기타: {other_cnt}개</span></p>
            <table border="1">
                <tr>
                    <th>TC Node ID</th>
                    <th>결과</th>
                    <th>메시지</th>
                    <th>소요시간(초)</th>
                </tr>
                <tr>
            """
            for r in tc_results:
                outcome = r['outcome']
                if outcome == 'passed': color = "green"
                elif outcome == 'failed': color = "red"
                else: color = "orange"
                message = None
                try: message = r['longrepr']['reprcrash']['message']
                except: pass
                html += f"""
                <tr>
                    <td style="color: {color};">{r['nodeid']}</td>
                    <td style="color: {color};">{r['outcome']}</td>
                    <td>{message}</td>
                    <td>{r['duration']}</td>
                </tr>
                """
            html += """
            </table>
            """
        elif exit_code >= 2:
            html += """
            <h2>채점 결과</h2>
            <p style="color: red;">실패: 오류가 발생했습니다.</p>
            """

        if cmd_output is not None:
            html += f"""
            <h2>커맨드라인 출력</h2>
            <pre>
{cmd_output}
            </pre>
            """

        html += """
        </body>
        </html>
        """
    
        # 마무리
        report = open("test_dir/report.html", "w")
        report.write(html)
        report.close()