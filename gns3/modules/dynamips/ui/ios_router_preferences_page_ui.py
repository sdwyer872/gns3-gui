# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/workspace/git/gns3-gui/gns3/modules/dynamips/ui/ios_router_preferences_page.ui'
#
# Created: Thu Jan 30 21:12:48 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IOSRouterPreferencesPageWidget(object):
    def setupUi(self, IOSRouterPreferencesPageWidget):
        IOSRouterPreferencesPageWidget.setObjectName(_fromUtf8("IOSRouterPreferencesPageWidget"))
        IOSRouterPreferencesPageWidget.resize(430, 525)
        self.vboxlayout = QtGui.QVBoxLayout(IOSRouterPreferencesPageWidget)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.uiTabWidget = QtGui.QTabWidget(IOSRouterPreferencesPageWidget)
        self.uiTabWidget.setObjectName(_fromUtf8("uiTabWidget"))
        self.uiIOSImagesTabWidget = QtGui.QWidget()
        self.uiIOSImagesTabWidget.setObjectName(_fromUtf8("uiIOSImagesTabWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.uiIOSImagesTabWidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.uiIOSImagesTreeWidget = QtGui.QTreeWidget(self.uiIOSImagesTabWidget)
        self.uiIOSImagesTreeWidget.setObjectName(_fromUtf8("uiIOSImagesTreeWidget"))
        self.gridLayout_3.addWidget(self.uiIOSImagesTreeWidget, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(self.uiIOSImagesTabWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uiIOSPathLabel = QtGui.QLabel(self.groupBox)
        self.uiIOSPathLabel.setObjectName(_fromUtf8("uiIOSPathLabel"))
        self.gridLayout_2.addWidget(self.uiIOSPathLabel, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.uiIOSPathLineEdit = QtGui.QLineEdit(self.groupBox)
        self.uiIOSPathLineEdit.setObjectName(_fromUtf8("uiIOSPathLineEdit"))
        self.horizontalLayout_3.addWidget(self.uiIOSPathLineEdit)
        self.uiIOSPathToolButton = QtGui.QToolButton(self.groupBox)
        self.uiIOSPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIOSPathToolButton.setObjectName(_fromUtf8("uiIOSPathToolButton"))
        self.horizontalLayout_3.addWidget(self.uiIOSPathToolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 2)
        self.uiStartupConfigLabel = QtGui.QLabel(self.groupBox)
        self.uiStartupConfigLabel.setObjectName(_fromUtf8("uiStartupConfigLabel"))
        self.gridLayout_2.addWidget(self.uiStartupConfigLabel, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uiStartupConfigLineEdit = QtGui.QLineEdit(self.groupBox)
        self.uiStartupConfigLineEdit.setObjectName(_fromUtf8("uiStartupConfigLineEdit"))
        self.horizontalLayout_4.addWidget(self.uiStartupConfigLineEdit)
        self.uiStartupConfigToolButton = QtGui.QToolButton(self.groupBox)
        self.uiStartupConfigToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiStartupConfigToolButton.setObjectName(_fromUtf8("uiStartupConfigToolButton"))
        self.horizontalLayout_4.addWidget(self.uiStartupConfigToolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 2)
        self.uiPlatformLabel = QtGui.QLabel(self.groupBox)
        self.uiPlatformLabel.setObjectName(_fromUtf8("uiPlatformLabel"))
        self.gridLayout_2.addWidget(self.uiPlatformLabel, 2, 0, 1, 1)
        self.uiPlatformComboBox = QtGui.QComboBox(self.groupBox)
        self.uiPlatformComboBox.setObjectName(_fromUtf8("uiPlatformComboBox"))
        self.gridLayout_2.addWidget(self.uiPlatformComboBox, 2, 1, 1, 2)
        self.uiChassisLabel = QtGui.QLabel(self.groupBox)
        self.uiChassisLabel.setObjectName(_fromUtf8("uiChassisLabel"))
        self.gridLayout_2.addWidget(self.uiChassisLabel, 3, 0, 1, 1)
        self.uiChassisComboBox = QtGui.QComboBox(self.groupBox)
        self.uiChassisComboBox.setObjectName(_fromUtf8("uiChassisComboBox"))
        self.gridLayout_2.addWidget(self.uiChassisComboBox, 3, 1, 1, 2)
        self.uiIdlePCLabel = QtGui.QLabel(self.groupBox)
        self.uiIdlePCLabel.setObjectName(_fromUtf8("uiIdlePCLabel"))
        self.gridLayout_2.addWidget(self.uiIdlePCLabel, 4, 0, 1, 1)
        self.uiIdlePCLineEdit = QtGui.QLineEdit(self.groupBox)
        self.uiIdlePCLineEdit.setObjectName(_fromUtf8("uiIdlePCLineEdit"))
        self.gridLayout_2.addWidget(self.uiIdlePCLineEdit, 4, 1, 1, 1)
        self.uiIdlePCFinderPushButton = QtGui.QPushButton(self.groupBox)
        self.uiIdlePCFinderPushButton.setObjectName(_fromUtf8("uiIdlePCFinderPushButton"))
        self.gridLayout_2.addWidget(self.uiIdlePCFinderPushButton, 4, 2, 1, 1)
        self.uiRAMLabel = QtGui.QLabel(self.groupBox)
        self.uiRAMLabel.setObjectName(_fromUtf8("uiRAMLabel"))
        self.gridLayout_2.addWidget(self.uiRAMLabel, 5, 0, 1, 1)
        self.uiRAMSpinBox = QtGui.QSpinBox(self.groupBox)
        self.uiRAMSpinBox.setMinimum(16)
        self.uiRAMSpinBox.setMaximum(65535)
        self.uiRAMSpinBox.setProperty("value", 128)
        self.uiRAMSpinBox.setObjectName(_fromUtf8("uiRAMSpinBox"))
        self.gridLayout_2.addWidget(self.uiRAMSpinBox, 5, 1, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.uiIOSImageTestSettingsPushButton = QtGui.QPushButton(self.uiIOSImagesTabWidget)
        self.uiIOSImageTestSettingsPushButton.setObjectName(_fromUtf8("uiIOSImageTestSettingsPushButton"))
        self.horizontalLayout_5.addWidget(self.uiIOSImageTestSettingsPushButton)
        self.uiSaveIOSImagePushButton = QtGui.QPushButton(self.uiIOSImagesTabWidget)
        self.uiSaveIOSImagePushButton.setObjectName(_fromUtf8("uiSaveIOSImagePushButton"))
        self.horizontalLayout_5.addWidget(self.uiSaveIOSImagePushButton)
        self.uiDeleteIOSImagePushButton = QtGui.QPushButton(self.uiIOSImagesTabWidget)
        self.uiDeleteIOSImagePushButton.setEnabled(False)
        self.uiDeleteIOSImagePushButton.setObjectName(_fromUtf8("uiDeleteIOSImagePushButton"))
        self.horizontalLayout_5.addWidget(self.uiDeleteIOSImagePushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.uiTabWidget.addTab(self.uiIOSImagesTabWidget, _fromUtf8(""))
        self.uiIOSRoutersTabWidget = QtGui.QWidget()
        self.uiIOSRoutersTabWidget.setObjectName(_fromUtf8("uiIOSRoutersTabWidget"))
        self.gridLayout = QtGui.QGridLayout(self.uiIOSRoutersTabWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget_2 = QtGui.QTreeWidget(self.uiIOSRoutersTabWidget)
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        self.gridLayout.addWidget(self.treeWidget_2, 0, 0, 2, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.uiIOSRoutersTabWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.uiIOSRoutersTabWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.uiIOSRoutersTabWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 354, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.uiTabWidget.addTab(self.uiIOSRoutersTabWidget, _fromUtf8(""))
        self.vboxlayout.addWidget(self.uiTabWidget)

        self.retranslateUi(IOSRouterPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IOSRouterPreferencesPageWidget)

    def retranslateUi(self, IOSRouterPreferencesPageWidget):
        IOSRouterPreferencesPageWidget.setWindowTitle(_translate("IOSRouterPreferencesPageWidget", "IOS routers", None))
        self.uiIOSImagesTreeWidget.headerItem().setText(0, _translate("IOSRouterPreferencesPageWidget", "File", None))
        self.uiIOSImagesTreeWidget.headerItem().setText(1, _translate("IOSRouterPreferencesPageWidget", "Platform", None))
        self.uiIOSImagesTreeWidget.headerItem().setText(2, _translate("IOSRouterPreferencesPageWidget", "Server", None))
        self.groupBox.setTitle(_translate("IOSRouterPreferencesPageWidget", "Settings", None))
        self.uiIOSPathLabel.setText(_translate("IOSRouterPreferencesPageWidget", "IOS path:", None))
        self.uiIOSPathToolButton.setText(_translate("IOSRouterPreferencesPageWidget", "...", None))
        self.uiStartupConfigLabel.setText(_translate("IOSRouterPreferencesPageWidget", "Startup-config:", None))
        self.uiStartupConfigToolButton.setText(_translate("IOSRouterPreferencesPageWidget", "...", None))
        self.uiPlatformLabel.setText(_translate("IOSRouterPreferencesPageWidget", "Platform:", None))
        self.uiChassisLabel.setText(_translate("IOSRouterPreferencesPageWidget", "Chassis:", None))
        self.uiIdlePCLabel.setText(_translate("IOSRouterPreferencesPageWidget", "Idle-PC:", None))
        self.uiIdlePCFinderPushButton.setText(_translate("IOSRouterPreferencesPageWidget", "Idle-PC finder", None))
        self.uiRAMLabel.setText(_translate("IOSRouterPreferencesPageWidget", "RAM:", None))
        self.uiRAMSpinBox.setSuffix(_translate("IOSRouterPreferencesPageWidget", " MB", None))
        self.uiIOSImageTestSettingsPushButton.setText(_translate("IOSRouterPreferencesPageWidget", "Test settings", None))
        self.uiSaveIOSImagePushButton.setText(_translate("IOSRouterPreferencesPageWidget", "Save", None))
        self.uiDeleteIOSImagePushButton.setText(_translate("IOSRouterPreferencesPageWidget", "Delete", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiIOSImagesTabWidget), _translate("IOSRouterPreferencesPageWidget", "IOS images", None))
        self.treeWidget_2.headerItem().setText(0, _translate("IOSRouterPreferencesPageWidget", "IOS routers", None))
        self.treeWidget_2.headerItem().setText(1, _translate("IOSRouterPreferencesPageWidget", "IOS file", None))
        self.pushButton_3.setText(_translate("IOSRouterPreferencesPageWidget", "New", None))
        self.pushButton_4.setText(_translate("IOSRouterPreferencesPageWidget", "Edit", None))
        self.pushButton_5.setText(_translate("IOSRouterPreferencesPageWidget", "Delete", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiIOSRoutersTabWidget), _translate("IOSRouterPreferencesPageWidget", "IOS routers", None))
