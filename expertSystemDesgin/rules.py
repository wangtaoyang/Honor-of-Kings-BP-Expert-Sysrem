import json
import operator

rules = []
attr_name = ['recover', 'defense', 'erupt', 'penetrate', 'control', 'poke', 'speed']
res_name = ['low', 'high']
heroes_info = []
heroes_class = []
with open("heroes_info.json", 'r') as f:
    heroes_info = json.load(f)
    # print(heroes_info)
with open("heroes_class.json", 'r') as f:
    heroes_class = json.load(f)
    print(heroes_class)


class Hero:
    def __init__(self, recover, defense, erupt, penetrate, control, poke, speed, hot):
        self.recover = recover  # 恢复 1
        self.defense = defense  # 坦度 2
        self.erupt = erupt  # 爆发 3
        self.penetrate = penetrate  # 穿透 4
        self.control = control  # 控制 5
        self.poke = poke  # 消耗 6
        self.speed = speed  # 机动性 7
        self.hot = hot  # 热度 8


# enemy 和 my_hero 是两个存储了敌方特征和我方特征的list，通过在规则集合中寻找匹配的规则然后进行推理，得到特定的我方英雄对特定的敌方英雄的克制指数，并且记录原因
def get_restrained_index(enemy, my_hero, my_hero_name):
    # print(my_hero_name)
    kz_index = []
    reason = []
    for rule in rules:
        # print(enemy)
        if (enemy[attr_name[rule['forward'] - 1]] > 0 and rule['forward_res'] == 1) or (
                enemy[attr_name[rule['forward'] - 1]] < 0 and rule['forward_res'] == 0):  # 前项匹配

            if (my_hero[attr_name[rule['backward'] - 1]] > 0 and rule['backward_res'] == 1) or (
                    my_hero[attr_name[rule['backward'] - 1]] < 0 and rule['backward_res'] == 0):  # 后项匹配
                # print(rule)
                # 对于匹配的规则，将属性的cf取绝对值然后乘上规则的cf得到通过这条规则，克制指数的变化。
                kz_index.append(
                    abs(my_hero[attr_name[rule['backward'] - 1]]) * abs(enemy[attr_name[rule['forward'] - 1]]) * rule[
                        'cf'])
                # print(abs(my_hero[attr_name[rule['backward'] - 1]]) * abs(enemy[attr_name[rule['forward'] - 1]]) * rule[
                #     'cf'])
                reason.append("{0}: {1} ({2}) kz {3} ({4}) [{5}]".format(my_hero_name, attr_name[rule['backward'] - 1],
                                                                         my_hero[attr_name[rule['backward'] - 1]],
                                                                         attr_name[rule['forward'] - 1],
                                                                         enemy[attr_name[rule['forward'] - 1]],
                                                                         rule['cf']))
                # if my_hero['{0}_cf'.format(attr_name[rule['backward'] - 1])] >= 0 and rule['cf'] > 0:  # 全都大于0
                #     my_hero['{0}_cf'.format(attr_name[rule['backward'] - 1])] = my_hero['{0}_cf'.format(
                #         attr_name[rule['backward'] - 1])] + rule['cf'] - my_hero['{0}_cf'.format(
                #         attr_name[rule['backward'] - 1])] * rule['cf']
                # elif my_hero['{0}_cf'.format(attr_name[rule['backward'] - 1])] < 0 and rule['cf'] < 0:  # 全都小于0
                #     my_hero['{0}_cf'.format(attr_name[rule['backward'] - 1])] = my_hero['{0}_cf'.format(
                #         attr_name[rule['backward'] - 1])] + rule['cf'] + my_hero['{0}_cf'.format(
                #         attr_name[rule['backward'] - 1])] * rule['cf']
                # else:  # 有一个大于0，一个小于0
                #     my_hero['{0}_cf'.format(attr_name[rule['backward'] - 1])] = (my_hero['{0}_cf'.format(
                #         attr_name[rule['backward'] - 1])] + rule['cf']) / (1 - min(
                #         abs(my_hero['{0}_cf'.format(attr_name[rule['backward'] - 1])]), abs(rule['cf'])))
                # print(my_hero['{0}_cf'.format(attr_name[rule['backward'] - 1])])
    print(kz_index)
    kz_index_sum = sum(kz_index)
    # cf = 0
    # cf_sum = 0
    # for key, value in my_hero.items():
    #     cf_sum += value
    #     if "cf" in key:
    #         if cf >= 0 and value >= 0:
    #             cf = cf + value - cf * value
    #         elif cf < 0 and value < 0:
    #             cf = cf + value + cf * value
    #         else:
    #             cf = (cf + value) / (1 - min(abs(cf), abs(value)))
    # print(cf)
    # print(cf_sum)
    return kz_index_sum, reason


