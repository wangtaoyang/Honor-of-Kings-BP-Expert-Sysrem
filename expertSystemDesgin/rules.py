import json
import operator
import random

import numpy as np


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
                reason.append(
                    "{0}: {1} ({2}) kz {3} ({4}) [{5}] score: {6}".format(my_hero_name, attr_name[rule['backward'] - 1],
                                                                          my_hero[attr_name[rule['backward'] - 1]],
                                                                          attr_name[rule['forward'] - 1],
                                                                          enemy[attr_name[rule['forward'] - 1]],
                                                                          rule['cf'], abs(
                            my_hero[attr_name[rule['backward'] - 1]]) * abs(enemy[attr_name[rule['forward'] - 1]]) *
                                                                          rule[
                                                                              'cf']))
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


def analyse_hot(hot):
    if hot == 0:
        return 2
    elif hot == 0.5:
        return 1.5
    elif hot == 1:
        return 1
    elif hot == 2:
        return 0.5
    else:
        return 0


# 将规则存储在rules中，并且生成一份规则的txt
def rules_maker():
    global rules, attr_name, res_name
    # 恢复
    rule1 = {'forward': 1, 'forward_res': 0, 'backward': 3, 'backward_res': 1, 'cf': 0.4}  # 高爆发克制低恢复
    rule2 = {'forward': 1, 'forward_res': 0, 'backward': 6, 'backward_res': 1, 'cf': 0.8}  # 高消耗克制低恢复
    rule3 = {'forward': 1, 'forward_res': 1, 'backward': 2, 'backward_res': 1, 'cf': -0.4}  # 高恢复克制高坦度
    rule4 = {'forward': 1, 'forward_res': 1, 'backward': 3, 'backward_res': 1, 'cf': -0.4}  # 高恢复克制高爆发
    rule5 = {'forward': 1, 'forward_res': 1, 'backward': 6, 'backward_res': 1, 'cf': -0.4}  # 高恢复克制高消耗

    # 坦度
    rule6 = {'forward': 2, 'forward_res': 0, 'backward': 3, 'backward_res': 1, 'cf': 0.8}  # 高爆发克制低坦度
    rule7 = {'forward': 2, 'forward_res': 0, 'backward': 5, 'backward_res': 1, 'cf': 0.4}  # 高控制克制低坦度
    rule8 = {'forward': 2, 'forward_res': 0, 'backward': 6, 'backward_res': 1, 'cf': 0.6}  # 高消耗克制低坦度
    rule9 = {'forward': 2, 'forward_res': 1, 'backward': 1, 'backward_res': 1, 'cf': 0.4}  # 高恢复克制高坦度
    rule10 = {'forward': 2, 'forward_res': 1, 'backward': 3, 'backward_res': 1, 'cf': -0.6}  # 高坦度克制高爆发
    rule11 = {'forward': 2, 'forward_res': 1, 'backward': 4, 'backward_res': 1, 'cf': 0.8}  # 高穿透克制高坦度
    rule12 = {'forward': 2, 'forward_res': 1, 'backward': 6, 'backward_res': 1, 'cf': -0.4}  # 高坦度克制高消耗

    # 爆发
    rule13 = {'forward': 3, 'forward_res': 1, 'backward': 1, 'backward_res': 0, 'cf': -0.4}  # 高爆发克制低恢复
    rule14 = {'forward': 3, 'forward_res': 1, 'backward': 1, 'backward_res': 1, 'cf': 0.4}  # 高恢复克制高爆发
    rule15 = {'forward': 3, 'forward_res': 1, 'backward': 2, 'backward_res': 1, 'cf': 0.6}  # 高坦度克制高爆发
    rule16 = {'forward': 3, 'forward_res': 1, 'backward': 2, 'backward_res': 0, 'cf': -0.8}  # 高爆发克制低坦度
    rule17 = {'forward': 3, 'forward_res': 1, 'backward': 7, 'backward_res': 0, 'cf': -0.6}  # 高爆发克制低机动性

    # 穿透
    rule18 = {'forward': 4, 'forward_res': 1, 'backward': 2, 'backward_res': 1, 'cf': -1}  # 高穿透克制高坦度
    rule19 = {'forward': 4, 'forward_res': 0, 'backward': 2, 'backward_res': 1, 'cf': 1}  # 低穿透被高坦度克制

    # 控制
    rule20 = {'forward': 5, 'forward_res': 0, 'backward': 7, 'backward_res': 1, 'cf': 0.8}  # 高机动性克制低控制
    rule21 = {'forward': 5, 'forward_res': 1, 'backward': 7, 'backward_res': 1, 'cf': -0.8}  # 高控制克制高机动性
    rule22 = {'forward': 5, 'forward_res': 1, 'backward': 2, 'backward_res': 0, 'cf': -0.4}  # 高控制克制低坦度

    # 消耗
    rule23 = {'forward': 6, 'forward_res': 1, 'backward': 1, 'backward_res': 0, 'cf': -0.8}  # 高消耗克制低恢复
    rule24 = {'forward': 6, 'forward_res': 1, 'backward': 1, 'backward_res': 1, 'cf': 0.4}  # 高恢复克制高消耗
    rule25 = {'forward': 6, 'forward_res': 1, 'backward': 2, 'backward_res': 0, 'cf': -0.6}  # 高消耗克制低坦度
    rule26 = {'forward': 6, 'forward_res': 1, 'backward': 2, 'backward_res': 1, 'cf': 0.4}  # 高坦度克制低消耗

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

            my_hero['hot'] = item['hot']

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

            cur_hero['hot'] = item['hot']
            kz_index_sum, reason = get_restrained_index(enemy_info, cur_hero, item['name'])
            list_res.append(
                {'name': item['name'], 'kz_index_sum': kz_index_sum, 'reason': reason, 'hot': cur_hero['hot']})
    with open('testJson/{0}.json'.format(name), 'w') as f:
        json.dump(list_res, f, indent=4, ensure_ascii=False)
    # print(list_res)
    return list_res


