# coding:utf-8

from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
import sys

from PyQt5.QtWidgets import QApplication

'''
    州的先生 - 在PyQt5中使用数据库
'''


class MainUi(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUi()

    # 初始化UI界面
    def initUi(self):
        # 设置窗口标题
        self.setWindowTitle("州的先生 - 在PyQt5中使用数据库")
        # 设置窗口大小
        self.resize(600, 400)

        # 创建一个窗口部件
        self.widget = QtWidgets.QWidget()
        # 创建一个网格布局
        self.grid_layout = QtWidgets.QGridLayout()
        # 设置窗口部件的布局为网格布局
        self.widget.setLayout(self.grid_layout)

        # 创建一个按钮组
        self.group_box = QtWidgets.QGroupBox('数据库按钮')
        self.group_box_layout = QtWidgets.QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)
        # 创建一个表格部件
        self.table_widget = QtWidgets.QTableView()
        # 将上述两个部件添加到网格布局中
        self.grid_layout.addWidget(self.group_box, 0, 0)
        self.grid_layout.addWidget(self.table_widget, 0, 1)

        # 创建按钮组的按钮
        self.b_create_db = QtWidgets.QPushButton("创建数据库")
        self.b_create_db.clicked.connect(self.create_db)
        self.b_view_data = QtWidgets.QPushButton("浏览数据")
        self.b_view_data.clicked.connect(self.view_data)
        self.b_add_row = QtWidgets.QPushButton("添加一行")
        self.b_add_row.clicked.connect(self.add_row_data)
        self.b_delete_row = QtWidgets.QPushButton("删除一行")
        self.b_delete_row.clicked.connect(self.del_row_data)
        self.b_close = QtWidgets.QPushButton("退出")
        self.b_close.clicked.connect(self.close)
        # 添加按钮到按钮组中
        self.group_box_layout.addWidget(self.b_create_db)
        self.group_box_layout.addWidget(self.b_view_data)
        self.group_box_layout.addWidget(self.b_add_row)
        self.group_box_layout.addWidget(self.b_delete_row)
        self.group_box_layout.addWidget(self.b_close)

        # 设置UI界面的核心部件
        self.setCentralWidget(self.widget)

    def create_db(self):
        try:
            # 调用输入框获取数据库名称
            db_text, db_action = QtWidgets.QInputDialog.getText(self, '数据库名称', '请输入数据库名称', QtWidgets.QLineEdit.Normal)
            if (db_text.replace(' ', '') != '') and (db_action is True):
                print(db_text)
                self.db_name = db_text
                # 添加一个sqlite数据库连接并打开
                db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
                db.setDatabaseName('{}.sqlite'.format(db_text))
                db.open()
                # 实例化一个查询对象
                query = QtSql.QSqlQuery()
                # # 创建一个数据库表
                # query.exec_("create table hero_info(ID int primary key, hero_class int,"
                #             "hero_name varchar(20),  recover double, defence double, erupt double, penetrate double,"
                #             " control double, poke double, speed double, hot double, partners varchar(40),"
                #             " partner_ability varchar(40))")
                # # 插入三条数据
                # query.exec_("insert into hero_info values(1, 1, '阿古朵', 0.6, 0.6, -0.4, -0.4, 0.4, -0.7, -0.1, -0.8, '孙膑 周瑜', '0.5, 0.2')")
                # query.exec_("insert into hero_info values(2, 1, '白起', 0.75, 0.95, 0.12, -0.7, 0.8, -0.95, -0.85, -0.6, '孙膑 杨玉环', '0.75, 0.68')")
                # query.exec_("insert into hero_info values(3, 1, '嫦娥', -0.2, 0.6, 0.7, 0.5, -0.2, 0.2.-0.75, -0.6, -0.47, '', '')")
                sql = "select * from hero_info where hero_name = '程咬金'"
                self.model = QtSql.QSqlTableModel()
                hero_dict = self.model.query()
                hero_dict.value()
                print(hero_dict)
                print('创建数据库成功')
        except Exception as e:
            print(e)

        # 浏览数据
    def view_data(self):
        # 实例化一个可编辑数据模型
        self.model = QtSql.QSqlTableModel()
        self.table_widget.setModel(self.model)

        self.model.setTable('hero_info')  # 设置数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据
        # 设置表格头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, '英雄类别')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, '英雄名称')

    # 添加一行数据行
    def add_row_data(self):
        # 如果存在实例化的数据模型对象
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.create_db()

    # 删除一行数据
    def del_row_data(self):
        if self.model:
            self.model.removeRow(self.table_widget.currentIndex().row())
        else:
            self.create_db()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db_ui = MainUi()
    db_ui.show()
    # child_window = Ui_Form(1)
    # child_window.show()
    sys.exit(app.exec_())