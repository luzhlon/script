#! /usr/bin/python3
# FileName   : diskeyb.py
# Author     : luzhlon
# Function   : 通过xinput命令禁用或启用某些输入设备
# LastChange : 2017/2/17

import sys,os,re,json

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

# 键盘设备列表
def keyb_list():
    out = os.popen("xinput list")
    str = out.read()
    out.close()
    list = re.findall('↳ (.+?)\s+id=(\d+).+?slave\s+keyboard', str)
    return list
# 根据设备名获取设备id
def get_device_id(device):
    list = keyb_list()
    for tup in list:
        if device == tup[0]:
            return tup[1]
def enable_device(id):
    os.system('xinput enable ' + id)
def disable_device(id):
    os.system('xinput disable ' + id)
# 向一个GUI对象中添加多个Widget
def addWidgets(obj, *args):
    for i in args:
        obj.addWidget(i)
# 向一个GUI对象中添加多个Layout
def addLayouts(obj, *args):
    for i in args:
        obj.addLayout(i)
# 配置文件路径
def config_path():
    # return os.getenv('HOME') + '/.config/diskeyb.json'
    return 'config.json'
    
class myDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_layout()
        self.init_tray()
        self.resize(450, 300)
        self.setMinimumSize(450, 300)
        self.load_conf()
    # 加载配置
    def load_conf(self):
        try:
            path = config_path()
            f = open(path)
            self.config = json.loads(f.read())
            self.reset_tray()
        except FileNotFoundError:
            self.show()
            self.tray.showMessage('提示', '请选择无线键盘设备')
            return
    # 重设托盘菜单
    def reset_tray(self):
        try:
            device = self.config['device']
            self.enable.setText('Enable '+device)
            self.disable.setText('Disable '+device)
            self.enable.setEnabled(True)
            self.disable.setEnabled(True)
        except Exception:
            self.enable.setEnabled(False)
            self.disable.setEnabled(False)
    # 保存设置
    def save_conf(self):
        str = json.dumps(self.config)
        f = open(config_path(), 'w')
        f.write(str)
        f.close()
    def onOk(self):
        table = self.table
        row = table.currentRow()
        config = { 'device': self.curlist[row][0] }
        self.config = config
        self.save_conf()
        self.reset_tray()
        self.tray.showMessage('提示', '设置保存成功')
        self.hide()
    # 初始化窗口布局
    def init_layout(self):
        okbtn = QPushButton("Save")
        okbtn.clicked.connect(self.onOk)
        canbtn = QPushButton("Cancel")
        canbtn.clicked.connect(self.hide)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        vbox.addStretch(1)
        addWidgets(vbox, okbtn, canbtn)

        self.init_table()
        lvbox = QVBoxLayout()
        addWidgets(lvbox, QLabel('选择无线键盘设备:'), self.table)
        addLayouts(hbox, lvbox, vbox)

        self.setLayout(hbox)
    # 初始化系统托盘图标
    def init_tray(self):
        tray = QSystemTrayIcon(QIcon('kb.ico'), self)
        menu = QMenu()
        enable = menu.addAction("Enable")
        enable.triggered.connect(self.onEnable)
        disable = menu.addAction("Disable")
        disable.triggered.connect(self.onDisable)
        menu.addSeparator()
        opt = menu.addAction("Options")
        opt.triggered.connect(self.show)
        menu.addSeparator()
        quit = menu.addAction("Quit")
        quit.triggered.connect(self.onQuit)
        tray.setContextMenu(menu)
        tray.show()
        # self.tray_menu = menu
        self.tray = tray
        self.enable = enable
        self.disable = disable
    # 初始化设备列表
    def init_table(self):
        table = QTableWidget(0, 2)
        table.setHorizontalHeaderLabels(['device', 'id'])
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setColumnWidth(0, 200)
        self.table = table

    # 更新设备列表
    def update_list(self):
        list = keyb_list()
        self.curlist = list
        self.clear_items()
        i = 0
        for item in list:
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(list[i][0]))
            self.table.setItem(i, 1, QTableWidgetItem(list[i][1]))
            i += 1
    # 清空列表
    def clear_items(self):
        table = self.table
        while table.rowCount():
            table.removeRow(0)

    def showEvent(self, e):
        self.update_list()
    # 点击关闭按钮时隐藏对话框
    def closeEvent(self, e):
        try:
            if self.quit:
                return
        except Exception:
            self.hide()
            e.ignore()      # 不关闭窗口
    def onQuit(self):
        self.quit = True
        self.close()

    def onEnable(self):
        device = self.config['device']
        id = get_device_id(device)
        enable_device(id)
    def onDisable(self):
        device = self.config['device']
        id = get_device_id(device)
        disable_device(id)

app = QApplication(sys.argv)
win = myDlg()

app.exec()