# 生成每个英雄对其他所有英雄的克制情况json
def make_all_kz_info():
    for item in heroes_info:
        compare_all(item['name'])


# 根据新加入阵容的英雄，更新所有的搭档的权重，并且返回更新之后的all_enemy_list, 这里要注意，不仅要更新当前加入英雄的所有搭档的权重，还要更新搭档中有当前角色的英雄权重，但是，只需要更新一次
def update_pick_list(cur_name, all_enemy_kz_list, cur_heroes):
    # 遍历所有搭档的名字
    name_list = [item['name'] for item in cur_heroes]
    for comp_hero in heroes_comp[cur_name]:
        for item in all_enemy_kz_list:
            if item['name'] == comp_hero and comp_hero not in name_list:
                item['kz_index_sum'] += COOP_WEIGHT * heroes_comp[cur_name][comp_hero]
                item['reason'].append(
                    "{0}: partner: {1}  score: {2}".format(comp_hero, cur_name, heroes_comp[cur_name][comp_hero]))
    for item in all_enemy_kz_list:
        # 还需要考虑当前角色成为其他角色搭档，但是当前角色中没有该搭档的可能性
        if cur_name in heroes_comp[item['name']] and item['name'] not in heroes_comp[cur_name] and item[
            'name'] not in name_list:
            item['kz_index_sum'] += COOP_WEIGHT * heroes_comp[item['name']][cur_name]
            item['reason'].append(
                "{0}: partner: {1}  score: {2}".format(item['name'], cur_name, heroes_comp[item['name']][cur_name]))
    all_enemy_kz_list = sorted(all_enemy_kz_list, key=operator.itemgetter('kz_index_sum'), reverse=True)
    return all_enemy_kz_list


