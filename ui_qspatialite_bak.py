        #self.SQLeditor = QtGui.QTextEdit(self.layoutWidget)
	#new one
	import autocompletion
	completer = autocompletion.DictionaryCompleter()
	self.SQLeditor = autocompletion.CompletionTextEdit(self.layoutWidget)
	self.SQLeditor.setCompleter(completer)
	self.SQLeditor.setAcceptRichText(False)
	#---------