# 将规则存储在rules中，并且生成一份规则的txt
def rules_maker():
    global rules, attr_name, res_name
    rule1 = {'forward': 1, 'forward_res': 0, 'backward': 3, 'backward_res': 1, 'cf': 0.3}  # 高爆发克制低恢复
    rule2 = {'forward': 1, 'forward_res': 0, 'backward': 6, 'backward_res': 1, 'cf': 0.9}  # 高消耗克制低恢复
    rule3 = {'forward': 1, 'forward_res': 1, 'backward': 2, 'backward_res': 1, 'cf': -0.6}  # 高恢复克制高坦度
    rule4 = {'forward': 1, 'forward_res': 1, 'backward': 3, 'backward_res': 1, 'cf': -0.3}  # 高恢复克制高爆发
    rule5 = {'forward': 1, 'forward_res': 1, 'backward': 6, 'backward_res': 1, 'cf': -0.9}  # 高恢复克制高消耗

    rule6 = {'forward': 2, 'forward_res': 0, 'backward': 3, 'backward_res': 1, 'cf': 0.9}  # 高爆发克制低坦度
    rule7 = {'forward': 2, 'forward_res': 0, 'backward': 5, 'backward_res': 1, 'cf': 0.3}  # 高控制克制低坦度
    rule8 = {'forward': 2, 'forward_res': 0, 'backward': 6, 'backward_res': 1, 'cf': 0.3}  # 高消耗克制低坦度
    rule9 = {'forward': 2, 'forward_res': 1, 'backward': 1, 'backward_res': 1, 'cf': 0.6}  # 高恢复克制高坦度
    rule10 = {'forward': 2, 'forward_res': 1, 'backward': 3, 'backward_res': 1, 'cf': -0.3}  # 高坦度克制高爆发
    rule11 = {'forward': 2, 'forward_res': 1, 'backward': 4, 'backward_res': 1, 'cf': 0.9}  # 高穿透克制高坦度
    rule12 = {'forward': 2, 'forward_res': 1, 'backward': 6, 'backward_res': 1, 'cf': -0.3}  # 高坦度克制高消耗

    rule13 = {'forward': 3, 'forward_res': 1, 'backward': 1, 'backward_res': 0, 'cf': -0.3}  # 高爆发克制低恢复
    rule14 = {'forward': 3, 'forward_res': 1, 'backward': 1, 'backward_res': 1, 'cf': 0.3}  # 高恢复克制高爆发
    rule15 = {'forward': 3, 'forward_res': 1, 'backward': 2, 'backward_res': 1, 'cf': 0.3}  # 高坦度克制高爆发
    rule16 = {'forward': 3, 'forward_res': 1, 'backward': 2, 'backward_res': 0, 'cf': -0.9}  # 高爆发克制低坦度
    rule17 = {'forward': 3, 'forward_res': 1, 'backward': 7, 'backward_res': 0, 'cf': -0.6}  # 高爆发克制低机动性

    rule18 = {'forward': 4, 'forward_res': 1, 'backward': 2, 'backward_res': 1, 'cf': -0.9}  # 高穿透克制高坦度
    rule19 = {'forward': 4, 'forward_res': 0, 'backward': 2, 'backward_res': 1, 'cf': 0.9}  # 低穿透被高坦度克制

    rule20 = {'forward': 5, 'forward_res': 0, 'backward': 7, 'backward_res': 1, 'cf': 0.9}  # 高机动性克制低控制
    rule21 = {'forward': 5, 'forward_res': 1, 'backward': 7, 'backward_res': 1, 'cf': -0.9}  # 高控制克制高机动性
    rule22 = {'forward': 5, 'forward_res': 1, 'backward': 2, 'backward_res': 0, 'cf': -0.3}  # 高机动性克制低坦度

    rule23 = {'forward': 6, 'forward_res': 1, 'backward': 1, 'backward_res': 0, 'cf': -0.9}  # 高消耗克制低恢复
    rule24 = {'forward': 6, 'forward_res': 1, 'backward': 1, 'backward_res': 1, 'cf': 0.9}  # 高恢复克制高消耗
    rule25 = {'forward': 6, 'forward_res': 1, 'backward': 2, 'backward_res': 0, 'cf': -0.3}  # 高消耗克制低坦度
    rule26 = {'forward': 6, 'forward_res': 1, 'backward': 2, 'backward_res': 1, 'cf': 0.3}  # 高坦度克制低消耗

    index = 1
    while 'rule{0}'.format(index) in dir():
        rules.append(eval('rule{0}'.format(index)))
        index += 1
    string_final = ''
    index = 1
    for rule in rules:
        rule_str = ''
        rule_str += "rule{5}:\nif {0} = {1} then \n{2} = {3} ({4})\n\n".format(attr_name[rule['forward'] - 1],
                                                                               res_name[rule['forward_res']],
                                                                               attr_name[rule['backward'] - 1],
                                                                               res_name[rule['backward_res']],
                                                                               rule['cf'], index)
        index += 1
        string_final += rule_str

    with open('rules.txt', 'w') as f:
        f.write(string_final)


