# [경희의 오늘] Server Softwares

Python 언어로 만들어진 '경희의 오늘'의 Server(들)입니다. <br>
'경희의 오늘' 서비스는 iOS/Android App, macOS/Windows/Linux Desktop Software, Web browser 등을 통해서 가능합니다. <br>

Web browser를 통한 접근은 아래의 링크를 클릭해서 경험할 수 있습니다.  <br>
[http://opensource.khu.ac.kr/run.html](http://opensource.khu.ac.kr/run.html)  <br>

'경희의 오늘' 서버는 다음과 같은 API를 제공합니다.<br>

(1) API #1 : 오늘 날자 정보<br>

* http://163.180.142.196:9090/today_api/today <br>

(2) API #2 : 이전 정보<br>

* 규칙: http://163.180.142.196:9090/today_api/[년-월-일] <br>
* 예시: http://163.180.142.196:9090/today_api/2023-10-18 <br>

'경희의 오늘' 서버는 다음과 같은 4가지 종류의 서버로 구성되어 있습니다.<br>

* crawler : 크롤링 서버 <br>
* aggregator : 크롤링 서버 결과를 취합하여 DB에 저장하는 서버 <br>
* generator : DB에서 새로운 정보를 취합하여 App에 전달하는 형태로 재구성하는 서버 <br>
* reception-handler : gunicorn을 통하여 실행하는 app으로부터의 http request 처리 서버 <br>

경희대학교 소프트웨어융합학과의 Full Stack Service Progamming 과목을 위하여 개발 되었습니다. <br>
해당 수업에 대한 정보는 다음의 링크를 통해서 접근할 수 있습니다. <br>
[http://mobilelab.khu.ac.kr/wordpress/fssp/](http://mobilelab.khu.ac.kr/wordpress/fssp/) <br>

Client에 대한 오픈소스 소프트웨어는 다음의 링크에서 확인할 수 있습니다.  <br>
[https://github.com/drsungwon/khu-today-server](https://github.com/drsungwon/khu-today-server) <br>

