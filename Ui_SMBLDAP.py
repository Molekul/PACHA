# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SMBLDAP.ui'
#
# Created: Tue Nov 30 14:40:27 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SMBLDAP(object):
    def setupUi(self, SMBLDAP):
        SMBLDAP.setObjectName(_fromUtf8("SMBLDAP"))
        SMBLDAP.resize(593, 595)
        self.horizontalLayout = QtGui.QHBoxLayout(SMBLDAP)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(SMBLDAP)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_5.addWidget(self.label)
        self.editUser = QtGui.QLineEdit(self.tab)
        self.editUser.setObjectName(_fromUtf8("editUser"))
        self.horizontalLayout_5.addWidget(self.editUser)
        self.btnUserAdd = QtGui.QPushButton(self.tab)
        self.btnUserAdd.setObjectName(_fromUtf8("btnUserAdd"))
        self.horizontalLayout_5.addWidget(self.btnUserAdd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.listUsers = QtGui.QListWidget(self.tab)
        self.listUsers.setObjectName(_fromUtf8("listUsers"))
        self.verticalLayout_2.addWidget(self.listUsers)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.btnUserDel = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUserDel.sizePolicy().hasHeightForWidth())
        self.btnUserDel.setSizePolicy(sizePolicy)
        self.btnUserDel.setObjectName(_fromUtf8("btnUserDel"))
        self.horizontalLayout_6.addWidget(self.btnUserDel)
        self.btnUsersRefresh = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUsersRefresh.sizePolicy().hasHeightForWidth())
        self.btnUsersRefresh.setSizePolicy(sizePolicy)
        self.btnUsersRefresh.setObjectName(_fromUtf8("btnUsersRefresh"))
        self.horizontalLayout_6.addWidget(self.btnUsersRefresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.editGroup = QtGui.QLineEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editGroup.sizePolicy().hasHeightForWidth())
        self.editGroup.setSizePolicy(sizePolicy)
        self.editGroup.setObjectName(_fromUtf8("editGroup"))
        self.horizontalLayout_2.addWidget(self.editGroup)
        self.btnGroupAdd = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGroupAdd.sizePolicy().hasHeightForWidth())
        self.btnGroupAdd.setSizePolicy(sizePolicy)
        self.btnGroupAdd.setObjectName(_fromUtf8("btnGroupAdd"))
        self.horizontalLayout_2.addWidget(self.btnGroupAdd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listGroups = QtGui.QListWidget(self.tab_2)
        self.listGroups.setObjectName(_fromUtf8("listGroups"))
        self.verticalLayout.addWidget(self.listGroups)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnGroupDel = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGroupDel.sizePolicy().hasHeightForWidth())
        self.btnGroupDel.setSizePolicy(sizePolicy)
        self.btnGroupDel.setObjectName(_fromUtf8("btnGroupDel"))
        self.horizontalLayout_3.addWidget(self.btnGroupDel)
        self.btnGroupsRefresh = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGroupsRefresh.sizePolicy().hasHeightForWidth())
        self.btnGroupsRefresh.setSizePolicy(sizePolicy)
        self.btnGroupsRefresh.setObjectName(_fromUtf8("btnGroupsRefresh"))
        self.horizontalLayout_3.addWidget(self.btnGroupsRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(SMBLDAP)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SMBLDAP)

    def retranslateUi(self, SMBLDAP):
        SMBLDAP.setWindowTitle(QtGui.QApplication.translate("SMBLDAP", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SMBLDAP", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUserAdd.setText(QtGui.QApplication.translate("SMBLDAP", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.listUsers.setSortingEnabled(True)
        self.btnUserDel.setText(QtGui.QApplication.translate("SMBLDAP", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUsersRefresh.setText(QtGui.QApplication.translate("SMBLDAP", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("SMBLDAP", "Users", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SMBLDAP", "Group:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGroupAdd.setText(QtGui.QApplication.translate("SMBLDAP", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.listGroups.setSortingEnabled(True)
        self.btnGroupDel.setText(QtGui.QApplication.translate("SMBLDAP", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGroupsRefresh.setText(QtGui.QApplication.translate("SMBLDAP", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("SMBLDAP", "Groups", None, QtGui.QApplication.UnicodeUTF8))
