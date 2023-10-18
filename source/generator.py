import json
import pymysql
from datetime import date
from datetime import datetime


def main():

    today = str(date.today())

    db_today = pymysql.connect(user='root', passwd='rootpassword', host='127.0.0.1', db='today', charset='utf8')
    db_cursor = db_today.cursor(pymysql.cursors.DictCursor)

    sql_command = "SELECT * FROM today_table WHERE crawl_time > '" + today + "';"

    result_count = db_cursor.execute(sql_command)
    db_today.commit()

    result_json = db_cursor.fetchall()
    stack_json = {}

    stack_json['GENERATED_TIME'] = datetime.now().isoformat()
    stack_json['STACK_NUMBER'] = str(result_count)
    stack_json['STACKS'] = []

    # Special care for COUNT based post ( 1 post per day )
    # [START]

    dept00000039 = [] # 미래인재센터.채용공고
    dept00000040 = [] # 미래인재센터.추천채용

    for element in result_json:
        if element['department_code'] == '00000039':
            dept00000039.append([
            element['department_code'],
            element['crawl_time'],
            element['post_title'],
            element['post_href']
        ])
        elif element['department_code'] == '00000040':
            dept00000040.append([
            element['department_code'],
            element['crawl_time'],
            element['post_title'],
            element['post_href']
        ])

    if len(dept00000039) != 0:
        final_index = len(dept00000039) - 1
        stack_json['STACKS'].append([
            dept00000039[final_index][0],
            dept00000039[final_index][1],
            dept00000039[final_index][2],
            dept00000039[final_index][3]
        ])
        result_count -= len(dept00000039) - 1

    if len(dept00000040) != 0:
        final_index = len(dept00000040) - 1
        stack_json['STACKS'].append([
            dept00000040[final_index][0],
            dept00000040[final_index][1],
            dept00000040[final_index][2],
            dept00000040[final_index][3]
        ])
        result_count -= len(dept00000040) - 1

    stack_json['STACK_NUMBER'] = str(result_count)

    # [END]
    # Special care for COUNT based post ( 1 post per day )

    for element in result_json:
        # Special care for COUNT based post ( 1 post per day )
        # [START]
        if element['department_code'] == '00000039':
            pass
        elif element['department_code'] == '00000040':
            pass
        # [END]
        # Special care for COUNT based post ( 1 post per day )
        else:
            stack_json['STACKS'].append([
                element['department_code'],
                element['crawl_time'],
                element['post_title'],
                element['post_href']
            ])

    with open('../result/stacks.json', 'w') as json_out_file:
        json.dump(stack_json, json_out_file, indent='\t')

    file_name = '../result/history/stacks-' + today + '.json'
    with open(file_name, 'w') as json_out_file:
        json.dump(stack_json, json_out_file, indent='\t')

if __name__ == "__main__":
    main()