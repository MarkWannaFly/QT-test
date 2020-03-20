import sys
import demo  # 这里是ui文件转换的文件名

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()  # 获取主窗口mainWindow
    ui = demo.Ui_MainWindow()  # 获取demo中的组件
    ui.setupUi(mainWindow)  # 生成窗口
    mainWindow.show()  # 显示mainWindow
    sys.exit(app.exec_())  # app.exec_()运行主循环，sys.exit()可以判断程序退出并返回到主线程