# 根据一个由五个英雄名字组成的list分析出我方推荐阵容，采用贪心算法
def compare_all_enemy(enemy_list):
    all_enemy_kz_list = []
    cur_my_heroes_list = []
    cur_my_class = []
    index = 0
    # 将每个英雄对敌方英雄五个英雄进行克制分析，并且最终将每个英雄对敌方五个英雄的克制指数相加，原因也相加。
    for enemy in enemy_list:
        with open("testJson/{}.json".format(enemy), 'r') as enemy_f:
            cur_enemy_kz_list = json.load(enemy_f)
            for to_be_delete_enemy in enemy_list:
                for item in cur_enemy_kz_list:
                    if item['name'] == to_be_delete_enemy:
                        cur_enemy_kz_list.remove(item)
            if index == 0:  # 第一次循环，用当前的克制列表初始化
                for cur_enemy_kz in cur_enemy_kz_list:
                    all_enemy_kz_list.append(cur_enemy_kz)
            elif index == 4:  # 最后一次循环，需要加上英雄的热度，并且要计算克制程度的权重和英雄热度的权重
                for hero_index in range(len(all_enemy_kz_list)):
                    if all_enemy_kz_list[hero_index]['name'] == cur_enemy_kz_list[hero_index]['name']:
                        all_enemy_kz_list[hero_index]['kz_index_sum'] += cur_enemy_kz_list[hero_index]['kz_index_sum']
                        all_enemy_kz_list[hero_index]['reason'].extend(cur_enemy_kz_list[hero_index]['reason'])
                        # 最后一次加上考虑英雄热度和权重，并且增加原因
                        all_enemy_kz_list[hero_index]['kz_index_sum'] = all_enemy_kz_list[hero_index][
                                                                            'kz_index_sum'] * KZ_WEIGHT + analyse_hot(
                            cur_enemy_kz_list[hero_index]['hot']) * HOT_WEIGHT
                        all_enemy_kz_list[hero_index]['reason'].append(
                            '{0}: gradient is {1} score: {2}'.format(cur_enemy_kz_list[hero_index]['name'],
                                                                     cur_enemy_kz_list[hero_index]['hot'], analyse_hot(
                                    cur_enemy_kz_list[hero_index]['hot'])))
                    else:
                        print("WRONG!")
            else:  # 中间循环，直接叠加
                for hero_index in range(len(all_enemy_kz_list)):
                    if all_enemy_kz_list[hero_index]['name'] == cur_enemy_kz_list[hero_index]['name']:
                        all_enemy_kz_list[hero_index]['kz_index_sum'] += cur_enemy_kz_list[hero_index]['kz_index_sum']
                        all_enemy_kz_list[hero_index]['reason'].extend(cur_enemy_kz_list[hero_index]['reason'])
            index += 1
    all_enemy_kz_list = sorted(all_enemy_kz_list, key=operator.itemgetter('kz_index_sum'), reverse=True)
    with open('{0} {1} {2} {3} {4}.json'.format(enemy_list[0], enemy_list[1], enemy_list[2], enemy_list[3],
                                                enemy_list[4]), 'w') as f:
        json.dump(all_enemy_kz_list, f, indent=4, ensure_ascii=False)

    # 遗传算法初始化
    # GA_algorithm(enemy_list, all_enemy_kz_list)
    # print(all_enemy_kz_list)
    final_kz_index = 0
    # 合作指数
    coop_index = 0
    # 选择5次我方英雄，每次选择都从剩余位置中找到克制程度最高的英雄
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
                    final_kz_index += hero['kz_index_sum']
                    # 考虑增加了某个英雄之后all_enemy_kz_list 的变化
                    all_enemy_kz_list = update_pick_list(hero['name'], all_enemy_kz_list, cur_my_heroes_list)
                    break
                elif heroes_class[hero['name']] == 2:
                    cur_my_class.append(2)
                    cur_my_heroes_list.append(hero)
                    final_kz_index += hero['kz_index_sum']
                    all_enemy_kz_list = update_pick_list(hero['name'], all_enemy_kz_list, cur_my_heroes_list)
                    break
                elif heroes_class[hero['name']] == 3:
                    cur_my_class.append(3)
                    cur_my_heroes_list.append(hero)
                    final_kz_index += hero['kz_index_sum']
                    all_enemy_kz_list = update_pick_list(hero['name'], all_enemy_kz_list, cur_my_heroes_list)
                    break
                elif heroes_class[hero['name']] == 4:
                    cur_my_class.append(4)
                    cur_my_heroes_list.append(hero)
                    final_kz_index += hero['kz_index_sum']
                    all_enemy_kz_list = update_pick_list(hero['name'], all_enemy_kz_list, cur_my_heroes_list)
                    break
                elif heroes_class[hero['name']] == 5:
                    cur_my_class.append(5)
                    cur_my_heroes_list.append(hero)
                    final_kz_index += hero['kz_index_sum']
                    all_enemy_kz_list = update_pick_list(hero['name'], all_enemy_kz_list, cur_my_heroes_list)
                    break
    print(cur_my_heroes_list)
    print(final_kz_index)
    return cur_my_heroes_list


