#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file controlestate.py
 @brief ModuleDescription
 @date $Date$


"""
class Color:
	BLACK          = '\033[30m'#(文字)黒
	RED            = '\033[31m'#(文字)赤
	GREEN          = '\033[32m'#(文字)緑
	YELLOW         = '\033[33m'#(文字)黄
	BLUE           = '\033[34m'#(文字)青
	MAGENTA        = '\033[35m'#(文字)マゼンタ
	CYAN           = '\033[36m'#(文字)シアン
	WHITE          = '\033[37m'#(文字)白
	COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
	BOLD           = '\033[1m'#太字
	UNDERLINE      = '\033[4m'#下線
	INVISIBLE      = '\033[08m'#不可視
	REVERCE        = '\033[07m'#文字色と背景色を反転
	BG_BLACK       = '\033[40m'#(背景)黒
	BG_RED         = '\033[41m'#(背景)赤
	BG_GREEN       = '\033[42m'#(背景)緑
	BG_YELLOW      = '\033[43m'#(背景)黄
	BG_BLUE        = '\033[44m'#(背景)青
	BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
	BG_CYAN        = '\033[46m'#(背景)シアン
	BG_WHITE       = '\033[47m'#(背景)白
	BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
	RESET          = '\033[0m'#全てリセット
# </rtc-template>
try:
    import sys
    import time
    sys.path.append(".")

    # Import RTM module
    import RTC
    import OpenRTM_aist

    import facedetection_idl
    import select_idl
    import voicerecog_idl
    import selenium_idl

    # Import Service implementation class
    # <rtc-template block="service_impl">

    # </rtc-template>

    # Import Service stub modules
    # <rtc-template block="consumer_import">
    import Library, Library__POA
    import subprocess
    import azure.cognitiveservices.speech as speechsdk
    speech_config = speechsdk.SpeechConfig(subscription="*************", region="japanwest")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_synthesis_voice_name='ja-JP-NanamiNeural'
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_config.speech_recognition_language="ja-JP"
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
except Exception as e:
    print(f'{Color.RED}'"Controlestate : "+str(e)+f'{Color.RESET}')
    subprocess.run(["ShutDown.bat"])


# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
controlestate_spec = ["implementation_id", "controlestate", 
         "type_name",         "controlestate", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class controlestate
# @brief ModuleDescription
# 
# 
# </rtc-template>


class datacode:
    def __init__(self,state,recogdata,command,phase):
        self.state=state
        self.recogdata=recogdata
        self.command=command
        self.phase=phase

class controlestate(OpenRTM_aist.DataFlowComponentBase):

    STATE=""#状態制御変数
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_controlesota = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._controlesotaOut = OpenRTM_aist.OutPort("controlesota", self._d_controlesota)
        self._d_callstaff = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
        """
        """
        self._callstaffOut = OpenRTM_aist.OutPort("callstaff", self._d_callstaff)
        self._d_log = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._logOut = OpenRTM_aist.OutPort("log", self._d_log)

        self._d_start = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._startOut = OpenRTM_aist.OutPort("start", self._d_start)

        """
        """
        self._facedetectionconsumerPort = OpenRTM_aist.CorbaPort("facedetectionconsumer")
        """
        """
        self._selectconusmerPort = OpenRTM_aist.CorbaPort("selectconsumer")
        """
        """
        self._voicerecogconsumerPort = OpenRTM_aist.CorbaPort("voicerecogconsumer")
        """
        """
        self._seleniumconsumerPort = OpenRTM_aist.CorbaPort("seleniumconsumer")

		

        """
        """
        self._libfacedetectionconsumer = OpenRTM_aist.CorbaConsumer(interfaceType=Library.facedetectiondata)
        """
        """
        self._libselectconsumer = OpenRTM_aist.CorbaConsumer(interfaceType=Library.selectdata)
        """
        """
        self._libvoicerecogconsumer = OpenRTM_aist.CorbaConsumer(interfaceType=Library.voicerecogdata)
        """
        """
        self._libseleniumconsumer = OpenRTM_aist.CorbaConsumer(interfaceType=Library.seleniumdata)

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>
        self.libdata=datacode("STATE_STOP","","NUM","DETECTION_1")
        self.start=True


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
		
        # Set OutPort buffers
        self.addOutPort("controlesota",self._controlesotaOut)
        self.addOutPort("callstaff",self._callstaffOut)
        self.addOutPort("log",self._logOut)
        self.addOutPort("start",self._startOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
        self._facedetectionconsumerPort.registerConsumer("facedetectiondata", "Library::facedetectiondata", self._libfacedetectionconsumer)
        self._selectconusmerPort.registerConsumer("selectdata", "Library::selectdata", self._libselectconsumer)
        self._voicerecogconsumerPort.registerConsumer("voicerecogdata", "Library::voicerecogdata", self._libvoicerecogconsumer)
        self._seleniumconsumerPort.registerConsumer("seleniumdata", "Library::seleniumdata", self._libseleniumconsumer)
		
        # Set CORBA Service Ports
        self.addPort(self._facedetectionconsumerPort)
        self.addPort(self._selectconusmerPort)
        self.addPort(self._voicerecogconsumerPort)
        self.addPort(self._seleniumconsumerPort)
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    def onStartup(self, ec_id):
        #起動時にseleniumを起動onstartupに書いててもいいかも

        try:
            self.processes = [
                subprocess.Popen(["python", "callstaff.py"], cwd=r"C:\Users\robot\Documents\library4.0\callstaff"),
                #subprocess.Popen(["python", "controlestate.py"], cwd=r"C:\Users\sotar\OneDrive\Desktop\library3.4\controlestate"),
                subprocess.Popen(["python", "facedetection.py"], cwd=r"C:\Users\robot\Documents\library4.0\facedetection"),
                subprocess.Popen(["python", "Log.py"], cwd=r"C:\Users\robot\Documents\library4.0\Log"),
                subprocess.Popen(["python", "select.py"], cwd=r"C:\Users\robot\Documents\library4.0\select"),
                subprocess.Popen(["python", "selenium1.py"], cwd=r"C:\Users\robot\Documents\library4.0\selenium"),
                subprocess.Popen(["python", "Sota_control.py"], cwd=r"C:\Users\robot\Documents\library4.0\Sota_control"),
                subprocess.Popen(["python", "vocerecog.py"], cwd=r"C:\Users\robot\Documents\library4.0\voicerecog")
            ]
        except Exception as e:
            print(f'{Color.RED}'"Controlestate : "+str(e)+f'{Color.RESET}')

    
        return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The activated action (Active state entry action)
    ##
    ## @param ec_id target ExecutionContext Id
    ## 
    ## @return RTC::ReturnCode_t
    ##
    ##
    def onActivated(self, ec_id):
        time.sleep(10)
        time.sleep(50)

        return RTC.RTC_OK
	
    ###
    ##
    ## The deactivated action (Active state exit action)
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onDeactivated(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def midfacedetection(self):
        if self.libdata.phase=="DETECTION_1" or self.libdata.phase=="DETECTION_2":
            if self.libdata.phase=="DETECTION_1":
                data="DETECTION_1"
            elif self.libdata.phase=="DETECTION_2":
                data="DETECTION_2"
            facedetectiondata=self.libdata 
            if self.libdata.phase=="DETECTION_1":         
                while(facedetectiondata.phase!="SELECT"):
                    facedetectiondata=datacode("STATE_RUNNING_PROVIDERREAD",self.libdata.recogdata,"NUM",data)
                    facedetectiondata=self.facedetectionconsumer(facedetectiondata)
            elif self.libdata.phase=="DETECTION_2":       
                    facedetectiondata=datacode("STATE_RUNNING_PROVIDERREAD",self.libdata.recogdata,"NUM",data)
                    facedetectiondata=self.facedetectionconsumer(facedetectiondata)
            #self.libdata=facedetectiondata          
        return facedetectiondata
    
    def facedetectionconsumer(self,data):
            temp=self._libfacedetectionconsumer._ptr().facedetection(data)
            print(temp.state)
            time.sleep(1)
            data=self._libfacedetectionconsumer._ptr().setresult("READ")
            while(data.state!="STATE_RUNNING_CONSUMERREAD"):
                data=self._libfacedetectionconsumer._ptr().setresult("READ")
            if data.state!="STATE_STOP" or data.state!="STATE_ERROR":
                data.state="STATE_RUNNING"
            print(data.state,data.phase)
            return data
    
    def facedetection2(self,data):#引数はtask
        if self.libdata.state=="STATE_RUNNING":
            print("----------FACEDETECTION_2_PHASE----------")
            temp=self.libdata.phase
            self.libdata.phase="DETECTION_2"
            self.libdata=self.midfacedetection()
            if self.libdata.phase=="STOP":
                self.libdata.state="STATE_STOP"
                self.libdata.phase="DETECTION_1"
                
            else:
                self.libdata.phase=temp
        
        return data
    
    def selectconsumer(self,data):
            temp=self._libselectconsumer._ptr().select(data)
            print(temp.state)
            time.sleep(1)
            data=self._libselectconsumer._ptr().setresult("READ")
            while(data.state!="STATE_RUNNING_CONSUMERREAD"):
                data=self._libselectconsumer._ptr().setresult("READ")
            if data.state!="STATE_STOP" or data.state!="STATE_ERROR":
                data.state="STATE_RUNNING"
            print(data.state,data.phase)
            return data

    def voicerecogconsumer(self,data):
            temp=self._libvoicerecogconsumer._ptr().voicerecog(data)
            print(temp.state)
            time.sleep(1)
            data=self._libvoicerecogconsumer._ptr().setresult("READ")
            while(data.state!="STATE_RUNNING_CONSUMERREAD"):
                data=self._libvoicerecogconsumer._ptr().setresult("READ")
            print(2,data.state,data.phase)
            if data.state!="STATE_STOP" or data.state!="STATE_ERROR":
                data.state="STATE_RUNNING"
            return data
    def seleniumconsumer(self,data):
            # if data.phase=="SEARCH":
            temp=self._libseleniumconsumer._ptr().search(data)
            # elif data.phase=="RECOM":
            #      temp=self._libseleniumconsumer._ptr().recom(data)
            # elif data.phase=="CERTIFICATE":
            #      temp=self._libseleniumconsumer._ptr().certificate(data)
            print(temp.state)
            time.sleep(1)
            data=self._libseleniumconsumer._ptr().setresult("READ")
            while(data.state!="STATE_RUNNING_CONSUMERREAD"):
                data=self._libseleniumconsumer._ptr().setresult("READ")
            if data.state!="STATE_STOP" or data.state!="STATE_ERROR":
                data.state="STATE_RUNNING"
            print(data.state,data.phase)
            return data

    def onExecute(self, ec_id):
        try:
            #seleniumをホームページに戻す
            seleniumdata=datacode("","","NUM","RESET_SELENIUM")
            temp=self._libseleniumconsumer._ptr().search(seleniumdata)
            print("RESET_SELENIUM")



            if self.libdata.phase=="DETECTION_1":
                self._d_controlesota.data="poweroff"
                self._controlesotaOut.write()
                print("----------FACEDETECTION_1_PHASE----------")
                self.libdata=self.midfacedetection()#self.libdata.phaseがDETECTION_1の時とDETECTION_2の時しか動かない

            selectcount=0
            task=""

            #select
            if self.libdata.state=="STATE_RUNNING" and (self.libdata.phase=="SELECT" or self.libdata.phase=="AGAIN"):
                while(selectcount<3):
                    task=self.facedetection2(task)
                    if self.libdata.phase=="DETECTION_1":
                        self.libdata.phase="DETECTION_1"
                        self.libdata.state="STATE_STOP"
                        break
                    if self.libdata.state=="STATE_RUNNING" and (self.libdata.phase=="SELECT" or self.libdata.phase=="AGAIN" or self.libdata.phase=="REPEAT" or self.libdata.phase=="TALK"):
                        print("----------SELECT_PHASE_",selectcount,"----------")
                        print(f'{Color.CYAN}'"SELECTの処理へ"f'{Color.RESET}')
                        selectdata=datacode("STATE_RUNNING_PROVIDERREAD","","NUM",self.libdata.phase)
                        selectdata =self.selectconsumer(selectdata)
                        print(selectdata.phase)
                        self.libdata=selectdata
                        task=self.libdata.phase
                        if task=="SEARCH" or task=="RECOM" or task=="CERTIFICATE" or task=="STAFFCALL" or task=="STAFFCALL" or task=="ARTICLE": 
                            break

                        elif self.libdata.phase=="SHUTDOWN":
                            print("************SHUTDOWN**************")
                            self.processes.subprocess.run(["exit"])
                            print("************SHUTDOWN**************")
                            break

                        elif self.libdata.phase=="TALK":
                            selectcount-=1
                        elif self.libdata.phase=="REPEAT":
                            selectcount+=1
                    if selectcount==2:
                        self.libdata.phase="DETECTION_1"
                        self.libdata.state="STATE_STOP"
                        break
                    print(selectcount)
            
            #facedetection
            task=self.facedetection2(task)


            print(self.libdata,task)
            #voicerecog
            if self.libdata.state=="STATE_RUNNING":
                self.libdata.recogdata=""
                if task=="SEARCH" or task=="RECOM":
                    print(f'{Color.CYAN}'"Voicerecogの処理へ"f'{Color.RESET}')
                    voicerecogdata=datacode("STATE_RUNNING_PROVIDERREAD","","NUM",self.libdata.phase)
                    voicerecogdata=self.voicerecogconsumer(voicerecogdata)
                    self.libdata=voicerecogdata
                    n=0
                    while(n<3):
                        n+=1
                        task=self.facedetection2(task)

                        if self.libdata.phase=="DETECTION_1":
                            self.libdata.phase="DETECTION_1"
                            self.libdata.state="STATE_STOP"
                            break
                        print(self.libdata.recogdata)
                        if self.libdata.recogdata!="" :#検索，お勧めへ
                            self.libdata.phase=task
                            break

                        elif n==2:##３回聞きなおしはやり直し
                            voicerecogdata=datacode("STATE_RUNNING_PROVIDERREAD","","NUM","END")
                            voicerecogdata=self.voicerecogconsumer(voicerecogdata)
                            self.libdata=voicerecogdata
                            self.libdata.phase="DETECTION_1"
                            self.libdata.state="STATE_STOP"
                            break

                        else:#やり直し
                            voicerecogdata=datacode("STATE_RUNNING_PROVIDERREAD","","NUM","KEYPHRASE_REPEAT")
                            voicerecogdata=self.voicerecogconsumer(voicerecogdata)
                            self.libdata=voicerecogdata
                        print(n)

            #facedetection
            print("okfoake")
            task=self.facedetection2(task)

            #selenium
            if self.libdata.state=="STATE_RUNNING":
                if task=="SEARCH":
                    print(f'{Color.CYAN}'"Seleniumの処理へ"f'{Color.RESET}')
                    print("----------SELENIUM_SEARCH_PHASE----------")
                    seleniumdata=datacode("STATE_RUNNING_PROVIDERREAD",voicerecogdata.recogdata,"NUM",task)
                    seleniumdata=self.seleniumconsumer(seleniumdata)
                    self.libdata=seleniumdata
                    if self.libdata.phase=="STAY_SEARCH":
                        while(seleniumdata.phase!="AGAIN"):    
                            print("----------SELENIUM_SEARCH_FACEDETECTION_2_PHASE----------")
                            temp=self.libdata.phase
                            self.libdata.phase="DETECTION_2"
                            self.libdata=self.midfacedetection()
                            if self.libdata.phase=="STOP":
                                self.libdata.state="STATE_STOP"
                                self.libdata.phase="DETECTION_1"
                                break
                            self.libdata.phase=temp   
                            seleniumdata=datacode("STATE_RUNNING_PROVIDERREAD","","NUM","STAY_SEARCH")
                            seleniumdata=self.seleniumconsumer(seleniumdata)
                        if self.libdata.phase!="DETECTION_1":
                            self.libdata=seleniumdata


                elif task=="RECOM":
                    print("----------SELENIUM_RECOM_PHASE----------")
                    print(f'{Color.CYAN}'"お勧めの処理へ"f'{Color.RESET}')
                    seleniumdata=datacode("STATE_RUNNING_PROVIDERREAD",voicerecogdata.recogdata,"NUM",task)
                    seleniumdata=self.seleniumconsumer(seleniumdata)
                    self.libdata=seleniumdata
                    if self.libdata.phase=="RECOM_REPEAT":
                        while(seleniumdata.phase!="AGAIN"):
                            print("----------SELENIUM_RECOM_FACEDETECTION_2_PHASE----------")
                            self.libdata.phase="DETECTION_2"
                            self.libdata=self.midfacedetection()
                            if self.libdata.phase=="STOP":
                                self.libdata.state="STATE_RUNNING_PROVIDERREAD"
                                self.libdata.phase="DETECTION_1" 
                                seleniumdata=self.seleniumconsumer(self.libdata)
                                self.libdata.state="STATE_RUNNING"
                                break 
                            else:
                                seleniumdata.state="STATE_RUNNING_PROVIDERREAD"
                                seleniumdata=self.seleniumconsumer(seleniumdata)
                                print(seleniumdata.phase)
                                self.libdata=seleniumdata                           
                        
                    # if self.libdata.phase=="STAY_SEARCH":
                    #     while(seleniumdata.phase!="AGAIN"):    
                    #         print("----------SELENIUM_SEARCH_FACEDETECTION_2_PHASE----------")
                    #         self.libdata.phase="DETECTION_2"
                    #         self.libdata=self.midfacedetection()
                    #         if self.libdata.phase=="STOP":
                    #             self.libdata.state="STATE_STOP"
                    #             self.libdata.phase="DETECTION_1"
                    #             break   
                    #         seleniumdata=datacode("STATE_RUNNING_PROVIDERREAD","","NUM","STAY_SEARCH")
                    #         seleniumdata=self.seleniumconsumer(seleniumdata)
                    #         self.libdata=seleniumdata

                elif task=="CERTIFICATE":
                    print("----------SELENIUM_CERTIFICATE_PHASE----------")
                    print(f'{Color.CYAN}'"サーティフィケイトの処理へ"f'{Color.RESET}')
                    seleniumdata=datacode("STATE_RUNNING_PROVIDERREAD","","NUM",task)
                    seleniumdata=self.seleniumconsumer(seleniumdata)
                    self.libdata=seleniumdata
                    self.libdata.state="STATE_RUNNING"


            #callstaff
            if self.libdata.state=="STATE_RUNNING":
                if task=="ARTICLE" or task=="STAFFCALL":
                    print(f'{Color.CYAN}'"Callstaffの処理へ"f'{Color.RESET}')
                    print("----------CALLSTAFF_PHASE----------")
                    self._d_callstaff.data=True
                    self._callstaffOut.write()
                    time.sleep(5)
                    self.libdata.phase="DETECTION_1"
                elif self.libdata.phase=="CALLSTAFF":
                    print(f'{Color.CYAN}'"職員呼び出しの処理へ"f'{Color.RESET}')
                    print("----------CALLSTAFF_CERTIFICATE_PHASE----------")
                    self._d_callstaff.data=True
                    self._callstaffOut.write()
                    time.sleep(10)
                    self.libdata.phase="DETECTION_1"

            
            print("******",self.libdata.state,self.libdata.phase,"******")
        except Exception as e:
            print(f'{Color.RED}'"Controlestate : "+str(e)+f'{Color.RESET}')
            subprocess.run(["ShutDown.bat"])

    
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def controlestateInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=controlestate_spec)
    manager.registerFactory(profile,
                            controlestate,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    controlestateInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("controlestate" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

