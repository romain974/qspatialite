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
from ui_querybuilder import Ui_Dialog
from dictionnary import *
import pickle

class querybuilder(QtGui.QDialog):
	def __init__(self,parent = None):
		QtGui.QDialog.__init__(self)
		# Set up the user interface from Designer.
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.parent=parent
		#Load Highlighter for SQLeditor
		SQLhighlighter1 = self.parent.highlighter.MyHighlighter( self.ui.col, "Classic" )
		SQLhighlighter2 = self.parent.highlighter.MyHighlighter( self.ui.where, "Classic" )
		self.get_tables=parent.get_tables #callbackfunction
		self.get_columns=parent.get_columns #callbackfunction
		self.run_query=parent.run_normal_query #callbackfunction
		self.functions=functions
		self.ui.functions.insertItems(1,self.functions)
		self.math=math
		self.ui.math.insertItems(1,self.math)
		self.aggregate=aggregate
		self.ui.aggregates.insertItems(1,self.aggregate)
		self.operators=operators
		self.ui.operators.insertItems(1,self.operators)
		self.stringfct=strings
		self.ui.stringfct.insertItems(1,self.stringfct)

		#show rtree operations
		self.rtreecommand=["RTreeIntersects","RTreeWithin","RTreeContain"]
		self.ui.Rtree.insertItems(1,self.rtreecommand)
		#show tables
		self.DBtables=self.get_tables()
		self.show_tables()
		#show spatial tables:
		self.tables_geo=[ """"%s".'%s'"""%(table[0],table[2]) for table in self.DBtables if (table[2] is not None)]
		self.ui.table_target.insertItems(1,self.tables_geo)
		#show spatial index table
		self.tables_idx=[""""%s".'%s'"""%(table[0],table[2]) for table in self.DBtables if (table[6] not in (None,0))]
		self.ui.table_idx.insertItems(1,self.tables_idx)
		#default values
		self.ui.extract.setChecked(True)
		self.table=None
		#restore previous state
		if self.parent.last_query is not None:
			self.coltables=self.parent.last_query["coltables"]
			self.col_col=self.parent.last_query["col_col"]
			self.col_where=self.parent.last_query["col_where"]
			self.ui.col.insertPlainText(self.parent.last_query["col"])
			self.ui.tab.setText(self.parent.last_query["tab"])
			self.ui.where.insertPlainText(self.parent.last_query["where"])
			self.ui.order.setText(self.parent.last_query["order"])
			self.ui.group.setText(self.parent.last_query["group"])
			#list previous colist:
			for table in self.coltables:
				columns=[""""%s".'%s'"""%(table,col[1]) for col in self.get_columns(table)]
				# first and second col combobox
				end=self.ui.columns.count()
				self.ui.columns.insertItems(end,columns)
				self.ui.columns_2.insertItems(end,columns)
				end=self.ui.columns.count()
				self.ui.columns.insertSeparator(end)
				self.ui.columns_2.insertSeparator(end)
		else:
			self.col_col=[]
			self.col_where=[]
			self.coltables=[]

		self.currentItem=None

		QtCore.QObject.connect(self.ui.aggregates, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.add_aggregate)
		QtCore.QObject.connect(self.ui.stringfct, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.add_stringfct)
		QtCore.QObject.connect(self.ui.operators, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.add_operators)
		QtCore.QObject.connect(self.ui.functions, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.add_functions)
		QtCore.QObject.connect(self.ui.math, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.add_math)
		QtCore.QObject.connect(self.ui.tables, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.add_tables)
		QtCore.QObject.connect(self.ui.tables, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.list_cols)
		QtCore.QObject.connect(self.ui.columns, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.add_columns)
		QtCore.QObject.connect(self.ui.columns_2, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.list_values)
		QtCore.QObject.connect(self.ui.reset, 
				QtCore.SIGNAL("clicked(bool)"), 
				self.reset)
		QtCore.QObject.connect(self.ui.extract, 
				QtCore.SIGNAL("stateChanged(int)"), 
				self.list_values)
        	QtCore.QObject.connect(self.ui.values, 
                              	QtCore.SIGNAL("doubleClicked(const QModelIndex &)"), 
                              	self.query_item)
        	QtCore.QObject.connect(self.ui.buttonBox, 
                              	QtCore.SIGNAL("accepted()"), 
                              	self.validate)
        	QtCore.QObject.connect(self.ui.checkBox, 
                              	QtCore.SIGNAL("stateChanged(int)"), 
                              	self.show_tables)
        	QtCore.QObject.connect(self.ui.usertree, 
                              	QtCore.SIGNAL("clicked(bool)"), 
                              	self.use_rtree)
        	QtCore.QObject.connect(self.ui.save, 
                              	QtCore.SIGNAL("clicked(bool)"), 
                              	self.saveSQL)
        	QtCore.QObject.connect(self.ui.load, 
                              	QtCore.SIGNAL("clicked(bool)"), 
                              	self.loadSQL)
	def show_tables(self):
		tables=self.DBtables
		if self.ui.checkBox.isChecked(): #show all tables
			self.tables=[table[0] for table in tables] #Tables
		else:
			self.tables=[table[0] for table in tables if ((table[0] not in self.parent.systables) and (table[0][:4].upper()!="IDX_"))] #Non system Tables and non IDX tables
		self.ui.tables.clear()
		self.ui.tables.insertItems(0,["Tables"])
		self.ui.tables.insertItems(1,self.tables)

	def add_aggregate(self):
		ag=self.ui.aggregates.currentText()
		if ag=="Aggregates" or (ag is None):
			return
		if self.ui.col.textCursor().hasSelection(): #user have selectedsomething...
			selection=self.ui.col.textCursor().selectedText()
			self.ui.col.insertPlainText(ag+selection+")")
		else:
			self.ui.col.insertPlainText(ag)
		self.ui.aggregates.setCurrentIndex(0)

	def add_functions(self):
		ag=self.ui.functions.currentText()
		if ag=="Functions" or (ag is None):
			return
		if self.ui.where.active==1: # in where section
			if self.ui.where.textCursor().hasSelection(): #user have selectedsomething...
				selection=self.ui.where.textCursor().selectedText()
				self.ui.where.insertPlainText(ag+selection+")")
			else:
				self.ui.where.insertPlainText(ag)
		else:
			if self.ui.col.textCursor().hasSelection(): #user have selectedsomething...
				selection=self.ui.col.textCursor().selectedText()
				self.ui.col.insertPlainText(ag+selection+")")
			else:
				self.ui.col.insertPlainText(ag)

		self.ui.functions.setCurrentIndex(0)



	def add_stringfct(self):
		ag=self.ui.stringfct.currentText()
		if ag=="Strings functions" or (ag is None):
			return
		if self.ui.where.active==1: # in where section
			if self.ui.where.textCursor().hasSelection(): #user have selectedsomething...
				selection=self.ui.where.textCursor().selectedText()
				self.ui.where.insertPlainText(ag+selection+")")
			else:
				self.ui.where.insertPlainText(ag)
		else:
			if self.ui.col.textCursor().hasSelection(): #user have selectedsomething...
				selection=self.ui.col.textCursor().selectedText()
				self.ui.col.insertPlainText(ag+selection+")")
			else:
				self.ui.col.insertPlainText(ag)

		self.ui.stringfct.setCurrentIndex(0)

	def add_math(self):
		ag=self.ui.math.currentText()
		if ag=="Math" or (ag is None):
			return
		if self.ui.where.active==1: # in where section
			if self.ui.where.textCursor().hasSelection(): #user have selectedsomething...
				selection=self.ui.where.textCursor().selectedText()
				self.ui.where.insertPlainText(ag+selection+")")
			else:
				self.ui.where.insertPlainText(ag)
		else:
			if self.ui.col.textCursor().hasSelection(): #user have selectedsomething...
				selection=self.ui.col.textCursor().selectedText()
				self.ui.col.insertPlainText(ag+selection+")")
			else:
				self.ui.col.insertPlainText(ag)

		self.ui.math.setCurrentIndex(0)
	def add_operators(self):
		ag=self.ui.operators.currentText()
		if ag=="Operators" or (ag is None):
			return
		if self.ui.where.active==1: # in where section
			if self.ui.where.textCursor().hasSelection(): #user have selectedsomething...
				selection=self.ui.where.textCursor().selectedText()
				self.ui.where.insertPlainText(ag+selection+")")
			else:
				self.ui.where.insertPlainText(ag)
		else:
			if self.ui.col.textCursor().hasSelection(): #user have selectedsomething...
				selection=self.ui.col.textCursor().selectedText()
				self.ui.col.insertPlainText(ag+selection+")")
			else:
				self.ui.col.insertPlainText(ag)
		self.ui.operators.setCurrentIndex(0)
	def add_tables(self):
		ag=self.ui.tables.currentText()
		if ag=="Tables" or (ag in (None,""," ")):
			return
		if (ag in self.coltables): #table already use
			reponse=QtGui.QMessageBox.question(self, "Table already used","Do you want to add table %s again ?"%ag, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
			if reponse==QtGui.QMessageBox.No:
				return
		txt=self.ui.tab.text()
		if (txt is None) or (txt in (""," ")):
			self.ui.tab.setText('"%s"'%ag)
		else:
			self.ui.tab.setText('%s, "%s"'%(txt,ag))
		self.table=ag
		#self.coltables.append(ag)
		self.ui.tables.setCurrentIndex(0)
	def add_columns(self):
		ag=self.ui.columns.currentText()
		if ag in (None,"Columns",""):
			return
		if self.ui.where.active==1:
			if ag in self.col_where: # column already called in where section
				reponse=QtGui.QMessageBox.question(self, "Column already used in WHERE clause","Do you want to add column %s again ?"%ag, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
				if reponse==QtGui.QMessageBox.No:
					self.ui.columns.setCurrentIndex(0)
					return
			self.ui.where.insertPlainText(ag)
			self.col_where.append(ag)
		else:
			if ag in self.col_col: # column already called in col section
				reponse=QtGui.QMessageBox.question(self, "Column already used in COLUMNS section","Do you want to add column %s again ?"%ag, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
				if reponse==QtGui.QMessageBox.No:
					self.ui.columns.setCurrentIndex(0)
					return
			ag2=ag
			# alias geometry column
			columnName=ag.split(".")[1][1:-1] #column
			tableName=ag.split(".")[0][1:-1] #table
			for table in self.DBtables:
				if table[2] is not None: #
					if table[0].upper()==tableName.toUpper() and table[2].upper()==columnName.toUpper():
						ag2="%s AS Geometry"%ag
			# alias ROWID column
			if columnName=='ROWID':
				ag2="%s AS ROWID"%ag
			txt=self.ui.col.toPlainText()
			if (txt is None) or (txt in (""," ")):
				self.ui.col.setText(ag2)
			else:
				self.ui.col.setText('%s,\n%s'%(txt,ag2))
			self.col_col.append(ag)
		self.ui.columns.setCurrentIndex(0)

	def list_cols(self):
		table=self.table
		if (table is None) or (table in self.coltables):
			return
		columns=[""""%s".'%s'"""%(table,col[1]) for col in self.get_columns(table)]
		#add ROWID column:
		columns=[""""%s".*"""%table,""""%s".'%s'"""%(table,'ROWID')]+columns
		self.coltables.append(table) #table columns have been listed
		# first and second col combobox
		end=self.ui.columns.count()
		self.ui.columns.insertItems(end,columns)
		self.ui.columns_2.insertItems(end,columns)
		end=self.ui.columns.count()
		self.ui.columns.insertSeparator(end)
		self.ui.columns_2.insertSeparator(end)

	def list_values(self):
		item=self.ui.columns_2.currentText()
		if item in (None,"Columns",""," "):
			return
		#recover column and table:
		column=item.split(".")  # "table".'column'
		table=column[0]
		#limit 20 values -- 
		query="SElECT DISTINCT %s FROM %s "%(item,table)
		if self.ui.extract.isChecked():
			query+=" LIMIT 10"
		rowList, columnNames = self.run_query(query)
		if len(rowList)<1:
			return
		#model for listing unique value
		model = QtGui.QStandardItemModel(0,1)
		for row in rowList:
			if not isinstance(row[0],buffer):
				model.appendRow(QtGui.QStandardItem("%s"%row[0]))
		self.ui.values.setModel(model)

    	def query_item(self, index):
		queryWord = index.data().toString()
		queryWord=' "%s"' %queryWord
		if queryWord != '':
			self.ui.where.insertPlainText(queryWord)
			self.ui.where.setFocus()

	def use_rtree(self):
		idx=self.ui.table_idx.currentText()
		try:
			tab_idx=idx.split(".")[0][1:-1] #remove "
			col_idx=idx.split(".")[1][1:-1] #remove '
		except:
			self.parent.pop_up_error("All fields are necessary")
		tab_target=self.ui.table_target.currentText()
		op=self.ui.Rtree.currentText()
		if idx in (None,""," ","Table (with Spatial Index)"):
			return
		if tab_target in (None,""," ","Table (Target)"):
			return
		if op in (None,""," ","Rtree Operation"):
			return
		sql=""
		if self.ui.where.toPlainText() not in (None,""," "):
			sql+="\nAND"
		sql+=""""%s".ROWID IN (\nSELECT pkid FROM "idx_%s_%s" WHERE pkid MATCH %s(\nMBRminX(%s),MBRminY(%s),MBRmaxX(%s),MBRmaxY(%s))) """%(tab_idx,tab_idx,col_idx,op,tab_target,tab_target,tab_target,tab_target)
		self.ui.where.insertPlainText(sql)

	def reset(self):
		#reset lists:
		self.ui.values.setModel(None)
		self.ui.columns_2.clear()
		self.ui.columns.insertItems(0,["Columns"])
		self.ui.columns_2.insertItems(0,["Columns"])
		self.coltables=[]
		self.col_col=[]
		self.col_where=[]
		self.ui.col.active=1
		self.ui.where.active=0

	def validate(self):
		query_col=unicode(self.ui.col.toPlainText())
		query_table=unicode(self.ui.tab.text())
		query_where=unicode(self.ui.where.toPlainText())
		query_group=unicode(self.ui.group.text())
		query_order=unicode(self.ui.order.text())
		query=""
		if query_col.strip()!='':
			query+="SELECT %s \nFROM %s"%(query_col,query_table)
		if query_where.strip()!='':
			query+="\nWHERE %s"%query_where
		if query_group.strip()!='':
			query+="\nGROUP BY %s"%query_group
		if query_order.strip()!='':
			query+="\nORDER BY %s"%query_order
		if query=='':
			return
		#check if a query already exists in SQl editor 
		sqleditor=unicode(self.parent.ui.SQLeditor.toPlainText()).strip()
		if len(sqleditor)>0:
			reponse=QtGui.QMessageBox.question(self, "SQL editor is not empty","Do you want to replace SQL editor text with your Query (yes)? ('no' will add the new query as a subquery)", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
			if reponse==QtGui.QMessageBox.Yes:
				self.parent.ui.SQLeditor.setPlainText(query)
			else:
				self.parent.ui.SQLeditor.setPlainText(sqleditor+' '+query)
		else:
			self.parent.ui.SQLeditor.setPlainText(query)
		self.parent.last_query=dict()
		self.parent.last_query["coltables"]=self.coltables
		self.parent.last_query["col_col"]=self.col_col
		self.parent.last_query["col_where"]=self.col_where
		self.parent.last_query["col"]=query_col
		self.parent.last_query["tab"]=query_table
		self.parent.last_query["where"]=query_where
		self.parent.last_query["group"]=query_group
		self.parent.last_query["order"]=query_order

	def saveSQL(self):
		#ask user where to save:
		path = QtGui.QFileDialog.getSaveFileName(self, "Save SQL query","nyQuery.qsql","QSpatialite query (*.qsql)")
		if path.isEmpty():
			return
		#save data as a python dict
		saveFile=dict()
		saveFile['query_cols']=unicode(self.ui.col.toPlainText())
		saveFile['query_table']=unicode(self.ui.tab.text())
		saveFile['query_where']=unicode(self.ui.where.toPlainText())
		saveFile['query_group']=unicode(self.ui.group.text())
		saveFile['query_order']=unicode(self.ui.order.text())
		saveFile["coltables"]=self.coltables
		saveFile["col_col"]=self.col_col
		saveFile["col_where"]=self.col_where
		#write dict to file
		try:
			f = open(path, "w") # write mode
			pickle.dump(saveFile,f)
		except:
			self.parent.pop_up_error("Impossible to write File to disk")
			return
		QtGui.QMessageBox.information(self, "SQL saved", "Data Saved in:\n%s"%path)

	def loadSQL(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, "Open QSpatiaLite SQL File","","QSpatialite query (*.qsql)")
		if filename.isEmpty():
			return
		try:
			f = open(filename, "r") # read mode
			saveFile = pickle.load(f) #Load dictionnary
			#load values
			self.ui.col.setPlainText(saveFile['query_cols'])
			self.ui.tab.setText(saveFile['query_table'])
			self.ui.where.setPlainText(saveFile['query_where'])
			self.ui.group.setText(saveFile['query_group'])
			self.ui.order.setText(saveFile['query_order'])
			self.coltables=saveFile["coltables"]
			self.col_col=saveFile["col_col"]
			self.col_where=saveFile["col_where"]
		except:
			self.parent.pop_up_error("Error while loading File: Incorrect File Format")
		#reset lists:
		self.ui.values.setModel(None)
		self.ui.columns.clear()
		self.ui.columns_2.clear()
		self.ui.columns.insertItems(0,["Columns"])
		self.ui.columns_2.insertItems(0,["Columns"])
		self.ui.col.active=1
		self.ui.where.active=0
		#write lists
		for table in self.coltables:
			columns=[""""%s".'%s'"""%(table,col[1]) for col in self.get_columns(table)]
			# first and second col combobox
			end=self.ui.columns.count()
			self.ui.columns.insertItems(end,columns)
			self.ui.columns_2.insertItems(end,columns)
			end=self.ui.columns.count()
			self.ui.columns.insertSeparator(end)
			self.ui.columns_2.insertSeparator(end)


#if __name__ == "__main__":
#	import sys
#	app = QtGui.QApplication( sys.argv )
#	window = querybuilder("ee","aa")
#	window.show()
#	sys.exit( app.exec_() )
