#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file vocerecog.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>
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
try:
    import sys
    import time

    sys.path.append(".")

    # Import RTM module
    import RTC
    import OpenRTM_aist

    import voicerecog_idl
    from keyphrase import speech_recog
    import winsound

    # Import Service implementation class
    # <rtc-template block="service_impl">
    # apiキー a64cf6b636ad4e0590a25b051a44adbc
    from voicerecog_idl_example import *
    import azure.cognitiveservices.speech as speechsdk
    speech_config = speechsdk.SpeechConfig(subscription="********", region="japanwest")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_synthesis_voice_name='ja-JP-NanamiNeural'
    speech_config.set_property(speechsdk.PropertyId.Speech_SegmentationSilenceTimeoutMs, "3000")
    speech_config.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "3000")
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_config.speech_recognition_language="ja-JP"
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
except Exception as e:
    print(f'{Color.RED}'"voicerecog : "+str(e)+f'{Color.RESET}')
    subprocess.run(["ShutDown.bat"])


# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
vocerecog_spec = ["implementation_id", "vocerecog", 
         "type_name",         "voicerecog", 
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
# @class vocerecog
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
class vocerecog(OpenRTM_aist.DataFlowComponentBase):
	
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
        self._voicereproviderPort = OpenRTM_aist.CorbaPort("voicereprovider")

        """
        """
        self._libvoicerecogprovider = voicerecogdata_i()
		


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
        self._voicereproviderPort.registerProvider("voicerecogdata", "Library::voicerecogdata", self._libvoicerecogprovider)
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
        self.addPort(self._voicereproviderPort)
		
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
    def onExecute(self, ec_id):
        voicerecogdata=self._libvoicerecogprovider.getdata()
        state=voicerecogdata.state
        command=voicerecogdata.command
        phase=voicerecogdata.phase
        try:
            if state=="STATE_RUNNING_PROVIDERREAD" and phase=="END":
                speech_synthesizer.speak_text("すみません。初めからやり直してください")
                returndata = datacode("STATE_RUNNING_CONSUMERREAD","",command,"DETECTION_1")
                voicerecogdata=self._libvoicerecogprovider.voicerecog(returndata)
                print("voicerecog: ",voicerecogdata.state,voicerecogdata.recogdata,voicerecogdata.phase)

            elif state=="STATE_RUNNING_PROVIDERREAD" and phase=="KEYPHRASE_REPEAT":##もう一度聞きなおす
                self._d_controlesota.data="question"
                self._controlesotaOut.write()
                time.sleep(0.5)
                #speech_synthesizer.speak_text("本の検索ですね。著者やキーワードを教えてください。")
                winsound.PlaySound('sound\mouitidoonegaisimasu2.wav',winsound.SND_FILENAME)
                self._d_controlesota.data="listening"
                self._controlesotaOut.write()
                time.sleep(0.5)
                text = speech_recog(0)
                self._d_controlesota.data="neutral"
                time.sleep(0.5)
                self._controlesotaOut.write()

                if str(text)!="":
                    self._d_controlesota.data="speaking"
                    self._controlesotaOut.write()
                    # speech_synthesizer.speak_text(str(text)+"で検索します")
                    self._d_controlesota.data="neutral"
                    self._controlesotaOut.write()
                    returndata = datacode("STATE_RUNNING_CONSUMERREAD",str(text),command,phase)
                    voicerecogdata=self._libvoicerecogprovider.voicerecog(returndata)
                    print("voicerecog: ",voicerecogdata.state,voicerecogdata.recogdata,voicerecogdata.phase)

                else:
                    returndata = datacode("STATE_RUNNING_CONSUMERREAD",str(text),command,"KEYPHRASE_REPEAT")
                    voicerecogdata=self._libvoicerecogprovider.voicerecog(returndata)
                    print("voicerecog: ",voicerecogdata.state,voicerecogdata.recogdata,voicerecogdata.phase)

            elif state=="STATE_RUNNING_PROVIDERREAD" and phase=="SEARCH":#検索のキーフレーズ抽出
                self._d_controlesota.data="question"
                self._controlesotaOut.write()
                time.sleep(0.5)
                #speech_synthesizer.speak_text("本の検索ですね。著者やキーワードを教えてください。")
                winsound.PlaySound('sound\honnnokennsaku2.wav',winsound.SND_FILENAME)
                self._d_controlesota.data="listening"
                self._controlesotaOut.write()
                time.sleep(0.5)
                text = speech_recog(0)
                self._d_controlesota.data="neutral"
                time.sleep(0.5)
                self._controlesotaOut.write()
                print(text)

                if str(text)!="":
                    self._d_controlesota.data="speaking"
                    self._controlesotaOut.write()
                    # speech_synthesizer.speak_text(str(text)+"で検索します")
                    self._d_controlesota.data="neutral"
                    self._controlesotaOut.write()
                    returndata = datacode("STATE_RUNNING_CONSUMERREAD",str(text),command,"SEARCH")
                    voicerecogdata=self._libvoicerecogprovider.voicerecog(returndata)
                    print("voicerecog: ",voicerecogdata.state,voicerecogdata.recogdata,voicerecogdata.phase)

                else:
                    returndata = datacode("STATE_RUNNING_CONSUMERREAD",str(text),command,"KEYPHRASE_REPEAT")
                    voicerecogdata=self._libvoicerecogprovider.voicerecog(returndata)
                    print("voicerecog: ",voicerecogdata.state,voicerecogdata.recogdata,voicerecogdata.phase)

            elif state=="STATE_RUNNING_PROVIDERREAD" and phase=="RECOM":#お勧めのキーフレーズ抽出
                self._d_controlesota.data="question"
                self._controlesotaOut.write()
                time.sleep(0.5)
                #speech_synthesizer.speak_text("おすすめの本ですね。どんなジャンルの本をお探しでしょうか？")
                winsound.PlaySound('sound\osuumenohonn2.wav',winsound.SND_FILENAME)
                self._d_controlesota.data="listening"
                self._controlesotaOut.write()
                time.sleep(0.5)
                text = speech_recog(1)
                self._d_controlesota.data="neutral"
                self._controlesotaOut.write()
                time.sleep(0.5)
                returndata = datacode("STATE_RUNNING_CONSUMERREAD",str(text),command,"RECOM")
                voicerecogdata=self._libvoicerecogprovider.voicerecog(returndata)
                print("voicerecog: ",voicerecogdata.state,voicerecogdata.recogdata,voicerecogdata.phase)
        except Exception as e:
            print(f'{Color.RED}'"voicerecog : "+str(e)+f'{Color.RESET}')
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
	



def vocerecogInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=vocerecog_spec)
    manager.registerFactory(profile,
                            vocerecog,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    vocerecogInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("vocerecog" + args)

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

