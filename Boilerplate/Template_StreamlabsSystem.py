
#---------------------------
#   Import Libraries
#---------------------------
from datetime import datetime, timedelta
import os
import sys
import json
import io

  


sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from Settings_Module import MySettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Subnext"
Website = "https://www.streamlabs.com"
Description = "Shows next subscriber in queue."
Creator = "Klobeard"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------


global SettingsFile
SettingsFile = ""
global ScriptSettings
ScriptSettings = {}


#   Create Settings Directory
directory = os.path.join(os.path.dirname(__file__), "Settings")
if not os.path.exists(directory):
    os.makedirs(directory)

#   Load settings
SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
ScriptSettings = MySettings(SettingsFile)

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():

    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and Parent.HasPermission(data.User,ScriptSettings.Permission,""):
        result = Parent.GetQueue(255)
        i = 0
        while i < len(result):
            if Parent.HasPermission(result[i],"subscriber",""):
                Parent.SendStreamMessage(result[i] + " " + ScriptSettings.Response)
                return
            i = i+1
        Parent.SendStreamMessage(ScriptSettings.NoSubsResponse)
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

