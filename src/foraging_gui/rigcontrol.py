import queue
from enum import Enum
from pyOSC3.OSC3 import OSCMessage
import numpy as np
class RigClient:
    def __init__(self, client):
        self.client = client
        self.client.addMsgHandler("default", self.msg_handler)
        self.msgs = queue.Queue(maxsize=0)

    def msg_handler(self, address, *args):
        msg = OSCMessage(address, args)
        CurrentMessage=[msg.address,args[1][0],msg.values()[2],msg.values()[3]]
        #self.msgs.put([CurrentMessage])
        self.msgs.put([msg,args])
        print(CurrentMessage)

    def send(self, address="", *args):
        message = OSCMessage(address, *args)
        return self.client.sendOSC(message)

    def receive(self):
        return self.msgs.get(block=True)
        #return self.msgs.get(block=False)
        #return self.msgs.get(block=True, timeout=None)
    
    def receive2(self):
        return self.msgs.get(block=False)
    
    def Left_Bait(self, value):
        self.send("/Left_Bait", value)
    
    def Right_Bait(self, value):
        self.send("/Right_Bait", value)

    def start(self, value):
        self.send("/start", value)

    def ITI(self, value):
        self.send("/ITI", value)

    def DelayTime(self, value):
        self.send("/DelayTime", value)

    def ResponseTime(self, value):
        self.send("/ResponseTime", value)
    
    def TriggerITIStart_Wave1(self, value):
        self.send("/TriggerITIStart_Wave1", value)

    def TriggerITIStart_Wave2(self, value):
        self.send("/TriggerITIStart_Wave2", value)
    
    def Trigger_Location1(self, value): # location 1
        self.send("/Trigger_Location1", value)

    def Trigger_Location2(self, value): # location 2
        self.send("/Trigger_Location2", value)

    def TriggerGoCue_Wave1(self, value): # location 1
        self.send("/TriggerGoCue_Wave1", value)

    def TriggerGoCue_Wave2(self, value): # location 2
        self.send("/TriggerGoCue_Wave2", value)

    # waveform 1, location 1
    def WaveForm1_1(self, value):
        #value=np.random.rand(2,441)
        self.send("/WaveForm1_1", value)
        #message = OSCMessage("/WaveForm1_1")
        #message.append(value.tobytes(),'b')
        #return self.client.sendOSC(message)
    # waveform 2, location 1
    def WaveForm2_1(self, value):
        #value=np.random.rand(1,441)
        self.send("/WaveForm2_1", value)
        #message = OSCMessage("/WaveForm2_1")
        #message.append(value.tobytes(),'b')
        #return self.client.sendOSC(message)

    # waveform 1, location 2
    def WaveForm1_2(self, value):
        #value=np.random.rand(1,441)
        self.send("/WaveForm1_2", value)
        
        #message = OSCMessage("/WaveForm1_2")
        #message.append(value.tobytes(),'b')
        #return self.client.sendOSC(message)

    # waveform 2, location 2
    def WaveForm2_2(self, value):
        #value=np.random.rand(2,441)
        self.send("/WaveForm2_2", value)
        
        #message = OSCMessage("/WaveForm2_2")
        #message.append(value.tobytes(),'b')
        #return self.client.sendOSC(message)

    def LeftValue(self, value):
        self.send("/LeftValueSize", value)

    def RightValue(self, value):
        self.send("/RightValueSize", value)

    def LeftValue1(self, value):
        self.send("/LeftValueSize1", value)

    def RightValue1(self, value):
        self.send("/RightValueSize1", value)

    def RewardConsumeTime(self, value):
        self.send("/RewardConsumeTime", value)

    def ManualWater_Left(self, value):
        self.send("/ManualWater_Left", value)
    
    def ManualWater_Right(self, value):
        self.send("/ManualWater_Right", value)

    def Location1_Size(self, value):
        self.send("/Location1Size", value)
    
    def Location2_Size(self, value):
        self.send("/Location2Size", value)

    def TriggerSource(self, value):
        self.send("/TriggerSource", value)

    def OptogeneticsCalibration(self, value):
        self.send("/OptogeneticsCalibration", value)
        
    def CameraControl(self, value):
        self.send("/cameracontrol", value)    

    def CameraFrequency(self, value):
        self.send("/camerafrequency", value)

    def SideCameraFile(self, value):
        # save file name of the SideCamera
        self.send("/sidecamerafile", value)    
    
    def BottomCameraFile(self, value):
        # save file name of the BottomCamera
        self.send("/bottomcamerafile", value) 

    def SideCameraCSV(self, value):
        # save file name of the SideCamera csv
        self.send("/sidecameracsv", value)

    def BottomCameraCSV(self, value):
        # save file name of the BottomCamera csv
        self.send("/bottomcameracsv", value) 

    def StopLogging(self,value):
        # stop the logging
        self.send("/stoplogging", value) 

    def StartLogging(self,value):
        # start the logging
        self.send("/startlogging", value) 