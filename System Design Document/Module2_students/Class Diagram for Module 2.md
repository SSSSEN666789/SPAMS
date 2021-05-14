# Class Diagram for Module 2

### 202 & 204
![classdiagram_UC202&204](img/Class%20Diagram%20202%26204%20제출물%20제출%26재제출.png)

UC 202와 UC 204를 합쳐서 설계한 Class Diagram.

UC 202와 UC 204를 따로 설계했을시 각각 추가적인 채널들을 가지고있었고(202 같은경우는 기존 제출물이 존재하는지 검사, 204는 기존 제출물을 지우고 새로 오브젝트를 생성하는 채널), 이 둘을 합치게 된다면 서로 상호 보완이 되어 불필요한 채널들을 제거함과 동시에 코드의 재활용성을 높일수 있게되어서 이 둘을 합친 System Sequence Diagram을 기반으로 Class Diagram을 작성하였다.

학생은 바운더리 오브젝트인 Interface Page를 통해 쿼리를 입력하고 컨트롤러로 전달되어 컨트롤러가 다른 오브젝트들이 지닌 메소드를 실행 시키기위한 트리거 역할을 해준다. 자세한 Event들의 흐름은 System Sequence Diagram 문서에 서술되어있다.


_



### 203 
![classdiagram_UC203](img/img/Class%20Diagram%20203%20제출물%20결과확인.png)



### 향후 방향성

UC 202와 204처럼 나머지 70%의 UC들도 서로 밀접한 UC들이 있어 이를 그룹화 하여 통일된 System Sequence Diagram 과 Class Diagram이 더 효율적으로 판단이 된다면 이를 통일할것도 염두에 두고있는 상황이다. 우선은 각 UC들이 가질 request와 event들을 확인해봐야겠지만.
