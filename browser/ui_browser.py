# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created: Mon Apr  4 11:51:54 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_browser(object):
    def setupUi(self, browser):
        browser.setObjectName("browser")
        browser.resize(436, 326)
        self.verticalLayout = QtGui.QVBoxLayout(browser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtGui.QTextBrowser(browser)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.buttonBox = QtGui.QDialogButtonBox(browser)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 15))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(browser)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), browser.reject)
        QtCore.QMetaObject.connectSlotsByName(browser)

    def retranslateUi(self, browser):
        browser.setWindowTitle(QtGui.QApplication.translate("browser", "QspatiaLite", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    browser = QtGui.QDialog()
    ui = Ui_browser()
    ui.setupUi(browser)
    browser.show()
    sys.exit(app.exec_())

