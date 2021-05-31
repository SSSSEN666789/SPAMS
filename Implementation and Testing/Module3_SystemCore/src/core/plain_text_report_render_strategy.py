from datetime import datetime
import json
import datetime

from .report_render_strategy import ReportRenderStrategy

class PlainTextReportRenderStrategy(ReportRenderStrategy):

    def render(self, test_result: str):
        # JSON 파싱
        result = json.loads(test_result)
        succeed = result["succeed"]
        results = result["results"]

        correct_cnt = len(list(filter(lambda r: r['isCorrect'] == True, results)))
        wrong_cnt = len(list(filter(lambda r: r['isCorrect'] == False, results)))
        
        # HTML 렌더링
        html = f"""
        <html>
        <head>
        <meta charset="UTF-8">
        </head>
        <body>
        <h1>자동채점 리포트</h1>
        <p>{datetime.datetime.now()}</p>
        """

        if succeed == False:
            html += """
            <h2>채점 결과</h2>
            <p style="color: red;">실패: 오류가 발생했습니다.</p>
            """
        else:
            html += f"""
            <h2>채점 결과</h2>
            <p>총 {correct_cnt + wrong_cnt}개의 응답 중 <span style="color: green;">정답: {correct_cnt}개, </span><span style="color: red;">오답: {wrong_cnt}개</p>
            <table border="1">
                <tr>
                    <th>#</th>
                    <th>응답</th>
                    <th>결과</th>
                </tr>
                <tr>
            """
            for i in range(0, len(results)):
                is_correct = results[i]['isCorrect']
                if is_correct == True: 
                    color = "green"
                    message = "정답"
                else: 
                    color = "red"
                    message = "오답"
                html += f"""
                <tr>
                    <td>{i+1}</td>
                    <td>{results[i]['response']}</td>
                    <td style="color: {color};">{message}</td>
                </tr>
                """
            html += """
            </table>
            """

        html += """
        </body>
        </html>
        """
    
        # 마무리
        report_location = "test_dir/plain_report.html"
        report = open(report_location, "w")
        report.write(html)
        report.close()
        return report_location