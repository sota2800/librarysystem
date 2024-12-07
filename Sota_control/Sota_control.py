﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Sota_control.py
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

    # SotaのIPアドレスを取得
    # import socket

    # PORT_SOTA = 5001
    # BUFFER_SIZE = 1024

    #from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM

    # # configparser
    # import configparser
    # import os
    # import errno

    # config_ini = configparser.ConfigParser()
    # config_ini_path = 'SotaAddress.ini'

    # # 指定したiniファイルが存在しない場合、エラー発生
    # if not os.path.exists(config_ini_path):
    #     raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)

    # config_ini.read(config_ini_path, encoding = 'utf-8')

    # # iniの値取得
    # read_default = config_ini['DEFAULT']
    # ADDRESS_SOTA = read_default.get('SotaAddress')

    # print('ADDRESS_SOTA: ', ADDRESS_SOTA)


    import socket
    from scapy.all import ARP, Ether, srp
except Exception as e:
    print(f'{Color.RED}'"Callstaff : "+str(e)+f'{Color.RESET}')
    subprocess.run(["ShutDown.bat"])

ADDRESS_SOTA = '192.168.11.11' # sotaを使用する場合
print(f'{Color.YELLOW}'"Sota_control :ADDRESS_SOTA  "+str(ADDRESS_SOTA)+f'{Color.RESET}')
#ADDRESS_SOTA = '0' # sotaを使用せずpcのみで行う場合
#ADDRESS_M5 = '1'

# target_ip = "192.168.11.1/24"
# packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target_ip)
# print(packet)
# result = srp(packet, timeout=3, verbose=0)[0]
# clients = []

# for set, recieved in result:
#     clients.append({'ip': recieved.psrc, 'mac': recieved.hwsrc})
# result = srp(packet, timeout=3, verbose=0)[0]
# for set, recieved in result:
#     clients.append({'ip': recieved.psrc, 'mac': recieved.hwsrc})
# result = srp(packet, timeout=3, verbose=0)[0]
# for set, recieved in result:
#     clients.append({'ip': recieved.psrc, 'mac': recieved.hwsrc})
# result = srp(packet, timeout=3, verbose=0)[0]
# for set, recieved in result:
#     clients.append({'ip': recieved.psrc, 'mac': recieved.hwsrc})
# result = srp(packet, timeout=3, verbose=0)[0]
# for set, recieved in result:
#     clients.append({'ip': recieved.psrc, 'mac': recieved.hwsrc})

# for client in clients:
#   print(client['mac'])
#   # 図書館sota 90:b6:86:11:16:fd
#   # Sota-1 cc:e1:d5:3f:17:93
#   # sota-2 90:b6:80:12:88:60
#   if client['mac'] == "90:b6:86:11:16:fd":
#     print('Sota is found.')
#     ADDRESS_SOTA = client['ip']
#     print(client['ip'])
#   elif client['mac'] == "24:0a:c4:f8:81:cc" or client['mac'] == "26:0a:c4:f8:81:cc":
#     print('M5 is found.')
#     ADDRESS_M5 = client['ip']
# print(ADDRESS_SOTA)
# print(ADDRESS_M5)
PORT_SOTA = 5001
BUFFER_SIZE = 1024

from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM

PORT_M5 = 50008

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
sota_control_spec = ["implementation_id", "Sota_control", 
         "type_name",         "Sota_control", 
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
# @class Sota_control
# @brief ModuleDescription
# 
# 
# </rtc-template>
class Sota_control(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_text = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._textIn = OpenRTM_aist.InPort("text", self._d_text)
        
        
        self._command = ""


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
        self.addInPort("text",self._textIn)
		
        # Set OutPort buffers
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
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
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):

        return RTC.RTC_OK
	
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
        if self._textIn.isNew():
            text = self._textIn.read()
            self._command = text.data
            
            if self._command != "":
                try:
                    print("Sota->",self._command)
                    with socket(AF_INET, SOCK_STREAM) as s:
                        s.settimeout(1)
                        s.connect((ADDRESS_SOTA, PORT_SOTA))
                        self._command = self._command + '\n'
                        s.send(self._command.encode())
                        #time.sleep(4)
                        #print("OK")
                        #return s.recv(BUFFER_SIZE).decode()
                except Exception as e:
                    print(f'{Color.RED}'"Sota_control : "+str(e)+f'{Color.RESET}')

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
	



def Sota_controlInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=sota_control_spec)
    manager.registerFactory(profile,
                            Sota_control,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    Sota_controlInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("Sota_control" + args)

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

