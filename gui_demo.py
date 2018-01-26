import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton, QDesktopWidget, QMainWindow, QAction, QMenu, QVBoxLayout,\
QGridLayout, QHBoxLayout, QLabel, QLineEdit

class GuiDemo(QMainWindow):

    def __init__(self):
        # 主页面区
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("BiliBili弹幕姬Python版")
        self.resize(500,400)
        self.add_menu_and_buttion()

    def add_menu_and_buttion(self):

        window_width = self.size().width()
        window_height = self.size().height()

        # 状态栏
        self.statusBar().showMessage("房间号：12580")

        # 添加标签
        lable_1 = QLabel("第1个标签:", self)
        lable_2 = QLabel("第2个标签:", self)
        lable_1.move(5, 0)
        lable_2.move(5, window_height/20)

        # 关闭程序按钮
        exit_btn = QPushButton("退出", self)
        exit_btn.clicked.connect(QApplication.instance().quit)
        exit_btn.setGeometry(100, 10, window_width - 120, window_height - 60)

        # 输入框
        house_number = QLineEdit(self)
        house_number.setGeometry(100, 10, 80, 20)

        # # 创建两个水平盒子
        # hbox_1 = QHBoxLayout()
        # hbox_2 = QHBoxLayout()
        #
        # # 创建一个垂直盒子
        # vbox = QVBoxLayout()
        #
        # # 在盒子中添加标签
        # hbox_1.addWidget(lable_1)
        # hbox_2.addWidget(exit_btn)
        # vbox.addLayout(hbox_1)
        # vbox.addLayout(hbox_2)
        #
        # # 创建一个窗口部件，设置布局为水平盒子
        # layout_widget = QWidget()
        # layout_widget.setLayout(vbox)
        #
        # self.setCentralWidget(layout_widget)


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = GuiDemo()
    g.show()
    sys.exit(app.exec_())