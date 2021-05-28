import json

from .report_render_strategy import ReportRenderStrategy

class PlainTextReportRenderStrategy(ReportRenderStrategy):

    def render(self, test_result: str):
        # JSON 파싱
        result = json.loads(test_result)

        correct_cnt = len(list(filter(lambda r: r['isCorrect'] == True, result)))
        wrong_cnt = len(list(filter(lambda r: r['isCorrect'] == False, result)))
        
        # HTML 렌더링
        html = """
        <html>
        <head>
        <meta charset="UTF-8">
        </head>
        <body>
        <h1>자동채점 리포트</h1>
        """
        
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
        for i in range(0, len(result)):
            is_correct = result[i]['isCorrect']
            if is_correct == True: 
                color = "green"
                message = "정답"
            else: 
                color = "red"
                message = "오답"
            html += f"""
            <tr>
                <td>{i+1}</td>
                <td>{result[i]['response']}</td>
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
        report = open("test_dir/plain_report.html", "w")
        report.write(html)
        report.close()