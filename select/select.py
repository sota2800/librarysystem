#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file select.py
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
    import socket
    PORT_M5 = 50008
    # M5Stack
    from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
    ADDRESS_M5= '192.168.11.129'

    # import socket
    # from scapy.all import ARP, Ether, srp
    # from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
    # ADDRESS_M5 = '192.168.11.129'
    # PORT_M5 = 50008

    import select_idl
    import winsound 
    import subprocess
    # Import Service implementation class
    # <rtc-template block="service_impl">
    from select_idl_example import *

    import azure.cognitiveservices.speech as speechsdk
    speech_config = speechsdk.SpeechConfig(subscription="fda3aee4298b4d83bbf4394ae7306678", region="japanwest")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_synthesis_voice_name='ja-JP-NanamiNeural'
    speech_config.set_property(speechsdk.PropertyId.Speech_SegmentationSilenceTimeoutMs, "3000")
    speech_config.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "3000")

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_config.speech_recognition_language="ja-JP"
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
except Exception as e:
    print(f'{Color.RED}'"Select : "+str(e)+f'{Color.RESET}')
    subprocess.run(["ShutDown.bat"])


class datacode:
    def __init__(self,state,recogdata,command,phase):
        self.state=state
        self.recogdata=recogdata
        self.command=command
        self.phase=phase

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
select_spec = ["implementation_id", "select", 
         "type_name",         "select", 
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
# @class select
# @brief ModuleDescription
# 
# 
# </rtc-template>
class select(OpenRTM_aist.DataFlowComponentBase):
	
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

        """
        """
        self._selectproviderPort = OpenRTM_aist.CorbaPort("selectprovider")

        """
        """
        self._selectprovider = selectdata_i()
		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
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
		
        # Set service provider to Ports
        self._selectproviderPort.registerProvider("selectdata", "Library::selectdata", self._selectprovider)
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
        self.addPort(self._selectproviderPort)
		
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
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
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
    #def onActivated(self, ec_id):
    #
    #    return RTC.RTC_OK
	
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
    def selectlist(self,state,recogdata,command,phase,response):
        if "ないです" in response.text or "ありません" in response.text or "いいえ" in response.text or "バイバイ" in response.text:
            self._d_controlesota.data="hello"
            speech_synthesizer.speak_text("ご利用ありがとうございました")
            print(f'{Color.GREEN}'"Select : 処理終了"+f'{Color.RESET}')
            self._controlesotaOut.write()
            time.sleep(7)
            self._d_controlesota.data="neutral"
            self._controlesotaOut.write()
            phase="DETECTION_1"
            returndata = datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,phase)
            selectdata=self._selectprovider.select(returndata)
            
        elif "はい" in response.text or "あります" in response.text:
            print(f'{Color.GREEN}'"Select : そのまま要件を聞く"+f'{Color.RESET}')
            phase="REPEAT"
            returndata = datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,phase)
            selectdata=self._selectprovider.select(returndata)

        elif "検索"in str(response):
            returndata = datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"SEARCH")
            selectdata=self._selectprovider.select(returndata)
            print("select: ",selectdata.state,selectdata.recogdata)
            print(f'{Color.GREEN}'"Select : 条件分岐，検索"+f'{Color.RESET}')

            
        elif "お勧め" in str(response) or "おすすめ" in str(response):
            returndata =datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"RECOM")
            selectdata=self._selectprovider.select(returndata)
            print("select: ",selectdata.state,selectdata.recogdata)
            print(f'{Color.GREEN}'"Select : 条件分岐，お勧め"+f'{Color.RESET}')

        elif "ないです" in response.text or "ありません" in response.text or "いいえ" in response.text or "バイバイ" in response.text:
            self._d_controlesota.data="hello"
            speech_synthesizer.speak_text("ご利用ありがとうございました")
            print(f'{Color.GREEN}'"Select : 処理終了"+f'{Color.RESET}')
            self._controlesotaOut.write()
            time.sleep(7)
            self._d_controlesota.data="neutral"
            self._controlesotaOut.write()
            phase="DETECTION_1"

        elif "サーティフィケート" in str(response) or "サーティフィケイト" in str(response):
            returndata =datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"CERTIFICATE")
            selectdata=self._selectprovider.select(returndata)
            print("select: ",selectdata.state,selectdata.recogdata)
            print(f'{Color.GREEN}'"Select : 条件分岐，サーティフィケート"+f'{Color.RESET}')

            
        elif "スタッフ" in str(response) or "職員" in str(response):
            self._d_controlesota.data="speaking"
            self._controlesotaOut.write()
            speech_synthesizer.speak_text("図書館職員さんをお呼びします。少々お待ちください")
            self._d_controlesota.data="neutral"
            self._controlesotaOut.write()
            returndata =datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"STAFFCALL")
            selectdata=self._selectprovider.select(returndata)
            print("select: ",selectdata.state,selectdata.recogdata)
            print(f'{Color.GREEN}'"Select : 条件分岐，職員呼び出し"+f'{Color.RESET}')

        elif "文献"in str(response):
            self._d_controlesota.data="speaking"
            self._controlesotaOut.write()
            speech_synthesizer.speak_text("文献の受け取りですね。図書館職員さんをお呼びします。少々お待ちください。")
            self._d_controlesota.data="neutral"
            self._controlesotaOut.write()
            returndata = datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"ARTICLE")
            selectdata=self._selectprovider.select(returndata)
            print("select: ",selectdata.state,selectdata.recogdata)
            print(f'{Color.GREEN}'"Select : 条件分岐，文献受け取り"+f'{Color.RESET}')

        elif "こんにちは" in response.text:
            speech_synthesizer.speak_text("こんにちは")
            returndata = datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"TALK")
            selectdata=self._selectprovider.select(returndata)
            print(f'{Color.GREEN}'"Select : 挨拶"+f'{Color.RESET}')

        elif "かわいい" in response.text or "可愛い" in response.text: 
            speech_synthesizer.speak_text("ありがとう")
            returndata = datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"TALK")
            selectdata=self._selectprovider.select(returndata)
            print(f'{Color.GREEN}'"Select : 褒められた"+f'{Color.RESET}')

        elif "名前" in response.text or "自己紹介" in response.text:
            speech_synthesizer.speak_text("私の名前はそーたです。図書館を利用する人のお手伝いをします。")
            returndata = datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"TALK")
            selectdata=self._selectprovider.select(returndata)
            print(f'{Color.GREEN}'"Select : 自己紹介"+f'{Color.RESET}')

        elif "システム" in str(response) or "終了" in str(response):
            speech_synthesizer.speak_text_async("システムを終了します．")
            self._d_controlesota.data="hello"
            speech_synthesizer.speak_text_async("ご利用ありがとうございました。")
            time.sleep(5)
            self._d_controlesota.data="poweroff"
            returndata = datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"SHUTDOWN")
            selectdata=self._selectprovider.select(returndata)
            print(f'{Color.GREEN}'"Select : システム終了"+f'{Color.RESET}')
            time.sleep(3)
            subprocess.run(["ShutDown.bat"])

        else:
            speech_synthesizer.speak_text("すみません，聞き取れませんでした．")
            returndata =datacode("STATE_RUNNING_CONSUMERREAD",recogdata,command,"REPEAT")
            selectdata=self._selectprovider.select(returndata)
            print("select: ",selectdata.state,selectdata.recogdata)
            print(f'{Color.GREEN}'"Select : もう一度聞き取り"+f'{Color.RESET}')

    def onExecute(self, ec_id):
        selectdata=self._selectprovider.getdata()
        state=selectdata.state
        recogdata=selectdata.recogdata
        command=selectdata.command
        phase=selectdata.phase
        response=""
        
        if state=="STATE_RUNNING_PROVIDERREAD" and (phase=="SELECT" or phase =="AGAIN" or phase=="REPEAT" or phase=="TALK"):
            try:
                if phase=="SELECT":
                    self._d_controlesota.data="hello"
                    self._controlesotaOut.write()
                    speech_synthesizer.speak_text("こんにちは")
                    self._d_controlesota.data="listening"
                    self._controlesotaOut.write()
                    time.sleep(0.8)
                    response=speech_recognizer.recognize_once_async().get()
                    print(f'{Color.GREEN}'"Select : 挨拶 * "+str(response.text)+" * を認識しました"+f'{Color.RESET}')
                    self._d_controlesota.data="neutral"
                    self._controlesotaOut.write()
                    time.sleep(0.8)
                    print(f'{Color.GREEN}'"Select :  *"+str(response.text)+"*  認識しました"+f'{Color.RESET}')
                    if "こんにちは" in response.text:
                        speech_synthesizer.speak_text("こんにちは")
                        print(f'{Color.GREEN}'"Select :  挨拶"+f'{Color.RESET}')
                    elif "名前" in response.text or "自己紹介" in response.text:
                        speech_synthesizer.speak_text("私の名前はそーたです。図書館を利用する人のお手伝いをします。")
                        print(f'{Color.GREEN}'"Select : 自己紹介"+f'{Color.RESET}')
                    elif "かわいい" in response.text or "可愛い" in response.text: 
                        speech_synthesizer.speak_text("ありがとう")
                        print(f'{Color.GREEN}'"Select : 褒められた"+f'{Color.RESET}')
            except Exception as e:
                print(f'{Color.RED}'"Select : "+str(e)+f'{Color.RESET}')
                subprocess.run(["ShutDown.bat"])

            try:              
                if phase=="AGAIN":
                    #speech_synthesizer.speak_text("他にご用件はありますか？")
                    self._d_controlesota.data="question"
                    self._controlesotaOut.write()
                    time.sleep(0.8)
                    winsound.PlaySound('sound\hokanigoyoukennhaharimasuka2.wav',winsound.SND_FILENAME)
                    self._d_controlesota.data="listening"
                    self._controlesotaOut.write()
                    time.sleep(0.8)
                    response=speech_recognizer.recognize_once_async().get()
                    print(f'{Color.GREEN}'"Select :  *"+str(response.text)+"*  認識しました"+f'{Color.RESET}')
                    self._d_controlesota.data="neutral"
                    self._controlesotaOut.write()
                    time.sleep(0.8)
                    self.selectlist(state,recogdata,command,phase,response)
            except Exception as e:
                print(f'{Color.RED}'"Select : "+str(e)+f'{Color.RESET}')
                subprocess.run(["ShutDown.bat"])
                    



            try:
                if phase=="REPEAT" or phase=="SELECT":
                    #speech_synthesizer.speak_text("ご用件は何でしょうか")
                    self._d_controlesota.data="question"
                    self._controlesotaOut.write()
                    time.sleep(0.8)
                    winsound.PlaySound('sound\goyoukennhananndeshouka2.wav',winsound.SND_FILENAME)
                    self._d_controlesota.data="listening"
                    self._controlesotaOut.write()
                    time.sleep(0.8)
                    response=speech_recognizer.recognize_once_async().get()
                    print(f'{Color.GREEN}'"Select :  *"+str(response.text)+"*  認識しました"+f'{Color.RESET}')
                    self._d_controlesota.data="neutral"
                    self._controlesotaOut.write()
                    time.sleep(0.8)
                    self.selectlist(state,recogdata,command,phase,response)
            except Exception as e:
                print(f'{Color.RED}'"Select : "+str(e)+f'{Color.RESET}')
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
	



def selectInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=select_spec)
    manager.registerFactory(profile,
                            select,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    selectInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("select" + args)

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

