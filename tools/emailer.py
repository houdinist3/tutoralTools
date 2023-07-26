import sys
import typing
from PySide2 import QtUiTools, QtWidgets
import PySide2.QtCore
import PySide2.QtWidgets
import yagmail
# from ui.Ui_emailer import Ui_Form

class EmailWidget(QtWidgets.QWidget):
    def __init__(self):
        super(EmailWidget, self).__init__()

        ui_file = '/home/megatron/GitRepo/tutotools/tutoralTools/ui/emailer.ui'
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)



        self.ui.sendBtn.clicked.connect(self.send)


    def send(self):
        print('send an eamil...')
        yag = yagmail.SMTP('byungsoo@4thparty.co.kr', 'sbs77diak')

        to = self.ui.toLineEdit.text()
        subject = self.ui.subLineEdit.text()
        body = self.ui.bodyTextEdit.toPlainText()
        yag.send(to, subject, body)



def main():
    app = QtWidgets.QApplication(sys.argv)
    win = EmailWidget()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