rules_maker()
# enemy_info = {'recover': -0.9, 'defense': 0.9, 'erupt': 0.8, 'penetrate': 0.1, 'control': -0.9, 'poke': -0.5,
#               'speed': -0.9, 'recover_cf': -0.9, 'defense_cf': 0.9, 'erupt_cf': 0.8, 'penetrate_cf': 0.1,
#               'control_cf': -0.9,
#               'poke_cf': -0.5,
#               'speed_cf': -0.9}
# my_hero_test1 = {'recover': 0.1, 'defense': 0.5, 'erupt': 0.1, 'penetrate': 0.9, 'control': -0.9, 'poke': 0.9,
#                  'speed': 0.9, 'recover_cf': 0.1, 'defense_cf': 0.5, 'erupt_cf': 0.1, 'penetrate_cf': 0.9,
#                  'control_cf': -0.9,
#                  'poke_cf': 0.9,
#                  'speed_cf': 0.9}
# my_hero_test2 = {'recover': 0.3, 'defense': 0.5, 'erupt': 0.9, 'penetrate': -0.5, 'control': -0.9, 'poke': -0.4,
#                  'speed': -0.4, 'recover_cf': 0.3, 'defense_cf': 0.5, 'erupt_cf': 0.9, 'penetrate_cf': -0.5,
#                  'control_cf': -0.9,
#                  'poke_cf': -0.4,
#                  'speed_cf': -0.4}

# 输入一个敌方英雄和一个我方英雄的名字，从json 中找到他们的属性并且存储，然后交给get_restrained_index函数进行比较
def compare_from_json(enemy_name, my_hero_name):
    enemy_info = {}
    my_hero = {}
    for item in heroes_info:
        if item['name'] == enemy_name:
            enemy_info['recover'] = item['recover']
            enemy_info['recover_cf'] = 0
            enemy_info['defense'] = item['defense']
            enemy_info['defense_cf'] = 0
            enemy_info['erupt'] = item['erupt']
            enemy_info['erupt_cf'] = 0
            enemy_info['penetrate'] = item['penetrate']
            enemy_info['penetrate_cf'] = 0
            enemy_info['control'] = item['control']
            enemy_info['control_cf'] = 0
            enemy_info['poke'] = item['poke']
            enemy_info['poke_cf'] = 0
            enemy_info['speed'] = item['speed']
            enemy_info['speed_cf'] = 0

        if item['name'] == my_hero_name:
            my_hero['recover'] = item['recover']
            my_hero['recover_cf'] = 0
            my_hero['defense'] = item['defense']
            my_hero['defense_cf'] = 0
            my_hero['erupt'] = item['erupt']
            my_hero['erupt_cf'] = 0
            my_hero['penetrate'] = item['penetrate']
            my_hero['penetrate_cf'] = 0
            my_hero['control'] = item['control']
            my_hero['control_cf'] = 0
            my_hero['poke'] = item['poke']
            my_hero['poke_cf'] = 0
            my_hero['speed'] = item['speed']
            my_hero['speed_cf'] = 0

    get_restrained_index(enemy_info, my_hero, my_hero_name)

