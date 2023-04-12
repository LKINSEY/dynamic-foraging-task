
import random, traceback, math,time
import numpy as np
from itertools import accumulate
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
class GenerateTrials():
    def __init__(self,win):
        self.win=win
        self.B_RewardFamilies=self.win.RewardFamilies
        #self.B_RewardFamilies = [[[float(x) for x in y] for y in z] for z in self.B_RewardFamilies]
        #self.B_RewardFamilies = np.array(self.B_RewardFamilies)
        self.B_CurrentTrialN=0
        self.B_LickPortN=2
        self.B_ANewBlock=np.array([1,1]).astype(int)
        self.B_RewardProHistory=np.array([[],[]]).astype(int)
        self.BlockLenHistory=[[],[]]
        self.B_BaitHistory=np.array([[],[]]).astype(bool)
        self.B_ITIHistory=[]
        self.B_DelayHistory=[]
        self.B_ResponseTimeHistory=[]
        self.B_CurrentRewardProb=np.empty((2,))
        self.B_AnimalCurrentResponse=[]
        self.B_AnimalResponseHistory=np.array([]).astype(float) # 0 lick left; 1 lick right; 2 no response
        self.B_Baited=np.array([False,False]).astype(bool)
        self.B_CurrentRewarded=np.array([[False],[False]]).astype(bool) # whether to receive reward
        self.B_RewardedHistory=np.array([[],[]]).astype(bool)
        self.B_Time=[]
        self.B_LeftLickTime=np.array([]).astype(float)
        self.B_RightLickTime=np.array([]).astype(float)
        self.B_TrialStartTime=np.array([]).astype(float)
        self.B_DelayStartTime=np.array([]).astype(float)
        self.B_TrialEndTime=np.array([]).astype(float)
        self.B_GoCueTime=np.array([]).astype(float)
        self.B_LeftRewardDeliveryTime=np.array([]).astype(float)
        self.B_RightRewardDeliveryTime=np.array([]).astype(float)
        self.B_RewardOutcomeTime=np.array([]).astype(float)
        self.B_LaserOnTrial=[] # trials with laser on
        self.B_LaserAmplitude=[]
        self.B_LaserDuration=[]
        self.B_SelectedCondition=[]
        self.B_AutoWaterTrial=[] # to indicate if it is a trial with outo water.
        self.NextWaveForm=1 # waveform stored for later use
        self.CurrentWaveForm=1 # the current waveform to trigger the optogenetics
        #self.B_LaserTrialNum=[] # B_LaserAmplitude, B_LaserDuration, B_SelectedCondition have values only on laser on trials, so we need to store the laser trial number
        
        self.Obj={}
        # get all of the training parameters of the current trial
        self._GetTrainingParameters(self.win)
    def _GenerateATrial(self,Channel4):
        # get all of the training parameters of the current trial
        self._GetTrainingParameters(self.win)
        # save all of the parameters in each trial
        self._SaveParameters()
        self.RewardPairs=self.B_RewardFamilies[int(self.TP_RewardFamily)-1][:int(self.TP_RewardPairsN)]
        self.RewardProb=np.array(self.RewardPairs)/np.expand_dims(np.sum(self.RewardPairs,axis=1),axis=1)*float(self.TP_BaseRewardSum)
        # determine the reward probability of the next trial based on tasks
        if (self.TP_Task in ['Coupled Baiting','Coupled Without Baiting']) and any(self.B_ANewBlock==1):
            # get the reward probabilities pool
            RewardProbPool=np.append(self.RewardProb,np.fliplr(self.RewardProb),axis=0)
            # exclude the previous reward probabilities
            if self.B_RewardProHistory.size!=0:
                RewardProbPool=RewardProbPool[RewardProbPool!=self.B_RewardProHistory[:,-1]]
                RewardProbPool=RewardProbPool.reshape(int(RewardProbPool.size/self.B_LickPortN),self.B_LickPortN)
            # get the reward probabilities of the current block
            self.B_CurrentRewardProb=RewardProbPool[random.choice(range(np.shape(RewardProbPool)[0]))]
            # randomly draw a block length between Min and Max
            self.BlockLen = np.array(int(np.random.exponential(float(self.TP_BlockBeta),1)+float(self.TP_BlockMin)))
            if self.BlockLen>float(self.TP_BlockMax):
                self.BlockLen=int(self.TP_BlockMax)
            for i in range(len(self.B_ANewBlock)):
                self.BlockLenHistory[i].append(self.BlockLen)
            self.B_ANewBlock=np.array([0,0])
        elif (self.TP_Task in ['Uncoupled Baiting','Uncoupled Without Baiting'])  and any(self.B_ANewBlock==1):
            # get the reward probabilities pool
            for i in range(len(self.B_ANewBlock)):
                if self.B_ANewBlock[i]==1:
                    #RewardProbPool=np.append(self.RewardProb,np.fliplr(self.RewardProb),axis=0)
                    #RewardProbPool=RewardProbPool[:,i]
                    string=self.win.UncoupledReward.text()
                    if '[' in string and ']' in string:
                        if ',' in string:
                            # string format is '[0.1, 0.3, 0.7]'
                            RewardProbPool = np.fromstring(string.strip('[]'), sep=',')
                        else:
                            # string format is '[0.1 0.3 0.7]'
                            RewardProbPool = np.fromstring(string.strip('[]'), sep=' ')
                    elif ',' in string:
                        # string format is '0.1,0.3,0.7'
                        RewardProbPool = np.fromstring(string, sep=',')
                    elif ' ' in string:
                        # string format is '0.1 0.3 0.7'
                        RewardProbPool = np.fromstring(string, sep=' ')
                    else:
                        print("Invalid string format")
                    self.RewardProbPoolUncoupled=RewardProbPool.copy()
                    # exclude the previous reward probabilities
                    if self.B_RewardProHistory.size!=0:
                        RewardProbPool=RewardProbPool[RewardProbPool!=self.B_RewardProHistory[i,-1]]
                    # get the reward probabilities of the current block
                    self.B_CurrentRewardProb[i]=RewardProbPool[random.choice(range(np.shape(RewardProbPool)[0]))]
                    # randomly draw a block length between Min and Max
                    self.BlockLen = np.array(int(np.random.exponential(float(self.TP_BlockBeta),1)+float(self.TP_BlockMin)))
                    if self.BlockLen>float(self.TP_BlockMax):
                        self.BlockLen=int(self.TP_BlockMax)
                    self.BlockLenHistory[i].append(self.BlockLen)
                    self.B_ANewBlock[i]=0
        self.B_RewardProHistory=np.append(self.B_RewardProHistory,self.B_CurrentRewardProb.reshape(self.B_LickPortN,1),axis=1)
        # show reward pairs and current reward probability
        try:
            if (self.TP_Task in ['Coupled Baiting','Coupled Without Baiting']):
                self.win.ShowRewardPairs.setText('Reward pairs: '+str(np.round(self.RewardProb,2))+'\n\n'+'Current pair: '+str(np.round(self.B_CurrentRewardProb,2)))
            elif (self.TP_Task in ['Uncoupled Baiting','Uncoupled Without Baiting']):
                self.win.ShowRewardPairs.setText('Reward pairs: '+str(np.round(self.RewardProbPoolUncoupled,2))+'\n\n'+'Current pair: '+str(np.round(self.B_CurrentRewardProb,2)))
        except:
            print('Can not show reward pairs')
        # decide if block transition will happen at the next trial
        for i in range(len(self.B_ANewBlock)):
            if self.B_CurrentTrialN>=sum(self.BlockLenHistory[i]):
                self.B_ANewBlock[i]=1
        # transition to the next block when NextBlock button is clicked
        if self.TP_NextBlock:
            self.B_ANewBlock[:]=1
            self.win.NextBlock.setChecked(False)
            self.win.NextBlock.setStyleSheet("background-color : none")
        # to decide if it's a auto water trial
        self._CheckAutoWater()
        # to decide if we should stop the session
        self._CheckStop()
        # get the ITI time and delay time
        self.CurrentITI = float(np.random.exponential(float(self.TP_ITIBeta),1)+float(self.TP_ITIMin))
        if self.CurrentITI>float(self.TP_ITIMax):
            self.CurrentITI=float(self.TP_ITIMax)
        self.CurrentDelay = float(np.random.exponential(float(self.TP_DelayBeta),1)+float(self.TP_DelayMin))
        if self.CurrentDelay>float(self.TP_DelayMax):
            self.CurrentDelay=float(self.TP_DelayMax)
        self.B_ITIHistory.append(self.CurrentITI)
        self.B_DelayHistory.append(self.CurrentDelay)
        self.B_ResponseTimeHistory.append(float(self.TP_ResponseTime))
        # optogenetics section
        try:
            if self.TP_OptogeneticsB=='on': # optogenetics is turned on
                # select the current optogenetics condition
                self._SelectOptogeneticsCondition()
                if self.SelctedCondition!=0: 
                    self.LaserOn=1
                    self.B_LaserOnTrial.append(self.LaserOn) 
                    # generate the optogenetics waveform of the next trial
                    self._GetLaserWaveForm()
                    # send the waveform to Bonsai temporarily stored for using in the next trial
                    #WaveForm_Number_Location
                    for i in range(len(self.CurrentLaserAmplitude)): # locations of these waveforms
                        if self.CurrentLaserAmplitude[i]!=0:
                            #eval('Channel4.WaveForm' + str(self.NextWaveForm)+'_'+str(i+1)+'(np.array('+'self.WaveFormLocation_'+str(i+1)+',\'b\''+'))')
                            #eval('Channel4.WaveForm' + str(self.NextWaveForm)+'_'+str(i+1)+'('+'self.WaveFormLocation_'+str(i+1)+')')
                            eval('Channel4.WaveForm' + str(self.NextWaveForm)+'_'+str(i+1)+'('+'str('+'self.WaveFormLocation_'+str(i+1)+'.tolist()'+')[1:-1]'+')')
                            #FinishOfWaveForm=Channel4.receive()
                            setattr(self, f"Location{i+1}_Size", getattr(self, f"WaveFormLocation_{i+1}").size)
                        else:
                            setattr(self, f"Location{i+1}_Size", 100) # arbitrary number 
                            
                    if self.NextWaveForm==1:
                        self.NextWaveForm=2
                    elif self.NextWaveForm==2:
                        self.NextWaveForm=1
                    # finish of this sectiom
                else:
                    # this is the control trial
                    self.LaserOn=0
                    self.B_LaserOnTrial.append(self.LaserOn) 
                    self.B_LaserAmplitude.append([0,0])
                    self.B_LaserDuration.append(0)
                    self.B_SelectedCondition.append(0)
                    self.CurrentLaserAmplitude=[0,0]
            else:
                # optogenetics is turned off
                self.LaserOn=0
                self.B_LaserOnTrial.append(self.LaserOn)
                self.B_LaserAmplitude.append([0,0])
                self.B_LaserDuration.append(0)
                self.B_SelectedCondition.append(0)
                self.CurrentLaserAmplitude=[0,0]
        except Exception as e:
            # optogenetics is turned off
            self.LaserOn=0
            self.B_LaserOnTrial.append(self.LaserOn)
            self.B_LaserAmplitude.append([0,0]) # corresponding to two locations
            self.B_LaserDuration.append(0) # corresponding to two locations
            self.B_SelectedCondition.append(0)
            self.CurrentLaserAmplitude=[0,0]
            # Catch the exception and print error information
            print("An error occurred:")
            print(traceback.format_exc())
        self.GeneFinish=1
    
    def _CheckStop(self):
        StopIgnore=int(self.win.StopIgnores.text())
        if np.shape(self.B_AnimalResponseHistory)[0]>=StopIgnore:
            if np.all(self.B_AnimalResponseHistory[-StopIgnore:]==2):
                self.Stop=1
                self.win.Start.setStyleSheet("background-color : none")
                self.win.Start.setChecked(False)
            else:
                self.Stop=0
        else:
            self.Stop=0
    def _CheckAutoWater(self):
        '''Check if it should be an auto water trial'''
        if self.win.AutoReward.isChecked:
            UnrewardedN=int(self.win.Unrewarded.text())
            IgnoredN=int(self.win.Ignored.text())
            if np.shape(self.B_AnimalResponseHistory)[0]>=IgnoredN or np.shape(self.B_RewardedHistory[0])[0]>=UnrewardedN:
                if np.all(self.B_AnimalResponseHistory[-IgnoredN:]==2) or (np.all(self.B_RewardedHistory[0][-UnrewardedN:]==False) and np.all(self.B_RewardedHistory[1][-UnrewardedN:]==False)):
                    self.CurrentAutoReward=1
                else:
                    self.CurrentAutoReward=0
            else:
                self.CurrentAutoReward=0
        else:
            self.CurrentAutoReward=0
        self.B_AutoWaterTrial.append(self.CurrentAutoReward)
    def _GetLaserWaveForm(self):
        '''Get the waveform of the laser. It dependens on color/duration/protocol(frequency/RD/pulse duration)/locations/laser power'''
        N=self.SelctedCondition
        # CLP, current laser parameter
        self.CLP_Color=eval('self.TP_Laser_'+N)
        self.CLP_Location=eval('self.TP_Location_'+N)
        self.CLP_LaserPower=eval('self.TP_LaserPower_'+N)
        self.CLP_Duration=float(eval('self.TP_Duration_'+N))
        self.CLP_Protocol=eval('self.TP_Protocol_'+N)
        self.CLP_Frequency=float(eval('self.TP_Frequency_'+N))
        self.CLP_RampingDown=float(eval('self.TP_RD_'+N))
        self.CLP_PulseDur=eval('self.TP_PulseDur_'+N)
        self.CLP_LaserStart=eval('self.TP_LaserStart_'+N)
        self.CLP_OffsetStart=float(eval('self.TP_OffsetStart_'+N))
        self.CLP_LaserEnd=eval('self.TP_LaserEnd_'+N)
        self.CLP_OffsetEnd=float(eval('self.TP_OffsetEnd_'+N)) # negative, backward; positive forward
        self.CLP_SampleFrequency=float(self.TP_SampleFrequency)
        # align to trial start
        if (self.CLP_LaserStart=='Trial start' or self.CLP_LaserStart=='Go cue') and self.CLP_LaserEnd=='NA':
            # the duration is determined by Duration
            self.CLP_CurrentDuration=self.CLP_Duration
        elif self.CLP_LaserStart=='Trial start' and self.CLP_LaserEnd=='Go cue':
            # the duration is determined by CurrentITI, CurrentDelay, self.CLP_OffsetStart, self.CLP_OffsetEnd
            # only positive CLP_OffsetStart is allowed
            if self.CLP_OffsetStart<0:
                self.win.WarningLabel.setText('Please set offset start to be positive!')
                self.win.WarningLabel.setStyleSheet("color: red;")
            self.CLP_CurrentDuration=self.CurrentITI+self.CurrentDelay-self.CLP_OffsetStart+self.CLP_OffsetEnd
        elif self.CLP_LaserStart=='Go cue' and self.CLP_LaserEnd=='Trial start':
            # The duration is inaccurate as it doesn't account for time outside of bonsai (can be solved in Bonsai)
            # the duration is determined by TP_ResponseTime, self.CLP_OffsetStart, self.CLP_OffsetEnd
            self.CLP_CurrentDuration=float(self.TP_ResponseTime)-self.CLP_OffsetStart+self.CLP_OffsetEnd
        else:
            pass
        self.B_LaserDuration.append(self.CLP_CurrentDuration)
        # generate the waveform based on self.CLP_CurrentDuration and Protocol, Frequency, RampingDown, PulseDur
        self._GetLaserAmplitude()
        # dimension of self.CurrentLaserAmplitude indicates how many locations do we have
        for i in range(len(self.CurrentLaserAmplitude)):
            if self.CurrentLaserAmplitude[i]!=0:
                # in some cases the other paramters except the amplitude could also be different
                self._ProduceWaveForm(self.CurrentLaserAmplitude[i])
                setattr(self, 'WaveFormLocation_' + str(i+1), self.my_wave)

    def _ProduceWaveForm(self,Amplitude):
        '''generate the waveform based on Duration and Protocol, Laser Power, Frequency, RampingDown, PulseDur and the sample frequency'''
        if self.CLP_Protocol=='Sine':
            resolution=self.CLP_SampleFrequency*self.CLP_CurrentDuration # how many datapoints to generate
            cycles=self.CLP_CurrentDuration*self.CLP_Frequency # how many sine cycles
            length = np.pi * 2 * cycles
            self.my_wave = Amplitude*(1+np.sin(np.arange(0+1.5*math.pi, length+1.5*math.pi, length / resolution)))/2
            # add ramping down
            if self.CLP_RampingDown>0:
                if self.CLP_RampingDown>self.CLP_CurrentDuration:
                    self.win.WarningLabel.setText('Ramping down is longer than the laser duration!')
                    self.win.WarningLabel.setStyleSheet("color: red;")
                else:
                    Constant=np.ones(int((self.CLP_CurrentDuration-self.CLP_RampingDown)*self.CLP_SampleFrequency))
                    RD=np.arange(1,0, -1/(np.shape(self.my_wave)[0]-np.shape(Constant)[0]))
                    RampingDown = np.concatenate((Constant, RD), axis=0)
                    self.my_wave=self.my_wave*RampingDown
            # add offset
            if self.CLP_OffsetStart>0:
                OffsetPoints=int(self.CLP_SampleFrequency*self.CLP_OffsetStart)
                Offset=np.zeros(OffsetPoints)
                self.my_wave=np.concatenate((Offset,self.my_wave),axis=0)
            self.my_wave=np.append(self.my_wave,[0,0])

        elif self.CLP_Protocol=='Pulse':
            if self.CLP_PulseDur=='NA':
                self.win.WarningLabel.setText('Pulse duration is NA!')
                self.win.WarningLabel.setStyleSheet("color: red;")
            else:
                self.CLP_PulseDur=float(self.CLP_PulseDur)
                PointsEachPulse=int(self.CLP_SampleFrequency*self.CLP_PulseDur)
                PulseIntervalPoints=int(1/self.CLP_Frequency*self.CLP_SampleFrequency-PointsEachPulse)
                if PulseIntervalPoints<0:
                    self.win.WarningLabel.setText('Pulse frequency and pulse duration are not compatible!')
                    self.win.WarningLabel.setStyleSheet("color: red;")
                TotalPoints=int(self.CLP_SampleFrequency*self.CLP_CurrentDuration)
                PulseNumber=np.floor(self.CLP_CurrentDuration*self.CLP_Frequency) 
                EachPulse=Amplitude*np.ones(PointsEachPulse)
                PulseInterval=np.zeros(PulseIntervalPoints)
                WaveFormEachCycle=np.concatenate((EachPulse, PulseInterval), axis=0)
                self.my_wave=np.empty(0)
                # pulse number should be greater than 0
                if PulseNumber>1:
                    for i in range(int(PulseNumber-1)):
                        self.my_wave=np.concatenate((self.my_wave, WaveFormEachCycle), axis=0)
                else:
                    self.win.WarningLabel.setText('Pulse number is less than 1!')
                    self.win.WarningLabel.setStyleSheet("color: red;")
                    return
                self.my_wave=np.concatenate((self.my_wave, EachPulse), axis=0)
                self.my_wave=np.concatenate((self.my_wave, np.zeros(TotalPoints-np.shape(self.my_wave)[0])), axis=0)
                # add offset
                if self.CLP_OffsetStart>0:
                    OffsetPoints=int(self.CLP_SampleFrequency*self.CLP_OffsetStart)
                    Offset=np.zeros(OffsetPoints)
                    self.my_wave=np.concatenate((Offset,self.my_wave),axis=0)
                self.my_wave=np.append(self.my_wave,[0,0])
        elif self.CLP_Protocol=='Constant':
            resolution=self.CLP_SampleFrequency*self.CLP_CurrentDuration # how many datapoints to generate
            self.my_wave=Amplitude*np.ones(int(resolution))
            if self.CLP_RampingDown>0:
            # add ramping down
                if self.CLP_RampingDown>self.CLP_CurrentDuration:
                    self.win.WarningLabel.setText('Ramping down is longer than the laser duration!')
                    self.win.WarningLabel.setStyleSheet("color: red;")
                else:
                    Constant=np.ones(int((self.CLP_CurrentDuration-self.CLP_RampingDown)*self.CLP_SampleFrequency))
                    RD=np.arange(1,0, -1/(np.shape(self.my_wave)[0]-np.shape(Constant)[0]))
                    RampingDown = np.concatenate((Constant, RD), axis=0)
                    self.my_wave=self.my_wave*RampingDown
            # add offset
            if self.CLP_OffsetStart>0:
                OffsetPoints=int(self.CLP_SampleFrequency*self.CLP_OffsetStart)
                Offset=np.zeros(OffsetPoints)
                self.my_wave=np.concatenate((Offset,self.my_wave),axis=0)
            self.my_wave=np.append(self.my_wave,[0,0])
        else:
            self.win.WarningLabel.setText('Unidentified optogenetics protocol!')
            self.win.WarningLabel.setStyleSheet("color: red;")

        '''
        # test
        import matplotlib.pyplot as plt
        plt.plot(np.arange(0, length, length / resolution), self.my_wave)   
        plt.show()
        '''
    def _GetLaserAmplitude(self):
        '''the voltage amplitude dependens on Protocol, Laser Power, Laser color, and the stimulation locations<>'''
        if self.CLP_Location=='Left':
            self.CurrentLaserAmplitude=[5,0]
        elif self.CLP_Location=='Right':
            self.CurrentLaserAmplitude=[0,5]
        elif self.CLP_Location=='Both':
            self.CurrentLaserAmplitude=[5,5]
        else:
            self.win.WarningLabel.setText('No stimulation location defined!')
            self.win.WarningLabel.setStyleSheet("color: red;")
        self.B_LaserAmplitude.append(self.CurrentLaserAmplitude)

    def _SelectOptogeneticsCondition(self):
        '''To decide if this should be an optogenetics trial'''
        # condition should be taken into account in the future
        ConditionsOn=[]
        Probabilities=[]
        for attr_name in dir(self):
            if attr_name.startswith('TP_Laser_'):
                if getattr(self, attr_name) !='NA':
                    parts = attr_name.split('_')
                    ConditionsOn.append(parts[-1])
                    Probabilities.append(float(eval('self.TP_Probability_'+parts[-1])))
        self.ConditionsOn=ConditionsOn
        self.Probabilities=Probabilities
        ProAccu=list(accumulate(Probabilities))
        b=random.uniform(0,1)
        for i in range(len(ProAccu)):
            if b <= ProAccu[i]:
                self.SelctedCondition=self.ConditionsOn[i]
                break
            else:
                self.SelctedCondition=0 # control is selected
        self.B_SelectedCondition.append(self.SelctedCondition)

    def _InitiateATrial(self,Channel1,Channel4):
        # Determine if the current lick port should be baited. self.B_Baited can only be updated after receiving response of the animal, so this part cannot appear in the _GenerateATrial section
        self.CurrentBait=self.B_CurrentRewardProb>np.random.random(2)
        if (self.TP_Task in ['Coupled Baiting','Uncoupled Baiting']):
             self.CurrentBait= self.CurrentBait | self.B_Baited
        self.B_Baited=  self.CurrentBait.copy()
        self.B_BaitHistory=np.append(self.B_BaitHistory, self.CurrentBait.reshape(2,1),axis=1)

        # if this is an optogenetics trial
        if self.B_LaserOnTrial[self.B_CurrentTrialN]==1:
            if self.CurrentWaveForm==1:
                # permit triggering waveform 1 after an event
                # waveform start event
                if self.CLP_LaserStart=='Trial start':
                    Channel1.TriggerITIStart_Wave1(int(1))
                    Channel1.TriggerITIStart_Wave2(int(0))
                    Channel1.TriggerGoCue_Wave1(int(0))
                    Channel1.TriggerGoCue_Wave2(int(0))
                elif self.CLP_LaserStart=='Go cue':
                    Channel1.TriggerGoCue_Wave1(int(1))
                    Channel1.TriggerGoCue_Wave2(int(0))
                    Channel1.TriggerITIStart_Wave1(int(0))
                    Channel1.TriggerITIStart_Wave2(int(0))
                else:
                    self.win.WarningLabel.setText('Unindentified optogenetics start event!')
                    self.win.WarningLabel.setStyleSheet("color: red;")
            elif self.CurrentWaveForm==2:
                # permit triggering waveform 2 after an event
                # waveform start event
                if self.CLP_LaserStart=='Trial start':
                    Channel1.TriggerITIStart_Wave1(int(0))
                    Channel1.TriggerITIStart_Wave2(int(1))
                    Channel1.TriggerGoCue_Wave1(int(0))
                    Channel1.TriggerGoCue_Wave2(int(0))
                elif self.CLP_LaserStart=='Go cue':
                    Channel1.TriggerGoCue_Wave1(int(0))
                    Channel1.TriggerGoCue_Wave2(int(1))
                    Channel1.TriggerITIStart_Wave1(int(0))
                    Channel1.TriggerITIStart_Wave2(int(0))
                else:
                    self.win.WarningLabel.setText('Unindentified optogenetics start event!')
                    self.win.WarningLabel.setStyleSheet("color: red;")
            # location of optogenetics
            # dimension of self.CurrentLaserAmplitude indicates how many locations do we have
            for i in range(len(self.CurrentLaserAmplitude)):
                if self.CurrentLaserAmplitude[i]!=0:
                    eval('Channel1.Trigger_Location'+str(i+1)+'(int(1))')
                else:
                    eval('Channel1.Trigger_Location'+str(i+1)+'(int(0))')
            # send the waveform size
            Channel1.Location1_Size(int(self.Location1_Size))
            Channel1.Location2_Size(int(self.Location2_Size))
            # change the position of the CurrentWaveForm and the NextWaveForm 
            self.CurrentWaveForm=self.NextWaveForm
        else:
            # 'Do not trigger the waveform'
            Channel1.TriggerGoCue_Wave1(int(0))
            Channel1.TriggerGoCue_Wave2(int(0))
            Channel1.TriggerITIStart_Wave1(int(0))
            Channel1.TriggerITIStart_Wave2(int(0))
            for i in range(len(self.CurrentLaserAmplitude)):
                eval('Channel1.Trigger_Location'+str(i+1)+'(int(0))')
            Channel1.Location1_Size(int(5000))
            Channel1.Location2_Size(int(5000))
        
        Channel1.LeftValue(float(self.TP_LeftValue)*1000)
        Channel1.RightValue(float(self.TP_RightValue)*1000)
        Channel1.RewardConsumeTime(float(self.TP_RewardConsumeTime))
        Channel1.Left_Bait(int(self.CurrentBait[0]))
        Channel1.Right_Bait(int(self.CurrentBait[1]))
        Channel1.ITI(float(self.CurrentITI))
        Channel1.DelayTime(float(self.CurrentDelay))
        Channel1.ResponseTime(float(self.TP_ResponseTime))
        Channel1.start(1)


    def _GetAnimalResponse(self,Channel1,Channel3):
        '''
        # random forager
        self.B_AnimalCurrentResponse=random.choice(range(2))
        # win stay, lose switch forager
        if self.B_CurrentTrialN>=2:
            if any(self.B_RewardedHistory[:,-1]==1):# win
                self.B_AnimalCurrentResponse=self.B_AnimalResponseHistory[-1]
            elif any(self.B_RewardedHistory[:,-1]==0) and self.B_AnimalResponseHistory[-1]!=2:# lose
                self.B_AnimalCurrentResponse=1-self.B_AnimalResponseHistory[-1]
            else: # no response
                self.B_AnimalCurrentResponse=random.choice(range(2))

        if np.random.random(1)<0.1: # no response
            self.B_AnimalCurrentResponse=2
        '''

        for i in range(6):
            Rec=Channel1.receive()
            if Rec.address=='/TrialStartTime':
                TrialStartTime=Rec[1]
            elif Rec.address=='/DelayStartTime':
                DelayStartTime=Rec[1]
            elif Rec.address=='/GoCueTime':
                # give auto water after Co cue
                if self.CurrentAutoReward==1:
                    self._GiveLeft()
                    self._GiveRight()
                self.B_GoCueTime=np.append(self.B_GoCueTime,Rec[1])
            elif Rec.address=='/RewardOutcomeTime':
                RewardOutcomeTime=Rec[1]
            elif Rec.address=='/RewardOutcome':
                TrialOutcome=Rec[1]
                if TrialOutcome=='NoResponse':
                    self.B_AnimalCurrentResponse=2
                    self.B_CurrentRewarded[0]=False
                    self.B_CurrentRewarded[1]=False
                elif TrialOutcome=='RewardLeft':
                    self.B_AnimalCurrentResponse=0
                    self.B_Baited[0]=False
                    self.B_CurrentRewarded[1]=False
                    self.B_CurrentRewarded[0]=True  
                elif TrialOutcome=='ErrorLeft':
                    self.B_AnimalCurrentResponse=0
                    self.B_Baited[0]=False
                    self.B_CurrentRewarded[0]=False
                    self.B_CurrentRewarded[1]=False
                elif TrialOutcome=='RewardRight':
                    self.B_AnimalCurrentResponse=1
                    self.B_Baited[1]=False
                    self.B_CurrentRewarded[0]=False
                    self.B_CurrentRewarded[1]=True
                elif TrialOutcome=='ErrorRight':
                    self.B_AnimalCurrentResponse=1
                    self.B_Baited[1]=False
                    self.B_CurrentRewarded[0]=False
                    self.B_CurrentRewarded[1]=False
                self.B_RewardedHistory=np.append(self.B_RewardedHistory,self.B_CurrentRewarded,axis=1)
                self.B_AnimalResponseHistory=np.append(self.B_AnimalResponseHistory,self.B_AnimalCurrentResponse)
            elif Rec.address=='/TrialEndTime':
                TrialEndTime=Rec[1]

        # get the trial end time at the end of the trial
        self.B_TrialStartTime=np.append(self.B_TrialStartTime,TrialStartTime)
        self.B_DelayStartTime=np.append(self.B_DelayStartTime,DelayStartTime)
        self.B_TrialEndTime=np.append(self.B_TrialEndTime,TrialEndTime)
        self.B_RewardOutcomeTime=np.append(self.B_RewardOutcomeTime,RewardOutcomeTime)
        self.B_CurrentTrialN+=1
    
    def _GiveLeft(self):
        '''manually give left water'''
        self.win.Channel.LeftValue(float(self.win.LeftValue.text())*1000*float(self.win.Multiplier.text())) 
        self.win.Channel3.ManualWater_Left(int(1))
        self.win.Channel.LeftValue(float(self.win.LeftValue.text())*1000)

    def _GiveRight(self):
        '''manually give right water'''
        self.win.Channel.RightValue(float(self.win.RightValue.text())*1000*float(self.win.Multiplier.text()))
        self.win.Channel3.ManualWater_Right(int(1))
        self.win.Channel.RightValue(float(self.win.RightValue.text())*1000)

    def _GetLicks(self,Channel2):
        '''Get licks and reward delivery time'''
        #while self.win.Start.isChecked():
        #    time.sleep(0.01)
        while not Channel2.msgs.empty():
            Rec=Channel2.receive()
            if Rec.address=='/LeftLickTime':
                self.B_LeftLickTime=np.append(self.B_LeftLickTime,Rec[1])
            elif Rec.address=='/RightLickTime':
                self.B_RightLickTime=np.append(self.B_RightLickTime,Rec[1])
            elif Rec.address=='/LeftRewardDeliveryTime':
                self.B_LeftRewardDeliveryTime=np.append(self.B_LeftRewardDeliveryTime,Rec[1])
            elif Rec.address=='/RightRewardDeliveryTime':
                self.B_RightRewardDeliveryTime=np.append(self.B_RightRewardDeliveryTime,Rec[1])
    def _DeletePreviousLicks(self,Channel2):
        '''Delete licks from the previous session'''
        while not Channel2.msgs.empty():
            Rec=Channel2.receive()
    # get training parameters
    def _GetTrainingParameters(self,win):
        '''Get training parameters'''
        # Iterate over each container to find child widgets and store their values in self
        for container in [win.TrainingParameters, win.centralwidget, win.Opto_dialog]:
            # Iterate over each child of the container that is a QLineEdit or QDoubleSpinBox
            for child in container.findChildren((QtWidgets.QLineEdit, QtWidgets.QDoubleSpinBox)):
                # Set an attribute in self with the name 'TP_' followed by the child's object name
                # and store the child's text value
                setattr(self, 'TP_'+child.objectName(), child.text())
            # Iterate over each child of the container that is a QComboBox
            for child in container.findChildren(QtWidgets.QComboBox):
                # Set an attribute in self with the name 'TP_' followed by the child's object name
                # and store the child's current text value
                setattr(self, 'TP_'+child.objectName(), child.currentText())
            # Iterate over each child of the container that is a QPushButton
            for child in container.findChildren(QtWidgets.QPushButton):
                # Set an attribute in self with the name 'TP_' followed by the child's object name
                # and store whether the child is checked or not
                setattr(self, 'TP_'+child.objectName(), child.isChecked())

    def _SaveParameters(self):
         for attr_name in dir(self):
                if attr_name.startswith('TP_'):
                    # Add the field to the dictionary with the 'TP_' prefix removed
                    # Check if the attribute exists in self.Obj
                    if attr_name in self.Obj:
                        # Check if the attribute value is already a list
                        if isinstance(self.Obj[attr_name], list):
                            self.Obj[attr_name].append(getattr(self, attr_name))
                        else:
                            # If the attribute value is not a list, create a new list and append to it
                            self.Obj[attr_name] = [self.Obj[attr_name], getattr(self, attr_name)]
                    else:
                        # If the attribute does not exist in self.Obj, create a new list and append to it
                        self.Obj[attr_name] = [getattr(self, attr_name)]

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.setAutoDelete(False) 
        # Add the callback to our kwargs
        #self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
