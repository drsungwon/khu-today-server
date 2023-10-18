# usage example : python show-crawling-result.py 00000001

import json
import sys


def main(target):
    file = '../result/crawling_result_' + target + '.json'
    with open(file, 'r') as result_file:
        result = json.load(result_file)
        num_records = int(result['NUMPOSTS'])
        for item in result['POSTS']:
            print(item)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("usage: python3 show-crawling-result.py all")
        print("usage: python3 show-crawling-result.py {department-index}")
    elif sys.argv[1] == 'all':
        departments = ['00000001', '00000002', '00000003']
        for item in departments:
            main(item)
    else:
        main(sys.argv[1])
