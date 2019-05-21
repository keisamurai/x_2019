# ///////////////////////////////
# // get_appstore_data.py
# ///////////////////////////////
import requests
import json

def get_apple_store_data(app_id):
    """
    description: apple store から対象のapp_idに関連するレビュー情報を取得して、一覧表示する。
    """
    QUERY_URL='https://itunes.apple.com/jp/rss/customerreviews/id={0}/json'.format(app_id)
    res = requests.get(QUERY_URL)
    json_body = res.json()
    return json_body


def draw_rate(rate):
    """
    description: レートを★表示する
    args       : (int)rate -> レート
    return     : none
    """
    if isinstance(rate, str):
        rate = int(rate)

    star = ''
    for i in range(rate):
        star += '★'
    print(star)

if __name__ == '__main__':
    APP_ID = 1200433570
    json_reputation = get_apple_store_data(APP_ID)
    entry = json_reputation['feed']['entry']
    length = len(entry) - 1
    for i in range(length):
        entry = json_reputation['feed']['entry'][i]
        name = entry['author']['name']['label']
        contents = entry['content']['label']
        title = entry['title']['label']
        rate = entry['im:rating']['label']

        print(name)
        draw_rate(rate)
        print(contents)
        print(title)
        
        print('--------------------------------------')

    print(json_reputation)