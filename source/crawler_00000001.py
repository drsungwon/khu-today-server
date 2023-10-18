import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import json
from os.path import exists


def crawling_handler(page, json_file, json_keys, max_title, max_href):
    # step.0
    # abnormal operation prohibition
    #
    try:
        if page > 10:
            raise
    except:
        print("abnormal page error.")
        raise


    # step.1
    # server access
    #
    try:
        url = 'http://swcon.khu.ac.kr/post/?mode=list&board_page=%d' % page
        html = requests.get(url, timeout=30)
        #print('[step.1] passed')
    except:
        print("http.urlopen() error.")
        raise

    # step.2
    # target region select
    #
    try:
        soup = BeautifulSoup(html.text, 'html.parser')
        s = soup.select('#DoubleMajor_board_body')

    except:
        print("soup error.")
        raise

    # retrieve record
    try:
        s = soup.find_all('tr')
        #print(s)
        if s == []:
            print("soup_find() error.")
            raise

        for item in s:
            for element in item.find_all('td', class_="mb-hide-mobile"):
                temp = element.get_text()
                if len(temp) == 10 and temp.count('-') == 2:  # 오늘 날자 게시글이 아닌 경우 (YYYY-MM-DD)
                    flag_notice = item.find(  # 공지 사항인지 확인
                        'span', class_="mb-notice mb-notice-pid")
                    if flag_notice == None:  # 공지 사항이 아닌, 일반 게시글이면, 오늘 날자 게시글이 없으니, 더 이상 crawling 하지 않음
                        return True, json_file
                elif len(temp) == 5 and temp.count(':') == 1:  # 오늘 날자 게시글인 경우 (HH:MM), crawling 진행
                    content = item.find('td', class_="text-left")
                    post_item = content.find('a')
                    # changed : start
                    if post_item.attrs['title'] in json_keys:
                        pass
                    else:
                        json_file['NUMPOSTS'] = str(int(json_file['NUMPOSTS']) + 1)
                        json_file['POSTS'].append(
                            {'INDEX': json_file['NUMPOSTS'],
                            'TITLE': post_item.attrs['title'],
                            'HREF': post_item.attrs['href'],
                            'TIME': datetime.now().isoformat()})  # new : single line
                        if len(post_item.attrs['title']) > max_title:
                            print("title size exceeds.")
                        if len(post_item.attrs['href']) > max_href:
                            print("href size exceeds.")
                    # changed : end
                else:
                    if len(temp) == 10 and temp.count('-') == 2:  # 미확인 상태
                        print("unexpected situation.")
                    else:  # 조회수 정보
                        pass
    except:
        print("crawling error.")
        raise

    return False, json_file  # 게시글의 끝까지 확인했으나, 오늘 날자 게시글이 끝나지 않았다면, 다음 페이지에서 crawling을 이어서 진행


def main():

    json_file = {}
    json_file['DEPARTMENT'] = '소프트웨어융합학과'
    json_file['UPDATED.START'] = datetime.now().isoformat()
    json_file['UPDATED.=END='] = datetime.now().isoformat()
    json_file['STATUS'] = 'PROCESS_START'
    json_file['NUMPOSTS'] = '0'
    json_file['POSTS'] = []

    with open('../configuration/database.json', 'r') as config_database_file:
        db = json.load(config_database_file)
        max_size_title = int(db['POST_TITLE_MAX_SIZE'])
        max_size_href = int(db['POST_HREF_MAX_SIZE'])

    # new : start
    json_keys = []

    file_exists = exists('../result/crawling_result_00000001.json')
    if file_exists == True:
        with open('../result/crawling_result_00000001.json', 'r') as json_in_file:
            current_json_file = json.load(json_in_file)
            log_date = datetime.fromisoformat(
                current_json_file['UPDATED.START']).date()
            if log_date == date.today():
                print("add operation.")
                json_file['UPDATED.START'] = current_json_file['UPDATED.START']
                json_file['NUMPOSTS'] = current_json_file['NUMPOSTS']
                json_file['POSTS'] = current_json_file['POSTS']
                if int(json_file['NUMPOSTS']) > 0:
                    for item in json_file['POSTS']:
                        json_keys.append(item['TITLE'])
                    #print('previous titles: ', json_keys)
            else:
                print("new operation.")
    else:
        print("new operation.")

    # new : end

    page = 1

    while True:
        try:
            job_finished, json_file = crawling_handler(
                page, json_file,
                json_keys,
                max_size_title,
                max_size_href)  # new : single line
            json_file['UPDATED.=END='] = datetime.now().isoformat()
            json_file['STATUS'] = 'OK'  # new : single line
            print("ok.")  # new : single line
        except:
            json_file['STATUS'] = 'ERROR'
            #json_file['NUMPOSTS'] = '0'
            #json_file['POSTS'] = []
            json_file['UPDATED.=END='] = datetime.now().isoformat()
            job_finished = True
            print("error.")

        if job_finished == True:
            try:
                with open('../result/crawling_result_00000001.json', 'w') as json_out_file:
                    json.dump(json_file, json_out_file, indent='\t')

                ''' logging may be added.
                '''
                print("> 00000001 : success.")

                break
            except:
                ''' logging may be added.
                '''
                print("> 00000001 : fail.")

                pass
        else:
            page += 1


if __name__ == "__main__":
    main()
