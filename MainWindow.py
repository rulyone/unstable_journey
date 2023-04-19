# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1214, 737)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionClearImage = QAction(MainWindow)
        self.actionClearImage.setObjectName(u"actionClearImage")
        self.actionOpenImage = QAction(MainWindow)
        self.actionOpenImage.setObjectName(u"actionOpenImage")
        icon = QIcon()
        icon.addFile(u":/icons/blue-folder-open-image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpenImage.setIcon(icon)
        self.actionSaveImage = QAction(MainWindow)
        self.actionSaveImage.setObjectName(u"actionSaveImage")
        icon1 = QIcon()
        icon1.addFile(u":/icons/disk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveImage.setIcon(icon1)
        self.actionInvertColors = QAction(MainWindow)
        self.actionInvertColors.setObjectName(u"actionInvertColors")
        self.actionFlipHorizontal = QAction(MainWindow)
        self.actionFlipHorizontal.setObjectName(u"actionFlipHorizontal")
        self.actionFlipVertical = QAction(MainWindow)
        self.actionFlipVertical.setObjectName(u"actionFlipVertical")
        self.actionNewImage = QAction(MainWindow)
        self.actionNewImage.setObjectName(u"actionNewImage")
        icon2 = QIcon()
        icon2.addFile(u":/icons/document-image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewImage.setIcon(icon2)
        self.actionBold = QAction(MainWindow)
        self.actionBold.setObjectName(u"actionBold")
        self.actionBold.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/edit-bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBold.setIcon(icon3)
        self.actionItalic = QAction(MainWindow)
        self.actionItalic.setObjectName(u"actionItalic")
        self.actionItalic.setCheckable(True)
        icon4 = QIcon()
        icon4.addFile(u":/icons/edit-italic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionItalic.setIcon(icon4)
        self.actionUnderline = QAction(MainWindow)
        self.actionUnderline.setObjectName(u"actionUnderline")
        self.actionUnderline.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u":/icons/edit-underline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUnderline.setIcon(icon5)
        self.actionFillShapes = QAction(MainWindow)
        self.actionFillShapes.setObjectName(u"actionFillShapes")
        self.actionFillShapes.setCheckable(True)
        icon6 = QIcon()
        icon6.addFile(u":/icons/paint-can-color.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFillShapes.setIcon(icon6)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rectButton = QPushButton(self.widget)
        self.rectButton.setObjectName(u"rectButton")
        self.rectButton.setMinimumSize(QSize(30, 30))
        self.rectButton.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/layer-shape.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rectButton.setIcon(icon7)
        self.rectButton.setCheckable(True)

        self.gridLayout.addWidget(self.rectButton, 6, 0, 1, 1)

        self.selectrectButton = QPushButton(self.widget)
        self.selectrectButton.setObjectName(u"selectrectButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectrectButton.sizePolicy().hasHeightForWidth())
        self.selectrectButton.setSizePolicy(sizePolicy1)
        self.selectrectButton.setMinimumSize(QSize(30, 30))
        self.selectrectButton.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/icons/selection.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectrectButton.setIcon(icon8)
        self.selectrectButton.setCheckable(True)

        self.gridLayout.addWidget(self.selectrectButton, 0, 1, 1, 1)

        self.eraserButton = QPushButton(self.widget)
        self.eraserButton.setObjectName(u"eraserButton")
        sizePolicy1.setHeightForWidth(self.eraserButton.sizePolicy().hasHeightForWidth())
        self.eraserButton.setSizePolicy(sizePolicy1)
        self.eraserButton.setMinimumSize(QSize(30, 30))
        self.eraserButton.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u":/icons/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eraserButton.setIcon(icon9)
        self.eraserButton.setCheckable(True)

        self.gridLayout.addWidget(self.eraserButton, 1, 0, 1, 1)

        self.stampButton = QPushButton(self.widget)
        self.stampButton.setObjectName(u"stampButton")
        sizePolicy1.setHeightForWidth(self.stampButton.sizePolicy().hasHeightForWidth())
        self.stampButton.setSizePolicy(sizePolicy1)
        self.stampButton.setMinimumSize(QSize(30, 30))
        self.stampButton.setMaximumSize(QSize(30, 30))
        icon10 = QIcon()
        icon10.addFile(u":/icons/cake.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stampButton.setIcon(icon10)
        self.stampButton.setCheckable(True)

        self.gridLayout.addWidget(self.stampButton, 2, 1, 1, 1)

        self.dropperButton = QPushButton(self.widget)
        self.dropperButton.setObjectName(u"dropperButton")
        sizePolicy1.setHeightForWidth(self.dropperButton.sizePolicy().hasHeightForWidth())
        self.dropperButton.setSizePolicy(sizePolicy1)
        self.dropperButton.setMinimumSize(QSize(30, 30))
        self.dropperButton.setMaximumSize(QSize(30, 30))
        icon11 = QIcon()
        icon11.addFile(u":/icons/pipette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dropperButton.setIcon(icon11)
        self.dropperButton.setCheckable(True)

        self.gridLayout.addWidget(self.dropperButton, 2, 0, 1, 1)

        self.brushButton = QPushButton(self.widget)
        self.brushButton.setObjectName(u"brushButton")
        sizePolicy1.setHeightForWidth(self.brushButton.sizePolicy().hasHeightForWidth())
        self.brushButton.setSizePolicy(sizePolicy1)
        self.brushButton.setMinimumSize(QSize(30, 30))
        self.brushButton.setMaximumSize(QSize(30, 30))
        icon12 = QIcon()
        icon12.addFile(u":/icons/paint-brush.png", QSize(), QIcon.Normal, QIcon.Off)
        self.brushButton.setIcon(icon12)
        self.brushButton.setCheckable(True)

        self.gridLayout.addWidget(self.brushButton, 3, 1, 1, 1)

        self.penButton = QPushButton(self.widget)
        self.penButton.setObjectName(u"penButton")
        sizePolicy1.setHeightForWidth(self.penButton.sizePolicy().hasHeightForWidth())
        self.penButton.setSizePolicy(sizePolicy1)
        self.penButton.setMinimumSize(QSize(30, 30))
        self.penButton.setMaximumSize(QSize(30, 30))
        icon13 = QIcon()
        icon13.addFile(u":/icons/pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.penButton.setIcon(icon13)
        self.penButton.setCheckable(True)

        self.gridLayout.addWidget(self.penButton, 3, 0, 1, 1)

        self.fillButton = QPushButton(self.widget)
        self.fillButton.setObjectName(u"fillButton")
        sizePolicy1.setHeightForWidth(self.fillButton.sizePolicy().hasHeightForWidth())
        self.fillButton.setSizePolicy(sizePolicy1)
        self.fillButton.setMinimumSize(QSize(30, 30))
        self.fillButton.setMaximumSize(QSize(30, 30))
        icon14 = QIcon()
        icon14.addFile(u":/icons/paint-can.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fillButton.setIcon(icon14)
        self.fillButton.setCheckable(True)

        self.gridLayout.addWidget(self.fillButton, 1, 1, 1, 1)

        self.sprayButton = QPushButton(self.widget)
        self.sprayButton.setObjectName(u"sprayButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sprayButton.sizePolicy().hasHeightForWidth())
        self.sprayButton.setSizePolicy(sizePolicy2)
        self.sprayButton.setMinimumSize(QSize(30, 30))
        self.sprayButton.setMaximumSize(QSize(30, 30))
        icon15 = QIcon()
        icon15.addFile(u":/icons/spray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sprayButton.setIcon(icon15)
        self.sprayButton.setCheckable(True)
        self.sprayButton.setFlat(False)

        self.gridLayout.addWidget(self.sprayButton, 4, 0, 1, 1)

        self.lineButton = QPushButton(self.widget)
        self.lineButton.setObjectName(u"lineButton")
        self.lineButton.setMinimumSize(QSize(30, 30))
        self.lineButton.setMaximumSize(QSize(30, 30))
        icon16 = QIcon()
        icon16.addFile(u":/icons/layer-shape-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lineButton.setIcon(icon16)
        self.lineButton.setCheckable(True)

        self.gridLayout.addWidget(self.lineButton, 0, 0, 1, 1)

        self.ellipseButton = QPushButton(self.widget)
        self.ellipseButton.setObjectName(u"ellipseButton")
        self.ellipseButton.setMinimumSize(QSize(30, 30))
        self.ellipseButton.setMaximumSize(QSize(30, 30))
        icon17 = QIcon()
        icon17.addFile(u":/icons/layer-shape-ellipse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ellipseButton.setIcon(icon17)
        self.ellipseButton.setCheckable(True)

        self.gridLayout.addWidget(self.ellipseButton, 4, 1, 1, 1)

        self.roundrectButton = QPushButton(self.widget)
        self.roundrectButton.setObjectName(u"roundrectButton")
        self.roundrectButton.setMinimumSize(QSize(30, 30))
        self.roundrectButton.setMaximumSize(QSize(30, 30))
        icon18 = QIcon()
        icon18.addFile(u":/icons/layer-shape-round.png", QSize(), QIcon.Normal, QIcon.Off)
        self.roundrectButton.setIcon(icon18)
        self.roundrectButton.setCheckable(True)

        self.gridLayout.addWidget(self.roundrectButton, 6, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.canvas = QLabel(self.centralWidget)
        self.canvas.setObjectName(u"canvas")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy3)
        self.canvas.setMaximumSize(QSize(512, 512))

        self.horizontalLayout.addWidget(self.canvas)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.widget_4 = QWidget(self.centralWidget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(50, 100))
        self.widget_4.setMaximumSize(QSize(50, 100))
        self.convertSDButton = QPushButton(self.widget_4)
        self.convertSDButton.setObjectName(u"convertSDButton")
        self.convertSDButton.setGeometry(QRect(10, 0, 30, 30))
        self.convertSDButton.setMinimumSize(QSize(30, 30))
        self.convertSDButton.setMaximumSize(QSize(30, 30))
        icon19 = QIcon()
        icon19.addFile(u"icons/arrowright.png", QSize(), QIcon.Normal, QIcon.Off)
        self.convertSDButton.setIcon(icon19)
        self.replaceSDButton = QPushButton(self.widget_4)
        self.replaceSDButton.setObjectName(u"replaceSDButton")
        self.replaceSDButton.setGeometry(QRect(10, 40, 30, 30))
        self.replaceSDButton.setMinimumSize(QSize(30, 30))
        self.replaceSDButton.setMaximumSize(QSize(30, 30))
        icon20 = QIcon()
        icon20.addFile(u"icons/arrowleft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.replaceSDButton.setIcon(icon20)

        self.verticalLayout_4.addWidget(self.widget_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.sdCanvas = QLabel(self.centralWidget)
        self.sdCanvas.setObjectName(u"sdCanvas")
        sizePolicy3.setHeightForWidth(self.sdCanvas.sizePolicy().hasHeightForWidth())
        self.sdCanvas.setSizePolicy(sizePolicy3)
        self.sdCanvas.setMaximumSize(QSize(512, 512))

        self.horizontalLayout.addWidget(self.sdCanvas)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(self.centralWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(78, 0))
        self.widget_3.setMaximumSize(QSize(78, 16777215))
        self.secondaryButton = QPushButton(self.widget_3)
        self.secondaryButton.setObjectName(u"secondaryButton")
        self.secondaryButton.setGeometry(QRect(30, 10, 40, 40))
        self.secondaryButton.setMinimumSize(QSize(40, 40))
        self.secondaryButton.setMaximumSize(QSize(40, 40))
        self.primaryButton = QPushButton(self.widget_3)
        self.primaryButton.setObjectName(u"primaryButton")
        self.primaryButton.setGeometry(QRect(10, 0, 40, 40))
        self.primaryButton.setMinimumSize(QSize(40, 40))
        self.primaryButton.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.centralWidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.widget_2.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 0, 15, 15)
        self.colorButton_11 = QPushButton(self.widget_2)
        self.colorButton_11.setObjectName(u"colorButton_11")
        sizePolicy1.setHeightForWidth(self.colorButton_11.sizePolicy().hasHeightForWidth())
        self.colorButton_11.setSizePolicy(sizePolicy1)
        self.colorButton_11.setMinimumSize(QSize(20, 20))
        self.colorButton_11.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_11, 0, 10, 1, 1)

        self.colorButton_7 = QPushButton(self.widget_2)
        self.colorButton_7.setObjectName(u"colorButton_7")
        sizePolicy1.setHeightForWidth(self.colorButton_7.sizePolicy().hasHeightForWidth())
        self.colorButton_7.setSizePolicy(sizePolicy1)
        self.colorButton_7.setMinimumSize(QSize(20, 20))
        self.colorButton_7.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_7, 0, 6, 1, 1)

        self.colorButton_9 = QPushButton(self.widget_2)
        self.colorButton_9.setObjectName(u"colorButton_9")
        sizePolicy1.setHeightForWidth(self.colorButton_9.sizePolicy().hasHeightForWidth())
        self.colorButton_9.setSizePolicy(sizePolicy1)
        self.colorButton_9.setMinimumSize(QSize(20, 20))
        self.colorButton_9.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_9, 0, 8, 1, 1)

        self.colorButton_10 = QPushButton(self.widget_2)
        self.colorButton_10.setObjectName(u"colorButton_10")
        sizePolicy1.setHeightForWidth(self.colorButton_10.sizePolicy().hasHeightForWidth())
        self.colorButton_10.setSizePolicy(sizePolicy1)
        self.colorButton_10.setMinimumSize(QSize(20, 20))
        self.colorButton_10.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_10, 0, 9, 1, 1)

        self.colorButton_23 = QPushButton(self.widget_2)
        self.colorButton_23.setObjectName(u"colorButton_23")
        sizePolicy1.setHeightForWidth(self.colorButton_23.sizePolicy().hasHeightForWidth())
        self.colorButton_23.setSizePolicy(sizePolicy1)
        self.colorButton_23.setMinimumSize(QSize(20, 20))
        self.colorButton_23.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_23, 1, 8, 1, 1)

        self.colorButton_18 = QPushButton(self.widget_2)
        self.colorButton_18.setObjectName(u"colorButton_18")
        sizePolicy1.setHeightForWidth(self.colorButton_18.sizePolicy().hasHeightForWidth())
        self.colorButton_18.setSizePolicy(sizePolicy1)
        self.colorButton_18.setMinimumSize(QSize(20, 20))
        self.colorButton_18.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_18, 1, 3, 1, 1)

        self.colorButton_20 = QPushButton(self.widget_2)
        self.colorButton_20.setObjectName(u"colorButton_20")
        sizePolicy1.setHeightForWidth(self.colorButton_20.sizePolicy().hasHeightForWidth())
        self.colorButton_20.setSizePolicy(sizePolicy1)
        self.colorButton_20.setMinimumSize(QSize(20, 20))
        self.colorButton_20.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_20, 1, 5, 1, 1)

        self.colorButton_6 = QPushButton(self.widget_2)
        self.colorButton_6.setObjectName(u"colorButton_6")
        sizePolicy1.setHeightForWidth(self.colorButton_6.sizePolicy().hasHeightForWidth())
        self.colorButton_6.setSizePolicy(sizePolicy1)
        self.colorButton_6.setMinimumSize(QSize(20, 20))
        self.colorButton_6.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_6, 0, 5, 1, 1)

        self.colorButton_3 = QPushButton(self.widget_2)
        self.colorButton_3.setObjectName(u"colorButton_3")
        sizePolicy1.setHeightForWidth(self.colorButton_3.sizePolicy().hasHeightForWidth())
        self.colorButton_3.setSizePolicy(sizePolicy1)
        self.colorButton_3.setMinimumSize(QSize(20, 20))
        self.colorButton_3.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_3, 0, 2, 1, 1)

        self.colorButton_24 = QPushButton(self.widget_2)
        self.colorButton_24.setObjectName(u"colorButton_24")
        sizePolicy1.setHeightForWidth(self.colorButton_24.sizePolicy().hasHeightForWidth())
        self.colorButton_24.setSizePolicy(sizePolicy1)
        self.colorButton_24.setMinimumSize(QSize(20, 20))
        self.colorButton_24.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_24, 1, 9, 1, 1)

        self.colorButton_17 = QPushButton(self.widget_2)
        self.colorButton_17.setObjectName(u"colorButton_17")
        sizePolicy1.setHeightForWidth(self.colorButton_17.sizePolicy().hasHeightForWidth())
        self.colorButton_17.setSizePolicy(sizePolicy1)
        self.colorButton_17.setMinimumSize(QSize(20, 20))
        self.colorButton_17.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_17, 1, 2, 1, 1)

        self.colorButton_1 = QPushButton(self.widget_2)
        self.colorButton_1.setObjectName(u"colorButton_1")
        sizePolicy1.setHeightForWidth(self.colorButton_1.sizePolicy().hasHeightForWidth())
        self.colorButton_1.setSizePolicy(sizePolicy1)
        self.colorButton_1.setMinimumSize(QSize(20, 20))
        self.colorButton_1.setMaximumSize(QSize(20, 13))
        self.colorButton_1.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.colorButton_1, 0, 0, 1, 1)

        self.colorButton_8 = QPushButton(self.widget_2)
        self.colorButton_8.setObjectName(u"colorButton_8")
        sizePolicy1.setHeightForWidth(self.colorButton_8.sizePolicy().hasHeightForWidth())
        self.colorButton_8.setSizePolicy(sizePolicy1)
        self.colorButton_8.setMinimumSize(QSize(20, 20))
        self.colorButton_8.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_8, 0, 7, 1, 1)

        self.colorButton_27 = QPushButton(self.widget_2)
        self.colorButton_27.setObjectName(u"colorButton_27")
        sizePolicy1.setHeightForWidth(self.colorButton_27.sizePolicy().hasHeightForWidth())
        self.colorButton_27.setSizePolicy(sizePolicy1)
        self.colorButton_27.setMinimumSize(QSize(20, 20))
        self.colorButton_27.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_27, 1, 12, 1, 1)

        self.colorButton_22 = QPushButton(self.widget_2)
        self.colorButton_22.setObjectName(u"colorButton_22")
        sizePolicy1.setHeightForWidth(self.colorButton_22.sizePolicy().hasHeightForWidth())
        self.colorButton_22.setSizePolicy(sizePolicy1)
        self.colorButton_22.setMinimumSize(QSize(20, 20))
        self.colorButton_22.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_22, 1, 7, 1, 1)

        self.colorButton_15 = QPushButton(self.widget_2)
        self.colorButton_15.setObjectName(u"colorButton_15")
        sizePolicy1.setHeightForWidth(self.colorButton_15.sizePolicy().hasHeightForWidth())
        self.colorButton_15.setSizePolicy(sizePolicy1)
        self.colorButton_15.setMinimumSize(QSize(20, 20))
        self.colorButton_15.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_15, 1, 0, 1, 1)

        self.colorButton_5 = QPushButton(self.widget_2)
        self.colorButton_5.setObjectName(u"colorButton_5")
        sizePolicy1.setHeightForWidth(self.colorButton_5.sizePolicy().hasHeightForWidth())
        self.colorButton_5.setSizePolicy(sizePolicy1)
        self.colorButton_5.setMinimumSize(QSize(20, 20))
        self.colorButton_5.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_5, 0, 4, 1, 1)

        self.colorButton_2 = QPushButton(self.widget_2)
        self.colorButton_2.setObjectName(u"colorButton_2")
        sizePolicy1.setHeightForWidth(self.colorButton_2.sizePolicy().hasHeightForWidth())
        self.colorButton_2.setSizePolicy(sizePolicy1)
        self.colorButton_2.setMinimumSize(QSize(20, 20))
        self.colorButton_2.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_2, 0, 1, 1, 1)

        self.colorButton_16 = QPushButton(self.widget_2)
        self.colorButton_16.setObjectName(u"colorButton_16")
        sizePolicy1.setHeightForWidth(self.colorButton_16.sizePolicy().hasHeightForWidth())
        self.colorButton_16.setSizePolicy(sizePolicy1)
        self.colorButton_16.setMinimumSize(QSize(20, 20))
        self.colorButton_16.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_16, 1, 1, 1, 1)

        self.colorButton_14 = QPushButton(self.widget_2)
        self.colorButton_14.setObjectName(u"colorButton_14")
        sizePolicy1.setHeightForWidth(self.colorButton_14.sizePolicy().hasHeightForWidth())
        self.colorButton_14.setSizePolicy(sizePolicy1)
        self.colorButton_14.setMinimumSize(QSize(20, 20))
        self.colorButton_14.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_14, 0, 13, 1, 1)

        self.colorButton_4 = QPushButton(self.widget_2)
        self.colorButton_4.setObjectName(u"colorButton_4")
        sizePolicy1.setHeightForWidth(self.colorButton_4.sizePolicy().hasHeightForWidth())
        self.colorButton_4.setSizePolicy(sizePolicy1)
        self.colorButton_4.setMinimumSize(QSize(20, 20))
        self.colorButton_4.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_4, 0, 3, 1, 1)

        self.colorButton_21 = QPushButton(self.widget_2)
        self.colorButton_21.setObjectName(u"colorButton_21")
        sizePolicy1.setHeightForWidth(self.colorButton_21.sizePolicy().hasHeightForWidth())
        self.colorButton_21.setSizePolicy(sizePolicy1)
        self.colorButton_21.setMinimumSize(QSize(20, 20))
        self.colorButton_21.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_21, 1, 6, 1, 1)

        self.colorButton_25 = QPushButton(self.widget_2)
        self.colorButton_25.setObjectName(u"colorButton_25")
        sizePolicy1.setHeightForWidth(self.colorButton_25.sizePolicy().hasHeightForWidth())
        self.colorButton_25.setSizePolicy(sizePolicy1)
        self.colorButton_25.setMinimumSize(QSize(20, 20))
        self.colorButton_25.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_25, 1, 10, 1, 1)

        self.colorButton_12 = QPushButton(self.widget_2)
        self.colorButton_12.setObjectName(u"colorButton_12")
        sizePolicy1.setHeightForWidth(self.colorButton_12.sizePolicy().hasHeightForWidth())
        self.colorButton_12.setSizePolicy(sizePolicy1)
        self.colorButton_12.setMinimumSize(QSize(20, 20))
        self.colorButton_12.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_12, 0, 11, 1, 1)

        self.colorButton_19 = QPushButton(self.widget_2)
        self.colorButton_19.setObjectName(u"colorButton_19")
        sizePolicy1.setHeightForWidth(self.colorButton_19.sizePolicy().hasHeightForWidth())
        self.colorButton_19.setSizePolicy(sizePolicy1)
        self.colorButton_19.setMinimumSize(QSize(20, 20))
        self.colorButton_19.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_19, 1, 4, 1, 1)

        self.colorButton_13 = QPushButton(self.widget_2)
        self.colorButton_13.setObjectName(u"colorButton_13")
        sizePolicy1.setHeightForWidth(self.colorButton_13.sizePolicy().hasHeightForWidth())
        self.colorButton_13.setSizePolicy(sizePolicy1)
        self.colorButton_13.setMinimumSize(QSize(20, 20))
        self.colorButton_13.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_13, 0, 12, 1, 1)

        self.colorButton_26 = QPushButton(self.widget_2)
        self.colorButton_26.setObjectName(u"colorButton_26")
        sizePolicy1.setHeightForWidth(self.colorButton_26.sizePolicy().hasHeightForWidth())
        self.colorButton_26.setSizePolicy(sizePolicy1)
        self.colorButton_26.setMinimumSize(QSize(20, 20))
        self.colorButton_26.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_26, 1, 11, 1, 1)

        self.colorButton_28 = QPushButton(self.widget_2)
        self.colorButton_28.setObjectName(u"colorButton_28")
        sizePolicy1.setHeightForWidth(self.colorButton_28.sizePolicy().hasHeightForWidth())
        self.colorButton_28.setSizePolicy(sizePolicy1)
        self.colorButton_28.setMinimumSize(QSize(20, 20))
        self.colorButton_28.setMaximumSize(QSize(20, 13))

        self.gridLayout_2.addWidget(self.colorButton_28, 1, 13, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.stampnextButton = QPushButton(self.centralWidget)
        self.stampnextButton.setObjectName(u"stampnextButton")
        self.stampnextButton.setMinimumSize(QSize(78, 55))
        self.stampnextButton.setMaximumSize(QSize(78, 55))
        self.stampnextButton.setIconSize(QSize(80, 50))

        self.horizontalLayout_2.addWidget(self.stampnextButton)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.promptTextEdit = QTextEdit(self.centralWidget)
        self.promptTextEdit.setObjectName(u"promptTextEdit")
        self.promptTextEdit.setAcceptRichText(False)

        self.verticalLayout_5.addWidget(self.promptTextEdit)

        self.negativePromptTextEdit = QTextEdit(self.centralWidget)
        self.negativePromptTextEdit.setObjectName(u"negativePromptTextEdit")

        self.verticalLayout_5.addWidget(self.negativePromptTextEdit)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.seedLabel = QLabel(self.centralWidget)
        self.seedLabel.setObjectName(u"seedLabel")
        sizePolicy4.setHeightForWidth(self.seedLabel.sizePolicy().hasHeightForWidth())
        self.seedLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_6.addWidget(self.seedLabel)

        self.seedLineEdit = QLineEdit(self.centralWidget)
        self.seedLineEdit.setObjectName(u"seedLineEdit")
        self.seedLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.horizontalLayout_6.addWidget(self.seedLineEdit)

        self.seedRandomizeButton = QPushButton(self.centralWidget)
        self.seedRandomizeButton.setObjectName(u"seedRandomizeButton")
        self.seedRandomizeButton.setFlat(False)

        self.horizontalLayout_6.addWidget(self.seedRandomizeButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cfgLabel = QLabel(self.centralWidget)
        self.cfgLabel.setObjectName(u"cfgLabel")

        self.horizontalLayout_7.addWidget(self.cfgLabel)

        self.cfgDoubleSpinBox = QDoubleSpinBox(self.centralWidget)
        self.cfgDoubleSpinBox.setObjectName(u"cfgDoubleSpinBox")
        self.cfgDoubleSpinBox.setMinimum(-99.000000000000000)
        self.cfgDoubleSpinBox.setSingleStep(0.100000000000000)
        self.cfgDoubleSpinBox.setValue(7.500000000000000)

        self.horizontalLayout_7.addWidget(self.cfgDoubleSpinBox)

        self.denoisingLabel = QLabel(self.centralWidget)
        self.denoisingLabel.setObjectName(u"denoisingLabel")

        self.horizontalLayout_7.addWidget(self.denoisingLabel)

        self.denoisingDoubleSpinBox = QDoubleSpinBox(self.centralWidget)
        self.denoisingDoubleSpinBox.setObjectName(u"denoisingDoubleSpinBox")
        self.denoisingDoubleSpinBox.setMinimum(-99.000000000000000)
        self.denoisingDoubleSpinBox.setSingleStep(0.010000000000000)
        self.denoisingDoubleSpinBox.setValue(0.500000000000000)

        self.horizontalLayout_7.addWidget(self.denoisingDoubleSpinBox)

        self.stepsLabel = QLabel(self.centralWidget)
        self.stepsLabel.setObjectName(u"stepsLabel")

        self.horizontalLayout_7.addWidget(self.stepsLabel)

        self.stepsSpinBox = QSpinBox(self.centralWidget)
        self.stepsSpinBox.setObjectName(u"stepsSpinBox")
        self.stepsSpinBox.setMinimum(1)
        self.stepsSpinBox.setValue(20)

        self.horizontalLayout_7.addWidget(self.stepsSpinBox)

        self.samplerLabel = QLabel(self.centralWidget)
        self.samplerLabel.setObjectName(u"samplerLabel")

        self.horizontalLayout_7.addWidget(self.samplerLabel)

        self.samplerComboBox = QComboBox(self.centralWidget)
        self.samplerComboBox.setObjectName(u"samplerComboBox")

        self.horizontalLayout_7.addWidget(self.samplerComboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.modelLabel = QLabel(self.centralWidget)
        self.modelLabel.setObjectName(u"modelLabel")
        sizePolicy4.setHeightForWidth(self.modelLabel.sizePolicy().hasHeightForWidth())
        self.modelLabel.setSizePolicy(sizePolicy4)
        self.modelLabel.setMinimumSize(QSize(20, 10))

        self.horizontalLayout_8.addWidget(self.modelLabel)

        self.modelComboBox = QComboBox(self.centralWidget)
        self.modelComboBox.setObjectName(u"modelComboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.modelComboBox.sizePolicy().hasHeightForWidth())
        self.modelComboBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.modelComboBox)

        self.refreshModelButton = QPushButton(self.centralWidget)
        self.refreshModelButton.setObjectName(u"refreshModelButton")

        self.horizontalLayout_8.addWidget(self.refreshModelButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cnPreLabel = QLabel(self.centralWidget)
        self.cnPreLabel.setObjectName(u"cnPreLabel")

        self.horizontalLayout_9.addWidget(self.cnPreLabel)

        self.cnPreComboBox = QComboBox(self.centralWidget)
        self.cnPreComboBox.setObjectName(u"cnPreComboBox")
        sizePolicy5.setHeightForWidth(self.cnPreComboBox.sizePolicy().hasHeightForWidth())
        self.cnPreComboBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_9.addWidget(self.cnPreComboBox)

        self.cnModelLabel = QLabel(self.centralWidget)
        self.cnModelLabel.setObjectName(u"cnModelLabel")

        self.horizontalLayout_9.addWidget(self.cnModelLabel)

        self.cnModelComboBox = QComboBox(self.centralWidget)
        self.cnModelComboBox.setObjectName(u"cnModelComboBox")
        sizePolicy5.setHeightForWidth(self.cnModelComboBox.sizePolicy().hasHeightForWidth())
        self.cnModelComboBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_9.addWidget(self.cnModelComboBox)

        self.refreshCNModelButton = QPushButton(self.centralWidget)
        self.refreshCNModelButton.setObjectName(u"refreshCNModelButton")

        self.horizontalLayout_9.addWidget(self.refreshCNModelButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setContentsMargins(-1, -1, 30, 30)
        self.hostLabel = QLabel(self.centralWidget)
        self.hostLabel.setObjectName(u"hostLabel")

        self.horizontalLayout_14.addWidget(self.hostLabel)

        self.hostLineEdit = QLineEdit(self.centralWidget)
        self.hostLineEdit.setObjectName(u"hostLineEdit")
        sizePolicy2.setHeightForWidth(self.hostLineEdit.sizePolicy().hasHeightForWidth())
        self.hostLineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.hostLineEdit)

        self.portLabel = QLabel(self.centralWidget)
        self.portLabel.setObjectName(u"portLabel")

        self.horizontalLayout_14.addWidget(self.portLabel)

        self.portLineEdit = QLineEdit(self.centralWidget)
        self.portLineEdit.setObjectName(u"portLineEdit")
        sizePolicy2.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.portLineEdit)

        self.httpsCheckBox = QCheckBox(self.centralWidget)
        self.httpsCheckBox.setObjectName(u"httpsCheckBox")

        self.horizontalLayout_14.addWidget(self.httpsCheckBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.helpPushButton = QPushButton(self.centralWidget)
        self.helpPushButton.setObjectName(u"helpPushButton")
        self.helpPushButton.setStyleSheet(u"font-size: 14pt; font-weight: bold")

        self.horizontalLayout_14.addWidget(self.helpPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1214, 21))
        self.menuFIle = QMenu(self.menuBar)
        self.menuFIle.setObjectName(u"menuFIle")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuImage = QMenu(self.menuBar)
        self.menuImage.setObjectName(u"menuImage")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.fileToolbar = QToolBar(MainWindow)
        self.fileToolbar.setObjectName(u"fileToolbar")
        self.fileToolbar.setIconSize(QSize(16, 16))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.fileToolbar)
        self.drawingToolbar = QToolBar(MainWindow)
        self.drawingToolbar.setObjectName(u"drawingToolbar")
        sizePolicy2.setHeightForWidth(self.drawingToolbar.sizePolicy().hasHeightForWidth())
        self.drawingToolbar.setSizePolicy(sizePolicy2)
        self.drawingToolbar.setMinimumSize(QSize(0, 0))
        self.drawingToolbar.setMaximumSize(QSize(200, 16777215))
        self.drawingToolbar.setIconSize(QSize(16, 16))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.drawingToolbar)

        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuImage.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFIle.addAction(self.actionNewImage)
        self.menuFIle.addAction(self.actionOpenImage)
        self.menuFIle.addAction(self.actionSaveImage)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClearImage)
        self.menuImage.addAction(self.actionInvertColors)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionFlipHorizontal)
        self.menuImage.addAction(self.actionFlipVertical)
        self.fileToolbar.addAction(self.actionNewImage)
        self.fileToolbar.addAction(self.actionOpenImage)
        self.fileToolbar.addAction(self.actionSaveImage)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Unstable Journey (Icnivad)", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionClearImage.setText(QCoreApplication.translate("MainWindow", u"Clear Image", None))
        self.actionOpenImage.setText(QCoreApplication.translate("MainWindow", u"Open Image...", None))
        self.actionSaveImage.setText(QCoreApplication.translate("MainWindow", u"Save Image As...", None))
        self.actionInvertColors.setText(QCoreApplication.translate("MainWindow", u"Invert Colors", None))
        self.actionFlipHorizontal.setText(QCoreApplication.translate("MainWindow", u"Flip Horizontal", None))
        self.actionFlipVertical.setText(QCoreApplication.translate("MainWindow", u"Flip Vertical", None))
        self.actionNewImage.setText(QCoreApplication.translate("MainWindow", u"New Image", None))
        self.actionBold.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
