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
from ui_newtable import Ui_NewTable

class newtable(QtGui.QDialog):
	def __init__(self,connexion, prepare_tree, srsdialog,parent = None):
		QtGui.QDialog.__init__(self)
        	# Set up the user interface from Designer.
        	self.ui = Ui_NewTable()
        	self.ui.setupUi(self)
		self.connexion=connexion
		#geometry types
		self.geotype=["POLYGON","MULTIPOLYGON","LINE","LINESTRING","POINT","MULTIPOINT","GEOMETRYCOLLECTION"]
		self.ui.geotype.insertItems(0,self.geotype)
		#dimensions
		self.dims=["2","3"]
		self.ui.dims.insertItems(0,self.dims)
		#column types
		self.coltype=["TEXT","NUMERIC","INTEGER","REAL","NONE"]
		self.ui.coltype.insertItems(0,self.coltype)
		#colback_functions
		self.prepare_tree=prepare_tree #callbackfunction
		self.srsdialog=srsdialog #callbackfunction
		#set up interface
		self.colList=[]
		self.ui.pkey.setChecked(True)
		self.ui.geocol.setChecked(False)
		self.ui.geoname.setEnabled(False)
		self.ui.geoname.setText("Geometry")
		self.ui.geotype.setEnabled(False)
		self.ui.geosrid.setEnabled(False)
		self.ui.browseSRID.setEnabled(False)
		self.geocol=0

        	QtCore.QObject.connect(self.ui.browseSRID, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.browseSRID)

        	QtCore.QObject.connect(self.ui.add, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.addcol)

        	QtCore.QObject.connect(self.ui.remove, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.remove)

        	QtCore.QObject.connect(self.ui.geocol, 
                               QtCore.SIGNAL("stateChanged(int)"), 
                               self.add_geocol)

        	QtCore.QObject.connect(self.ui.buttonBox, 
                               QtCore.SIGNAL("accepted()"), 
                               self.validate)

    	def addcol(self):
		try:
			colname=str(self.ui.colname.text())
			coltype=str(self.ui.coltype.currentText())
		except:
			QtGui.QMessageBox.information(self, "Error", "No special chars/accents please")
			return
		if colname=="" or coltype=="":
			QtGui.QMessageBox.information(self, "Error", "Enter column Name please")
			return
		if colname in [col[0] for col in self.colList]:
			QtGui.QMessageBox.information(self, "Error", "Column name already exists")
			return
		self.colList.append([colname,coltype])
		self.ui.colname.setText("")
		self.showcols() #show columns

    	def add_geocol(self): #toggle geocol
		if self.ui.geocol.isChecked():
			self.geocol=1
			self.ui.geoname.setEnabled(True)
			self.ui.geotype.setEnabled(True)
			self.ui.geosrid.setEnabled(True)
			self.ui.dims.setEnabled(True)
			self.ui.browseSRID.setEnabled(True)
		else:
			self.geocol=0
			self.ui.geoname.setEnabled(False)
			self.ui.geotype.setEnabled(False)
			self.ui.geosrid.setEnabled(False)
			self.ui.dims.setEnabled(False)
			self.ui.browseSRID.setEnabled(False)

    	def showcols(self): #fecth cols in widget
		model = QtGui.QStandardItemModel(0,2)
		for col in self.colList:
			item=QtGui.QStandardItem('%s (%s)'%(col[0],col[1]))
			model.appendRow(item)
		self.ui.columns.setModel(model)

    	def remove(self): #fecth cols in widget
		if len(self.colList)==0:
			return
		try:
			item=self.ui.columns.selectedIndexes()[0].row() #get selected Index
			del self.colList[item] #remove col from list
			self.showcols()
		except:
			QtGui.QMessageBox.information(self, "Error", "Please select a column first")
			
    	def browseSRID(self):
		dialog = self.srsdialog( "Select desired SRS" )
		if dialog.exec_():
			self.ui.geosrid.setText(dialog.getProjection())
		

    	def validate(self):
		try:
			tableName=str(self.ui.name.text())
			if self.geocol==1:
				geoname=str(self.ui.geoname.text())
				geotype=str(self.ui.geotype.currentText())
				dims=str(self.ui.dims.currentText())
				geosrid=int(self.ui.geosrid.text())
		except:
			QtGui.QMessageBox.information(self, "Error", "No accents/special chars please\nNote: srid must be INTEGER")
			return
		if tableName=='' or self.colList==[]:
			QtGui.QMessageBox.information(self, "Error", "Empty Table")
			return
		if self.geocol==1 and (geoname=='' or geotype=='' or geosrid=='' or dims==''): 
			QtGui.QMessageBox.information(self, "Error", "Empty Geometry Column details")
			return
		#create table
		query="CREATE TABLE '%s' ("%tableName
		if self.ui.pkey.isChecked(): #add pkey
			query+="PK_UID integer primary key autoincrement,"
		if self.geocol==1: #add geocol
			query+="'%s' %s,"%(geoname,geotype)
		for col in self.colList:
			query+="'%s' %s,"%(col[0],col[1])
		query=query[:-1]+")"
		cursor=self.connexion.cursor()
		try:
			cursor.execute(query)
		except:
			QtGui.QMessageBox.information(self, "Error", "Table Creation Failed")
			self.connexion.rollback()
			cursor.close()
			return
		self.connexion.commit()
		cursor.close()
		#recover geometry table:
		if self.geocol==1:
			query="SELECT RecoverGeometryColumn('%s','%s',%s,'%s',%s)"%(tableName,geoname,geosrid,geotype,dims)
			cursor=self.connexion.cursor()
			cursor.execute(query)
			rep=cursor.fetchall()
			if rep[0][0]==0:
				QtGui.QMessageBox.information(self, "Error", "Unable to recover Geometry Column")
				self.connexion.rollback()
				cursor.close()
				return
			self.connexion.commit()
			cursor.close()
		QtGui.QMessageBox.information(self, "New Table Created", "New table '%s' created"%tableName)
		self.prepare_tree()
	


#if __name__ == "__main__":
#  import sys
#  app = QtGui.QApplication( sys.argv )
#  window = browser()
#  window.show()
#  sys.exit( app.exec_() )
