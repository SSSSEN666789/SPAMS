# Sequence Diagram for Use Case 202 & 204: 제출물 제출(combined)


--------
## Object Sequence Diagram
![Object Sequence Diagram for UC 202&204](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/UC%20202%20%26%20204%20Sequence%20Diagram%20(combined).png)

User Story와 Use Case 구상 단계에서는 팀에서 제출과 재제출은 엄연히 다르고 분리하는게 낫다고 판단했었다. 하지만 Sequence Diagram 설계를 하다보니 이 둘을 합치는게 오히려 더 효율적으로 보여서 Use Case 202제출물 제출과 Use Case 204제출물 재제출을 합친 Sequence Diagram을 디자인 해보았다. UC 202는 제출 요청시 제출물이 이미 존재하는지 검사 절차가 있었고 UC 204는 제출 요청시 기존 제출물을 확인할 필요없이 put메소드를 통해 DB에 갱신을 했다. 그리고 이보다 더 초기 디자인에는 이 두개의 UC를 분리하고자 UC 204에서는 기존 제출물을 삭제후 새 오브젝트를 생성하여 저장하는 식으로 재제출을 디자인했었는데, 제출과 재제출을 따로두기 위해 억지로 비효율적인 길을 택하는거로 판단하여 이 둘의 단점들을 제거하여 결합한 버젼의 디자인을 설계 해보았다.

제출과 재제출 구분없이 학생이 제출 요청을 할때마다 요청이 성공하면 계속 DB에 저장된 파일을 갱신하게끔 한다. 





--------
