# -*- coding: utf-8 -*-

# extracted from GDALTool plugin
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class GdalToolsSRSDialog(QDialog):
  def __init__(self, title):
      QDialog.__init__(self)
      self.setWindowTitle( title )

      layout = QVBoxLayout()
      self.selector = QgsProjectionSelector(self)
      buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Close)

      layout.addWidget(self.selector)
      layout.addWidget(buttonBox)
      self.setLayout(layout)

      self.connect(buttonBox, SIGNAL("accepted()"), self.accept)
      self.connect(buttonBox, SIGNAL("rejected()"), self.reject)

  def epsg(self):
      return str(self.selector.selectedEpsg())

  def proj4string(self):
      return self.selector.selectedProj4String()

  def getProjection(self):
      if self.selector.selectedEpsg() != 0:
        return self.epsg()

      if not self.selector.selectedProj4String().isEmpty():
        return self.proj4string()

      return QString()