# 仅仅根据当前我方已经选择的英雄和当前加入到队伍中的英雄来计算是否有搭配得分
def cal_coop_score_for_my_team(cur_my_team, cur_hero):
    coop_score = 0
    reason = []
    for hero in cur_my_team:
        if cur_hero in heroes_comp[hero]:
            coop_score += heroes_comp[hero][cur_hero]
            reason.append("{0}: partner: {1}  score: {2}".format(cur_hero, hero, heroes_comp[hero][cur_hero]))
        elif hero in heroes_comp[cur_hero]:
            coop_score += heroes_comp[cur_hero][hero]
            reason.append("{0}: partner: {1}  score: {2}".format(hero, cur_hero, heroes_comp[cur_hero][hero]))
    return coop_score, reason


# 对给定的我方阵容和对方阵容，计算克制程度
def cal_score_for_my_team(enemy_team, my_team):
    reason = []
    all_score = 0
    hot = 5
    cur_my_team = []
    kz_index = 0
    hot_index = 0
    coop_index = 0
    # 在现有的json 文件中，已经计算好了英雄的克制程度，我们只需要对克制情况进行叠加以及增加英雄热度指数和英雄搭配指数
    for my_hero in my_team:
        score = 0
        for enemy_name in enemy_team:
            with open("testJson/{}.json".format(enemy_name), 'r') as f:
                enemy_kz_info = json.load(f)
                for item in enemy_kz_info:
                    if item['name'] == my_hero:
                        score += item['kz_index_sum']
                        reason.extend(item['reason'])
                        hot = item['hot']
        # 完成所有英雄克制程度的合并之后，加上考虑英雄本身的热度以及权重
        reason.append('{0}: gradient is {1} score: {2}'.format(my_hero, hot, analyse_hot(hot)))
        # 计算当前我方英雄加入阵容，带来的阵容搭配收益， 并且记录原因
        coop_score, coop_reason = cal_coop_score_for_my_team(cur_my_team, my_hero)
        cur_my_team.append(my_hero)
        all_score += (score * KZ_WEIGHT + analyse_hot(hot) * HOT_WEIGHT + coop_score * COOP_WEIGHT)
        # 分别记录三项参数，方便数据的分析
        kz_index += score
        hot_index += analyse_hot(hot)
        coop_index += coop_score
        reason.extend(coop_reason)
    # print(all_score)
    # print(kz_index)
    # print(hot_index)
    # print(coop_index)
    # print(reason)
    return all_score, reason


