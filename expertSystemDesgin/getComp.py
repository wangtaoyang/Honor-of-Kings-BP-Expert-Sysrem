import json
import os

import requests

url1 = "https://api.91m.top/hero/v1/app.php"
os.environ['NO_PROXY'] = url1
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5958.400 SLBrowser/10.0.3533.400'}


def add_hero_compare():
    with open("heroes_class.json", 'r') as loop_f:
        name_dict = json.load(loop_f)
        for name in name_dict:
            params = {"type": "getRanking", "aid": "1", "bid": "0", "cid": "0", "did": "0", "heroName": name}
            Body = {"openId": "b0d357ec78ca3e4152373a309b9128eb", "accessToken": "ac340485fb7020b40b7e9e3367571998"}
            requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
            s = requests.session()
            s.keep_alive = False  # 关闭多余连接
            res = requests.get(url=url1, params=params, headers=headers, verify=False)
            print(res.json())
            cur_hero_comp = {}
            for comp_hero in res.json()['data']['result']['rows']:
                if comp_hero['adaptation'] > 0.5:
                    cur_hero_comp[comp_hero['hero_2']['name']] = comp_hero['adaptation']
            with open("heroes_info.json", 'r') as f:
                hero_info = json.load(f)
                for hero in hero_info:
                    if hero['name'] == name:
                        hero['fit_heroes'] = cur_hero_comp
                with open("heroes_info.json", 'w') as write_f:
                    json.dump(hero_info, write_f, indent=4, ensure_ascii=False)
                    write_f.close()
                f.close()


# add_hero_compare()

url2 = "https://api.91m.top/hero/v1/app/public/json/heroList.json?t=1643862303"


def add_hero_hot():
    res = requests.get(url=url2, verify=False)
    print(res.json())
    with open("heroes_hot.json", 'w+') as f:
        json.dump(res.json(), f, indent=4, ensure_ascii=False)
        f.close()
    f.close()
    with open("heroes_info.json", 'r') as f:
        hero_info = json.load(f)
        for hot_hero in res.json():
            for hero in hero_info:
                if hot_hero['heroName'] == hero['name']:
                    hero['hot'] = float(hot_hero['gradient'])
        with open("heroes_info.json", 'w') as write_f:
            json.dump(hero_info, write_f, indent=4, ensure_ascii=False)
            write_f.close()
        f.close()

add_hero_hot()
