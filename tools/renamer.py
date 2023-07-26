import sys
from PySide2 import QtUiTools, QtWidgets
import osutils
# from ui.Ui_emailer import Ui_Form

class RenameWidget(QtWidgets.QWidget):
    def __init__(self):
        super(RenameWidget, self).__init__()

        ui_file = '/home/megatron/GitRepo/tutotools/tutoralTools/ui/renamer.ui'
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)

        self.ui.dirBtn.clicked.connect(self.selectDir)
        self.ui.renameBtn.clicked.connect(self.rename)
        

    def selectDir(self):
        assetDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select dir', '/home/megatron')
        self.ui.dirLineEdit.setText(assetDir)

    def rename(self):
        if self.ui.prependRadioBtn.isChecked():
            mode = 'prepend'
        elif self.ui.replaceRadioBtn.isChecked():
            mode = 'replace'

        osutils.rename(self.ui.dirLineEdit.text(), self.ui.textLineEdit.text(), mode, self.ui.replaceLineEdit.text())

        




def main():
    app = QtWidgets.QApplication(sys.argv)
    win = RenameWidget()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
