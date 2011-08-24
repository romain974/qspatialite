"""
/***************************************************************************
 QspatiaLite
                                 A QGIS plugin inspired by "CustomDBquery" and "SpatiaLite_manager" plugins
 SpatiaLite GUI for SpatiaLite

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_browser import Ui_browser

class browser(QtGui.QDialog):
	def __init__(self, parent = None):
		QtGui.QDialog.__init__(self)
        	# Set up the user interface from Designer.
        	self.ui = Ui_browser()
        	self.ui.setupUi(self)





#if __name__ == "__main__":
#  import sys
#  app = QtGui.QApplication( sys.argv )
#  window = browser()
#  window.show()
#  sys.exit( app.exec_() )
