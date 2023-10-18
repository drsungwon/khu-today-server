# usage : python show-department.py

import json
import sys
from os.path import exists
from datetime import date
from datetime import datetime


def main():

    print("\n\n::== betify-log start  ==::")


    _departmentCode = ''
    json_file = {}
    flag = False
    flag_err_count = 0

    with open('../configuration/department.json', 'r') as index_department_file:
        with open('../result/log/log.txt', 'w') as log_file:
            dept = json.load(index_department_file)
            for item in dept['DEPARTMENTS']:
                _departmentCode = item['INDEX']
                # print(_departmentCode)
                json_final_name = '../result/crawling_result_' + _departmentCode + '.json'
                file_exists = exists(json_final_name)
                if file_exists == True:
                    with open(json_final_name, 'r') as json_in_file:
                        current_json_file = json.load(json_in_file)
                        log_date = datetime.fromisoformat(
                            current_json_file['UPDATED.START']).date()
                        if log_date == date.today():
                            # print("add operation.")
                            json_file['UPDATED.START'] = current_json_file['UPDATED.START']
                            json_file['UPDATED.=END='] = current_json_file['UPDATED.=END=']
                            json_file['NUMPOSTS'] = current_json_file['NUMPOSTS']
                            json_file['STATUS'] = current_json_file['STATUS']
                            # print(json_file)

                            msg = _departmentCode + ', '
                            if json_file['STATUS'] == "OK":
                                msg += 'ok, '
                                msg += item['TITLE']
                                msg += '\n'
                                # log_file.write(msg)
                            elif json_file['STATUS'] == "ERROR":
                                msg += 'ERROR, '
                                msg += item['TITLE']
                                msg += '\n'
                                log_file.write(msg)

                                flag_err_count += 1
                            else:
                                msg += 'UNKNOWN, '
                                msg += item['TITLE']
                                msg += '\n'
                                log_file.write(msg)

                            # msg += str(datetime.fromisoformat(json_file['UPDATED.=END='])) + ', '
                            msg_time = '\n--> ' + str(datetime.fromisoformat(json_file['UPDATED.=END=']))

                            flag = True
            
            if flag_err_count != 0:
                msg = '\n--> error : ' + str(flag_err_count)
            else:
                msg = '\n--> error : none'

            log_file.write(msg_time)
            log_file.write(msg)

    if flag == True:
        backup_file_name = str(datetime.fromisoformat(datetime.now().isoformat()))[:16].replace(' ', '_').replace(':', '-')

        if flag_err_count != 0:
            backup_file_name += '_ERROR'

        backup_file_name += '.txt'

        print(' ==> ', backup_file_name)

        backup_file_name = '../result/log/' + backup_file_name
        with open(backup_file_name, 'w') as log_backup_file:
            with open('../result/log/log.txt', 'r') as log_file:
                f = log_file.read()
                log_backup_file.write(f)
    else:
        print(' ==> no-log', )

    
    print("::== betify-log   end  ==::\n\n")

    '''
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
    '''


if __name__ == "__main__":
    main()
