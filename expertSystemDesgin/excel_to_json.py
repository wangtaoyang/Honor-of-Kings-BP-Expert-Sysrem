# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import json
import collections


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


area_data = pd.read_excel('heroes_info.xlsx', engine="openpyxl", sheet_name='Sheet1')
one_cell = area_data.iat[0, 2]
heroes_info = []
heroes_class = {}
# print(one_cell)
for i in range(len(area_data)):
    hero_info = {}
    hero_info['id'] = area_data.iat[i, 0]
    hero_info['class'] = area_data.iat[i, 1]
    hero_info['name'] = area_data.iat[i, 2]
    hero_info['recover'] = area_data.iat[i, 3]
    hero_info['defense'] = area_data.iat[i, 4]
    hero_info['erupt'] = area_data.iat[i, 5]
    hero_info['penetrate'] = area_data.iat[i, 6]
    hero_info['control'] = area_data.iat[i, 7]
    hero_info['poke'] = area_data.iat[i, 8]
    hero_info['speed'] = area_data.iat[i, 9]
    hero_info['hot'] = area_data.iat[i, 10]
    # 加入队友搭配指数
    partners_dict = {}
    if area_data.iat[i, 11] is not np.nan:
        partners = area_data.iat[i, 11].split(' ')
        partners_fit_index = area_data.iat[i, 12].split(' ')
        for j in range(len(partners)):
            partners_dict[partners[j]] = float(partners_fit_index[j])
    hero_info['fit_heroes'] = partners_dict
    heroes_info.append(hero_info)
    heroes_class['{0}'.format(hero_info['name'])] = hero_info['class']
    with open('heroes_class.json', 'w') as f:
        json.dump(heroes_class, f, indent=4, ensure_ascii=False, cls=NpEncoder)


print(heroes_info)
with open('heroes_info.json', 'w') as f:
    json.dump(heroes_info, f, ensure_ascii=False, indent=4, cls=NpEncoder)
# print(area_data)
# indicator = area_data.columns[3:].tolist()
# print(indicator)
#
# f = open("newAreaData.json", "w+")
# for i in range(len(area_data)):
#     area_dict = collections.OrderedDict()  ##利用OrderedDict()建立有序词典
#     area_dict['area'] = area_data.ix[i, '新区名称']
#     area_dict['lng'] = str(area_data.ix[i, '纬度'])
#     area_dict['lat'] = str(area_data.ix[i, '经度'])
#
#     area_dict['indicators'] = indicator
#     value_list = area_data.iloc[i, 3:].tolist()
#     value_list_new = [str(x) for x in value_list]
#     # value_list.append(area_data.iloc[i,3:].tolist().astype(str))
#     area_dict['values'] = value_list_new
#     # print (area_dict)
#
#     # 使用json模块将构造好的字典保存到文件中
#     # area_dict.encode("utf-8")
#     f.writelines(json.dumps(area_dict, ensure_ascii=False, indent=4) + ',\n')
# f.close()  # 将文件关闭
#
# for i
