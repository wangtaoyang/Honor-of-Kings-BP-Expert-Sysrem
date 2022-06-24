from PyQt5 import QtSql

hero_name = {'坦克': ['阿古朵', '白起', '嫦娥', '程咬金', '达摩', '东皇太一', '盾山', '铠', '廉颇', '刘邦'
    , '刘禅', '吕布', '蒙恬', '芈月', '牛魔', '苏烈', '孙策', '太乙真人', '夏侯惇', '项羽', '亚瑟', '张飞'
    , '钟无艳', '猪八戒', '庄周'],
             '战士': ['曹操', '程咬金', '达摩', '典韦', '暃', '宫本武藏', '关羽', '花木兰', '橘右京', '铠'
                 , '狂铁', '老夫子', '李信', '刘备', '露娜', '吕布', '马超', '蒙恬', '梦奇', '墨子', '哪吒'
                 , '盘古', '裴擒虎', '司空震', '孙策', '孙悟空', '夏侯惇', '夏洛特', '雅典娜', '亚瑟', '杨戬'
                 , '曜', '云缨', '云中君', '赵云', '钟无艳'],
             '刺客': ['阿轲', '百里守约', '百里玄策', '不知火舞', '貂蝉', '暃', '韩信', '花木兰', '镜', '橘右京'
                 , '兰陵王', '澜', '李白', '马超', '娜可露露', '裴擒虎', '上官婉儿', '司马懿', '孙悟空', '元歌'
                 , '云缨', '云中君', '赵云'],
             '法师': ['安琪拉', '扁鹊', '不知火舞', '嫦娥', '妲己', '貂蝉', '干将莫邪', '高渐离', '姜子牙', '金蝉', '露娜'
                 , '梦奇', '米莱狄', '芈月', '墨子', '女娲', '上官婉儿', '沈梦溪', '司空震', '司马懿', '孙膑', '王昭君'
                 , '武则天', '西施', '小乔', '杨玉环', '弈星', '嬴政', '张良', '甄姬', '钟馗', '周瑜', '诸葛亮'],
             '射手': ['艾琳', '百里守约', '成吉思汗', '狄仁杰', '伽罗', '公孙离', '后羿', '黄忠', '李元芳',
                    '鲁班七号', '马可波罗', '蒙犽', '孙尚香', '虞姬'],
             '辅助': ['蔡文姬', '大乔', '东皇太一', '盾山', '鬼谷子', '刘禅', '鲁班大师', '明世隐', '牛魔', '桑启', '苏烈'
                 , '孙膑', '太乙真人', '瑶', '张飞', '钟馗', '庄周']}

index = 0
final_string = ''
label_string = ''
cur_index = 0


def forDict(class_index: int, name: str):
    global final_string
    global label_string
    final_string += "self.pushButton_{0} = QtWidgets.QPushButton(self.tab_{1})\n".format(index, class_index)
    final_string += "self.pushButton_{0}.setGeometry(QtCore.QRect({1}, {2}, 100, 100))\n".format(index, (
            cur_index - 1) % 5 * 192 + 46, (cur_index - 1) // 5 * 150 + 40)
    final_string += "self.pushButton_{0}.setObjectName(\"{1}\")\n".format(index, name)
    final_string += "img_path = 'touxiang/{0}.jpg'  # 图片路径\n".format(name)
    final_string += "self.pushButton_{0}.setIcon(QtGui.QIcon(img_path))\n".format(index)
    final_string += "self.pushButton_{0}.setIconSize(QtCore.QSize(100, 100))\n".format(index)
    final_string += "self.pushButton_{0}.clicked.connect(lambda: self.writeCurrentChoose(name=self.pushButton_{1}.objectName()))\n".format(
        index, index)
    final_string += "\n"
    final_string += "self.label_{0} = QtWidgets.QLabel(self.tab_{1})\n".format(index, class_index)
    length = len(name)
    final_string += "self.label_{0}.setGeometry(QtCore.QRect({1}, {2}, {3}, 20))\n".format(index, (
            cur_index - 1) % 5 * 192 + 46 + int((100 - 15 * length) / 2), 150 * ((cur_index - 1) // 5 + 1), length * 15)
    final_string += "self.label_{0}.setObjectName(\"label_{1}\")\n\n".format(index, index)

    label_string += "self.label_{0}.setText(_translate(\"Form\", \"{1}\"))\n".format(index, name)

for name in hero_name['坦克']:
    index += 1
    cur_index += 1
    forDict(1, name)
cur_index = 0

for name in hero_name['战士']:
    index += 1
    cur_index += 1
    forDict(2, name)
cur_index = 0

for name in hero_name['刺客']:
    index += 1
    cur_index += 1
    forDict(3, name)
cur_index = 0

for name in hero_name['法师']:
    index += 1
    cur_index += 1
    forDict(4, name)
cur_index = 0

for name in hero_name['射手']:
    index += 1
    cur_index += 1
    forDict(5, name)
cur_index = 0

for name in hero_name['辅助']:
    index += 1
    cur_index += 1
    forDict(6, name)
cur_index = 0

# with open('select_hero_code.txt', 'w') as f:
#     f.write(final_string)
# with open('label_code.txt', 'w') as f:
#     f.write(label_string)