#if QT_CONFIG(shortcut)
        self.actionBold.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionItalic.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
#if QT_CONFIG(shortcut)
        self.actionItalic.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionUnderline.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
        self.actionFillShapes.setText(QCoreApplication.translate("MainWindow", u"Fill Shapes?", None))
        self.rectButton.setText("")
        self.selectrectButton.setText("")
        self.eraserButton.setText("")
        self.stampButton.setText("")
        self.dropperButton.setText("")
        self.brushButton.setText("")
        self.penButton.setText("")
        self.fillButton.setText("")
        self.sprayButton.setText("")
        self.lineButton.setText("")
        self.ellipseButton.setText("")
        self.roundrectButton.setText("")
        self.canvas.setText("")
        self.convertSDButton.setText("")
        self.replaceSDButton.setText("")
        self.sdCanvas.setText("")
        self.secondaryButton.setText("")
        self.primaryButton.setText("")
        self.colorButton_11.setText("")
        self.colorButton_7.setText("")
        self.colorButton_9.setText("")
        self.colorButton_10.setText("")
        self.colorButton_23.setText("")
        self.colorButton_18.setText("")
        self.colorButton_20.setText("")
        self.colorButton_6.setText("")
        self.colorButton_3.setText("")
        self.colorButton_24.setText("")
        self.colorButton_17.setText("")
        self.colorButton_1.setText("")
        self.colorButton_8.setText("")
        self.colorButton_27.setText("")
        self.colorButton_22.setText("")
        self.colorButton_15.setText("")
        self.colorButton_5.setText("")
        self.colorButton_2.setText("")
        self.colorButton_16.setText("")
        self.colorButton_14.setText("")
        self.colorButton_4.setText("")
        self.colorButton_21.setText("")
        self.colorButton_25.setText("")
        self.colorButton_12.setText("")
        self.colorButton_19.setText("")
        self.colorButton_13.setText("")
        self.colorButton_26.setText("")
        self.colorButton_28.setText("")
        self.stampnextButton.setText("")
        self.promptTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">wtrcolor style, watercolor</p></body></html>", None))
        self.promptTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prompt", None))
        self.negativePromptTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.negativePromptTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Negative Prompt", None))
        self.seedLabel.setText(QCoreApplication.translate("MainWindow", u"Seed:", None))
        self.seedLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A Random Value will be generated at First", None))
        self.seedRandomizeButton.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
        self.cfgLabel.setText(QCoreApplication.translate("MainWindow", u"CFG:", None))
        self.denoisingLabel.setText(QCoreApplication.translate("MainWindow", u"Denoising:", None))
        self.stepsLabel.setText(QCoreApplication.translate("MainWindow", u"Steps:", None))
        self.samplerLabel.setText(QCoreApplication.translate("MainWindow", u"Sampler:", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.refreshModelButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.cnPreLabel.setText(QCoreApplication.translate("MainWindow", u"CN PreProcessor:", None))
        self.cnModelLabel.setText(QCoreApplication.translate("MainWindow", u"CN Model:", None))
        self.refreshCNModelButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.hostLabel.setText(QCoreApplication.translate("MainWindow", u"Host:", None))
        self.hostLineEdit.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.portLineEdit.setText(QCoreApplication.translate("MainWindow", u"7860", None))
        self.httpsCheckBox.setText(QCoreApplication.translate("MainWindow", u"use HTTPS?", None))
        self.helpPushButton.setText(QCoreApplication.translate("MainWindow", u"Help !", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.fileToolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.drawingToolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

