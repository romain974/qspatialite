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
from ui_recovergeometry import Ui_RecoverGeometryColumn

class recovergeometry(QtGui.QDialog):
	def __init__(self,connexion,table,column, prepare_tree, srsdialog,parent = None):
		QtGui.QDialog.__init__(self)
        	# Set up the user interface from Designer.
        	self.ui = Ui_RecoverGeometryColumn()
        	self.ui.setupUi(self)
		self.srsdialog=srsdialog
		self.connexion=connexion
		self.table=table
		self.column=column
		self.prepare_tree=prepare_tree #callbackfunction
		self.ui.table.setText(table)
		self.ui.table.setEnabled(False)
		self.ui.column.setText(column)
		self.ui.column.setEnabled(False)
		self.dims=["2","3"]
		self.ui.dims.insertItems(0,self.dims)
		self.geometry=["POINT","MULTIPOINT","LINESTRING","MULTILINESTRING","POLYGON","MULTIPOLYGON","GEOMETRYCOLLECTION"]
		self.ui.geometry.insertItems(0,self.geometry)

        	QtCore.QObject.connect(self.ui.buttonBox, 
                               QtCore.SIGNAL("accepted()"), 
                               self.validate)

        	QtCore.QObject.connect(self.ui.browseSRID, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.browseSRID)

    	def validate(self):
		try:
			srid=int(self.ui.srid.text())
		except:
			QtGui.QMessageBox.information(self, "Error", "SRID must be Integer")
			return #srid must be integer
		dims=self.ui.dims.currentText()
		geometry=self.ui.geometry.currentText()
		if (self.table=='') or (self.column=='') or (srid=='') or (dims=='') or (geometry==''):
			QtGui.QMessageBox.information(self, "Error", "All fields are required")
			return # all fields are needed...
		Query="SELECT recovergeometryColumn('%s','%s',%s,'%s',%s)"%( self.table, self.column, srid, geometry,dims)
		cursor=self.connexion.cursor()
		rep=cursor.execute(Query)
		if rep.fetchall()[0][0]!=1:
			QtGui.QMessageBox.information(self,"Geometry column validation failed","Geometry column doesn't satisfies required constraints\na ROLLBACK was automatically performed")
			self.connexion.rollback()
			cursor.close
			return
		QtGui.QMessageBox.information(self,"Information","Geometry column validation succeed")
		self.connexion.commit()
		cursor.close()
		self.prepare_tree()
	
    	def browseSRID(self):
		dialog = self.srsdialog( "Select desired SRS" )
		if dialog.exec_():
			self.ui.srid.setText(dialog.getProjection())
		





#if __name__ == "__main__":
#  import sys
#  app = QtGui.QApplication( sys.argv )
#  window = browser()
#  window.show()
#  sys.exit( app.exec_() )