# def init_population(enemy, all_enemy_kz_info):
#     population_num = 200
#     population = []
#     class1_heroes = []
#     class1_heroes_index = []
#     class2_heroes = []
#     class2_heroes_index = []
#     class3_heroes = []
#     class3_heroes_index = []
#     class4_heroes = []
#     class4_heroes_index = []
#     class5_heroes = []
#     class5_heroes_index = []
#     heroes = []
#     heroes_p = []
#     for hero in all_enemy_kz_info:
#
#         if hero['name'] not in enemy:
#             if heroes_class[hero['name']] == 1:
#                 class1_heroes.append(hero['name'])
#                 class1_heroes_index.append(hero['kz_index_sum'])
#             elif heroes_class[hero['name']] == 2:
#                 class2_heroes.append(hero['name'])
#                 class2_heroes_index.append(hero['kz_index_sum'])
#             elif heroes_class[hero['name']] == 3:
#                 class3_heroes.append(hero['name'])
#                 class3_heroes_index.append(hero['kz_index_sum'])
#             elif heroes_class[hero['name']] == 4:
#                 class4_heroes.append(hero['name'])
#                 class4_heroes_index.append(hero['kz_index_sum'])
#             else:
#                 class5_heroes.append(hero['name'])
#                 class5_heroes_index.append(hero['kz_index_sum'])
#     heroes.append(class1_heroes)
#     heroes_p.append(class1_heroes_index)
#     heroes.append(class2_heroes)
#     heroes_p.append(class2_heroes_index)
#     heroes.append(class3_heroes)
#     heroes_p.append(class3_heroes_index)
#     heroes.append(class4_heroes)
#     heroes_p.append(class4_heroes_index)
#     heroes.append(class5_heroes)
#     heroes_p.append(class5_heroes_index)
#     for i in range(0, 5):
#         min_score = min(heroes_p[i])
#         if min_score < 0:
#             for j in range(len(heroes_p[i])):
#                 heroes_p[i][j] -= min_score
#                 heroes_p[i][j] = heroes_p[i][j] * heroes_p[i][j]
#         sum_score = sum(heroes_p[i])
#         for j in range(len(heroes_p[i])):
#             heroes_p[i][j] = heroes_p[i][j] / sum_score
#     init_score = []
#     while True:
#         if len(population) == population_num:
#             break
#         cur_my_team = []
#         for j in range(5):
#             cur_my_team.append(np.random.choice(heroes[j], 1, p=heroes_p[j])[0])
#         if cur_my_team not in population:
#             population.append(cur_my_team)
#             cur_team_score, reason = cal_score_for_my_team(enemy, cur_my_team)
#             init_score.append(cur_team_score)
#
#     print(population)
#     print(population[init_score.index(max(init_score))])
#     # init_score.sort(reverse=True)
#     print(init_score)
#     return population,


def GA_algorithm(enemy, all_enemy_kz_info):
    population_num = 200

    # 初始化
    population = []
    class1_heroes = []
    class1_heroes_index = []
    class2_heroes = []
    class2_heroes_index = []
    class3_heroes = []
    class3_heroes_index = []
    class4_heroes = []
    class4_heroes_index = []
    class5_heroes = []
    class5_heroes_index = []
    heroes = []
    heroes_p = []
    for hero in all_enemy_kz_info:

        if hero['name'] not in enemy:
            if heroes_class[hero['name']] == 1:
                class1_heroes.append(hero['name'])
                class1_heroes_index.append(hero['kz_index_sum'])
            elif heroes_class[hero['name']] == 2:
                class2_heroes.append(hero['name'])
                class2_heroes_index.append(hero['kz_index_sum'])
            elif heroes_class[hero['name']] == 3:
                class3_heroes.append(hero['name'])
                class3_heroes_index.append(hero['kz_index_sum'])
            elif heroes_class[hero['name']] == 4:
                class4_heroes.append(hero['name'])
                class4_heroes_index.append(hero['kz_index_sum'])
            else:
                class5_heroes.append(hero['name'])
                class5_heroes_index.append(hero['kz_index_sum'])
    heroes.append(class1_heroes)
    heroes_p.append(class1_heroes_index)
    heroes.append(class2_heroes)
    heroes_p.append(class2_heroes_index)
    heroes.append(class3_heroes)
    heroes_p.append(class3_heroes_index)
    heroes.append(class4_heroes)
    heroes_p.append(class4_heroes_index)
    heroes.append(class5_heroes)
    heroes_p.append(class5_heroes_index)
    for i in range(0, 5):
        min_score = min(heroes_p[i])
        if min_score < 0:
            for j in range(len(heroes_p[i])):
                heroes_p[i][j] -= min_score
                heroes_p[i][j] = heroes_p[i][j] * heroes_p[i][j]
        sum_score = sum(heroes_p[i])
        for j in range(len(heroes_p[i])):
            heroes_p[i][j] = heroes_p[i][j] / sum_score
    init_score = []
    while True:
        if len(population) >= population_num:
            break
        cur_my_team = []
        for j in range(5):
            cur_my_team.append(np.random.choice(heroes[j], 1, p=heroes_p[j])[0])
        if cur_my_team not in population:
            population.append(cur_my_team)
            cur_team_score, reason = cal_score_for_my_team(enemy, cur_my_team)
            init_score.append(cur_team_score)

    print(population)
    print(population[init_score.index(max(init_score))])
    # init_score.sort(reverse=True)
    print(init_score)

    pre_population = population
    pre_p = []
    # 交叉概率
    cross_p = 0.7
    # 突变概率
    change_p = 0.001

    init_sum_score = sum(init_score)
    for i in range(len(init_score)):
        pre_p.append(init_score[i] / init_sum_score)
    iteration_num = 100
    score_in_all_iteration = []
    max_in_all_iteration = []
    # 迭代遗传多次
    for i in range(iteration_num):
        print(i)
        max_score = 0
        next_population = []
        next_score = []
        while True:
            # 以一定概率在父辈中选中双亲
            if len(next_population) >= population_num:
                break
            parent = np.random.choice(list(range(0, len(population))), 2, p=pre_p)
            test = random.random()
            if test < cross_p:
                change_position = np.random.choice([0, 1, 2, 3, 4], 2, p=[0.2, 0.2, 0.2, 0.2, 0.2])
                temp = population[parent[0]][change_position[0]]
                population[parent[0]][change_position[0]] = population[parent[1]][change_position[0]]
                population[parent[1]][change_position[0]] = temp

                temp = population[parent[0]][change_position[1]]
                population[parent[0]][change_position[1]] = population[parent[1]][change_position[1]]
                population[parent[1]][change_position[1]] = temp

                child1 = population[parent[0]]
                child2 = population[parent[1]]
                if test < change_p:
                    change_position = random.randint(0, 4)
                    child1[change_position] = np.random.choice(heroes[change_position], 1, p=heroes_p[change_position])[0]
                    child2[change_position] = np.random.choice(heroes[change_position], 1, p=heroes_p[change_position])[0]
                if child1 not in next_population:
                    next_population.append(child1)
                if child2 not in next_population:
                    next_population.append(child2)
        for j in range(len(next_population)):
            score, reason = cal_score_for_my_team(enemy, next_population[j])
            next_score.append(score)
        cur_max_score = max(next_score)
        max_in_all_iteration.append(cur_max_score)
        score_in_all_iteration.append(next_score)
    print()
    print(max_in_all_iteration)
    print(score_in_all_iteration)


