# khu-today-server
[경희의 오늘] Server

경희의 오늘은 Android App, iOS App, macOS, Windows, Linux, Web browser 등을 통해서 접근 가능합니다. <br>
Web browser를 통한 접근은 아래의 링크를 클릭해서 경험할 수 있습니다.  <br>
[http://opensource.khu.ac.kr/run.html](http://opensource.khu.ac.kr/run.html)  <br>

경희의 오늘 서버는 다음과 같은 API를 제공합니다.<br>

(1) API #1 : 오늘 날자 정보

http://163.180.142.196:9090/today_api/today

(2) API #2 : 이전 정보

규칙: http://163.180.142.196:9090/today_api/[년-월-일]<br>
예시: http://163.180.142.196:9090/today_api/2023-10-18

경희의 오늘 서버는 다음과 같은 4가지 종류의 서버로 구성되어 있습니다.<br>

crawler : 크롤링 서버 <br>
aggregator : 크롤링 서버 결과를 취합하여 DB에 저장하는 서버 <br>
generator : DB에서 새로운 정보를 취합하여 App에 전달하는 형태로 재구성하는 서버 <br>
reception-handler : gunicorn을 통하여 실행하는 app으로부터의 http request 처리 서버 <br>
