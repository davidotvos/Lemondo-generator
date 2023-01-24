# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import utils
import lemondok

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.iktatoLayout = QtWidgets.QHBoxLayout()
        self.iktatoLayout.setObjectName("iktatoLayout")
        self.iktatoszamLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.iktatoszamLabel.setFont(font)
        self.iktatoszamLabel.setObjectName("iktatoszamLabel")
        self.iktatoLayout.addWidget(self.iktatoszamLabel)
        self.iktatoszamInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(218)
        sizePolicy.setVerticalStretch(33)
        sizePolicy.setHeightForWidth(self.iktatoszamInput.sizePolicy().hasHeightForWidth())
        self.iktatoszamInput.setSizePolicy(sizePolicy)
        self.iktatoszamInput.setMinimumSize(QtCore.QSize(200, 33))
        self.iktatoszamInput.setMaximumSize(QtCore.QSize(5000, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.iktatoszamInput.setFont(font)
        self.iktatoszamInput.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.iktatoszamInput.setText("")
        self.iktatoszamInput.setObjectName("iktatoszamInput")
        self.iktatoLayout.addWidget(self.iktatoszamInput)
        self.tipusBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tipusBox.sizePolicy().hasHeightForWidth())
        self.tipusBox.setSizePolicy(sizePolicy)
        self.tipusBox.setMinimumSize(QtCore.QSize(240, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.tipusBox.setFont(font)
        self.tipusBox.setObjectName("tipusBox")
        self.tipusBox.addItem("")
        self.tipusBox.addItem("")
        self.tipusBox.addItem("")
        self.iktatoLayout.addWidget(self.tipusBox)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(180, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.iktatoLayout.addWidget(self.addButton)
        self.gridLayout.addLayout(self.iktatoLayout, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy)
        self.createButton.setMinimumSize(QtCore.QSize(200, 0))
        self.createButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.createButton.setFont(font)
        self.createButton.setObjectName("createButton")
        self.gridLayout_3.addWidget(self.createButton, 1, 0, 1, 1)
        self.folderButton = QtWidgets.QPushButton(self.centralwidget)
        self.folderButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderButton.sizePolicy().hasHeightForWidth())
        self.folderButton.setSizePolicy(sizePolicy)
        self.folderButton.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.folderButton.setFont(font)
        self.folderButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.folderButton.setObjectName("folderButton")
        self.gridLayout_3.addWidget(self.folderButton, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.tervcimLayout = QtWidgets.QHBoxLayout()
        self.tervcimLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.tervcimLayout.setSpacing(44)
        self.tervcimLayout.setObjectName("tervcimLayout")
        self.tervcimLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.tervcimLabel.setFont(font)
        self.tervcimLabel.setObjectName("tervcimLabel")
        self.tervcimLayout.addWidget(self.tervcimLabel)
        self.tervcimTextInput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tervcimTextInput.sizePolicy().hasHeightForWidth())
        self.tervcimTextInput.setSizePolicy(sizePolicy)
        self.tervcimTextInput.setMaximumSize(QtCore.QSize(16777215, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.tervcimTextInput.setFont(font)
        self.tervcimTextInput.setObjectName("tervcimTextInput")
        self.tervcimLayout.addWidget(self.tervcimTextInput)
        self.gridLayout.addLayout(self.tervcimLayout, 0, 0, 1, 1)
        self.tableViewLayout = QtWidgets.QHBoxLayout()
        self.tableViewLayout.setObjectName("tableViewLayout")
        self.lemondoTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lemondoTable.sizePolicy().hasHeightForWidth())
        self.lemondoTable.setSizePolicy(sizePolicy)
        self.lemondoTable.setMinimumSize(QtCore.QSize(682, 0))
        self.lemondoTable.setMaximumSize(QtCore.QSize(5000, 5000))
        self.lemondoTable.setStyleSheet("font: 18pt \"Arial\";")
        self.lemondoTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.lemondoTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.lemondoTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.lemondoTable.setObjectName("lemondoTable")
        self.lemondoTable.setRowCount(0)
        self.lemondoTable.setColumnCount(3)
        self.lemondoTable.horizontalHeader().setCascadingSectionResizes(True)
        self.lemondoTable.verticalHeader().setCascadingSectionResizes(True)
        self.tableViewLayout.addWidget(self.lemondoTable)
        self.tableviewButtonLayout = QtWidgets.QVBoxLayout()
        self.tableviewButtonLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.tableviewButtonLayout.setObjectName("tableviewButtonLayout")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.tableviewButtonLayout.addWidget(self.deleteButton)
        self.tableViewLayout.addLayout(self.tableviewButtonLayout)
        self.gridLayout.addLayout(self.tableViewLayout, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tervcimTextInput, self.iktatoszamInput)
        MainWindow.setTabOrder(self.iktatoszamInput, self.tipusBox)
        MainWindow.setTabOrder(self.tipusBox, self.addButton)
        MainWindow.setTabOrder(self.addButton, self.lemondoTable)
        MainWindow.setTabOrder(self.lemondoTable, self.deleteButton)
        MainWindow.setTabOrder(self.deleteButton, self.folderButton)
        MainWindow.setTabOrder(self.folderButton, self.createButton)

        self.tervcimTextInput.setTabChangesFocus(True)

        self.addButton.clicked.connect(self.add_row)
        self.folderButton.clicked.connect(self.pick_folder)

        self.deleteButton.clicked.connect(self.delete_row)

        self.lemondoTable.setHorizontalHeaderLabels(['Iktatószám', 'Tervcím', 'Engedélytípus'])
        self.lemondoTable.resizeColumnsToContents()

        self.createButton.clicked.connect(self.create_pdfs)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lemondó készítő"))
        self.iktatoszamLabel.setText(_translate("MainWindow", "Iktatószám:"))
        self.tipusBox.setItemText(0, _translate("MainWindow", "Használatbavételi"))
        self.tipusBox.setItemText(1, _translate("MainWindow", "Építési"))
        self.tipusBox.setItemText(2, _translate("MainWindow", "Bontási"))
        self.addButton.setText(_translate("MainWindow", "Hozzáad"))
        self.createButton.setText(_translate("MainWindow", "Létrehoz"))
        self.folderButton.setText(_translate("MainWindow", "Mappa választása"))
        self.tervcimLabel.setText(_translate("MainWindow", "Tervcím:"))
        self.tervcimTextInput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.deleteButton.setText(_translate("MainWindow", "Törlés"))


    def add_row(self):

        if self.iktatoszamInput.text().isspace() or self.iktatoszamInput.text() == '':
            return
        
        if self.tervcimTextInput.toPlainText().isspace() or self.tervcimTextInput.toPlainText() == '':
            return


        count = self.lemondoTable.rowCount()
        self.lemondoTable.insertRow(count)
        self.lemondoTable.setItem(count, 0, QtWidgets.QTableWidgetItem(self.iktatoszamInput.text()))
        self.lemondoTable.setItem(count, 1, QtWidgets.QTableWidgetItem(self.tervcimTextInput.toPlainText()))
        self.lemondoTable.setItem(count, 2, QtWidgets.QTableWidgetItem(self.tipusBox.currentText() + ' engedély'))
        
        # inputok frissítése
        self.iktatoszamInput.setText('')
        self.tervcimTextInput.setText('')

        # cellák méretre igazítása
        self.lemondoTable.resizeColumnsToContents()
        
            

    def pick_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self,"Select folder")
        utils.save_folder = folder_path


    def delete_row(self):
        print(utils.save_folder)

    
    def create_pdfs(self):
        tempLemondoObj = lemondok.Lemondo
        tempLemondoLi = []
        for row in range(self.lemondoTable.rowCount()):
            tempRow = []
            for col in range(self.lemondoTable.columnCount()):
                tempRow.append(self.lemondoTable.item(row,col).text())
            
            tempLemondoObj = lemondok.Lemondo(iktatoszam=tempRow[0], tervcim=tempRow[1], tipus=tempRow[2])
            tempLemondoLi.append(tempLemondoObj)
        
        utils.lemondoLi = tempLemondoLi

        #TODO itt hívni meg a create pdfs methódust