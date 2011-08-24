'''
Modified By RIVIERE Romain for QSpatiaLite QGIS plugin
Python Syntax Highlighting Example

Copyright (C) 2009 Carson J. Q. Farmer

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public Licence as published by the Free Software
Foundation; either version 2 of the Licence, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public Licence for more 
details.

You should have received a copy of the GNU General Public Licence along with
this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
Street, Fifth Floor, Boston, MA  02110-1301, USA
'''

#import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from dictionnary import f1,f2,f3
class MyHighlighter( QSyntaxHighlighter ):

    def __init__( self, parent, theme ):
      QSyntaxHighlighter.__init__( self, parent )
      self.parent = parent
      SQLkeyword = QTextCharFormat()
      SQLfunction = QTextCharFormat()
      Spatial_function = QTextCharFormat()
      assignmentOperator = QTextCharFormat()
      delimiter = QTextCharFormat()
      specialConstant = QTextCharFormat()
      boolean = QTextCharFormat()
      number = QTextCharFormat()
      comment = QTextCharFormat()
      string = QTextCharFormat()
      singleQuotedString = QTextCharFormat()

      self.highlightingRules = []

      # SQL keywords
      brush = QBrush( Qt.blue, Qt.SolidPattern )
      SQLkeyword.setForeground( brush )
      SQLkeyword.setFontWeight( QFont.Bold )
      keywords = QStringList( f1 )
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, SQLkeyword )
        self.highlightingRules.append( rule )

      # SQLite functions
      brush = QBrush( Qt.darkYellow, Qt.SolidPattern )
      SQLfunction.setForeground( brush )
      keywords = QStringList( f2 )
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, SQLfunction )
        self.highlightingRules.append( rule )

      # SpatiaLite functions
      brush = QBrush( Qt.darkYellow, Qt.SolidPattern )
      Spatial_function.setForeground( brush )
      Spatial_function.setFontWeight( QFont.Bold )
      keywords = QStringList( f3 )
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, SQLfunction )
        self.highlightingRules.append( rule )
      
      # delimiter
      pattern = QRegExp( "[\)\(]" )
      delimiter.setForeground( brush )
      rule = HighlightingRule( pattern, delimiter )
      self.highlightingRules.append( rule )

      # boolean
      brush = QBrush( Qt.magenta, Qt.SolidPattern )
      boolean.setForeground( brush )
      keywords = QStringList( [ "TRUE", "FALSE" ] )
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, boolean )
        self.highlightingRules.append( rule )

      # numbers
      pattern = QRegExp( r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b' ) 
      pattern.setMinimal( True )
      number.setForeground( brush )
      rule = HighlightingRule( pattern, number )
      self.highlightingRules.append( rule )


      # string
      pattern = QRegExp( r'"[^"\\]*(\\.[^"\\]*)*"' )
      pattern.setMinimal( True )
      string.setForeground( brush )
      rule = HighlightingRule( pattern, string )
      self.highlightingRules.append( rule )
      
      # singleQuotedString
      pattern = QRegExp( r"'[^'\\]*(\\.[^'\\]*)*'" )
      pattern.setMinimal( True )
      singleQuotedString.setForeground( brush )
      rule = HighlightingRule( pattern, singleQuotedString )
      self.highlightingRules.append( rule )

    def highlightBlock( self, text ):
      text=text.toLower()
      for rule in self.highlightingRules:
        expression = QRegExp( rule.pattern )
        index = expression.indexIn( text, 0 )
        while index >= 0:
          index = expression.pos(0)
          length = expression.cap(0).length()
          self.setFormat( index, length, rule.format )
          index = expression.indexIn( text, index + length )
      self.setCurrentBlockState( 0 )

class HighlightingRule():
  def __init__( self, pattern, format ):
    self.pattern = pattern
    self.format = format
   
#class TestApp( QMainWindow ):
#  def __init__(self):
#    QMainWindow.__init__(self)
#    font = QFont()
#    font.setFamily( "Courier" )
#    font.setFixedPitch( True )
#    font.setPointSize( 10 )
#    editor = QTextEdit()
#    editor.setFont( font )
#    highlighter = MyHighlighter( editor, "Classic" )
#    self.setCentralWidget( editor )
#    self.setWindowTitle( "Syntax Highlighter" )


#if __name__ == "__main__":
#  app = QApplication( sys.argv )
#  window = TestApp()
#  window.show()
#  sys.exit( app.exec_() )

