# usage : python show-department.py

import json
import sys


def main(type):
    db = {}
    if type == 'by_code':
        with open('../configuration/department.json', 'r') as index_department_file:
            dept = json.load(index_department_file)
            for item in dept['DEPARTMENTS']:
                db[item['INDEX']] = item['TITLE']
            db_sorted = sorted(db.items())
            for item in db_sorted:
                print(item[0], ": ", item[1])
    else:
        with open('../configuration/department.json', 'r') as index_department_file:
            dept = json.load(index_department_file)
            for item in dept['DEPARTMENTS']:
                db[item['TITLE']] = item['INDEX']
            db_sorted = sorted(db.items())
            for item in db_sorted:
                print(item[1], ": ", item[0])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main('by_name')
    else:  # 실행시 소스코드 이름 뒤에 뭐라도 쓰면 아래 문장 수행
        main('by_code')
