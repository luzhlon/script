
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import keyboard
import os

# 向一个GUI对象中添加多个Widget
def addWidgets(obj, *args):
    for i in args:
        obj.addWidget(i)

# 向一个GUI对象中添加多个Layout
def addLayouts(obj, *args):
    for i in args:
        obj.addLayout(i)
    
class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_tray()
        self.resize(450, 300)
        self.setMinimumSize(450, 300)

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

    def onOk(self):
        table = self.table
        row = table.currentRow()
        config = { 'device': self.curlist[row][0] }
        self.config = config
        self.reset_tray()
        self.tray.showMessage('提示', '设置保存成功')
        self.hide()

    def init_tray(self):
        tray = QSystemTrayIcon(QIcon('monitor.ico'), self)
        menu = QMenu()

        enable = menu.addAction("Enable")
        enable.triggered.connect(self.onEnable)
        disable = menu.addAction("Disable")
        disable.triggered.connect(self.onDisable)
        menu.addSeparator()

        show = menu.addAction("Show window")
        show.triggered.connect(self.show)
        menu.addSeparator()

        quit = menu.addAction("Quit")
        quit.triggered.connect(self.onQuit)

        tray.setContextMenu(menu)
        tray.show()
        # self.tray_menu = menu
        self.tray = tray
        self.enable = enable
        self.disable = disable

    def showEvent(self, e):
        pass

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
        pass

    def onDisable(self):
        pass

keyboard.add_hotkey('win+enter', lambda: os.system('start open-wsl'))
keyboard.add_hotkey('ctrl+alt+enter', lambda: os.system('start cmd'))
keyboard.add_hotkey('win+v', lambda: os.system('start nvim-qt'))
keyboard.add_hotkey('win+g', lambda: os.system('start gvim'))

app = QApplication(sys.argv)
dialog = MyDialog()
# dialog.show()
app.exec()
