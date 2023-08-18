# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calibration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WaterCalibration(object):
    def setupUi(self, WaterCalibration):
        WaterCalibration.setObjectName("WaterCalibration")
        WaterCalibration.resize(1080, 869)
        self.OpenRightTime = QtWidgets.QDoubleSpinBox(WaterCalibration)
        self.OpenRightTime.setGeometry(QtCore.QRect(434, 130, 80, 20))
        self.OpenRightTime.setDecimals(3)
        self.OpenRightTime.setSingleStep(0.005)
        self.OpenRightTime.setProperty("value", 0.03)
        self.OpenRightTime.setObjectName("OpenRightTime")
        self.OpenLeftTime = QtWidgets.QDoubleSpinBox(WaterCalibration)
        self.OpenLeftTime.setGeometry(QtCore.QRect(434, 90, 80, 20))
        self.OpenLeftTime.setDecimals(3)
        self.OpenLeftTime.setSingleStep(0.005)
        self.OpenLeftTime.setProperty("value", 0.03)
        self.OpenLeftTime.setObjectName("OpenLeftTime")
        self.label_3 = QtWidgets.QLabel(WaterCalibration)
        self.label_3.setGeometry(QtCore.QRect(356, 90, 71, 23))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(WaterCalibration)
        self.label_4.setGeometry(QtCore.QRect(340, 130, 91, 23))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.IntervalLeft = QtWidgets.QDoubleSpinBox(WaterCalibration)
        self.IntervalLeft.setGeometry(QtCore.QRect(650, 90, 80, 20))
        self.IntervalLeft.setDecimals(3)
        self.IntervalLeft.setSingleStep(0.005)
        self.IntervalLeft.setProperty("value", 0.5)
        self.IntervalLeft.setObjectName("IntervalLeft")
        self.label_5 = QtWidgets.QLabel(WaterCalibration)
        self.label_5.setGeometry(QtCore.QRect(552, 90, 91, 23))
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(WaterCalibration)
        self.label_6.setGeometry(QtCore.QRect(552, 130, 91, 23))
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.IntervalRight = QtWidgets.QDoubleSpinBox(WaterCalibration)
        self.IntervalRight.setGeometry(QtCore.QRect(650, 130, 80, 20))
        self.IntervalRight.setDecimals(3)
        self.IntervalRight.setSingleStep(0.005)
        self.IntervalRight.setProperty("value", 0.5)
        self.IntervalRight.setObjectName("IntervalRight")
        self.label_7 = QtWidgets.QLabel(WaterCalibration)
        self.label_7.setGeometry(QtCore.QRect(163, 90, 71, 23))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(WaterCalibration)
        self.label_8.setGeometry(QtCore.QRect(165, 130, 71, 23))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.CycleLeft = QtWidgets.QLineEdit(WaterCalibration)
        self.CycleLeft.setGeometry(QtCore.QRect(240, 90, 80, 20))
        self.CycleLeft.setObjectName("CycleLeft")
        self.CycleRight = QtWidgets.QLineEdit(WaterCalibration)
        self.CycleRight.setGeometry(QtCore.QRect(240, 130, 80, 20))
        self.CycleRight.setObjectName("CycleRight")
        self.OpenLeft = QtWidgets.QPushButton(WaterCalibration)
        self.OpenLeft.setGeometry(QtCore.QRect(50, 90, 80, 23))
        self.OpenLeft.setCheckable(True)
        self.OpenLeft.setObjectName("OpenLeft")
        self.OpenRight = QtWidgets.QPushButton(WaterCalibration)
        self.OpenRight.setGeometry(QtCore.QRect(50, 130, 80, 23))
        self.OpenRight.setCheckable(True)
        self.OpenRight.setObjectName("OpenRight")
        self.OpenLeftForever = QtWidgets.QPushButton(WaterCalibration)
        self.OpenLeftForever.setGeometry(QtCore.QRect(49, 50, 121, 23))
        self.OpenLeftForever.setCheckable(True)
        self.OpenLeftForever.setObjectName("OpenLeftForever")
        self.OpenRightForever = QtWidgets.QPushButton(WaterCalibration)
        self.OpenRightForever.setGeometry(QtCore.QRect(200, 50, 121, 23))
        self.OpenRightForever.setCheckable(True)
        self.OpenRightForever.setObjectName("OpenRightForever")
        self.StartCalibratingLeft = QtWidgets.QPushButton(WaterCalibration)
        self.StartCalibratingLeft.setGeometry(QtCore.QRect(50, 290, 121, 31))
        self.StartCalibratingLeft.setCheckable(True)
        self.StartCalibratingLeft.setObjectName("StartCalibratingLeft")
        self.StartCalibratingRight = QtWidgets.QPushButton(WaterCalibration)
        self.StartCalibratingRight.setGeometry(QtCore.QRect(50, 332, 121, 31))
        self.StartCalibratingRight.setCheckable(True)
        self.StartCalibratingRight.setObjectName("StartCalibratingRight")
        self.Continue = QtWidgets.QPushButton(WaterCalibration)
        self.Continue.setGeometry(QtCore.QRect(220, 380, 121, 61))
        self.Continue.setCheckable(True)
        self.Continue.setObjectName("Continue")
        self.VisuCalibration = QtWidgets.QGroupBox(WaterCalibration)
        self.VisuCalibration.setGeometry(QtCore.QRect(30, 490, 1011, 291))
        self.VisuCalibration.setObjectName("VisuCalibration")
        self.showrecent = QtWidgets.QSpinBox(self.VisuCalibration)
        self.showrecent.setGeometry(QtCore.QRect(900, 20, 61, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showrecent.sizePolicy().hasHeightForWidth())
        self.showrecent.setSizePolicy(sizePolicy)
        self.showrecent.setMaximum(100000)
        self.showrecent.setProperty("value", 2)
        self.showrecent.setDisplayIntegerBase(10)
        self.showrecent.setObjectName("showrecent")
        self.label_69 = QtWidgets.QLabel(self.VisuCalibration)
        self.label_69.setGeometry(QtCore.QRect(775, 20, 121, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        self.label_69.setTextFormat(QtCore.Qt.AutoText)
        self.label_69.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.VisuCalibration)
        self.label_70.setGeometry(QtCore.QRect(500, 20, 141, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setTextFormat(QtCore.Qt.AutoText)
        self.label_70.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_70.setObjectName("label_70")
        self.showspecificcali = QtWidgets.QComboBox(self.VisuCalibration)
        self.showspecificcali.setGeometry(QtCore.QRect(650, 20, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showspecificcali.sizePolicy().hasHeightForWidth())
        self.showspecificcali.setSizePolicy(sizePolicy)
        self.showspecificcali.setObjectName("showspecificcali")
        self.showspecificcali.addItem("")
        self.label_9 = QtWidgets.QLabel(WaterCalibration)
        self.label_9.setGeometry(QtCore.QRect(190, 296, 71, 23))
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(WaterCalibration)
        self.label_10.setGeometry(QtCore.QRect(360, 296, 71, 23))
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(WaterCalibration)
        self.label_11.setGeometry(QtCore.QRect(530, 296, 71, 23))
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(WaterCalibration)
        self.label_12.setGeometry(QtCore.QRect(670, 296, 71, 23))
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(WaterCalibration)
        self.label_13.setGeometry(QtCore.QRect(35, 380, 91, 23))
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(WaterCalibration)
        self.label_14.setGeometry(QtCore.QRect(360, 336, 71, 23))
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(WaterCalibration)
        self.label_15.setGeometry(QtCore.QRect(190, 336, 71, 23))
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(WaterCalibration)
        self.label_16.setGeometry(QtCore.QRect(35, 420, 91, 23))
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(WaterCalibration)
        self.label_17.setGeometry(QtCore.QRect(670, 336, 71, 23))
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(WaterCalibration)
        self.label_18.setGeometry(QtCore.QRect(530, 336, 71, 23))
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.TimeLeftMin = QtWidgets.QLineEdit(WaterCalibration)
        self.TimeLeftMin.setGeometry(QtCore.QRect(266, 296, 80, 20))
        self.TimeLeftMin.setObjectName("TimeLeftMin")
        self.TimeRightMin = QtWidgets.QLineEdit(WaterCalibration)
        self.TimeRightMin.setGeometry(QtCore.QRect(266, 336, 80, 20))
        self.TimeRightMin.setObjectName("TimeRightMin")
        self.TimeLeftMax = QtWidgets.QLineEdit(WaterCalibration)
        self.TimeLeftMax.setGeometry(QtCore.QRect(436, 296, 80, 20))
        self.TimeLeftMax.setObjectName("TimeLeftMax")
        self.TimeRightMax = QtWidgets.QLineEdit(WaterCalibration)
        self.TimeRightMax.setGeometry(QtCore.QRect(436, 336, 80, 20))
        self.TimeRightMax.setObjectName("TimeRightMax")
        self.StrideLeft = QtWidgets.QLineEdit(WaterCalibration)
        self.StrideLeft.setGeometry(QtCore.QRect(605, 296, 80, 20))
        self.StrideLeft.setObjectName("StrideLeft")
        self.StrideRight = QtWidgets.QLineEdit(WaterCalibration)
        self.StrideRight.setGeometry(QtCore.QRect(605, 336, 80, 20))
        self.StrideRight.setObjectName("StrideRight")
        self.CycleCaliLeft = QtWidgets.QLineEdit(WaterCalibration)
        self.CycleCaliLeft.setGeometry(QtCore.QRect(746, 296, 80, 20))
        self.CycleCaliLeft.setObjectName("CycleCaliLeft")
        self.CycleCaliRight = QtWidgets.QLineEdit(WaterCalibration)
        self.CycleCaliRight.setGeometry(QtCore.QRect(746, 336, 80, 20))
        self.CycleCaliRight.setObjectName("CycleCaliRight")
        self.TotalWaterLeft = QtWidgets.QLineEdit(WaterCalibration)
        self.TotalWaterLeft.setGeometry(QtCore.QRect(130, 380, 80, 20))
        self.TotalWaterLeft.setText("")
        self.TotalWaterLeft.setObjectName("TotalWaterLeft")
        self.TotalWaterRight = QtWidgets.QLineEdit(WaterCalibration)
        self.TotalWaterRight.setGeometry(QtCore.QRect(130, 420, 80, 20))
        self.TotalWaterRight.setText("")
        self.TotalWaterRight.setObjectName("TotalWaterRight")
        self.Warning = QtWidgets.QLabel(WaterCalibration)
        self.Warning.setGeometry(QtCore.QRect(360, 384, 541, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Warning.sizePolicy().hasHeightForWidth())
        self.Warning.setSizePolicy(sizePolicy)
        self.Warning.setText("")
        self.Warning.setTextFormat(QtCore.Qt.AutoText)
        self.Warning.setScaledContents(False)
        self.Warning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Warning.setObjectName("Warning")
        self.label_19 = QtWidgets.QLabel(WaterCalibration)
        self.label_19.setGeometry(QtCore.QRect(755, 130, 91, 23))
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.TotalWaterSingleLeft = QtWidgets.QLineEdit(WaterCalibration)
        self.TotalWaterSingleLeft.setGeometry(QtCore.QRect(850, 90, 80, 20))
        self.TotalWaterSingleLeft.setText("")
        self.TotalWaterSingleLeft.setObjectName("TotalWaterSingleLeft")
        self.label_20 = QtWidgets.QLabel(WaterCalibration)
        self.label_20.setGeometry(QtCore.QRect(755, 90, 91, 23))
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.TotalWaterSingleRight = QtWidgets.QLineEdit(WaterCalibration)
        self.TotalWaterSingleRight.setGeometry(QtCore.QRect(850, 130, 80, 20))
        self.TotalWaterSingleRight.setText("")
        self.TotalWaterSingleRight.setObjectName("TotalWaterSingleRight")
        self.SaveLeft = QtWidgets.QPushButton(WaterCalibration)
        self.SaveLeft.setGeometry(QtCore.QRect(950, 90, 80, 23))
        self.SaveLeft.setCheckable(True)
        self.SaveLeft.setObjectName("SaveLeft")
        self.SaveRight = QtWidgets.QPushButton(WaterCalibration)
        self.SaveRight.setGeometry(QtCore.QRect(950, 130, 80, 23))
        self.SaveRight.setCheckable(True)
        self.SaveRight.setObjectName("SaveRight")
        self.label_21 = QtWidgets.QLabel(WaterCalibration)
        self.label_21.setGeometry(QtCore.QRect(50, 240, 91, 23))
        self.label_21.setTextFormat(QtCore.Qt.AutoText)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.CalibrationType = QtWidgets.QComboBox(WaterCalibration)
        self.CalibrationType.setGeometry(QtCore.QRect(150, 237, 91, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalibrationType.sizePolicy().hasHeightForWidth())
        self.CalibrationType.setSizePolicy(sizePolicy)
        self.CalibrationType.setObjectName("CalibrationType")
        self.CalibrationType.addItem("")
        self.CalibrationType.addItem("")
        self.label_22 = QtWidgets.QLabel(WaterCalibration)
        self.label_22.setGeometry(QtCore.QRect(852, 336, 91, 23))
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.IntervalRight_2 = QtWidgets.QDoubleSpinBox(WaterCalibration)
        self.IntervalRight_2.setGeometry(QtCore.QRect(950, 336, 80, 20))
        self.IntervalRight_2.setDecimals(3)
        self.IntervalRight_2.setSingleStep(0.005)
        self.IntervalRight_2.setProperty("value", 0.5)
        self.IntervalRight_2.setObjectName("IntervalRight_2")
        self.label_23 = QtWidgets.QLabel(WaterCalibration)
        self.label_23.setGeometry(QtCore.QRect(852, 296, 91, 23))
        self.label_23.setTextFormat(QtCore.Qt.AutoText)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.IntervalLeft_2 = QtWidgets.QDoubleSpinBox(WaterCalibration)
        self.IntervalLeft_2.setGeometry(QtCore.QRect(950, 296, 80, 20))
        self.IntervalLeft_2.setDecimals(3)
        self.IntervalLeft_2.setSingleStep(0.005)
        self.IntervalLeft_2.setProperty("value", 0.5)
        self.IntervalLeft_2.setObjectName("IntervalLeft_2")
        self.SaveCalibrationPar = QtWidgets.QPushButton(WaterCalibration)
        self.SaveCalibrationPar.setGeometry(QtCore.QRect(870, 240, 161, 31))
        self.SaveCalibrationPar.setCheckable(True)
        self.SaveCalibrationPar.setObjectName("SaveCalibrationPar")
        self.groupBox = QtWidgets.QGroupBox(WaterCalibration)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 1011, 161))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(WaterCalibration)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 210, 1011, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.EmergencyStop = QtWidgets.QPushButton(WaterCalibration)
        self.EmergencyStop.setGeometry(QtCore.QRect(910, 380, 121, 61))
        self.EmergencyStop.setCheckable(True)
        self.EmergencyStop.setObjectName("EmergencyStop")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.OpenRightTime.raise_()
        self.OpenLeftTime.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.IntervalLeft.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.IntervalRight.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.CycleLeft.raise_()
        self.CycleRight.raise_()
        self.OpenLeft.raise_()
        self.OpenRight.raise_()
        self.OpenLeftForever.raise_()
        self.OpenRightForever.raise_()
        self.StartCalibratingLeft.raise_()
        self.StartCalibratingRight.raise_()
        self.Continue.raise_()
        self.VisuCalibration.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.TimeLeftMin.raise_()
        self.TimeRightMin.raise_()
        self.TimeLeftMax.raise_()
        self.TimeRightMax.raise_()
        self.StrideLeft.raise_()
        self.StrideRight.raise_()
        self.CycleCaliLeft.raise_()
        self.CycleCaliRight.raise_()
        self.TotalWaterLeft.raise_()
        self.TotalWaterRight.raise_()
        self.Warning.raise_()
        self.label_19.raise_()
        self.TotalWaterSingleLeft.raise_()
        self.label_20.raise_()
        self.TotalWaterSingleRight.raise_()
        self.SaveLeft.raise_()
        self.SaveRight.raise_()
        self.label_21.raise_()
        self.CalibrationType.raise_()
        self.label_22.raise_()
        self.IntervalRight_2.raise_()
        self.label_23.raise_()
        self.IntervalLeft_2.raise_()
        self.SaveCalibrationPar.raise_()
        self.EmergencyStop.raise_()

        self.retranslateUi(WaterCalibration)
        QtCore.QMetaObject.connectSlotsByName(WaterCalibration)

    def retranslateUi(self, WaterCalibration):
        _translate = QtCore.QCoreApplication.translate
        WaterCalibration.setWindowTitle(_translate("WaterCalibration", "Water calibration"))
        self.label_3.setText(_translate("WaterCalibration", "Open left (s)="))
        self.label_4.setText(_translate("WaterCalibration", "Open right (s)="))
        self.label_5.setText(_translate("WaterCalibration", "Interval left (s)="))
        self.label_6.setText(_translate("WaterCalibration", "Interval right (s)="))
        self.label_7.setText(_translate("WaterCalibration", "Cycle left="))
        self.label_8.setText(_translate("WaterCalibration", "Cycle right="))
        self.CycleLeft.setText(_translate("WaterCalibration", "200"))
        self.CycleRight.setText(_translate("WaterCalibration", "200"))
        self.OpenLeft.setText(_translate("WaterCalibration", "Open left"))
        self.OpenRight.setText(_translate("WaterCalibration", "Open right"))
        self.OpenLeftForever.setText(_translate("WaterCalibration", "Keep left open"))
        self.OpenRightForever.setText(_translate("WaterCalibration", "Keep right open"))
        self.StartCalibratingLeft.setText(_translate("WaterCalibration", "Start calibrating left"))
        self.StartCalibratingRight.setText(_translate("WaterCalibration", "Start calibrating right"))
        self.Continue.setText(_translate("WaterCalibration", "Continue"))
        self.VisuCalibration.setTitle(_translate("WaterCalibration", "Last calibration date:"))
        self.label_69.setText(_translate("WaterCalibration", "show recent calibration="))
        self.label_70.setText(_translate("WaterCalibration", "show specific calibration="))
        self.showspecificcali.setItemText(0, _translate("WaterCalibration", "NA"))
        self.label_9.setText(_translate("WaterCalibration", "time min(s)="))
        self.label_10.setText(_translate("WaterCalibration", "time max(s)="))
        self.label_11.setText(_translate("WaterCalibration", "stride(s)="))
        self.label_12.setText(_translate("WaterCalibration", "cycle="))
        self.label_13.setText(_translate("WaterCalibration", "total water(mg)="))
        self.label_14.setText(_translate("WaterCalibration", "time max(s)="))
        self.label_15.setText(_translate("WaterCalibration", "time min(s)="))
        self.label_16.setText(_translate("WaterCalibration", "total water(mg)="))
        self.label_17.setText(_translate("WaterCalibration", "cycle="))
        self.label_18.setText(_translate("WaterCalibration", "stride(s)="))
        self.TimeLeftMin.setText(_translate("WaterCalibration", "0.005"))
        self.TimeRightMin.setText(_translate("WaterCalibration", "0.005"))
        self.TimeLeftMax.setText(_translate("WaterCalibration", "0.08"))
        self.TimeRightMax.setText(_translate("WaterCalibration", "0.08"))
        self.StrideLeft.setText(_translate("WaterCalibration", "0.005"))
        self.StrideRight.setText(_translate("WaterCalibration", "0.005"))
        self.CycleCaliLeft.setText(_translate("WaterCalibration", "200"))
        self.CycleCaliRight.setText(_translate("WaterCalibration", "200"))
        self.label_19.setText(_translate("WaterCalibration", "Total water(g)="))
        self.label_20.setText(_translate("WaterCalibration", "Total water(g)="))
        self.SaveLeft.setText(_translate("WaterCalibration", "Save"))
        self.SaveRight.setText(_translate("WaterCalibration", "Save"))
        self.label_21.setText(_translate("WaterCalibration", "Calibration type="))
        self.CalibrationType.setItemText(0, _translate("WaterCalibration", "Monthly"))
        self.CalibrationType.setItemText(1, _translate("WaterCalibration", "Biweekly"))
        self.label_22.setText(_translate("WaterCalibration", "interval right (s)="))
        self.label_23.setText(_translate("WaterCalibration", "interval left (s)="))
        self.SaveCalibrationPar.setText(_translate("WaterCalibration", "Save calibration parameters"))
        self.groupBox.setTitle(_translate("WaterCalibration", "Single value calibration"))
        self.groupBox_2.setTitle(_translate("WaterCalibration", "Multi-value calibration"))
        self.EmergencyStop.setText(_translate("WaterCalibration", "Emergency stop"))
