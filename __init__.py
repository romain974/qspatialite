"""
/***************************************************************************
 QspatiaLite
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "QSpatiaLite"
def description():
    return "SpatiaLite GUI for SpatiaLite: load/export SpatiaLite tables/Query to QGIS Canvas, Import DBF, ..."
def version():
    return "Version 5.0.3"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.6"
def classFactory(iface):
    # load QspatiaLite class from file QspatiaLite
    from qspatialite import QspatiaLite
    return QspatiaLite(iface)
