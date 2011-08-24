# -*- coding: iso-8859-15 -*-
"""
/***************************************************************************
 QspatiaLiteDialog
                                 A QGIS plugin
 SpatiaLite GUI for SpatiaLite
                             -------------------
        begin                : 2011-03-15
        copyright            : (C) 2011 by riviere
        email                : romain.riviere.974@gmail.com
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
import time
from ui_qspatialite import Ui_QspatiaLite
from browser.browser import browser
from browser.browser import browser as sqlbrowser
import qgis.utils
from dialogSRS import GdalToolsSRSDialog as SRSDialog
#initialize qt resource from ressource.py
import resources
# create the dialog for zoom to point
class QspatiaLiteDialog(QtGui.QDialog):
    def __init__(self, callbackFunction,  callbackFunction1,  callbackFunction2, callbackFunction3, callbackFunction4,callbackFunction5,callbackFunction6, parent=None):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_QspatiaLite()
        self.ui.setupUi(self)
	self.settings = QtCore.QSettings()
	#Load PySpatiaLite
	try:
        	from pyspatialite import dbapi2 as sqlite
	except:
		self.pop_up_error("PySpatiaLite python module is required for QSpatiaLite")
		return
        self.connectionModule = sqlite
	#Load Highlighter for SQLeditor
	import highlighter
	self.highlighter=highlighter
	SQLhighlighter = self.highlighter.MyHighlighter( self.ui.SQLeditor, "Classic" )
	#Gui TABS: queryPage,inspectPage,uploadPage
        self.queryPage = self.ui.tabWidget.widget(0)
        self.uploadPage = self.ui.tabWidget.widget(1)
	self.exportPage = self.ui.tabWidget.widget(2)
	#List Charsets
	self.encodings = ['ISO-8859-15','ISO-8859-1', 'ISO-8859-2', 'UTF-8', 'CP1250']
	self.ui.charset_gis.clear()
        self.ui.charset_gis.insertItems(0, self.encodings)
	self.ui.charsetList.clear()
        self.ui.charsetList.insertItems(0, self.encodings)
	self.ui.charsetExport.clear()
        self.ui.charsetExport.insertItems(0, self.encodings)
	self.ui.charsetList_DBF.clear()
        self.ui.charsetList_DBF.insertItems(0, self.encodings)
	self.ui.charsetList_CSV.clear()
        self.ui.charsetList_CSV.insertItems(0, self.encodings)
	self.ui.custom_col.setEnabled(False)
	#prepare listbox for CSV/TXT import
	decimal=['point (.)','comma (,)']
	self.decimals={'point (.)':'POINT','comma (,)':'COMMA'}
	self.ui.decimal.clear()
	self.ui.decimal.insertItems(0,decimal)
	textseparator=['double quote"','single quote\'']
	self.textseparator={'double quote"':'DOUBLEQUOTE','single quote\'':'SINGLEQUOTE'}
	self.ui.text.insertItems(0,textseparator)
	columnseparator=['Tab','Space','Comma ,','Colon :','Semicolon ;','Other']
	self.columnseparator={'Tab':"TAB",'Space':"' '",'Comma ,':"','",'Colon :':"':'",'Semicolon ;':"';'",'Other':""}
	self.ui.column.insertItems(0,columnseparator)
	#prepare GIS extensions for 'upload GIS Layers'
	gisExt="*.shp *.SHP *.tab *.TAB *.mif *.MIF *.gml *.GML *.kml *.KML *.xml *.XML" #all vector extension:shp|mif|tab|000|dgn|vrt|bna|csv|gml|gpx|kml|geojson|itf|xml|ili|gmt|sqlite|mdb|e00|dxf|gxt|txt|xml)
	self.ui.gisExt.setText(gisExt)
	#prepare file list for 'upload GIS Layers'
	self.resetFiles()
	#prepare ogr format list for "export spatial Tables"
	formats=[QtCore.QString(u'ESRI Shapefile'), QtCore.QString(u'Mapinfo File'), QtCore.QString(u'GeoJSON'), QtCore.QString(u'GeoRSS'), QtCore.QString(u'GMT'), QtCore.QString(u'SQLite'), QtCore.QString(u'Interlis 1'), QtCore.QString(u'GML'), QtCore.QString(u'Geoconcept'), QtCore.QString(u'DXF'), QtCore.QString(u'Interlis 2'), QtCore.QString(u'DGN'), QtCore.QString(u'CSV'), QtCore.QString(u'BNA'), QtCore.QString(u'GPX'), QtCore.QString(u'S57'), QtCore.QString(u'KML')]
	self.ui.outForm.insertItems(0,formats)
	#prepare listbox for query command
	command=["Fetch Query","Create Table","Create Spatial Table","Load in QGIS","Create Table and Load in QGIS","Create Spatial View","Create Spatial View and Load in QGIS"]
	self.ui.Command.insertItems(0,command)
	#system tables:
	self.systables=[ "geom_cols_ref_sys","geometry_columns" ,"geometry_columns_auth" ,"spatial_ref_sys", "sqlite_sequence" ,"views_geometry_columns" ,"virts_geometry_columns","layer_params","layer_statistics",
"layer_sub_classes","layer_table_layout","pattern_bitmaps","symbol_bitmaps","project_defs","raster_pyramids",
"tableprefix_metadata","tableprefix_rasters" ,"sqlite_stat1","sqlite_stat2","spatialite_history"]
	#initialize query historic for QueryBuilder
	self.last_query=None

	#Load SpatiaLite Connexion
	if self.list_connexions()!=True:
		self.connectionSettings=None
		self.connection=None
		pass
	else:
		if not self.connect_to_spatialite(): #get connectionSettings and connection to spatialite DB
			return
		#get spatialite version
		self.ui.SpatiaLiteVersion.setText(self.get_spatialite_version())
	#Load callback functions from Qspatialite.py
	self.callbackFunction = callbackFunction
	self.layerNames = callbackFunction1
	self.saveLayer = callbackFunction2
	self.removeTmpShp = callbackFunction3
	self.import_gis_files = callbackFunction4
	self.viewresult = callbackFunction5
	self.export2ogr = callbackFunction6

	# signals and slots:

        QtCore.QObject.connect(self.ui.tabWidget, 
                               QtCore.SIGNAL("currentChanged(int)"), 
                               self.load_qgis_layers)


        QtCore.QObject.connect(self.ui.connexionDB, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.connect_to_spatialite)

        QtCore.QObject.connect(self.ui.column, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.toggle_csv_custom_col)

        QtCore.QObject.connect(self.ui.pushButton, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.parse_SQL_text)

        QtCore.QObject.connect(self.ui.removeDB, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.removeDB)

        QtCore.QObject.connect(self.ui.export_2, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.ExportTablesToOgr)

        QtCore.QObject.connect(self.ui.uploadQGIS, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.upload_qgis_layers)

        QtCore.QObject.connect(self.ui.tablename, 
                               QtCore.SIGNAL("editingFinished()"), 
                               self.update_new_table_name)

        QtCore.QObject.connect(self.ui.Command, 
                               QtCore.SIGNAL("currentIndexChanged(const QString&)"), 
                               self.toggle_load_to_canvas)

        QtCore.QObject.connect(self.ui.justQgis, 
                               QtCore.SIGNAL("stateChanged(int)"), 
                               self.toggle_export2ogr)

        QtCore.QObject.connect(self.ui.geometry, 
                               QtCore.SIGNAL("textChanged(const QString&)"), 
                               self.update_geom_field)

        QtCore.QObject.connect(self.ui.id, 
                               QtCore.SIGNAL("textChanged(const QString&)"), 
                               self.update_id_field)

        QtCore.QObject.connect(self.ui.vacuum, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.vacuumDB)

        QtCore.QObject.connect(self.ui.treeView, 
                               QtCore.SIGNAL("doubleClicked(const QModelIndex &)"), 
                               self.query_item)

        QtCore.QObject.connect(self.ui.searchDBF, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.browseFile)

        QtCore.QObject.connect(self.ui.searchCSV, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.browseFileCSV)

        QtCore.QObject.connect(self.ui.folderExportChoose, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.folderExport)

        QtCore.QObject.connect(self.ui.precedent, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.precedent)

        QtCore.QObject.connect(self.ui.suivant, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.suivant)

        QtCore.QObject.connect(self.ui.searchSRID, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.browseSRID)

        QtCore.QObject.connect(self.ui.searchSRID2, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.browseSRID2)

        QtCore.QObject.connect(self.ui.sridExportChoose, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.browseSRID3)

        QtCore.QObject.connect(self.ui.uploadDBF, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.upload_DBF)

        QtCore.QObject.connect(self.ui.uploadCSV, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.uploadCSV)

        QtCore.QObject.connect(self.ui.helpsql, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.browser)

        QtCore.QObject.connect(self.ui.toolButton, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.queryBuilder)

        QtCore.QObject.connect(self.ui.helpquit, 
                               QtCore.SIGNAL("helpRequested()"), 
                               self.call_help)

        QtCore.QObject.connect(self.ui.newdb, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.NewDB)

        QtCore.QObject.connect(self.ui.addFiles, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.addFiles)

        QtCore.QObject.connect(self.ui.resetFiles, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.resetFiles)

        QtCore.QObject.connect(self.ui.Upload, 
                               QtCore.SIGNAL("clicked(bool)"), 
                               self.upload_gis_layers)

	#menu for resultsetview
	self.ui.result.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        QtCore.QObject.connect(self.ui.result, 
				QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), 
				self.menuContextResult)

	#Set rigth clik tree menu actions
	#refrech tree
	self.action_saveToCSV=QtGui.QAction("Save to TXT",self)
	QtCore.QObject.connect(self.action_saveToCSV, QtCore.SIGNAL('triggered()'), self.saveToCSV)
	self.action_ViewInQgis=QtGui.QAction("Load in QGIS",self)
	QtCore.QObject.connect(self.action_ViewInQgis, QtCore.SIGNAL('triggered()'), self.ViewInQgis)


	#menu for tree
	self.ui.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        QtCore.QObject.connect(self.ui.treeView, 
				QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), 
				self.menuContextTree)
	#Set rigth clik tree menu actions
	#refrech tree
	self.action_refresh=QtGui.QAction("Refresh",self)
	QtCore.QObject.connect(self.action_refresh, QtCore.SIGNAL('triggered()'), self.prepare_tree)
	#dropTable
	self.action_drop=QtGui.QAction("Drop Table",self)
	QtCore.QObject.connect(self.action_drop, QtCore.SIGNAL('triggered()'), self.droptable)
	#dropTable
	self.action_dropView=QtGui.QAction("Drop View",self)
	QtCore.QObject.connect(self.action_dropView, QtCore.SIGNAL('triggered()'), self.dropview)
	#ShowColumns
	self.action_showcol=QtGui.QAction("Show Columns",self)
	QtCore.QObject.connect(self.action_showcol, QtCore.SIGNAL('triggered()'), self.showcol)
	#ShowDataSample
	self.action_sample=QtGui.QAction("Show Sample",self)
	QtCore.QObject.connect(self.action_sample, QtCore.SIGNAL('triggered()'), self.showsample)
	#ShowAllDatas
	self.action_showall=QtGui.QAction("Show Table",self)
	QtCore.QObject.connect(self.action_showall, QtCore.SIGNAL('triggered()'), self.showall)
	#Rename
	self.action_rename=QtGui.QAction("Rename Table",self)
	QtCore.QObject.connect(self.action_rename, QtCore.SIGNAL('triggered()'), self.rename)
	#newtable
	self.action_newtable=QtGui.QAction("Create New Table",self)
	QtCore.QObject.connect(self.action_newtable, QtCore.SIGNAL('triggered()'), self.newtable)
	#newview
	self.action_newview=QtGui.QAction("Create New View",self)
	QtCore.QObject.connect(self.action_newview, QtCore.SIGNAL('triggered()'), self.newview)
	#Metadata
	self.action_metadata=QtGui.QAction("Metadata",self)
	QtCore.QObject.connect(self.action_metadata, QtCore.SIGNAL('triggered()'), self.metadata)
	#newcol
	self.action_newcol=QtGui.QAction("Add New Column",self)
	QtCore.QObject.connect(self.action_newcol, QtCore.SIGNAL('triggered()'), self.newcol)
	#newindex
	self.action_newindex=QtGui.QAction("Create New Index",self)
	QtCore.QObject.connect(self.action_newindex, QtCore.SIGNAL('triggered()'), self.newindex)
	#newtrigger
	self.action_newtrigger=QtGui.QAction("Create New Trigger",self)
	QtCore.QObject.connect(self.action_newtrigger, QtCore.SIGNAL('triggered()'), self.newtrigger)
	#newspatialIndex
	self.action_newspatialindex=QtGui.QAction("Create Spatial Index",self)
	QtCore.QObject.connect(self.action_newspatialindex, QtCore.SIGNAL('triggered()'), self.newspatialindex)
	#remove spatial index
	self.action_rmspatialindex=QtGui.QAction("Remove Spatial Index",self)
	QtCore.QObject.connect(self.action_rmspatialindex, QtCore.SIGNAL('triggered()'), self.rmspatialindex)
	#checkgeom
	self.action_checkgeom=QtGui.QAction("Check geometry",self)
	QtCore.QObject.connect(self.action_checkgeom, QtCore.SIGNAL('triggered()'), self.checkgeom)
	#toQGIS
	self.action_toQGIS=QtGui.QAction("Load in QGIS",self)
	QtCore.QObject.connect(self.action_toQGIS, QtCore.SIGNAL('triggered()'), self.toQGIS)
	#dump CSV
	self.action_dumpCSV=QtGui.QAction("Export as TXT/TAB",self)
	QtCore.QObject.connect(self.action_dumpCSV, QtCore.SIGNAL('triggered()'), self.dumpCSV)
	#dcolumn unique values
	self.action_colvalues=QtGui.QAction("Show Unique values",self)
	QtCore.QObject.connect(self.action_colvalues, QtCore.SIGNAL('triggered()'), self.colvalues)
	#recovergeometry
	self.action_recovergeometry=QtGui.QAction("Recover Geometry Column",self)
	QtCore.QObject.connect(self.action_recovergeometry, QtCore.SIGNAL('triggered()'), self.recovergeometry)
	#update column
	self.action_updatecolumn=QtGui.QAction("Update Column",self)
	QtCore.QObject.connect(self.action_updatecolumn, QtCore.SIGNAL('triggered()'), self.updatecolumn)

	#Set default values for tablename
	self.currentTable=''
	#set default values for Load to Canvas Option
        self.newTableName = None #New Table Name for "load to canvas"
	self.geomField="Geometry"
	self.idField="PKUID"
	self.ui.geometry.setEnabled(False)
	self.ui.id.setEnabled(False)
	self.ui.tablename.setEnabled(False)
	self.ui.geometry.setText('Geometry')
	self.ui.id.setText('PKUID')
	#current data for resulytsetview
	self.rowList=[]
	self.columnNames=[]
	#set query historic
	self.userQueries=[]
	self.currentQuery=-1
	#set default TAB WIDGET
        self.ui.tabWidget.setCurrentWidget(self.queryPage)#set current tab =tab1: queryPage

#Methodes
    def addFiles(self): #add files to fileList in 'upload gis layers'
	#Choose files
	ext=self.ui.gisExt.text()
	fileNames = QtGui.QFileDialog.getOpenFileNames(self, \
		QtCore.QString.fromLocal8Bit("Select layers:"),"", ext )

	if fileNames.count()<=0:
		return
	#creating/uploading a model for qlistview
	model = self.ui.filesList.model()
	for fileName in fileNames: 
		self.fileList.append(unicode(fileName))
		model.appendRow(QtGui.QStandardItem(fileName))
	self.ui.filesList.setModel(model)
	self.ui.filesList.show()

    def resetFiles(self): #reset fileList in 'upload gis layers'
	self.fileList=[]
	filesList_model = QtGui.QStandardItemModel(0,1)
        filesList_model.setHorizontalHeaderItem(0,QtGui.QStandardItem('Files to upload'))
	self.ui.filesList.setModel(filesList_model)
	self.ui.filesList.show()

    def upload_gis_layers(self): #upload files to fileList in 'upload gis layers'

	if len(self.fileList)<=0:
		self.pop_up_error('Please select files before, using ADD button')
		return

	#check desired srid
	try:
		srid=int(self.ui.sridFiles.text())
	except:
		QtGui.QMessageBox.warning(None, 'Uploading failed', "SRID must be INTEGER")
		return

	#check desired charset
	charset=unicode(self.ui.charset_gis.currentText())

	#get SQL for each file via callbackfunction
	SQL_List, params_List=self.import_gis_files(self.fileList,srid,charset)

	#create tables
	i=-1 #count
	errors=[] #stores non loaded files
	for SQL in SQL_List: #One element per table
		i+=1
		params=params_List[i] #get parameters for current table
		#get cursor
		cursor = self.connection.cursor()
		try:
			j=-1
			for sql in SQL:
				j+=1
				param=params[j]
				cursor.execute(sql,param)	

		except self.connectionModule.OperationalError, errorMsg:
			#self.pop_up_error("Error While upLoading GIS Layer:\n%s\n%s\nThe layer will not be uploaded"%(self.fileList[i],errorMsg)
			self.connection.rollback()
			cursor.close()
			errors.append(self.fileList[i])
			continue
		#everything is okay
		self.connection.commit()
		cursor.close()
	if len(errors)>0:
		errors='\n'.join(errors)
		self.pop_up_error('Non uploaded Files:\n%s'%errors)
	else:
		QtGui.QMessageBox.information(None,"Information","All the GIS Layers have been uploaded")
	self.resetFiles()
	self.ui.filesList.reset() #reset fileList
	self.prepare_tree()#reload tree
		
		


    def list_connexions(self):
        self.settings.beginGroup('/SpatiaLite/connections')
        connections = [item for item in self.settings.childGroups()]
	self.dblist=connections
        self.settings.endGroup()
	#case: no connection available
	if len(connections)==0:
		QtGui.QMessageBox.information(self, "No available Connections", "You apparently haven't defined any database connections yet.\n\n With SpatiaLite, you can create a new spatial database and/or connecting to an existing one by clicking on 'New DB' button.\n\n (To connect to a new DB, ignore the replace warning: your DB will not be replaced by a new empty one)")
		return False
	#case: connetions available
        self.ui.connexionDB.clear()
        self.ui.connexionDB.insertItems(0, connections)
	#try to select directly last opened dataBase
	try:
		lastDB=self.settings.value(u'/SpatiaLite/connections/selected').toString()
		lastDB=lastDB.split('@',1)[0]
		#get last connexion index
		i = self.dblist.index(lastDB)
		self.ui.connexionDB.setCurrentIndex(i)
	
	except:
		pass
	return True

    def NewDB(self):
	#path and name of new db
	path = QtGui.QFileDialog.getSaveFileName(self, "New DB","myDB.sqlite","Spatialite (*.sqlite)")
	if path.isEmpty():
		return
	name=unicode(path.split('/')[-1]) #get name
	#create Spatialite database
	conn=self.connectionModule.connect(unicode(path))
	cursor=conn.cursor() 
	cursor.execute("SELECT InitSpatialMetadata()")
	conn.close()
	#create SpatiaLite Connexion
        self.settings.beginGroup('/SpatiaLite/connections')
	self.settings.setValue(u'%s/sqlitepath'%name,'%s'%unicode(path))
        self.settings.endGroup()
	self.ui.connexionDB.setEnabled(False)
	self.list_connexions() #list new connexion
	#get new db index
	idx=0
	for item in self.dblist:
		if item==name:
			break
		idx=idx+1
	self.ui.connexionDB.setCurrentIndex(idx)
	self.ui.connexionDB.setEnabled(True)
	self.connect_to_spatialite()


    def removeDB(self):
	if len(self.dblist)<=1: #avoid to remove all DBs
		self.pop_up_error('You must have at least a DB connexion to get QSpatiaLite work. You should not remove this link before opening/creating a new DB')
		return
	selectedConnection = unicode(self.ui.connexionDB.currentText())
	reponse=QtGui.QMessageBox.question(self, "Remove DB link","Do you really want to remove the link to this DataBase: %s ? \n(This will not REMOVE your DataBase from your computer, just from QGIS/QSpatiaLite)"%selectedConnection, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
	if reponse==QtGui.QMessageBox.No:
		return
	#remove currentDB
	self.ui.connexionDB.setEnabled(False)
	self.settings.remove('/SpatiaLite/connections/%s'%selectedConnection)
	self.list_connexions()
	self.ui.connexionDB.setEnabled(True)
	self.connect_to_spatialite()

#contextual menu for treeview
    def menuContextTree(self, point):
	#define contextual menu
	self.menu=QtGui.QMenu(self)
	#retrieve item info
	item=self.ui.treeView.indexAt(point)
	#check if it is a table
	parent = item.parent().data().toString()
	section= item.parent().parent().data().toString()
	if parent not in ("","My Tables","Spatial Index","Sys. Table"): #this a a column...
		self.currentCol=unicode(item.data().toString()) #column name
		self.currentTable=unicode(item.parent().data().toString()) #table name
		#table metadata
		metadatas=item.parent().data(32).toList()
		if len(metadatas)>0:
			self.geomcol=unicode(item.parent().data(32).toList()[0].toString())
			self.reltype=unicode(item.parent().data(32).toList()[4].toString())
		else:
			self.geomcol=u""
			self.reltype=u'table'
		#general actions
		self.menu.addAction("Col: %s"%self.currentCol)
		self.menu.addSeparator()
		self.menu.addAction(self.action_updatecolumn)
		if self.geomcol!=self.currentCol:
			self.menu.addAction(self.action_colvalues)
			self.menu.addSeparator()
			if self.reltype=='table':
				self.menu.addAction(self.action_recovergeometry)
	else:
		name = unicode(item.data().toString())
		if name in ("","My Tables","Spatial Index","Sys. Table"):
			return
		#We are on a table
		self.currentTable=unicode(name)
		#table_metadata
		metadatas=item.data(32).toList()
		if len(metadatas)>0: #compatibility check : avoid "index out of range" pb
			self.geomcol=unicode(metadatas[0].toString())
			self.spatialindex=unicode(metadatas[3].toString())
			self.reltype=unicode(metadatas[4].toString())
			self.viewgeomcol=unicode(metadatas[5].toString())
		else:
			self.geomcol=""
			self.spatialindex="0"
			self.reltype='table'
			self.viewgeomcol=""

		#general actions
		self.menu.addAction("Table: %s"%self.currentTable)
		self.menu.addSeparator()
		self.menu.addAction(self.action_refresh)
		self.menu.addSeparator()
		self.menu.addAction(self.action_newtable)
		self.menu.addAction(self.action_newview)
		self.menu.addSeparator()
		self.menu.addAction(self.action_dumpCSV)
		if (self.geomcol!="") or (self.viewgeomcol!=""):
			self.menu.addAction(self.action_toQGIS)
		self.menu.addSeparator()
		self.menu.addAction(self.action_showall)
		self.menu.addAction(self.action_sample)
		self.menu.addAction(self.action_showcol)
		self.menu.addSeparator()
		if self.reltype=='table':
			self.menu.addAction(self.action_newcol)
			self.menu.addAction(self.action_rename)
			self.menu.addAction(self.action_drop)
		else:
			self.menu.addAction(self.action_dropView)		
		self.menu.addSeparator()
		self.menu.addAction(self.action_newindex)
		self.menu.addAction(self.action_newtrigger)	
		#geometry tables
		if self.geomcol!="":
			#SpatialIndex add/remove
			if self.spatialindex=='1':
				self.menu.addAction(self.action_rmspatialindex)
			else:
				self.menu.addAction(self.action_newspatialindex)
			self.menu.addSeparator()
			self.menu.addAction(self.action_checkgeom)
			self.menu.addAction(self.action_metadata)
	self.menu.exec_(QtGui.QCursor.pos())

#contextual menu for resultSetView
    def menuContextResult(self, point):
	#define contextual menu
	self.menu2=QtGui.QMenu(self)
	#general actions
	self.menu2.addAction(self.action_saveToCSV)
	self.menu2.addAction(self.action_ViewInQgis)
	self.menu2.exec_(QtGui.QCursor.pos())

    def precedent(self): #set previous query
	if len(self.userQueries)<1: #no historic
		return
	self.currentQuery=max(self.currentQuery-1,0)
	query=self.userQueries[self.currentQuery] 
	self.ui.SQLeditor.setPlainText(query)

    def suivant(self): #set next query
	if len(self.userQueries)<1: #no historic
		return
	self.currentQuery=min(self.currentQuery+1,len(self.userQueries)-1)
	query=self.userQueries[self.currentQuery] 
	self.ui.SQLeditor.setPlainText(query)

    def add_historic(self,selectQuery): #add new query to historic
	if len(self.userQueries)<1: #first query to be saved
		self.userQueries.append(selectQuery) #add query to historic
		self.currentQuery+=1 
	elif selectQuery != self.userQueries[self.currentQuery] and selectQuery !="": #new query to save
		self.userQueries.append(selectQuery) #add query to historic
		self.currentQuery+=1 

    def vacuumDB(self): #vacuumDB
	query="VACUUM"
	reponse=QtGui.QMessageBox.question(self, "PERFORM VACUUM DB","Do you really want to VACUUM DataBase ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
	if reponse==QtGui.QMessageBox.Yes:
		try:
	        	self.run_normal_query(query)
			QtGui.QMessageBox.information(self, "VACUUM PERFORMED", "VACUUM performed")
		except:
			QtGui.QMessageBox.information(self, "VACUUM ERROR", "Unable to perfom VACUUM on the current Database")
    def dropview(self): #drop view
	table=self.currentTable
	if table=='' or self.reltype!='view':
		return False
	#Table isn't empty
	if table in self.systables: #is it a system table ?
		self.pop_up_error("System table, you'd better not to remove it")
		return
	reponse=QtGui.QMessageBox.question(self, "DROP VIEW","Do you really want to DROP view: %s ?"%table, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
	if reponse==QtGui.QMessageBox.Yes: #user has confirmed action
		query="""DROP VIEW "%s" """%table
        	self.run_normal_query(query)
		isgeom=self.viewgeomcol
		if isgeom!='':
			query="DELETE FROM views_geometry_columns WHERE view_name = ? AND view_geometry = ? "
			params=(table,isgeom,)
			self.run_normal_query(query,params)
		QtGui.QMessageBox.information(self, "View dropped", "View %s dropped"%table)
		#prepare tree
		self.prepare_tree()
		#reset inspect page
		self.currentTable=''
	
    def droptable(self): #dropTable
	#to do: fordib system table removal ....
	table=self.currentTable
	if table=='':
		return False
	#Table isn't empty
	if table in self.systables: #is it a system table ?
		self.pop_up_error("System table, you'd better not to remove it")
		return
	reponse=QtGui.QMessageBox.question(self, "DROP TABLE","Do you really want to DROP table: %s ?"%table, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
	if reponse==QtGui.QMessageBox.Yes: #user has confirmed action
		table_col=self.get_columns(table) #check real col name
		#if geometry table: drop geometry column in corresponding system table
		#isgeom=''
		#for col in table_col:
		#	if col[1].upper()==unicode(self.geomcol).upper(): # case insensitive
		#		isgeom=col[1]
		isgeom=self.geomcol
		if isgeom!='':
			query="DELETE FROM geometry_columns WHERE f_table_name = ? AND f_geometry_column = ? " 
			params=(table,isgeom,)
			self.run_normal_query(query,params)
		if self.spatialindex=='1':
			#drop spatialIndex if exists
			query="SELECT disableSpatialIndex(?,?) "
			params=(table,isgeom,)
			self.run_normal_query(query,params)
			query="""DROP TABLE IF EXISTS "idx_%s_%s" """ %(table,isgeom)
			self.run_normal_query(query)
			query="""DROP TABLE IF EXISTS "cache_%s_%s" """ %(table,isgeom)
			self.run_normal_query(query)

		query="""DROP TABLE "%s" """%table
        	self.run_normal_query(query)
		QtGui.QMessageBox.information(self, "Table dropped", "Table %s dropped"%table)
		#prepare tree
		self.prepare_tree()
		#reset inspect page
		self.currentTable=''
	

    def prepare_tree(self):
	#list tables
	tableList = self.get_tables() # for each table: tablename, reltype, geom_col, geom_type, geom_dim, geom_srid, index_spatial_enable, spatialViewname
	self.spatialTables=dict()
	#prepare RTree Model
	model = QtGui.QStandardItemModel(0,1)
        model.setHorizontalHeaderItem(0,QtGui.QStandardItem('Tables'))
	user_item=QtGui.QStandardItem("My Tables")
	index_item=QtGui.QStandardItem("Spatial Index")
	system_item=QtGui.QStandardItem("Sys. Table")
        for record in tableList: #List tables
		#to do: detect virtual tables
		geo=0
		if record[3] is not None: #detects geometry Type and assign icons
			geo=1 #it's a geo table
			if record[3] in ('POINT','MULTIPOINT'):
				item=QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/layer_point.png"),record[0])
			elif record[3] in ('LINESTRING','MULTILINESTRING'):
				item=QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/layer_line.png"),record[0])
			elif record[3] in ("POLYGON","MULTIPOLYGON","GEOMETRYCOLLECTION"):
				item=QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/layer_polygon.png"),record[0])
			else:
				item=QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/layer_unknown.png"),record[0])
			self.spatialTables[record[0]]=[record[2],record[5]] #add table to spatial table list (for export2ogr)
		else:
			if record[0] in self.systables: #system table
				item=QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/systable.xpm"),record[0])
			elif record[1]=='view': #Detects VIEWS
				if record[7] not in ("",None): #SpatialView
					geo=2
					item=QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/spatialview.png"),record[0])
				else:
					item=QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/view.png"),record[0])
			else:
				item=QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/table.png"),record[0])
		#metadata for each table
		meta=[record[2],record[3],record[5],record[6],record[1],record[7]] #geom_col, geom_type, geom_srid, spatial index enable,rel type,spatialviewgeometrycol
		item.setData(meta,32)
		if (record[0] in self.systables):
			system_item.appendRow(item)
		elif (record[0][:4].upper()=="IDX_"):
			index_item.appendRow(item)
		else: 
                	user_item.appendRow(item)
		columnsList = self.get_columns(record[0])
		for col in columnsList: #List Columns
			if col[5]==1: #Pk
				item.appendRow(QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/pkey.xpm"),col[1]))
			elif geo==1 and col[1]==meta[0]: #geo column
				if meta[3]==1: # spatial index
					item.appendRow(QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/spatialidx.xpm"),col[1]))
				else:
					item.appendRow(QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/geometry.xpm"),col[1]))
			elif geo==2 and col[1]==meta[5]: #view geocol
				item.appendRow(QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/geometry.xpm"),col[1]))
			else:
				item.appendRow(QtGui.QStandardItem(QtGui.QIcon(":/plugins/QspatiaLite/icons/column.xpm"),col[1]))
	model.appendRow(user_item)
	model.appendRow(index_item)
	model.appendRow(system_item)
        self.ui.treeView.setModel(model)
	self.ui.treeView.setExpanded(model.index(0, 0),True)

    def get_spatialite_version(self):
	query="SELECT SpatiaLite_Version()"
	rowList, columnNames = self.run_normal_query(query)
	result=rowList[0]
	if result[0][2]=='3':
		QtGui.QMessageBox.information(self, "SpatiaLite v2.3", "You are using SpatiaLite V2.3 ( standart with QGIS<1.7). Please note that QspatiaLite full potential require SpatiaLite V2.4. Please update your SpatiaLite version, or move to QGIS 1.7")
	return str(result[0])

    def parse_SQL_text(self):
        # not parsing anything at the moment, this may change in the future
        selectQuery = unicode(self.ui.SQLeditor.toPlainText()).strip()
        if selectQuery.endswith(';'):
            selectQuery = selectQuery[:-1]
	self.add_historic(selectQuery) 
	self.execute_query(selectQuery) 
	self.ui.Command.setCurrentIndex(0)

#Menu Specific Actions_______________________________________________________________________
    def showsample(self):
        table = self.currentTable
	if table != "":
		query = """SELECT * FROM "%s" LIMIT 10 """ %table
            	rowList, columnNames = self.run_normal_query(query)
		self.add_historic(query)
		self.ui.SQLeditor.setPlainText(query)
            	self.update_table_widget(self.ui.result, columnNames, rowList)
		self.ui.tabWidget.setCurrentWidget(self.queryPage)
    def showall(self):
        table = self.currentTable
	if table != "":
		query = """SELECT * FROM "%s" """ %table
            	rowList, columnNames = self.run_normal_query(query)
		self.add_historic(query)
		self.ui.SQLeditor.setPlainText(query)
            	self.update_table_widget(self.ui.result, columnNames, rowList)
		self.ui.tabWidget.setCurrentWidget(self.queryPage)
    def rename(self):
        table = self.currentTable
	isgeom = self.geomcol #can't rename geometry tables
	if isgeom!='':
		self.pop_up_error("This is a Spatial Table, you'd better not to rename it\nAnyway, you can create a new table from this one with the good name and then delete the old one.")
		return
	if table != "":
		(name, ok) = QtGui.QInputDialog.getText (self, 
                        "Enter New Table Name", 
                        "Name:")
		if (not ok) or name=='':
			return
		query = """ALTER TABLE "%s" RENAME TO "%s" """ %(table,name.replace('"'," "))
		self.add_historic(query)
		self.ui.SQLeditor.setPlainText(query)
		if self.run_normal_query(query):
			QtGui.QMessageBox.information(self, "Table renamed", "Table %s is now called %s "%(table,name))
			self.ui.tabWidget.setCurrentWidget(self.queryPage)
			self.prepare_tree()
    def newtable(self):
	#query = 'CREATE TABLE ...name... ( \n...column1,\n...column2,\n...columnN)'
	#self.ui.SQLeditor.setPlainText(query)
	#self.ui.tabWidget.setCurrentWidget(self.queryPage)
	from newtable.newtable import newtable
	self.createtable = newtable(self.connection,self.prepare_tree,SRSDialog)
	self.createtable.setModal(False)
	self.createtable.show()	
    def newview(self):
	query = 'CREATE VIEW ...name... AS \nSELECT ...sql-select-statement..'
	self.ui.SQLeditor.setPlainText(query)
	self.ui.tabWidget.setCurrentWidget(self.queryPage)
    def newcol(self):
        table = self.currentTable
	if table != "":
		query = 'ALTER TABLE "%s" \nADD COLUMN ...col-name col-type...'%table
		self.ui.SQLeditor.setPlainText(query)
		self.ui.tabWidget.setCurrentWidget(self.queryPage)
    def newindex(self):
        table = self.currentTable
	if table != "":
		query = 'CREATE [ UNIQUE ] INDEX ...indexname....\n ON "%s" \n(\n ...col1, col2, colN...\n)'%table
		self.ui.SQLeditor.setPlainText(query)
		self.ui.tabWidget.setCurrentWidget(self.queryPage)
    def newtrigger(self):
        table = self.currentTable
	if table != "":
		query = 'CREATE TRIGGER ...name...\n [BEFORE | AFTER ] \n [INSERT | UPDATE | DELETE ]\nON "%s" \n ...sql-statement...'%table
		self.ui.SQLeditor.setPlainText(query)
		self.ui.tabWidget.setCurrentWidget(self.queryPage)
    def newspatialindex(self):
        table = self.currentTable
	geocol=self.geomcol
	index=self.spatialindex
	if table != "" and geocol !="" and index=='0': #no spatial index on table
		query = "SELECT CreateSpatialIndex(?,?)"
		params=(table,geocol,)
		cursor=self.connection.cursor()
		cursor.execute(query,params)
		rep=cursor.fetchall()
		if rep[0][0]==0:
			self.pop_up_error("Can't create SpatialIndex")
		elif rep[0][0]==1:
			QtGui.QMessageBox.information(self, "Spatial Index Created", "New Spatial Index created for table '%s' , on column '%s'"%(table,geocol))
			self.prepare_tree()
    def rmspatialindex(self):
        table = self.currentTable
	geocol=self.geomcol
	index=self.spatialindex
	reponse=QtGui.QMessageBox.question(self, "DROP Spatial Index","Do you really want to DROP Spatial Index on table %s ?"%table, 							QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
	if reponse!=QtGui.QMessageBox.Yes: #user hasn't confirmed action
		return
	if table != "" and geocol !="" and index=='1': #spatial index on table
		query1 = "SELECT DisableSpatialIndex(?,?)"
		params=(table,geocol,)
		query2 = """ DROP TABLE IF EXISTS "idx_%s_%s" """%(table,geocol)
		cursor=self.connection.cursor()
		cursor.execute(query1,params)
		rep=cursor.fetchall()
		if rep[0][0]!=1:
			self.pop_up_error("Can't disable Spatial Index: idx_%s_%s"%(table,geocol))
			return
		cursor.execute(query2)
		self.prepare_tree()
		QtGui.QMessageBox.information(self, "Spatial Index Removed", "Spatial Index idx_%s_%s removed"%(table,geocol))

    def metadata(self):
        table = self.currentTable
	geocol = self.geomcol
	if table != "" and geocol != "":
		query = "SELECT * FROM geom_cols_ref_sys WHERE f_table_name = ? AND f_geometry_column = ? "
		params=(table,geocol,)
            	rowList, columnNames = self.run_normal_query(query,params)
		query_deco="SELECT * FROM geom_cols_ref_sys WHERE f_table_name = %s AND f_geometry_column = %s "%(table,geocol)
		self.add_historic(query_deco)
		self.ui.SQLeditor.setPlainText(query_deco)
            	self.update_table_widget(self.ui.result, columnNames, rowList)
		self.ui.tabWidget.setCurrentWidget(self.queryPage)

#load a table in qgis
    def toQGIS(self): 
	table = self.currentTable
	geocol=self.geomcol
	if geocol=="":
		geocol=self.viewgeomcol
	if table!="" and geocol!="":
		self.callbackFunction(table, "spatialite", self.connectionSettings, geocol, 'rowid', table)

    def showcol(self):
	tableName = self.currentTable
        if tableName != '':
		query = 'PRAGMA table_info("%s")' % tableName
		self.ui.SQLeditor.setPlainText(query)
		self.add_historic(query)
		rowList, columnNames = self.run_normal_query(query)
		self.update_table_widget(self.ui.result, columnNames, rowList)
		self.ui.tabWidget.setCurrentWidget(self.queryPage)

#check geometry and try to sanitize if find non valid
    def checkgeom(self):
	tableName = self.currentTable
	geocol=self.geomcol
        if tableName != '' and geocol!="":
		query = """SELECT rowid FROM "%s" \n WHERE isValid("%s"."%s")<>1 """ % (tableName,tableName,geocol)
		self.ui.SQLeditor.setPlainText(query)
		self.add_historic(query)
		rowList, columnNames = self.run_normal_query(query)
		self.update_table_widget(self.ui.result, columnNames, rowList)
		self.ui.tabWidget.setCurrentWidget(self.queryPage)
		if rowList==[("This is not an error",)]: 
			QtGui.QMessageBox.information(self, "Information", "Geometry is valid")
		else: #invalid geom detected
			reponse=QtGui.QMessageBox.question(self, "Invalid geometry detected","Your table contains at least 				one incorrect geometry (see resultSet).\n\nTry to sanitize invalid geometries ?", 				QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
			if reponse==QtGui.QMessageBox.Yes:
				query = """UPDATE "%s" \nSET "%s"=sanitizegeometry("%s"."%s")\nWHERE isValid("%s"."%s")<>1"""%(tableName,geocol,tableName,geocol,tableName,geocol)
				self.add_historic(query)
        			self.run_normal_query(query)
				self.ui.SQLeditor.setPlainText(query)
				QtGui.QMessageBox.information(self, "SanitizeGeometry Performed", "Please note: current implementation only affects:\n- repeated vertices suppression\n- Ring's closure enforcement")

    def colvalues(self): #get unique values for current column
	table=self.currentTable
	col=self.currentCol
	if table=='' or col=='':
		return
	query="""SELECT "%s"."%s" FROM "%s" GROUP BY 1"""%(table,col,table)
	rowList, columnNames = self.run_normal_query(query)
	self.valuelist=browser()
	txt="<p>Unique Values for column <b>%s</b> (table: <b>%s</b>):</p><p>(Select value, then Drag and drop it to SQL editor)</p>"%(col,table)
	for val in rowList:
		try:
			txt+="<p>%s</p>"%val
		except:
			txt+="<p>GeomObject</p>"
	self.valuelist.ui.textBrowser.setHtml(txt)
	self.valuelist.setModal(False)
	self.valuelist.show()

    def updatecolumn(self): #update column
	table=self.currentTable
	col=self.currentCol
	if table=='' or col=='':
		return
	query="""UPDATE "%s" SET '%s'= ... \nWHERE ...conditions..."""%(table,col)
	self.ui.tabWidget.setCurrentWidget(self.queryPage)
	self.ui.SQLeditor.setPlainText(query)	
						
#__________________________________________________________________________________________

    def toggle_load_to_canvas(self):
        if self.ui.Command.currentText() in ["Load in QGIS","Create Table and Load in QGIS","Create Spatial Table","Create Spatial View","Create Spatial View and Load in QGIS"]: 
            self.ui.geometry.setEnabled(True)
            self.ui.id.setEnabled(True)
            self.ui.tablename.setEnabled(True)
            if 	self.ui.Command.currentText() in ["Create Spatial View","Create Spatial View and Load in QGIS"]: # spatial view need Idfield to be ROWID
		self.ui.id.setText('ROWID')
            else:
		self.ui.id.setText('PKUID')		
        elif self.ui.Command.currentText()=="Create Table":
            self.ui.tablename.setEnabled(True)
            self.ui.geometry.setEnabled(False)
            self.ui.id.setEnabled(False)
	else:
            self.ui.tablename.setEnabled(False)
            self.ui.geometry.setEnabled(False)
            self.ui.id.setEnabled(False)

    def toggle_export2ogr(self):
	if self.ui.justQgis.isChecked():
		self.ui.outForm.setEnabled(False)
		self.ui.folderExport.setEnabled(False)
		self.ui.folderExportChoose.setEnabled(False)
		self.ui.charsetExport.setEnabled(False)
		self.ui.sridExportChoose.setEnabled(False)
		self.ui.sridExport.setEnabled(False)
	else:
		self.ui.outForm.setEnabled(True)
		self.ui.folderExport.setEnabled(True)
		self.ui.folderExportChoose.setEnabled(True)
		self.ui.charsetExport.setEnabled(True)
		self.ui.sridExportChoose.setEnabled(True)
		self.ui.sridExport.setEnabled(True)

    def update_new_table_name(self):
        # use a validator in the future
        self.newTableName = unicode(self.ui.tablename.text())
	if self.newTableName=="":
		self.newTableName=None

    def update_geom_field(self):
        # use a validator in the future
        self.geomField = unicode(self.ui.geometry.text())

    def update_id_field(self):
        # use a validator in the future
        self.idField = unicode(self.ui.id.text())


    def query_item(self, index):
	if self.ui.tabWidget.currentWidget()==self.queryPage:
		queryWord = index.data().toString()
		parent = index.parent().data().toString() #parent
		if parent not in ('',"My Tables","Spatial Index","Sys. Table"): #user has clicked on a column name
			queryWord=""" "%s".'%s'""" %(parent,queryWord)
		else: #user has clicked on a table name
			queryWord=' "%s"' %queryWord
		if index.data().toString() not in ('',"My Tables","Spatial Index","Sys. Table"):
			self.ui.SQLeditor.insertPlainText(queryWord)
			self.ui.SQLeditor.setFocus()

    def add_geometry_column(self, initialQuery):
        # run the initial query again, to determine the srid and geometry type
        alteredQuery = '''
        SELECT DISTINCT srid, geomType 
        FROM (
            SELECT SRID(a."%s") AS srid, GeometryType(a."%s") AS geomType 
            FROM (%s) as a
        )
        ''' % (self.geomField, self.geomField, initialQuery) 
        print("getting srid and geomType...")
        rowList, columnNames = self.run_normal_query(alteredQuery)
        srid = rowList[0][0]
        geomType = rowList[0][1]
	#get real column name: Geometry <-> geometry ... case problem
	tablecols=self.get_columns(self.newTableName) #get real columns names
	for col in tablecols:
		if col[1].upper()==self.geomField.upper():
			self.geomField=col[1] #be sure geometry column name refer to real column name
        query = 'SELECT RecoverGeometryColumn(?, ?, ?, ?, 2)'
	params=(self.newTableName, self.geomField, srid, geomType,)
        print("adding support for geometry...")
        rowList, columnNames = self.run_normal_query(query,params)

    def execute_query(self, selectQuery):
    	if self.ui.Command.currentText() in ["Create Spatial Table","Create Table and Load in QGIS"]:
		print("creating a new table")# and add primary key to new spatial table -> prevent any further spatial index pb
		cursor=self.connection.cursor()
		try:
		    #create table tmp
		    createViewQuery = """CREATE TABLE "%s_tmp" AS %s """ % (self.newTableName, selectQuery)
		    cursor.execute(createViewQuery)
		    	#get new view column
		    cols=self.get_columns('%s_tmp'%self.newTableName)
		    colList="PKUID integer primary key autoincrement," #create primary key
		    colList2=""
		    colList3=""	
		    for col in cols:
			colname=col[1]
			if col[1].upper()=="PKUID": #PKUID already exists...
				print "Former PKUID deleted"
			else:
				colList3+=""" "%s_tmp"."%s","""%(self.newTableName,colname)
				colList2+='"%s",'%colname
				colList+='"%s",'%colname
		    colList=colList[:-1]
		    colList2=colList2[:-1]
		    colList3=colList3[:-1]			
		    #Create new table
		    createTableQuery = """CREATE TABLE "%s" (%s)"""%(self.newTableName,colList)
		    cursor.execute(createTableQuery)
		    #Populate Table			
		    createTableQuery = """INSERT INTO "%s" (%s) SELECT %s FROM "%s_tmp" """%(self.newTableName,colList2,colList3,self.newTableName)
		    cursor.execute(createTableQuery)
		    #createTableQuery = "CREATE TABLE '%s' AS %s" % (self.newTableName, selectQuery)
		    #self.run_normal_query(createTableQuery)
		    query="""DROP TABLE "%s_tmp" """%self.newTableName #drop view
		    cursor.execute(query)	
		except:
		    self.pop_up_error("Error while saving the new table")
		    self.connection.rollback()
		    query="""DROP TABLE IF EXISTS "%s" """%self.newTableName #drop table
		    cursor.execute(query)
		    query="""DROP TABLE IF EXISTS "%s_tmp" """%self.newTableName #drop table tmp
		    cursor.execute(query)
		    self.connection.commit()
		    cursor.close()						
		    return		
		self.connection.commit()
		cursor.close()
		print("created the new table. About to insert geometry info...")
		try:
			self.add_geometry_column(selectQuery) # add srid and geomType
		except:
			self.pop_up_error("Unable to recover geometry column")
			cursor=self.connection.cursor()
			cursor.execute("""DROP TABLE IF EXISTS "%s" """%self.newTableName)
			self.connection.commit()
			cursor.close()
			return
		if self.ui.Command.currentText()=="Create Table and Load in QGIS": 
			self.callbackFunction(self.newTableName, "spatialite", self.connectionSettings, self.geomField, self.idField, self.newTableName)
	elif self.ui.Command.currentText() in ["Create Spatial View","Create Spatial View and Load in QGIS"]:
		print("creating a new spatial view")
		cursor=self.connection.cursor()
		try:
		    #create view
		    createViewQuery = """CREATE VIEW "%s" AS %s""" % (self.newTableName, selectQuery)
		    cursor.execute(createViewQuery)
		    #Is geomfield ok?	
		    view_geocol=[col[1] for col in self.get_columns(self.newTableName) if col[1].upper()==self.geomField.upper()] # [] if geomfield incorect
		    if len(view_geocol)==0: #geomfield is incorrect
			cursor.execute("""DROP VIEW IF EXISTS "%s" """%self.newTableName)
			self.pop_up_error("Incorrect Geometry Column")
			return
		    else:
			self.geomField=unicode(view_geocol[0])
		    #ask some informations to user:
		    tables=["%s.%s"%(table[0],table[2]) for table in self.get_tables() if table[2] is not None]			
		    (ref_table, ok) = QtGui.QInputDialog.getItem (self, 
                        "Source geometry table:", 
                        "Name:",tables)
		    if (not ok) or ref_table=='':
			cursor.execute("""DROP VIEW IF EXISTS "%s" """%self.newTableName)
			return		
		    self.original_table=unicode(ref_table.split(".")[0])
		    self.original_geomfield=unicode(ref_table.split(".")[1])					
		    #recover geometry column			
		    query = "INSERT INTO views_geometry_columns (view_name, view_geometry, view_rowid, f_table_name, f_geometry_column) VALUES (?, ?, 'ROWID', ?, ?)"
		    params=(self.newTableName,self.geomField,self.original_table,self.original_geomfield,)	
		    self.run_normal_query(query,params)	
		except:
		    self.pop_up_error("Error while saving the new view")
		    cursor.close()
		    self.connection.rollback()						
		    return		
		cursor.close()
		self.connection.commit()
		if self.ui.Command.currentText()=="Create Spatial View and Load in QGIS": 
			self.callbackFunction(self.newTableName, "spatialite", self.connectionSettings, self.geomField, self.idField, self.newTableName)

	elif self.ui.Command.currentText()=="Load in QGIS":
		selectQuery = "(%s)" % selectQuery
		# use QGIS's own methods to run the query and return a new map layer
		self.callbackFunction(selectQuery, "spatialite", 
		                      self.connectionSettings, self.geomField, self.idField, self.newTableName)
        else:
            # use python's own SQL modules (pyspatialite, psycopg2) to run the query
            if self.ui.Command.currentText()=="Create Table": #user want to create a new table
			selectQuery = """CREATE TABLE "%s" AS %s """ %(self.newTableName,selectQuery)
            rowList, columnNames = self.run_normal_query(selectQuery)
            self.update_table_widget(self.ui.result, columnNames, rowList)
		
	self.prepare_tree()

    def get_tables(self):   #liste les tables et leur description	
	query = """SELECT m.name, m.type, g.f_geometry_column, g.type, g.coord_dimension, g.srid, g.spatial_index_enabled, 			v.view_geometry
		FROM sqlite_master AS m LEFT JOIN geometry_columns AS g ON m.name = g.f_table_name
		LEFT JOIN views_geometry_columns AS v ON m.name = v.view_name
		WHERE m.type in ('table', 'view') ORDER BY m.name, g.f_geometry_column"""
	#rowList, columnNames = self.run_normal_query(query)
	#tableList = [row for row in rowList]
	#return rowList
	cursor = self.connection.cursor()
	items=[]
        try:
		cursor.execute(query)
		for geo_item in cursor.fetchall():
			items.append( geo_item )
		cursor.close()
        except:
		self.pop_up_error("This DB a valid SQlite DB, but not a valid SpatiaLite DB. QSpatiaLite will now try to Create a valid SpatiaLite DB")
		row,col=self.run_normal_query("SELECT initspatialmetadata()")
		if row[0][0]==1:
			self.pop_up_error("This DB is now a valid SpatiaLite DB")
		else:
			self.pop_up_error("Error. Try to execute by yourself: SELECT InitSpatialMetadata()")
			return [] 
		try:
			cursor.execute(query)
			for geo_item in cursor.fetchall():
				items.append( geo_item )
			cursor.close()
		except self.connectionModule.OperationalError, errorMsg:
			self.pop_up_error("Impossible to get DB tables.\n\n%s\n\n'" %errorMsg)

	return items

    def get_columns(self, tableName):   #list columns
        #self.connection.text_factory = str  #return text as bytestring instead of unicode
        query = 'PRAGMA table_info("%s")' % tableName
	cursor = self.connection.cursor()
	items=[]
	rep=cursor.execute(query)
	try:
		for geo_item in rep:
			items.append(geo_item)
        except self.connectionModule.OperationalError, errorMsg:
		self.pop_up_error("Invalid Operation.\n\n%s" %
                                errorMsg)
	cursor.close()
	return items

    def get_geocol(self, tableName):
        query = """SELECT g.f_geometry_column
		FROM sqlite_master AS m LEFT JOIN geometry_columns AS g ON m.name = g.f_table_name
		WHERE m.name=?"""
	cursor = self.connection.cursor()
	items=[]
        try:
		cursor.execute(query,tuple(tableName))
		for geo_item in cursor.fetchall():
			items.append( geo_item )
        except self.connectionModule.OperationalError, errorMsg:
		self.pop_up_error("Invalid Operation.\n\n%s" %
                                errorMsg)
	cursor.close()
	return items #col name


    def connect_to_spatialite(self):
	if not self.ui.connexionDB.isEnabled():
			return
        selectedConnection = unicode(self.ui.connexionDB.currentText())
        self.connectionSettings = dict()
        self.settings.beginGroup(u"/SpatiaLite/connections/%s" %selectedConnection) 
        for item in self.settings.allKeys():
            self.connectionSettings[unicode(item)] = unicode(self.settings.value(item).toString())
        self.settings.endGroup()
	try:
        	self.connection=self.connectionModule.connect(self.connectionSettings[u"sqlitepath"])  #connect to selected SQLITE DB
	except: #can't connect to last DB
		# Remove non valid link
		self.settings.remove('/SpatiaLite/connections/%s'%selectedConnection)
		self.pop_up_error("Impossible to connect to last opened DataBase.\nThe link has been removed from QGIS.\nPlease Restart QSpatiaLite")
		return False
	self.prepare_tree() # prepare tree for new DB
	#save last used DB
	self.settings.setValue('/SpatiaLite/connections/selected',unicode(self.ui.connexionDB.currentText())+'@'+self.connectionSettings[u"sqlitepath"])
	return True

    def run_normal_query(self, query, param=None):  #param=sal parameters: '?'
        cursor = self.connection.cursor()
        rowList = []
        columnNames = []
        try:
            start=time.clock()
            if param is None:		
            	cursor.execute(query)	
            else:
		cursor.execute(query,tuple(param))	
            if (cursor.description is not None): # empty resultset
                rowList = [row for row in cursor]
                columnNames = [item[0] for item in cursor.description]
            stop=time.clock()
            elapsed_time=round(stop-start,3)
            self.resultrows=len(rowList)
            self.ui.time.setText("SQL Elapsed Time: %s s" %elapsed_time)
        except self.connectionModule.OperationalError, errorMsg:
            self.connection.rollback()	
            cursor.close()
            self.pop_up_error("The SQL query seems to be invalid.\n\n%s" %
                                errorMsg)
            self.resultrows=0
            return [("Incorrect Query",)],["Error"]
	self.connection.commit()
	cursor.close()
	if len(rowList)==0:
		columnNames=["Empty ResultSet"]
		rowList=[("This is not an error",)]
		self.resultrows=0
	return rowList, columnNames

    def pop_up_error(self, msg=''):
        QtGui.QMessageBox.warning(None, 'error', '%s' % (msg))

	
#Import selected Layer in SpatiaLite
    def load_qgis_layers(self):
	if self.connection is None:
		return
	elif self.ui.tabWidget.currentWidget()==self.uploadPage: #executed only on tab2
		layerList=self.layerNames()
		self.ui.layerlist.clear()
		self.ui.layerlist.insertItems(0, layerList)
	elif self.ui.tabWidget.currentWidget()==self.exportPage: # get all geometry tables
		self.prepare_tree() #refresh tree
		self.ui.geomTables.clear()
		#creating/uploading a model for qlistview
		for table in self.spatialTables.keys(): 
			self.ui.geomTables.addItem(table)
		self.ui.geomTables.show()
		
		
#Upload QGIS Layer:
    def upload_qgis_layers(self):
	#detect parameters
	try:
		layer=self.ui.layerlist.currentText()
		layer=unicode(layer)
		name=self.ui.name.text()
		name=str(name)
		vname=name+'_tmp'
		charset=self.ui.charsetList.currentText()
		charset=str(charset)
		srid=self.ui.srid.text()
		srid=str(srid)
	except:
		self.pop_up_error("No accents/special characters please")
		return False
		
	if (layer=='') or (name=='') or(charset=='') or(srid ==''):
		self.pop_up_error("All the fields are necessary")
	else:
		try:
			srid=int(srid)
		except:
			self.pop_up_error("SRID must be INTEGER")
			return False
		#verify if table already exists in DB
		tablelist=self.get_tables()
		for table in tablelist:
			if table[0]==name:
				self.pop_up_error("Table name already exists")
				return False
		selected=self.ui.selectedvalues.isChecked()
		virtualShape=self.ui.virtualShape.isChecked()

		#use virtual shape import
		if virtualShape==True:
			try:
				ok=self.saveLayer(layer,'',charset,srid,selected,True)
				if ok=="ok":
					self.pop_up_error("No Feature Selected")
					return
				elif ok==False:
					self.pop_up_error("Unable to create tmp shapefile")
					return
			except:
				self.pop_up_error("Saving Shapefile failed.")
				return False

			shp="shape_export"
			cursor = self.connection.cursor()
			#create virtual table
			try:
				vtsql="""CREATE VIRTUAL TABLE "%s" USING VirtualShape("%s","%s",%s)""" %(vname,shp, charset, srid)
				cursor.execute(vtsql)
				#check geometry type of virtual table
				query= ("""select geometrytype(Geometry) from "%s" group by 1""" %vname)
				cursor.execute(query)
				SHPgeometry=cursor.fetchall()
				if len(SHPgeometry)==0:
					self.pop_up_error("Could not import Shape: geometry incompatibility")
					return
				geometryType=str(SHPgeometry[0][0])
			except self.connectionModule.OperationalError, errorMsg:
				self.pop_up_error("VirtualShapeFile Loading failed.\n\n%s" %
		                        errorMsg)
				self.connection.rollback()
				self.removeTmpShp()
				cursor.close()
				return False


			#create new table from virtual Table
			try:
				#vtsql=("CREATE TABLE '%s' AS SELECT * FROM '%s'" %(name, vname))
				vtsql="""CREATE TABLE "%s" ( PKUID INTEGER PRIMARY KEY AUTOINCREMENT,""" %name
				colList=""
				colList2=""
				params=[]
				columns=self.get_columns( vname ) 
				del columns[0] #remove pkuid columns
				for col in columns:
					colname=col[1] #new table cols name
					colname2=col[1] #vname table cols
					coltype=col[2]
					#check for duplicate col pkuid
					if colname.upper()=="PKUID": #PKUID already exists...
						print "Former PKUID deleted"
					else:
						#Check if it is a geometry col
						if colname.upper()=="GEOMETRY":
							coltype=geometryType
						vtsql+=""" "%s" %s,""" %(colname,coltype) # col name, col type
						colList+=""" "%s",""" %colname
						colList2+=""" "%s"."%s",""" %(vname,colname2)
				vtsql=vtsql[:-1] #remove last ','
				colList=colList[:-1]
				colList2=colList2[:-1]
				vtsql+=")"
				cursor.execute(vtsql)
			except self.connectionModule.OperationalError, errorMsg:
				self.pop_up_error("New Empty Table creation failed.\n\n%s" %
		                        errorMsg)
				self.connection.rollback()
				self.removeTmpShp()
				cursor.close()
				return False


			# populate new table
			try:
				vtsql=('INSERT INTO "%s" (%s) SELECT %s FROM "%s"' %(name, colList, colList2, vname))
				cursor.execute(vtsql)
			except self.connectionModule.OperationalError, errorMsg:
				self.pop_up_error("Table creation failed.\n\n%s" %
		                        errorMsg)
				self.connection.rollback()
				self.removeTmpShp()
				cursor.close()
				return False
	
			#drop virtual table
			try:
				vtsql=("""DROP TABLE "%s" """ %(vname))
				cursor.execute(vtsql)
			except self.connectionModule.OperationalError, errorMsg:
				self.pop_up_error("DROP VirtualTable failed.\n\n%s" %
		                        errorMsg)
				self.connection.rollback()
				self.removeTmpShp()
				cursor.close()

			#recover geometry column
		
			cursor.execute("SELECT RecoverGeometryColumn(?,'Geometry',?,?,2)",(name, srid, geometryType,))
			rep=cursor.fetchall()
			if rep[0][0]==0:
				self.pop_up_error("Can't create geometry column: INCORRECT GEOMETRY TYPE")


			#create spatialindex if required:
			if self.ui.SpatialIndex.isChecked()==True:	
				try:
					cursor.execute("SELECT CreateSpatialIndex(?, 'Geometry')",(name,))
				except self.connectionModule.OperationalError, errorMsg:
					self.pop_up_error("SpatiaL Index creation failed.\n\n%s" %
				                       errorMsg)
					self.connection.rollback()
					cursor.close()
					return False

			#everything is okay
			self.connection.commit()
			cursor.close()
			QtGui.QMessageBox.information(None,"Information","QGIS Layer has been uploaded")
			self.removeTmpShp()
			self.prepare_tree()
			return

		#use direct import //without virtualshape
		SQL,params=self.saveLayer(layer, name, charset, srid, selected,False)
		if SQL==False:
			if params==False:
				self.pop_up_error("No Feature Selected")
				return
			elif params=='srid':
				self.pop_up_error("Invalid SRID")
				return
			else:
				self.pop_up_error("An unknown error occured while loading table")
				return
				
		cursor = self.connection.cursor()
		#create table and populate
		try:
			i=-1
			for sql in SQL:
				i+=1
				cursor.execute(sql,params[i])

		except self.connectionModule.OperationalError, errorMsg:
			self.pop_up_error("Error While upLoading QGIS Layer.\n\n%s" %
                                errorMsg)
			self.connection.rollback()
			cursor.close()
			return False

		#create spatialindex if required:
		if self.ui.SpatialIndex.isChecked()==True:	
			try:
				cursor.execute("SELECT CreateSpatialIndex(?, 'Geometry')",(name,))
			except self.connectionModule.OperationalError, errorMsg:
				self.pop_up_error("SpatiaL Index creation failed.\n\n%s" %
			                       errorMsg)
				self.connection.rollback()
				cursor.close()
				return False

		#everything is okay
		self.connection.commit()
		cursor.close()
		QtGui.QMessageBox.information(None,"Information","QGIS Layer has been uploaded")
		self.prepare_tree()

#Upload DBF File:   #without using virtualtable.... like customqueryDB.... Why not ?
    def upload_DBF(self):
	from qgis.core import QgsRectangle, QgsFeature
	#detect parameters
	try:
		layer=self.ui.dbf_path.text()
		layer=str(layer)
		name=self.ui.name_dbf.text()
		name=str(name)
		charset=self.ui.charsetList_DBF.currentText()
		charset=str(charset)
	except:
		self.pop_up_error("No accents/special characters please")
		return False
		
	if (layer=='') or (name=='') or(charset==''):
		self.pop_up_error("All the fields are necessary")
		return False
	#verify if table already exists in DB
	tablelist=self.get_tables()
	for table in tablelist:
		if table[0]==name:
			self.pop_up_error("Table name already exists")
			return False
	#load dbf file with QGIS
	try:
		columns,vlayer=self.load_dbf(layer,charset)
	except:
		self.pop_up_error("Unable to Load DBF")
		return False
		
	cursor = self.connection.cursor()
	# create the new table
	try:
		vtsql="""CREATE TABLE "%s" (""" %name
		for col in columns:
			vtsql+=""" "%s" %s,""" %(col[0],col[1]) # col name, col type
		vtsql=vtsql[:-1] #remove last ','
		vtsql+=")"
		cursor.execute(vtsql)
	except self.connectionModule.OperationalError, errorMsg:
		self.pop_up_error("New Empty Table creation failed.\n\n%s" %
                               errorMsg)
		self.connection.rollback()
		cursor.close()
		return False
	# now let's get the features and import them to database
	try:
		pr = vlayer.dataProvider()
		flds = pr.fields()
		pr.enableGeometrylessFeatures(True)
		pr.select(pr.attributeIndexes(), QgsRectangle(), False) # all attrs, no geometry
		f = QgsFeature()
		while pr.nextFeature(f):
			attrs = f.attributeMap()
			values = []
			for (i,val) in attrs.iteritems():
				vartype = flds[i].type()
				if val.isNull():
					values.append("NULL")
				elif vartype == QtCore.QVariant.Int:
					values.append(str(val.toInt()[0]))
				elif vartype == QtCore.QVariant.Double:
					values.append(str(val.toDouble()[0]))
				else: # string or something else
					values.append("%s" % str(val.toString().toUtf8()))
			vtsql="""INSERT INTO "%s" VALUES (""" %name
			vtsql+=",".join("?"*len(values))
			vtsql+=")"
			params=tuple([val for val in values])
			cursor.execute(vtsql,params)
	except self.connectionModule.OperationalError, errorMsg:
		self.pop_up_error("Table creation failed.\n\n%s" %
                               errorMsg)
		self.connection.rollback()
		cursor.close()
		return False
	#everything is okay
	self.connection.commit()
	cursor.close()
	QtGui.QMessageBox.information(None,"Information","DBF Layer has been uploaded")
	self.prepare_tree()	
	
	
    def load_dbf(self, filename, encoding):
	from qgis.core import QgsVectorLayer
	v = QgsVectorLayer(filename, "x", "ogr")
	if not v.isValid():
		vlayer = None
		self.pop_up_error("DBF Loading Failed: wrong file type")
		return False
		
	vlayer = v
	pr = v.dataProvider()
	pr.setEncoding(encoding)
	
	# now find out what fields are in the dbf file
	dbf_fields = []
	flds = pr.fields()
	for (i,fld) in flds.iteritems():
		
		name = unicode(fld.name())
		modifier = None
		if fld.type() == QtCore.QVariant.Int:
			data_type = "int"
		elif fld.type() == QtCore.QVariant.Double:
			data_type = "double precision"
		elif fld.type() == QtCore.QVariant.String:
			data_type = "varchar"
			modifier = fld.length()
		else:
			# unsupported type
			data_type = "varchar"
			modifier = fld.length()
			
		dbf_fields.append([name, data_type])
	
	return dbf_fields, vlayer

   # loadCSV:
    def toggle_csv_custom_col(self):
	if self.ui.column.currentText()=='Other':
		self.ui.custom_col.setEnabled(True)
	else:
		self.ui.custom_col.setText('')
		self.ui.custom_col.setEnabled(False)
    def uploadCSV(self):  
	#detect parameters
	try:
		filename=unicode(self.ui.csv_path.text())
		name=unicode(self.ui.name_csv.text())
		vname=name+"_virt"
		first_col=0 
		if self.ui.first_col.isChecked()==True:
			first_col=1
		charset=unicode(self.ui.charsetList_CSV.currentText())
		decimal_sep=self.decimals[unicode(self.ui.decimal.currentText())]
		text_sep=self.textseparator[unicode(self.ui.text.currentText())]
		if unicode(self.ui.column.currentText())=="Other":
			column_sep="'"+unicode(self.ui.custom_col.text())+"'"
		else:
			column_sep=self.columnseparator[unicode(self.ui.column.currentText())]
	except:
		self.pop_up_error("No accents/special characters please")
		return False
		
	if (filename=='') or (name=='') or(charset=='')or(decimal_sep=='')or(column_sep=="''"):
		self.pop_up_error("All the fields are necessary")
		return False
	#verify if table already exists in DB
	tablelist=self.get_tables()
	for table in tablelist:
		if table[0] in (name,vname):
			self.pop_up_error("Table name already exists: %s"%table[0])
			return False
		cursor = self.connection.cursor()
	#create virtual table
	try:
		vtsql="""CREATE VIRTUAL TABLE "%s" USING VirtualText("%s",%s,%s,%s,%s,%s)""" %(vname, filename, charset, first_col, decimal_sep, text_sep, column_sep)
		cursor.execute(vtsql)
	except self.connectionModule.OperationalError, errorMsg:
		self.pop_up_error("VirtualText Loading failed.\n\n%s" %
                        errorMsg)
		self.connection.rollback()
		cursor.close()
		return False

	#create new table from virtual Table
	try:
		vtsql=("""CREATE TABLE "%s" AS SELECT * FROM "%s" """ %(name, vname))
		cursor.execute(vtsql)
	except self.connectionModule.OperationalError, errorMsg:
		self.pop_up_error("New Empty Table creation failed.\n\n%s" %
                        errorMsg)
		self.connection.rollback()
		cursor.close()
		return False

	#drop virtual table
	try:
		vtsql=("""DROP TABLE "%s" """ %(vname))
		cursor.execute(vtsql)
	except self.connectionModule.OperationalError, errorMsg:
		self.pop_up_error("DROP VirtualTable failed.\n\n%s" %
                        errorMsg)
		self.connection.rollback()
		cursor.close()

	#everything is okay
	self.connection.commit()
	cursor.close()
	QtGui.QMessageBox.information(None,"Information","TXT/CSV Layer has been uploaded")
	self.prepare_tree()
#dump table as csv
    def dumpCSV(self):
	table=self.currentTable
	filename = QtGui.QFileDialog.getSaveFileName(self, "Save File","%s.txt"%table,"TXT file (*.txt)")
	if filename.isEmpty() or table=='':
		return
	#prepare datas
	try:
		query="""SELECT * FROM "%s" """%table
		rows,col=self.run_normal_query(query)
	except:
		self.pop_up_error("Error: can't select data from '%s'"%table)
		return
	self.writeCSV(filename,col,rows)

    def writeCSV(self,filename,col,rows): #write txt from cols and rows
	#is table empty ?
	if len(rows)==0:
		self.pop_up_error("Empty Table")
		return
	try:
		myfile=open(filename,'wb')
		import csv
		linewriter=csv.writer(myfile, delimiter='\t')
	except:
		self.pop_up_error("Error while creating TXT empty File: '%s'"%filename)
		return
	#write colnames
	try:
		linewriter.writerow(col)
	except:
#accent or special char found in col names:---------------------------------------------
		colc=[]
		for val in col:
			if isinstance(val,int) or isinstance(val,long)or isinstance(val,float)or isinstance(val,complex):#numbers
				colc.append(str(val))
			elif isinstance(val,buffer):  #geometry object
				colc.append("GeomObject")
			elif (val is None):
				colc.append("Null")
			else: #strings, date, ....
				colc.append(str(val.encode("utf-8")))
		linewriter.writerow(colc)
#--------------------------------------------------------------------------------------------end
	#write rows
	for row in rows:
		try:
			linewriter.writerow(row)
		except:
#accent or special char found in col names:---------------------------------------------
			rowc=[]
			for val in row:
				if isinstance(val,int) or isinstance(val,long)or isinstance(val,float)or isinstance(val,complex):#numbers
					rowc.append(str(val))
				elif isinstance(val,buffer):  #geometry object
					rowc.append("GeomObject")
				elif (val is None):
					rowc.append("Null")
				else: #strings, date, ....
					rowc.append(str(val.encode("utf-8")))
			linewriter.writerow(rowc)
#--------------------------------------------------------------------------------------------end
	myfile.close()
	nbrows=len(rows)
	QtGui.QMessageBox.information(None,"Information","TXT file (%s rows) succesfully created\n Charset: UTF-8"%nbrows)

    def saveToCSV(self): #save resultset to TXT/Tab
	if len(self.rowList)<=0:
		return #nothing to save
	filename = QtGui.QFileDialog.getSaveFileName(self, "Save File","resultSet.txt","TXT file (*.txt)")
	if filename.isEmpty():
		return
	datas=[]
	for row in self.rowList:  # replace all sqlite blob by WKT
		newRow=[]
		i=-1
		for val in row:
			i+=1
			if isinstance(val,buffer):
				cur = self.connection.cursor()
				cur.execute("""SELECT AsText(?)""",(self.connectionModule.Binary(val),))
				element=cur.fetchall()[0][0]
				cur.close()
			else:
				element=val
			newRow.append(element)
		datas.append(newRow)
	self.writeCSV(filename,self.columnNames,datas)

    def ViewInQgis(self): #view resultset in QGIS
	if len(self.rowList)<=0:
		return #nothing to save
	cols=[col for col in self.columnNames]
	#detects col types from first row:
	cols_type=[type(el) for el in self.rowList[0]]
		
	geometry=None #Geometry Type
	#Detect geometry column, using the first row
	i=-1
	for element in self.rowList[0]:
		i+=1
		if isinstance(element,buffer):
			cur = self.connection.cursor()
			cur.execute("""SELECT GeometryType(?)""",(self.connectionModule.Binary(element),))
			geometry=cur.fetchall()[0][0]
			cur.close()
			break 
	attr_data=[]
	geom_data=[]

	if geometry is None: #geometry column not found
		self.pop_up_error("No Geometry column found.\nOperation cancelled")
		return

	del cols[i] #remove geometry column
	del cols_type[i]	

	for row in self.rowList:  # go throught dataset
		attr_row=[]
		j=-1
		for val in row:
			j+=1
			if j==i: # geom data column
				cur=self.connection.cursor()
				cur.execute("""SELECT AsBinary(?)""",(self.connectionModule.Binary(val),))
				geomval=cur.fetchall()[0][0]
				cur.close()
				geom_data.append(geomval)
			else: #attribute datas
				attr_row.append(val)
		attr_data.append(attr_row)

	#Ask user SRID information
	(srid, ok) = QtGui.QInputDialog.getText (self, 
                "Enter Geometry SRID", 
                "Desired SRID (leave blank for srid=4326) :")
	if (not ok) or srid=='':
		srid=None
	else:
		try:
			srid=int(srid)
		except:
			self.pop_up_error("SRID must be integer.\nOperation cancelled")
			return

	self.viewresult(cols,cols_type,attr_data,geom_data,geometry,srid)
				

    def browseFile(self):
	filename = QtGui.QFileDialog.getOpenFileName(self, "Open DBF","","DBF files (*.dbf)")
	if filename.isEmpty():
		return
	self.ui.dbf_path.setText(filename)

    def browseFileCSV(self):
	filename = QtGui.QFileDialog.getOpenFileName(self, "Open CSV/TXT","", "TXT (*.txt);; CSV (*.csv)")
	if filename.isEmpty():
		return
	self.ui.csv_path.setText(filename)

    def folderExport(self):
	filename = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory","", QtGui.QFileDialog.ShowDirsOnly|QtGui.QFileDialog.DontResolveSymlinks)
	if filename.isEmpty():
		return
	self.ui.folderExport.setText(filename)	


    def browseSRID(self):
	dialog = SRSDialog( "Select desired SRS" )
	if dialog.exec_():
		self.ui.srid.setText(dialog.getProjection())

    def browseSRID2(self): #same function for selecting SRID in 'upload gis layers'
	dialog = SRSDialog( "Select desired SRS" )
	if dialog.exec_():
		self.ui.sridFiles.setText(dialog.getProjection())

    def browseSRID3(self): #same function for selecting SRID in 'export spatial tables'
	dialog = SRSDialog( "Select desired SRS" )
	if dialog.exec_():
		self.ui.sridExport.setText(dialog.getProjection())

#Export tables to OGR Layers
    def ExportTablesToOgr(self):
	#list selected tables
	tables=[unicode(item.text()) for item in self.ui.geomTables.selectedItems()] #get selected items
	if len(tables)<=0:
		self.pop_up_error("Please select at least one table")
		return	
	# Retrieve geometry columns 
	geocols=[self.spatialTables[table][0] for table in tables]
	#user just want to load layers in QGIS
	if self.ui.justQgis.isChecked():
		i=0
		for table in tables:
			self.callbackFunction(table, "spatialite", self.connectionSettings, geocols[i], 'rowid', table)
			i+=1
		self.pop_up_error("Operation completed")
		self.ui.justQgis.setChecked(False)
		return
	#user want to save layers
	#get informations:
	format=unicode(self.ui.outForm.currentText()) #get Format
	folder=unicode(self.ui.folderExport.text()).strip()
	charset=unicode(self.ui.charsetExport.currentText()).strip()
	if format=='' or folder=='' or charset=='':
		self.pop_up_error("All fields except SRID are mandatory")
		return
	srid=unicode(self.ui.sridExport.text()).strip()
	if srid=='':
		srid=[self.spatialTables[table][1] for table in tables]  #conserve table srid
	else:
		try:
			srid=int(self.ui.sridExport.text())
		except:
			self.pop_up_error("SRID must be INTEGER")
			return
		srid=[srid for table in tables] #same srid for all tables

	#run savetoOgr function
	errors=self.export2ogr(tables,geocols,self.connectionSettings,format,folder,charset,srid)

	if len(errors)>0:
		message="Non Saved Tables:"
		for error in errors:
			message+="\n Table: %s Reason: %s"%(error[0],error[1])
		self.pop_up_error(message)
	else: #everything is ok
		self.pop_up_error("All selected layers have been saved")
	return

		

#call QGIS Help Plugin
    def call_help(self):
        qgis.utils.showPluginHelp()

#recover geometry column menu action
    def recovergeometry(self):
	from recovergeometry.recovergeometry import recovergeometry
	self.georecovery = recovergeometry(self.connection,self.currentTable,self.currentCol,self.prepare_tree,SRSDialog)
	self.georecovery.setModal(False)
	self.georecovery.show()	

#Load Browser
    def browser(self):
	from browser.sqlpage import html
	self.sqlbrowser = sqlbrowser()
	self.sqlbrowser.ui.textBrowser.setHtml(html)
	self.sqlbrowser.setModal(False)
	self.sqlbrowser.show()

#Load Query builder:
    def queryBuilder(self):
	from querybuilder.querybuilder import querybuilder
	self.querybuilder = querybuilder(self)
	self.querybuilder.setModal(True)
	self.querybuilder.show()

#update result widget
    def update_table_widget(self, widget, columnNames, rowList):
	model=MyTableModel(rowList, columnNames, self)
	widget.setModel(model)
	#rows=model.rowCount(None)
	self.rowList=rowList  #save var for resultset txt export
	self.columnNames=columnNames
	self.ui.Result.setText("ResultSet (%s rows)"%self.resultrows)

#Model for result widget: #http://www.saltycrane.com/blog/2007/12/pyqt-43-qtableview-qabstracttablemodel/
from types import StringType, NoneType
import datetime
class MyTableModel(QtCore.QAbstractTableModel): 
    def __init__(self, datain, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QtCore.QAbstractTableModel.__init__(self, parent, *args) 
        self.arraydata = datain
        self.headerdata = headerdata
	self.parent=parent
 
    def rowCount(self, parent): 
        return len(self.arraydata) 
 
    def columnCount(self, parent): 
	if len(self.arraydata)==0:
		return 0
        return len(self.arraydata[0]) 
 
    def data(self, index, role): 
        if not index.isValid(): 
            return QtCore.QVariant() 
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant() 
	val=self.arraydata[index.row()][index.column()]
	
	if type(val) == StringType:
		return QtCore.QVariant(QtCore.QString.fromUtf8(val))
	elif type(val) == NoneType:
		return QtCore.QVariant("NULL")
	elif isinstance(val, buffer):
		return QtCore.QVariant('GeomObject')
	elif isinstance(val, datetime.datetime):
		return QtCore.QVariant(str(val))
	else:
		return QtCore.QVariant(val) 

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant() 
	if orientation == QtCore.Qt.Vertical:
		# header for a row
		return QtCore.QVariant(section+1)
	else:
		# header for a column
		return QtCore.QVariant(QtCore.QString.fromUtf8(self.headerdata[section]))

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
	import operator
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
        if order == QtCore.Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))

