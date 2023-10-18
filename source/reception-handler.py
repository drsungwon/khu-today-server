# gunicorn --bind 0.0.0.0:9090 -w 4 --access-logfile ~/crawler/log/gunicorn/9090/access.log --error-logfile ~/crawler/log/gunicorn/9090/error.log reception-handler:app
# gunicorn --bind 0.0.0.0:9092 -w 4 --access-logfile ~/crawler/log/gunicorn/9092/access.log --error-logfile ~/crawler/log/gunicorn/9092/error.log reception-handler:app

import json
from flask import Flask, request, send_file
from flask_restx import Resource, Api
from os.path import exists
from flask_cors import CORS
from datetime import date
from datetime import datetime

app = Flask(__name__)
CORS(app)
api = Api(app, doc=False)


class ReceptionHandler():
    # dictionary for membership management
    stacks = {}

    def __init__(self):
        self.today = str(date.today())
        self.visitCounter = 0

    def increaseVisitCounter(self):
        if self.today == str(date.today()):
            self.visitCounter += 1
        else:
            print("{} -->> {}", self.today, self.visitCounter)
            self.visitCounter = 1
            self.today = str(date.today())

    # GET request
    def read(self, target):

        if target == 'today':
            self.increaseVisitCounter()
            with open('../result/stacks.json', 'r') as json_file:
                stacks = json.load(json_file)
                with open('../appconfiguration/dna.json', 'r') as dna_file:
                    dna = json.load(dna_file)
                    stacks['VERSION_DNA'] = dna['VERSION_DNA']
                return stacks

        elif target == 'dna':
            with open('../appconfiguration/dna.json', 'r') as dna_file:
                stacks = json.load(dna_file)
            return stacks

        else:
            file_name = '../result/history/stacks-' + target + '.json'
            file_exists = exists(file_name)
            if file_exists == True:
                with open(file_name, 'r') as json_file:
                    stacks = json.load(json_file)
                    return stacks
            else:
                return "404 File not found"


eventHandler = ReceptionHandler()


@api.route('/today_api/<string:date>')
class MembershipManager(Resource):
    # 'R'ead handler
    def get(self, date):
        return eventHandler.read(date)


# Belows are blocking CensysInspect

@api.route('/')
class BlockingManager(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        pass


@api.route('/favicon.ico')
class BlockingManager(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        pass


@api.route('/api/')
class BlockingManager(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        pass


@api.route('/swaggerui/{something}')
class BlockingManager(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        pass


@api.route('/swaggerui')
class BlockingManager(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        pass


''' usage : 
    http://172.30.1.49:9090/today_api/today
    http://172.30.1.49:9090/today_api/2022-05-07
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=9090)