# 定义一些重要的数据
rules = []
attr_name = ['recover', 'defense', 'erupt', 'penetrate', 'control', 'poke', 'speed']
res_name = ['low', 'high']
heroes_info = []
heroes_class = []
heroes_comp = {}
# 宏定义层次分析法权重
KZ_WEIGHT = 0.65
HOT_WEIGHT = 0.23
COOP_WEIGHT = 0.12

# 初始化重要的数据，从json中读取
with open("heroes_info.json", 'r') as f:
    heroes_info = json.load(f)
    for fit_hero_item in heroes_info:
        heroes_comp[fit_hero_item['name']] = fit_hero_item['fit_heroes']
    # print(heroes_info)
with open("heroes_class.json", 'r') as f:
    heroes_class = json.load(f)
    print(heroes_class)

# 生成克制关系规则，放在rules中
rules_maker()

# 重新生成知识库
make_all_kz_info()

# 生成所有的英雄对其他英雄的克制指数，放到testJson 文件夹
# make_all_kz_info()

# compare_from_json('阿古朵', '白起')
# compare_from_json('阿古朵', '嫦娥')
# compare_all("嫦娥")
# compare_all("白起")
# test_enemys = ['廉颇', '盘古', '嫦娥', '黄忠', '猪八戒']
# test_my_team = ['芈月', '澜', '貂蝉', '马可波罗', '蔡文姬']
# # cal_score_for_my_team(test_enemys, test_my_team)
# compare_all_enemy(test_enemys)
#
# max_score, reason = cal_score_for_my_team(test_enemys, test_my_team)
# print(max_score)
# print(reason)
# compare_all_enemy(test_enemys)
#
# get_restrained_index(enemy_info, my_hero_test1)
# get_restrained_index(enemy_info, my_hero_test2)