# 输入一个英雄名称，生成所有英雄对该英雄的克制情况，并且生成json
def compare_all(name):
    enemy_info = {}
    cur_hero = {}
    list_res = []
    for item in heroes_info:
        if item['name'] == name:
            enemy_info['recover'] = item['recover']
            enemy_info['recover_cf'] = 0
            enemy_info['defense'] = item['defense']
            enemy_info['defense_cf'] = 0
            enemy_info['erupt'] = item['erupt']
            enemy_info['erupt_cf'] = 0
            enemy_info['penetrate'] = item['penetrate']
            enemy_info['penetrate_cf'] = 0
            enemy_info['control'] = item['control']
            enemy_info['control_cf'] = item['control']
            enemy_info['poke'] = item['poke']
            enemy_info['poke_cf'] = item['poke']
            enemy_info['speed'] = item['speed']
            enemy_info['speed_cf'] = item['speed']

    for item in heroes_info:
        if item['name'] != name:
            cur_hero['recover'] = item['recover']
            cur_hero['recover_cf'] = item['recover']
            cur_hero['defense'] = item['defense']
            cur_hero['defense_cf'] = item['defense']
            cur_hero['erupt'] = item['erupt']
            cur_hero['erupt_cf'] = item['erupt']
            cur_hero['penetrate'] = item['penetrate']
            cur_hero['penetrate_cf'] = item['penetrate']
            cur_hero['control'] = item['control']
            cur_hero['control_cf'] = item['control']
            cur_hero['poke'] = item['poke']
            cur_hero['poke_cf'] = item['poke']
            cur_hero['speed'] = item['speed']
            cur_hero['speed_cf'] = item['speed']
            kz_index_sum, reason = get_restrained_index(enemy_info, cur_hero, item['name'])
            list_res.append({'name': item['name'], 'kz_index_sum': kz_index_sum, 'reason': reason})
    with open('{0}.json'.format(name), 'w') as f:
        json.dump(list_res, f, indent=4, ensure_ascii=False)
    # print(list_res)
    return list_res


# 根据一个由五个英雄名字组成的list分析出我方推荐阵容，采用贪心算法
def compare_all_enemy(enemy_list):
    all_enemy_kz_list = []
    cur_my_heroes_list = []
    cur_my_class = []
    index = 0
    hero_index = 0
    # 将每个英雄对敌方英雄五个英雄进行克制分析，并且最终将每个英雄对敌方五个英雄的克制指数相加，原因也相加。
    for enemy in enemy_list:
        cur_enemy_kz_list = compare_all(enemy)
        if index == 0:  # 第一次循环，用当前的克制列表初始化
            for cur_enemy_kz in cur_enemy_kz_list:
                all_enemy_kz_list.append(cur_enemy_kz)
        else:
            for enemy_kz in cur_enemy_kz_list:
                if all_enemy_kz_list[hero_index]['name'] == enemy_kz['name']:
                    all_enemy_kz_list[hero_index]['kz_index_sum'] += enemy_kz['kz_index_sum']
                    all_enemy_kz_list[hero_index]['reason'].extend(enemy_kz['reason'])
                    hero_index += 1
        index += 1
        hero_index = 0
    all_enemy_kz_list = sorted(all_enemy_kz_list, key=operator.itemgetter('kz_index_sum'), reverse=True)
    with open('{0} {1} {2} {3} {4}.json'.format(enemy_list[0], enemy_list[1], enemy_list[2], enemy_list[3],
                                                enemy_list[4]), 'w') as f:
        json.dump(all_enemy_kz_list, f, indent=4, ensure_ascii=False)
    # print(all_enemy_kz_list)
    for i in range(5):
        for hero in all_enemy_kz_list:
            # 贪心算法
            if hero['name'] not in enemy_list and hero not in cur_my_heroes_list and heroes_class[
                hero['name']] not in cur_my_class:
                # 选取满足条件的得分最高的英雄,
                # 并且符合位置条件,使用贪心算法.假设我方选择英雄是理性的，我方一定会选择5个符合位置条件的英雄
                if heroes_class[hero['name']] == 1:
                    cur_my_class.append(1)
                    cur_my_heroes_list.append(hero)
                elif heroes_class[hero['name']] == 2:
                    cur_my_class.append(2)
                    cur_my_heroes_list.append(hero)
                elif heroes_class[hero['name']] == 3:
                    cur_my_class.append(3)
                    cur_my_heroes_list.append(hero)
                elif heroes_class[hero['name']] == 4:
                    cur_my_class.append(4)
                    cur_my_heroes_list.append(hero)
                elif heroes_class[hero['name']] == 5:
                    cur_my_class.append(5)
                    cur_my_heroes_list.append(hero)
    print(cur_my_heroes_list)
    return cur_my_heroes_list

# compare_from_json('阿古朵', '白起')
# compare_from_json('阿古朵', '嫦娥')
# compare_all("嫦娥")
# compare_all("白起")
# test_enemys = ['廉颇', '盘古', '嫦娥', '黄忠', '猪八戒']
# compare_all_enemy(test_enemys)
#
# get_restrained_index(enemy_info, my_hero_test1)
# get_restrained_index(enemy_info, my_hero_test2)
