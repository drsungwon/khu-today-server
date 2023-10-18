# khu-today-server
[경희의 오늘] Server

(1) API #1 : 오늘 날자 정보

http://163.180.142.196:9090/today_api/today

(2) API #2 : 이전 정보

규칙: http://163.180.142.196:9090/today_api/[년-월-일]
예시: http://163.180.142.196:9090/today_api/2023-10-18

(3) 서버 구성

crawler : 크롤링 서버 <br>
aggregator : 크롤링 서버 결과를 취합하여 DB에 저장하는 서버 <br>
generator : DB에서 새로운 정보를 취합하여 App에 전달하는 형태로 재구성하는 서버 <br>
reception-handler : gunicorn을 통하여 실행하는 app으로부터의 http request 처리 서버 <br>
