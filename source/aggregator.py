import json
import pymysql
from datetime import date
from datetime import datetime
from os.path import exists

def main():

    # step.1 mysql connect
    db_today = pymysql.connect(
        user='root', passwd='rootpassword', host='127.0.0.1', db='today', charset='utf8')
    db_cursor = db_today.cursor(pymysql.cursors.DictCursor)
    dept_json = {}

    # step.2 department.json read for aggregation list and time retrival
    print("\n\n::== aggregation start ==::")
    with open('../configuration/department.json', 'r') as index_department_file:
        dept_json = json.load(index_department_file)

    for count in range(0, len(dept_json['DEPARTMENTS'])):

        # step.3 [start] retrive each crawler's output
        #
        file = '../result/crawling_result_' + \
            dept_json['DEPARTMENTS'][count]["INDEX"] + '.json'

        file_exists = exists(file)
        if file_exists == True:
            with open(file, 'r') as result_file:
                crawl_json = json.load(result_file)

                for item in crawl_json['POSTS']:

                    if item['TIME'] > dept_json['DEPARTMENTS'][count]["AGGREGATION_TIME"]:

                        try:
                            sql_command = 'INSERT INTO today_table VALUES('\
                                + "'" + dept_json['DEPARTMENTS'][count]["INDEX"] + "', "\
                                + "'" + item['TIME'] + "', "\
                                + "'" + item['TITLE'] + "', "\
                                + "'" + item['HREF'] + "', "\
                                + "now());"

                            result = db_cursor.execute(sql_command)
                            db_today.commit()

                            if result != 1:
                                print("sql insert error.")

                            print('[ok_] new aggregation.')
                        except:
                            print('[err] ', sql_command)

                dept_json['DEPARTMENTS'][count]["AGGREGATION_TIME"] = datetime.now(
                ).isoformat()
        else:
            print('not-found: ', dept_json['DEPARTMENTS'][count]["INDEX"])
        #
        # step.3 [end] retrive each crawler's output

    # step.4 wrapup process
    dept_json["UPDATED"] = datetime.now().isoformat()

    with open('../configuration/department.json', 'w') as json_out_file:
        json.dump(dept_json, json_out_file, indent='\t')

    print("::== aggregation   end ==::\n")


if __name__ == "__main__":
    main()
