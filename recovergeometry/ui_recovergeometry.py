# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recovergeometry.ui'
#
# Created: Mon Apr  4 16:39:44 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RecoverGeometryColumn(object):
    def setupUi(self, RecoverGeometryColumn):
        RecoverGeometryColumn.setObjectName("RecoverGeometryColumn")
        RecoverGeometryColumn.resize(223, 242)
        self.horizontalLayout_6 = QtGui.QHBoxLayout(RecoverGeometryColumn)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(RecoverGeometryColumn)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.table = QtGui.QLineEdit(RecoverGeometryColumn)
        self.table.setObjectName("table")
        self.horizontalLayout.addWidget(self.table)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(RecoverGeometryColumn)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.column = QtGui.QLineEdit(RecoverGeometryColumn)
        self.column.setObjectName("column")
        self.horizontalLayout_2.addWidget(self.column)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(RecoverGeometryColumn)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.srid = QtGui.QLineEdit(RecoverGeometryColumn)
        self.srid.setObjectName("srid")
        self.horizontalLayout_3.addWidget(self.srid)
        self.browseSRID = QtGui.QToolButton(RecoverGeometryColumn)
        self.browseSRID.setObjectName("browseSRID")
        self.horizontalLayout_3.addWidget(self.browseSRID)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtGui.QLabel(RecoverGeometryColumn)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.dims = QtGui.QComboBox(RecoverGeometryColumn)
        self.dims.setObjectName("dims")
        self.horizontalLayout_4.addWidget(self.dims)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(RecoverGeometryColumn)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.geometry = QtGui.QComboBox(RecoverGeometryColumn)
        self.geometry.setObjectName("geometry")
        self.horizontalLayout_5.addWidget(self.geometry)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(RecoverGeometryColumn)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)

        self.retranslateUi(RecoverGeometryColumn)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), RecoverGeometryColumn.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), RecoverGeometryColumn.reject)
        QtCore.QMetaObject.connectSlotsByName(RecoverGeometryColumn)

    def retranslateUi(self, RecoverGeometryColumn):
        RecoverGeometryColumn.setWindowTitle(QtGui.QApplication.translate("RecoverGeometryColumn", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RecoverGeometryColumn", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RecoverGeometryColumn", "Column", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RecoverGeometryColumn", "SRID", None, QtGui.QApplication.UnicodeUTF8))
        self.browseSRID.setText(QtGui.QApplication.translate("RecoverGeometryColumn", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("RecoverGeometryColumn", "Dims", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("RecoverGeometryColumn", "Geometry Type", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RecoverGeometryColumn = QtGui.QDialog()
    ui = Ui_RecoverGeometryColumn()
    ui.setupUi(RecoverGeometryColumn)
    RecoverGeometryColumn.show()
    sys.exit(app.exec_())

