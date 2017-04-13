#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import socket
from tc_common import *
from subprocess import call
import subprocess
import os
import time

# Function to run the command to go to Home Screen
# Usage: goto_home_screen(self.tc_details['dev0'])            #Todo: if oly dev0 can be used in call
def goto_home_screen(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 3")

def press_switch_app(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent KEYCODE_APP_SWITCH")

# Usage: go_back(self.tc_details['dev0'])
# Function to run the command that generates a keypress event to send the display one step back
def go_back(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 4")


# Usage: receive_call(self.tc_details['dev0'])
# Function to run the command that makes a call 
def receive_call(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 5")


# Usage: end_call(self.tc_details['dev0'])
# Function to run the command that disconnects a call 
def end_call(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 6")


# Usage: DPad_up(self.tc_details['dev0'])
# Function to run the command that sends the keyboard cursor 'up' by one position
def DPad_up(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 19")

# Usage: DPad_down(self.tc_details['dev0'])
# Function to run the command that sends the keyboard cursor 'up' by one position
def DPad_down(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 20")

# Usage: DPad_left(self.tc_details['dev0'])
# Function to run the command that shifts the control to the key on the right by one position 
def DPad_left(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 21")

# Usage: DPad_right(self.tc_details['dev0'])
# Function to run the command that shifts the control to the key on the right by one position 
def DPad_right(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 22")

# Usage: DPad_center(self.tc_details['dev0'])
# Function to run the command that clicks the center key
def DPad_center(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 23")


# Usage: volume_up(self.tc_details['dev0'])
# Function to run the command that increases the volume by one level
def volume_up(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 24")


# Usage: volume_down(self.tc_details['dev0'])
# Function to run the command that decreases the volume by one level
def volume_down(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 25")


# Usage: screen_on_off(self.tc_details['dev0'])
# Function to run the command that sends the power button event to turn the device on or off. You can use this with keyevent 82 to unlock the device 
def screen_on_off(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 26")

# Usage: power_on_off(self.tc_details['dev0'])
# Function to run the command that sends the power button event to turn the device on or off. You can use this with keyevent 82 to unlock the device 
def power_on_off(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 26")

# Usage: launch_camera(self.tc_details['dev0'])  not working
# Function to run the command that launch a camera application or take pictures
def launch_camera(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 27")


# Usage: click_enter(self.tc_details['dev0'])
# Function to run the command that generates a keypress event to enter into the selected option
def click_enter(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 66")


# Usage: screen_unlock(self.tc_details['dev0'])
# Function to run the command that unlock the lockscreen on the device
def screen_unlock(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 82")


# Usage: google_search(self.tc_details['dev0'])
# Function to run the command to goto Google search
def google_search(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 84")


# Usage: stop_media(self.tc_details['dev0'])
# Function to run the command to stop the media
def stop_media(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 86")


# Usage: pause_media(self.tc_details['dev0'])
# Function to run the command to pause the media
def pause_media(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 127")

# Usage: capture_image(self.tc_details['dev0']) 
# Function to run the command to capture image in camera app
def capture_image(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent KEYCODE_CAMERA")

# Usage: press_enter(self.tc_details['dev0']) 
# Function to press enter 
def press_enter(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent KEYCODE_ENTER")


# Usage: enter_keycode_numb(self.tc_details['dev0'], 1) 
# Function to enter numbers using keycode
def enter_keycode_numb(dev_id, val):
    Run_Adb_Cmd(dev_id, "shell input keyevent KEYCODE_" + val)
    return



# Usage: reboot_device(self.tc_details['dev0'])
# Function to reboot the device
def reboot_device(dev_id):
    Run_Adb_Cmd(dev_id, "reboot")



#-----------------------------------------------------------------------------------------------------------------------------------------------


# Usage: open_direct_settings(self.tc_details['dev0'], "AIRPLANE_MODE_SETTINGS" )
# Function to open settings tab for different parameter inputs
def open_direct_settings(dev_id, settings_name):
    cmd = "shell am start -a android.settings." + settings_name
    Run_Adb_Cmd(dev_id, cmd)


# Usage: open_settings(self.tc_details['dev0'], "DisplaySettings")  
# Function to open mobile settings
def open_settings(dev_id, settings_name):
    cmd = "shell am start -n com.android.settings/." + settings_name
    Run_Adb_Cmd(dev_id, cmd)


def open_Bluetooth_settings(dev_id):
    #cmd = "shell am start -n com.android.settings/." + settings_name
    cmd = "shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE"
    Run_Adb_Cmd(dev_id, cmd)

#.......Wi-Fi related functions......#
#opening wifi settings directly
def open_wifi_settings(dev_id):
    cmd = "shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings"
    Run_Adb_Cmd(dev_id, cmd)



#.......Developer options related functions......#
#opening Developer options settings directly
def open_Developer_settings(dev_id):
    cmd = "shell am start -n com.android.settings/.DevelopmentSettings"
    Run_Adb_Cmd(dev_id, cmd)



# Usage: read_write_status(self.tc_details['dev0'], 'r'/'w', "global", "airplane_mode_on", 1 )   #Todo: check diff conditions 
# Function to read the status of settings
def read_write_status(dev_id, operation, namespace, key, value=""):
    if operation == 'r':
        cmd = "shell settings get " + namespace + " " + key
        n = Run_Adb_Cmd(dev_id, cmd)
        print n
        return n
   
    elif operation == 'w':
        cmd = "shell settings put " + namespace + " " + key + " " + value + " "
        Run_Adb_Cmd(dev_id, cmd)
    else:
	print "Invalid Syntax"

    '''if operation == 0 and value == int(""):
        cmd = "shell settings get " + namespace + " " + key
	status = Run_Adb_Cmd(dev_id, cmd)
        return status
    elif operation == 0 and value != int(""):
        print "Too many arguments"
    elif operation == 1 and value != int(""):
        cmd = "shell settings put " + namespace + " " + key + " " + value
        Run_Adb_Cmd(dev_id, "cmd")
    elif operation == 1 and value == int(""):
        print "Less arguments passed"	
    else:
        print "Invalid Input, please enter r or w" '''


#--------------------------------------------------------------------------------------------------------------------------------



# Usage: open_browser(self.tc_details['dev0'], "chrome")
# Function to launch a specific(chrome) browser
def open_browser(dev_id, browser_name):
    cmd = "shell am start com.android." + browser_name + "/com.google.android.apps." + browser_name + ".Main"
    Run_Adb_Cmd(dev_id, cmd)


# Function to launch a browser
# Usage: open_default_browser(self.tc_details['dev0'])
def open_default_browser(dev_id):
    cmd = "shell am start com.android.browser/.BrowserActivity"
    Run_Adb_Cmd(dev_id, cmd)


# Function to launch an app
#Usage: open_app(self.tc_details['dev0'], 'messaging')
def open_app(dev_id, app_name):
    # Look up the command to open this app    
    config = ConfigParser.ConfigParser()
    config.read("../../../framework/common/commands.config")
    #config.read("commands.config")
    app_full_name = config.get('app_open_commands',app_name)
    cmd = "shell am start " + app_full_name
    Run_Adb_Cmd(dev_id, cmd)


# -----------------------------------------------------------------------------------------


# Function to close an app
#Usage: close_app(self.tc_details['dev0'], 'youtube')
def close_app(dev_id, app_name):
    config = ConfigParser.ConfigParser()
    config.read("../../../framework/common/commands.config")
    #config.read("commands.config")
    app_full_name = config.get('app_close_commands',app_name)
    cmd = "shell am force-stop " + app_full_name
    Run_Adb_Cmd(dev_id, cmd)


# Function to install an app
#Usage: install_app(self.tc_details['dev0'], 'twitter')
def install_app(dev_id, app_name):
    config = ConfigParser.ConfigParser()
    config.read("../../../framework/common/commands.config")
    #config.read("commands.config")
    app_full_name = config.get('app_install_commands',app_name)
    cmd = "shell am force-stop " + app_full_name
    Run_Adb_Cmd(dev_id, cmd)


# Function to uninstall an app
#Usage: uninstall_app(self.tc_details['dev0'], 'play_books')
def uninstall_app(dev_id, app_name):
    config = ConfigParser.ConfigParser()
    config.read("../../../framework/common/commands.config")
    #config.read("commands.config")
    app_full_name = config.get('app_uninstall_commands',app_name)
    cmd = "shell pm uninstall " + app_full_name
    Run_Adb_Cmd(dev_id, cmd)



#--------------------------------------------------------------------------------------



# Function to clear the contacts
#Usage: clear_contacts(self.tc_details['dev0'])
def clear_contacts(dev_id):
    Run_Adb_Cmd(dev_id, "shell pm clear com.android.providers.contacts")




# Function to make a call #Todo
#Usage: call_intent(self.tc_details['dev0'], self.tc_details['contact_number'])
def call_intent(dev_id, destination_number):
    cmd = "shell am start -a android.intent.action.CALL -d tel:" + destination_number + ""
    Run_Adb_Cmd(dev_id, cmd)
# Run_Adb_Cmd(self.tc_details['dev0'],"shell am start -a android.intent.action.CALL -d tel:" + self.tc_details['contact_number'] + "" )


# Function to send an sms #Todo
#Usage: send_message(self.tc_details['dev0'], self.tc_details['contact_number'])
def send_message(dev_id, destination_number):
    cmd = "shell am start -a android.intent.action.SENDTO -d sms:" + destination_number + ""
    Run_Adb_Cmd(dev_id, cmd)
# Run_Adb_Cmd(self.tc_details['dev0'], "shell am start -a android.intent.action.SENDTO -d sms:" + self.tc_details['contact_number'] + "")



# "shell am start -a android.intent.action.VIEW -d \"http://www.google.com\" ")
# Function to view a required website
# Usage: view_web(self.tc_details['dev0'], "http://www.google.com")
def view_web(dev_id, web_name):
    cmd = "shell am start -a android.intent.action.VIEW -d" + web_name  
    Run_Adb_Cmd(dev_id, cmd)



# "shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name "  +  self.tc_details['tc_contactname'] + " -e phone " + self.tc_details['tc_contactnumber'] + "")
# Function to create a new contact
# Usage: create_contact(self.tc_details['dev0'], self.tc_details['tc_contactname'], self.tc_details['contact_number'])
def create_contact(dev_id, contact_name, contact_number):
    cmd = "shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name " + contact_name + " -e phone " + contact_number + ""
    Run_Adb_Cmd(dev_id, cmd)


# cmd = "shell am start -a android.intent.action.VIEW -d file:/sdcard/Music/audio.%s -t audio/%s" %(file_ext, file_ext)
#Function to play audio file of mp3 format
#Usage: play_audio(self.tc_details['dev0'], file_ext)
def play_audio(dev_id, file_ext):
    cmd = "shell am start -a android.intent.action.VIEW -d file:/sdcard/Music/audio.%s -t audio/%s" %(file_ext, file_ext)
    Run_Adb_Cmd(dev_id, cmd)


# -------------------------------------------------------------------------------------------------------------------------------------------
#this function return number of directories present in a directory:
#file_count(self.tc_details['dev0'],"/storage/ipsm/log")
def file_count(dev_id,path):  
	cmd=path
	ret_val=Run_Adb_Cmd(dev_id, cmd)
        sysdate=(time.strftime("%Y_%m_%d"))
        return ret_val.count(sysdate)

#open_directory(self.tc_details['dev0'],+"log/")
def open_directory(dev_id,path):
	#sysdate=(time.strftime("%Y_%m_%d"))
	cmd=path
	val=Run_Adb_Cmd(dev_id, cmd)
	print val
	return val
#search_directory(self.tc_details['dev0'])
def search_directory(dev_id):
	cmd="shell ls -la /storage/IPSM/"
	val=Run_Adb_Cmd(dev_id, cmd)
	name_list=['log','dbgbuf']
	for name in name_list:
		if val.find(name)!=0:
			return True

#function is used to direct open use USB:
#Use_USB(self.tc_details['dev0'])
def Use_USB(dev_id):
	cmd="shell am start -n com.android.settings/.deviceinfo.UsbModeChooserActivity"
	Run_Adb_Cmd(dev_id, cmd)

# Function to input text to the device  
#Usage: input_text(self.tc_details['dev0'], "enter the text here")
def input_text(dev_id, text):
    cmd = "shell input text " + text 
    Run_Adb_Cmd(dev_id, cmd)


#Function to swipe on the device
#Usage: swipe(self.tc_details['dev0'], 242, 764, 242, 278)
def swipe(dev_id, x1, y1, x2, y2):
    cmd = "shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) 
    Run_Adb_Cmd(dev_id, cmd)

#Function to swipe on the device
#Usage: touchscreen_swipe(self.tc_details['dev0'], 300, 0, 300, 800)
def touchscreen_swipe(dev_id, x1, y1, x2, y2):
    cmd = "shell input touchscreen swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) 
    Run_Adb_Cmd(dev_id, cmd)

#Function to remove the file
#Usage: remove_camera_file(self.tc_details['dev0'], "/sdcard/DCIM/Camera")		#Todo : not sure
def remove_camera_file(dev_id, path):
    cmd = "shell rm -r " + path
    Run_Adb_Cmd(dev_id, cmd)



# Function to list packages                                           
#Usage: list_packages(self.tc_details['dev0'])
def list_packages(dev_id):
    cmd = "shell pm list packages"
    list_packs = Run_Adb_Cmd(dev_id, cmd)
    return list_packs


# Function to close the package
#Usage: close_package(self.tc_details['dev0'], "settings")
def close_package(dev_id, package_name):
    config = ConfigParser.ConfigParser()
    config.read("../../../framework/common/commands.config")
    package_full_name = config.get('app_close_commands', package_name)
    cmd = "shell pm clear " + package_full_name
    Run_Adb_Cmd(dev_id, cmd)
    return


# Run_Adb_Cmd(self.tc_details['dev0'], "shell pm clear com.skype.raider")    #Todo:not tested yet
# Function to clear the package
#Usage: clear_package(self.tc_details['dev0'], "com.skype.raider")
def clear_package(dev_id, package_name):
    cmd = "shell pm clear " + package_name 
    Run_Adb_Cmd(dev_id, cmd)

#This function will clear the notification bar
#clear_notification_bar(self.tc_details['dev0'])
def clear_notification_bar(dev_id):
	cmd="root"
	Run_Adb_Cmd(dev_id, cmd)
	cmd= "shell service call notification 1"
	Run_Adb_Cmd(dev_id, cmd)


# Function to open a web page
# Usage: open_web_page(self.tc_details['dev0'], "http://www.gmail.com")   #Todo: ASP.net tc not tested yet
def open_web_page(dev_id, web_page ):
    cmd = "shell am start " + web_page
    Run_Adb_Cmd(dev_id, cmd)

# Function to delete internal sdcard contents
# Usage: rm_sdcard_contents(self.tc_details['dev0'])
def rm_sdcard_contents(dev_id):
    cmd = "shell rm -r /sdcard/DCIM/Camera"
    Run_Adb_Cmd(dev_id, cmd)

# Function to delete internal sdcard contents
# Usage: rm_ipsm_contents(self.tc_details['dev0'])
def rm_ipsm_contents(dev_id):
    cmd = "shell rm -r /storage/IPSM"
    Run_Adb_Cmd(dev_id, cmd)

# Function to enable/disable settings
# Usage: enable_disable_settings(self.tc_details['dev0'],  "wifi", "enable/disable")
def enable_disable_settings(dev_id, settings_name, op_name):
    cmd = "shell svc " + settings_name + " " + op_name
    Run_Adb_Cmd(dev_id, cmd)
	
# Function to pull sdcard contents
# Usage: pull_sdcard_contents(self.tc_details['dev0'], "../images/tmp")
def pull_sdcard_contents(dev_id, tmp_path):
    cmd = "pull /sdcard/DCIM/Camera" + " " + tmp_path
    Run_Adb_Cmd(dev_id, cmd)

# Function to pull ipsm contents
# Usage: pull_ipsm_contents(self.tc_details['dev0'], "../images/tmp")
def pull_ipsm_contents(dev_id, tmp_path):
    cmd = "pull /storage/IPSM/Test" + " " + tmp_path
    Run_Adb_Cmd(dev_id, cmd)

# Function to push sdcard contents
# Usage: push_music_sdcard(self.tc_details['dev0'], file_ext)
def push_music_sdcard(dev_id, tmp_path):
    # cmd = "push ../music/audio.%s /sdcard/Music" + tmp_path
    cmd = "push ../music/audio." + tmp_path + " " + "/sdcard/Music"  
    ret_val=Run_Adb_Cmd(dev_id, cmd)
    return ret_val


# Function to push file
# Usage: push(self.tc_details['dev0'], "../video/video.3gp", "/sdcard/Video" )
def push(dev_id, from_path ,to_path):
    cmd="push " + from_path + " " + to_path
    val=Run_Adb_Cmd(dev_id, cmd)
    return val


# Function to root
# Usage: root_device(self.tc_details['dev0'])
def root_device(dev_id):
    Run_Adb_Cmd(dev_id, "root")
    time.sleep(5)



# Function to make directory
# Usage: make_dir(self.tc_details['dev0'], "/sdcard/Video")
def make_dir(dev_id, dir_name):
    cmd = "shell mkdir " + dir_name
    Run_Adb_Cmd(dev_id, cmd)


#Function to remove the file
#Usage: remove_music_file(self.tc_details['dev0'], file_ext)		#Todo : not sure
def remove_music_file(dev_id, tmp_path):
    cmd = "shell rm -f /sdcard/Music/audio." + tmp_path
    Run_Adb_Cmd(dev_id, cmd)

# Function to view a required website
# Usage: play_audio(self.tc_details['dev0'], file_ext, file_ext)
def play_audio(dev_id, path, tmp_path):
    # cmd = "shell am start -a android.intent.action.VIEW -d file:/sdcard/Music/audio.%s -t audio/%s" + web_name 
    cmd = "shell am start -a android.intent.action.VIEW -d file:/sdcard/Music/audio." + path + " " + "-t audio/" + tmp_path 
    Run_Adb_Cmd(dev_id, cmd)

# Usage: list_device(self.tc_details['dev0'])
# Function to list the connected devices
def list_device(dev_id):
    device = Run_Adb_Cmd(dev_id, "devices")
    return device

# Usage: media_play_pause(self.tc_details['dev0'])
# Function to run the command to play/pause the media
def media_play_pause(dev_id):
    Run_Adb_Cmd(dev_id, "shell input keyevent 85")


# Usage: wifi_enable(self.tc_details['dev0'])
# Function to enable wifi while in root
def wifi_enable(dev_id):
    Run_Adb_Cmd(dev_id, "shell svc wifi enable")
    return

# Usage: wifi_disable(self.tc_details['dev0'])
# Function to disable wifi while in root
def wifi_disable(dev_id):
    Run_Adb_Cmd(dev_id, "shell svc wifi disable")
    return
    
# Usage: data_enable(self.tc_details['dev0'])
# Function to enable data while in root
def data_enable(dev_id):
    Run_Adb_Cmd(dev_id, "shell svc data enable")

# Usage: data_disable(self.tc_details['dev0'])
# Function to disable data while in root
def data_disable(dev_id):
    Run_Adb_Cmd(dev_id, "shell svc data disable")

# Usage: install_apk(self.tc_details['dev0'], "com.loudtalks-1.apk")
# Function to install an application by its apk
def install_apk(dev_id, apk_name):
    cmd = "install ../../../apk/" + apk_name
    ret_val = Run_Adb_Cmd(dev_id, cmd)
    return ret_val


'''# Usage: uninstall_apk(self.tc_details['dev0'], "com.loudtalks-1.apk")
# Function to uninstall an application by its apk
def uninstall_apk(dev_id, apk_name):
    cmd = "install ../../../apk/" + apk_name
    ret_val = Run_Adb_Cmd(dev_id, cmd)
    return ret_val '''



# Run_Adb_Cmd(self.tc_details['dev0'], "shell pm clear com.skype.raider")    
# Function to clear cache
#Usage: clear_cache(self.tc_details['dev0'], "com.skype.raider")
def clear_cache(dev_id, cache_name):
    cmd = "shell pm clear " + cache_name 
    Run_Adb_Cmd(dev_id, cmd)

# Function to make directory
# Usage: make_dir(self.tc_details['dev0'], "/sdcard/Video")
def make_dir(dev_id, dir_name):
    cmd = "shell mkdir " + dir_name
    Run_Adb_Cmd(dev_id, cmd)

# Function to remove directory
# Usage: remove_dir(self.tc_details['dev0'], "/sdcard/Bt_files/")
def remove_dir(dev_id, dir_name):
    cmd = "shell rm -r " + dir_name
    Run_Adb_Cmd(dev_id, cmd)

# Function to push file
# Usage: push(self.tc_details['dev0'], "../video/video.3gp", "/sdcard/Video" )
def push(dev_id, from_path ,to_path):
    cmd = "push " + from_path + " " + to_path
    val = Run_Adb_Cmd(dev_id, cmd)
    return val

# Function to pull file
# Usage: pull(self.tc_details['dev0'], "../video/video.3gp", "/sdcard/Video")
def pull(dev_id, from_path ,to_path):
    cmd = "pull " + from_path + " " + to_path
    val = Run_Adb_Cmd(dev_id, cmd)
    return val


def read_file_sdcard(dev_id):
    cmd = "shell cat /sdcard/Sample/Hello.txt."  
    Run_Adb_Cmd(dev_id, cmd)




#Function to pull down notification bar on the device
#Usage: bt_notification_swipe(self.tc_details['dev0'])
def bt_notification_swipe(dev_id):
    cmd = "shell sendevent /dev/input/event4 1 330 1"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 48 576"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 58 224"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 53 205"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 54 25"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 0 2 0"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 0 0 0"
    Run_Adb_Cmd(dev_id, cmd)

    cmd = "shell sendevent /dev/input/event4 3 48 335"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 58 465"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 53 203"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 54 767"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 0 2 0"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 0 0 0"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 1 330 0"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 48 0"
    Run_Adb_Cmd(dev_id, cmd)
    cmd = "shell sendevent /dev/input/event4 3 58 0"
    Run_Adb_Cmd(dev_id, cmd)
    return	




# Function to simulate connection of device (plugging in of USB cable) using the relay
# Usage: reconnect_usb()
def reconnect_usb(dev_num=0):    
    tc_log('Creating socket to connect USB', 'INFO')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((tc_details['usb_relay_ip'] , int(tc_details['usb_relay_port'])))

    tc_log('Sending command connectusb to server', 'INFO')
    client_socket.send('connectusb')
    time.sleep(2)
    client_socket.send('q')
    client_socket.close()
    return

# Function to simulate disconnection of device (pulling out the USB cable) using the relay
# Usage: disconnect_usb()
def disconnect_usb(dev_num=0):
    tc_log('Creating socket to disconnect USB', 'INFO')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((tc_details['usb_relay_ip'] , int(tc_details['usb_relay_port'])))

    tc_log('Sending command disconnectusb to server', 'INFO')
    client_socket.send('disconnectusb')
    time.sleep(2)
    client_socket.send('q')
    client_socket.close()
    return

# Function to open Intermec Scanner Settings   
#Usage: open_scanner_settings(self.tc_details['dev0'])
def open_scanner_settings(dev_id):
    cmd = "shell am start -n com.intermec.datacollectionservice/.settings.SettingsActivity"
    Run_Adb_Cmd(dev_id, cmd)




# Function to take backup of the DUT 	#todo:backup stucks, check.
#Usage: backup(self.tc_details['dev0'])
def backup(dev_id):
    cmd = "backup -all &"
    Run_Adb_Cmd(dev_id, cmd)



# Function to restore backup of the DUT		
#Usage: restore_backup(self.tc_details['dev0'])
def restore_backup(dev_id):
    cmd = "restore backup.ab"
    Run_Adb_Cmd(dev_id, cmd)



# Function to launch hardware scan button
#Usage: launch_scan_button(self.tc_details['dev0'])
def launch_scan_button(dev_id):
    cmd="shell am broadcast -a com.intermec.datacollectionservice.intent.action.EXECUTE -e com.intermec.datacollectionservice.intent.extra.JSON_RPC \'{\\\"jsonrpc\\\":\\\"2.0\\\"\,\\\"method\\\":\\\"scanner.iscp\\\"\,\\\"params\\\":{\\\"device\\\":\\\"dcs.scanner.imager\\\"\,\\\"iscp\\\":[65,112,64,3]}}\'"
    Run_Adb_Cmd(dev_id, cmd)



# Function to bring back the scanner to default operations
#Usage: stop_scan_button(self.tc_details['dev0'])
def stop_scan_button(dev_id):
    cmd = "shell am broadcast -a com.intermec.datacollectionservice.intent.action.EXECUTE -e com.intermec.datacollectionservice.intent.extra.JSON_RPC \'{\\\"jsonrpc\\\":\\\"2.0\\\"\,\\\"method\\\":\\\"scanner.iscp\\\"\,\\\"params\\\":{\\\"device\\\":\\\"dcs.scanner.imager\\\"\,\\\"iscp\\\":[65,112,64,1]}}\'"
    Run_Adb_Cmd(dev_id, cmd)

# Function to launch hardware scan button on marshmellow
#Usage: launch_scan_button_mm(self.tc_details['dev0'])
def launch_scan_button_mm(dev_id):
    cmd="shell am broadcast -a com.honeywell.intent.action.SCAN_BUTTON --ez test true"
    Run_Adb_Cmd(dev_id, cmd)

# Function to stop hardware scan button on marshmellow
#Usage: stop_scan_button_mm(self.tc_details['dev0'])
def stop_scan_button_mm(dev_id):
    cmd="shell am broadcast -a com.honeywell.intent.action.SCAN_BUTTON --ez test false"
    Run_Adb_Cmd(dev_id, cmd)


# Function to simulate connection of ethernet (plugging in of ethernet cable) using the relay
# Usage: connect_ethernet(self.tc_details['dev0'])
def connect_ethernet():
    return

# Function to simulate disconnection of ethernet (pulling out the ethernet cable) using the relay
#Usage: disconnect_ethernet(self.tc_details['dev0'])
def disconnect_ethernet():
    return

#.......Wi-Fi related functions......#
#Usage: open_wifi_settings(self.tc_details['dev0'])
#opening wifi settings directly
def open_wifi_settings(dev_id):
    cmd = "shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings"
    Run_Adb_Cmd(dev_id, cmd)

# Function to open device settings
def open_device_settings(dev_id):
    cmd = "shell am start -a android.settings.SETTINGS"
    Run_Adb_Cmd(dev_id, cmd)

# Function to enter the wifi password
def enter_wifi_password(dev_id, password):
    Run_Adb_Cmd(dev_id, "shell input text %s"%(password))

# Function to scroll up
def scroll_up(dev_id):
    cmd = "shell input touchscreen swipe 300 600 300 130"
    Run_Adb_Cmd(dev_id, cmd)

# Function to scroll down
def scroll_down(dev_id):
    cmd = "shell input touchscreen swipe 300 130 300 600"
    Run_Adb_Cmd(dev_id, cmd)

# Function to check the wifi status
def wifi_status(dev_id):
    cmd = "shell am start -n com.android.settings/.wifi.WifiStatusTest"
    Run_Adb_Cmd(dev_id, cmd)


def search_ssid(dev_id, ssid_name, duration=60):
    init_time = time.time()
    #duration = 60
    dev_str = 'ui_dev' + str(dev_id)
    ret_val = False

    while True:
        # Check the current time and see if we are searching for more than the specified duration. If so, abort the search and fail TC
        cur_time = time.time()
        diff = cur_time - init_time
	print cur_time, init_time, diff
        if(diff > duration):
            # Exit this loop with the objective of ending the test case!
	    tc_log('Could not locate SSID %s. Searched for %d secs. Aborting search!'%(ssid_name, duration), 'INFO')
            ret_val = False
	    break

	# Search the ssid_name using the UIAutomator. If not found, scroll up and search.
        print tc_details[dev_str]
        if(tc_details[dev_str](text=ssid_name).exists):
            tc_log("SSID %s listed"%(ssid_name), 'INFO')
	    ret_val = True              
            break
        else:
	    tc_log('Could not locate SSID %s. Scrolling up...'%ssid_name, 'INFO')	
            scroll_up(tc_details['dev' + str(dev_id)])

	time.sleep(3)

    return ret_val


# Function to reset the device
def reset_device(dev_id):
    cmd = "shell recovery --wipe_data"
    Run_Adb_Cmd(dev_id, cmd)

# Function to open browser and browse a google site.
def open_browser_site(dev_id, url):
    cmd = "shell am start -a android.intent.action.VIEW -d %s" %url
    Run_Adb_Cmd(dev_id, cmd)

# Function to press a Tab
def press_Tab(dev_id):
    Run_Adb_Cmd(dev_id,"shell input keyevent 61")

# Function to find the ip address of wifi
def find_connected_wifi_ip(dev_id):
    Run_Adb_Cmd(dev_id,"shell ifconfig wlan0 ")

# Function to find the ip address of wifi
def find_static_ip(dev_id):
    Run_Adb_Cmd(dev_id,"shell ifconfig wlan0 ")
	
# Function to launch a browser and open url

'''def open_browser(dev_id, url):
    tc_log("Launching browser and opening website..", 'INFO')
    open_browser_site(dev_id, url )  # Launching browser
    try:		
        dut0(text = "Browser").click()   # Handling pop-ups specific to native browser
        dut0(text = "Always").click()
    except Exception as e:
        pass

    time.sleep(10)
    close_app(dev_id, 'browser') '''


#--------------------------------------------------------------------------------------------------------------

# Function to open Google quick search
# Usage: open_google_quick_search(self.tc_details['dev0'])
def open_google_quick_search(dev_id):
    cmd = "shell am start com.google.android.googlequicksearchbox/.SearchActivity"
    Run_Adb_Cmd(dev_id, cmd)



# Function to open Google Play Books
# Usage: open_google_play_books(self.tc_details['dev0'])
def open_google_play_books(dev_id):
    cmd = "shell am start com.google.android.apps.books/.app.BooksActivity"
    Run_Adb_Cmd(dev_id, cmd)

# Function to open youtube
# Usage: open_youtube(self.tc_details['dev0'])
def open_youtube(dev_id):
    cmd = "shell am start com.google.android.youtube"
    Run_Adb_Cmd(dev_id, cmd)


# Function to open Desk clock
# Usage: open_deskclock(self.tc_details['dev0'])
def open_deskclock(dev_id):
    cmd = "shell am start com.android.deskclock"
    Run_Adb_Cmd(dev_id, cmd)

#----------------------------------------OS PACKAGE INSTALLATION FUNCTIONS--------------------------------------#

# Function to reboot for fastboot
# Usage: reboot_fast_boot(self.tc_details['dev0'])
def reboot_fast_boot(dev_id):
    tc_log("Reboots boot loader to set up the DUT for the OS Package installation", 'INFO')
    cmd = "reboot-bootloader"
    Run_Adb_Cmd(dev_id, cmd)

# Usage: reboot_the_device('0','20')
'''def reboot_the_device(dev_id, duration):
    tc_log("Before reboot", 'INFO')
    reboot_device(tc_details['dev' + str(dev_id)])
    # This is time to allow the device to reboot
    tc_log("This is time to allow the device to reboot", 'INFO')
    while True:
        return_val = list_device(tc_details['dev' + str(dev_id)])
	search_str = tc_details['dev' + str(dev_id)] + "	device"
	if return_val.find(search_str) != -1 :
	    tc_log("Device has rebooted!", 'INFO')
	    tc_log("The UI takes %s seconds to be up"%(duration), 'INFO')
	    time.sleep(float(duration)) # This is because the UI takes time to be up
	    screen_unlock(tc_details['dev' + str(dev_id)])
	    goto_home_screen(tc_details['dev' + str(dev_id)])
	    tc_log("after reboot", 'INFO')
	    break
	time.sleep(1)
    
    time.sleep(float(duration))
    return'''
	
	
# Usage: reboot_the_device('0', 10)
def reboot_the_device(dev_id, duration):
    global loganalyzer
    tc_log("Before reboot", 'INFO')
    reboot_device(tc_details['dev' + str(dev_id)])
    # This is time to allow the device to reboot
    tc_log("This is time to allow the device to reboot", 'INFO')
    while True:
        return_val = list_device(tc_details['dev' + str(dev_id)])
	search_str = tc_details['dev' + str(dev_id)] + "	device"
	if return_val.find(search_str) != -1 :
	    while True:	        
		try:
		    screen_unlock(tc_details['dev' + str(dev_id)])
		    goto_home_screen(tc_details['dev' + str(dev_id)])
		    time.sleep(3)		    			
		    if tc_details['ui_dev' + str(dev_id)](description="Apps").exists:
		        tc_log("Home screen up!", "INFO")
			tc_log("Signal the loganalyzer to restart the adb logcat capture", "INFO")
			loganalyzer[int(dev_id)].restart_adb = True
	    
			time.sleep(2)		    			
			break
		except Exception as e:
		    tc_log("Device home screen not yet up...", "INFO")
                    time.sleep(1)
		    pass		    		    
	    break
	time.sleep(1)        
    return 




	
			
# Function to install OS Package with GMS on device
# Usage: install_os(0)
def install_os(dev_num):
    dev_id = 'dev' + str(dev_num)
    ui_dev_id= 'ui_dev' + str(dev_num)

    # Check if the required directory to install OS from, is present in the DUT
    tc_log("\nCheck if the required directory to install OS from, is present in the DUT", 'INFO')
    ls = view_dut_files(tc_details[dev_id], "/ipsm")
    if "media" in ls:
	tc_log("DUT contains '/ipsm/media' directory", 'INFO')
    else:
        tc_log("DUT doesn't have '/ipsm/media' directory", 'INFO')
	raise TCFailureError 

    # Check if the session config file contains the OS Image Name
    tc_log("\nCheck if the session config file contains the OS Image Name", 'INFO')
    if config_strings['dev' + str(dev_num)]['image'] in tc_details:
	tc_log("Session Config file contains the required OS Image Name", 'INFO')
    else:
        tc_log("Session Config file doesn't contain the required OS Image Name", 'INFO')
	raise TCFailureError 

    # Check if the required OS Image exists in the PC
    tc_log("\nCheck if the required OS Image exists in the PC", 'INFO')
    if os.path.isfile("../../../os_images/" + tc_details[config_strings['dev' + str(dev_num)]['image']]):
	tc_log("%s exists in the PC" % config_strings['dev' + str(dev_num)]['image'], 'INFO')	
    else:
	tc_log("%s doesn't exist in the PC" % config_strings['dev' + str(dev_num)]['image'], 'INFO')
	raise TCFailureError

    # Check if the required OS Image exists in the DUT, if not push it
    tc_log("\nCheck if the required OS Image exists in the DUT, if not push it", 'INFO')
    ls = view_dut_files(tc_details[dev_id], "/ipsm/media")
    if tc_details[config_strings['dev' + str(dev_num)]['image']] in ls:
	tc_log("%s is already present in the DUT" % config_strings['dev' + str(dev_num)]['image'], 'INFO')
    else:
	tc_log("Push the OS Image to the DUT", 'INFO')
    	push_status = push(tc_details[dev_id], "../../../os_images/" + tc_details[config_strings['dev' + str(dev_num)]['image']], "/ipsm/media/")  
	time.sleep(1)		 
    	if push_status == "error":
	    tc_log('Failed to push the OS Image to the DUT', 'INFO')
	    raise TCFailureError	
     
    cmd = "shell \"echo \"--update_package=/ipsm/media/%s\" > /cache/recovery/command\"" % tc_details[config_strings['dev' + str(dev_num)]['image']]
    Run_Adb_Cmd(tc_details[dev_id], cmd)            
    time.sleep(1)                
    cmd = "shell \"echo \"--wipe_data\" > /cache/recovery/command\""
    Run_Adb_Cmd(tc_details[dev_id], cmd)
    time.sleep(3)
    dut_recovery_mode(dev_num) 
  
    tc_log('Starting thread to handle popups', 'INFO')
    tc_details['popup_thread']=popup_thread("popup thread", dev_num)
    tc_details['popup_thread'].start()    
    while True:
        return_val = list_device(tc_details[dev_id])
	search_str = tc_details[dev_id] + "	device"
	if return_val.find(search_str) != -1 :
	    while True:	  
	        try:
	    	    # Recreate the UIAutomator instance
                    tc_details[ui_dev_id] = Device(tc_details[dev_id])
	    	    start_coord = tc_validate_image(tc_details[dev_id], "../images/Factory_reset_start_button.png", 'WARN', 3)
	    	    if start_coord != (-1, -1):
	    	    	tc_log( "Welcome screen up!",'INFO')

		    	# Turn OFF Mobile data
			enable_disable_settings(tc_details[dev_id],  "data", "disable")
	    	    	time.sleep(3)
	    	        
	    	    	# Enable stay awake to keep the device screen on
	    	    	cmd = "shell svc power stayon usb"
	    	    	Run_Adb_Cmd(tc_details[dev_id], cmd)

	    	    	# To Enable Installation from Unknown Sources 
	    	    	cmd = "shell settings put secure install_non_market_apps 1"
	    	    	Run_Adb_Cmd(tc_details[dev_id], cmd)
	    	    	time.sleep(3)		    		
	    	    	break	   
	    	    else:
	    	    	# Enable stay awake to keep the device screen on
	    	    	cmd = "shell svc power stayon usb"
	    	    	Run_Adb_Cmd(tc_details[dev_id], cmd)
	    	        tc_log("Welcome string NOT FOUND!", "INFO")
	    	        time.sleep(30)
	    	    	
	    	except Exception as e:		        
	    	    tc_log("Welcome screen not yet up...",'INFO')
	    	    # Enable stay awake option
	    	    cmd = "shell svc power stayon usb"
	    	    Run_Adb_Cmd(tc_details[dev_id], cmd)
	    	    time.sleep(60)	# To make Welcome screen not yet up message display every 1 min
	    	    pass
	    	    		    	    	    
	    break
	time.sleep(50) # To make reboot device message display every 1 min

            
    # Call the initial set up function
    init_setup(dev_num)
             
    # Enable stay awake to keep the device screen on
    enable_stayAwake_developerOptions(dev_num)
    
    # To disable google security popup (ACCEPT or CONTINUE)
    cmd = "shell settings put global package_verifier_enable 0"
    Run_Adb_Cmd(tc_details[dev_id], cmd)                
    tc_log("********************OS Installation Completed*******************","INFO")
    time.sleep(10)
    return


# Function to do DUT's Initial setup after OS Installation
# Usage : init_setup(dev_num)
def init_setup(dev_num):
    dev_id = 'dev' + str(dev_num)
    ui_dev_id= 'ui_dev' + str(dev_num)
    tc_log('\nInitial setup started', 'INFO')

    # Initial setup starts            
    # Select English (United States) language from session config file 
    tc_log('Select Language', 'INFO')	    
    tc_details[ui_dev_id](className='android.widget.Button',resourceId='com.google.android.setupwizard:id/language_picker').click()
    time.sleep(3)
    if tc_details[ui_dev_id](text=tc_details['device_language']).exists:
    	    tc_details[ui_dev_id](text=tc_details['device_language']).click()
    else:
    	    tc_details[ui_dev_id](scrollable=True).scroll.to(text=tc_details['device_language'])
    	    time.sleep(3)
    	    tc_details[ui_dev_id](text=tc_details['device_language']).click() #ToDO: Change to device_language
    time.sleep(5)
        
    # Click the message popup
    if tc_details[ui_dev_id](className='android.widget.Button',resourceId='com.android.vending:id/positive_button').exists:
        tc_details[ui_dev_id](className='android.widget.Button',resourceId='com.android.vending:id/positive_button').click()
    time.sleep(5)

    if tc_details['dev' + str(dev_num) + '_type'] == "ct50":
        Run_Adb_Cmd(tc_details[dev_id], "shell input tap 41 49")
        Run_Adb_Cmd(tc_details[dev_id], "shell input tap 650 49")
        Run_Adb_Cmd(tc_details[dev_id], "shell input tap 655 1197")
        Run_Adb_Cmd(tc_details[dev_id], "shell input tap 47 1221")

    elif tc_details['dev' + str(dev_num) + '_type'] == "cn51":
        Run_Adb_Cmd(tc_details[dev_id], "shell input tap 95 111")
        Run_Adb_Cmd(tc_details[dev_id], "shell input tap 418 106")
        Run_Adb_Cmd(tc_details[dev_id], "shell input tap 414 637")
        Run_Adb_Cmd(tc_details[dev_id], "shell input tap 44 657")
    time.sleep(5)

    tc_validate_screentext(dev_num, "GOT IT", 'WARN', 30)
    if tc_details[ui_dev_id](text="GOT IT").exists:
    	tc_details[ui_dev_id](text="GOT IT").click() 
    if tc_validate_screentext(dev_num, "Apps", 'WARN', 150):
	tc_log('Initial setup completed', 'INFO')
    else:	
	tc_log('DUT did not reach HOME Screen after tap', 'INFO')
 	raise TCFailureError
    return








#Function to Add Google Account to device
#Usage : add_google_account(0)
def add_google_account(dev_num):
    dev_id = 'dev' + str(dev_num)
    ui_dev_id= 'ui_dev' + str(dev_num)
    open_settings(tc_details[dev_id], "Settings" )
    tc_validate_screentext(dev_num,"Settings",'WARN',15)
    tc_details[ui_dev_id](scrollable=True).scroll.to(text='Accounts')
    tc_details[ui_dev_id](text='Accounts').click()
    tc_validate_screentext(dev_num,"Google",'WARN',15)
    if tc_details[ui_dev_id](text='Google').exists:
    	    tc_log("Account already added",'INFO')
    else:
    	    tc_validate_screentext(dev_num,"Add account",'WARN',15)
    	    tc_details[ui_dev_id](text='Add account').click()
    	    tc_validate_screentext(dev_num,"Google",'WARN',15)
    	    tc_details[ui_dev_id](text='Google').click()
    	    tc_validate_screentext(dev_num, "Add your account", 'FAIL', 120)
    	    #tc_details[ui_dev_id](className='android.widget.EditText',resourceId='identifierId').click()
    	    DPad_right(tc_details[dev_id])
    	    input_text(tc_details[dev_id], tc_details['google_id'])
    	    tc_details[ui_dev_id](description='NEXT',resourceId="identifierNext",className="android.widget.Button").click()
    	    tc_validate_screentext(dev_num, "Forgot password?", "FAIL", 50)
    	    DPad_right(tc_details[dev_id])
    	    input_text(tc_details[dev_id], tc_details['google_passwd'])
            tc_details[ui_dev_id](description='NEXT',resourceId="passwordNext",className="android.widget.Button").click()
    	    tc_validate_screentext(dev_num, "ACCEPT", "WARN", 50)
    	    time.sleep(2)
    	    tc_details[ui_dev_id](description='ACCEPT',className='android.widget.Button',resourceId='next').click()
    	    tc_validate_screentext(dev_num,'Google services','WARN', 150)
    	    tc_details[ui_dev_id](scrollable=True).fling.vert.toEnd()
    	    tc_details[ui_dev_id](text='Next').click()
    	    if tc_validate_screentext(dev_num, "Set up payment info", "WARN", 120)==1:
    	    	    tc_validate_screentext(dev_num, "No thanks", "WARN", 20)
    	    	    if tc_details[ui_dev_id](text='No thanks').exists:
    	    	    	    tc_details[ui_dev_id](text='No thanks').click()   
    	    	    else:
    	    	    	    tc_details[ui_dev_id](scrollable=True).fling.vert.toEnd()
    	    	    	    tc_details[ui_dev_id](text='No thanks').click()
    	    	    tc_validate_screentext(dev_num, "Continue", "WARN", 10)
    	    	    tc_details[ui_dev_id](text='Continue').click()
    	    time.sleep(3)
    	    clear_package(tc_details[dev_id], "com.android.settings")
    	    goto_home_screen(tc_details[dev_id])
    	    
    return


#-------------------------------------------------------------------------------------------------------------------#

#Usage: initial_setup(dev_num):
#Function to do initial setup

def initial_setup(dev_num):

    dev_id = 'dev' + str(dev_num)
    ui_dev_id= 'ui_dev' + str(dev_num)
    
    #tc_details[ui_dev_id].watcher("Initial setup Popup_1").when(text="DECLINE").click(text="ACCEPT")
    #tc_details[ui_dev_id].watcher("Initial setup Popup_2").when(text="स्वीकार करें").click(text="स्वीकार करें")  
    tc_log("Initial set up started", "INFO")    
    
    #if welcome screen in hindi to select language options ToDo: Check is Welcome is actually seen on screen (using resource id/desc/classname)
    tc_log("Factory Reset: Selecting language setup - Taking language setting from session config", "INFO")
    
    #check_for_security_popup(dev_num)
    
    #Select English (United States) language from session config file 
    tc_details[ui_dev_id](className='android.widget.Button',resourceId='com.google.android.setupwizard:id/language_picker').click()
    time.sleep(3)
    if tc_details[ui_dev_id](text=tc_details['device_language']).exists:
    	    tc_details[ui_dev_id](text=tc_details['device_language']).click()
    else:
    	    tc_details[ui_dev_id](scrollable=True).scroll.to(text="English (United States)")
    	    time.sleep(3)
    	    tc_details[ui_dev_id](text=tc_details['device_language']).click() #ToDO: Change to device_language
    time.sleep(5)
    
    #check_for_security_popup(dev_num)
    
    # Click the message popup
    if tc_details[ui_dev_id](className='android.widget.Button',resourceId='com.android.vending:id/positive_button').exists:
        tc_details[ui_dev_id](className='android.widget.Button',resourceId='com.android.vending:id/positive_button').click()
    
    #First step to do click Start
    tc_log("Factory Reset: Selecting Start button to continue with setup", "INFO")
    tc_validate_screentext(dev_num,"Start",'WARN',15)
    tc_details[ui_dev_id](description='Start',resourceId="com.google.android.setupwizard:id/start",className="android.widget.ImageButton").click()
    time.sleep(30)
    
    #check_for_security_popup(dev_num)
    
    #May or maynot come Activating cellular networks
    if tc_details[ui_dev_id](text='Activating cellular service…').exists:    
        tc_log("Factory Reset: Activating cellular services if SIM inserted", "INFO")    
        tc_details[ui_dev_id](text='Skip').click()
        tc_validate_screentext(dev_num,"Skip anyway",'WARN',15)
        tc_details[ui_dev_id](text='Skip anyway').click()
        tc_validate_screentext(dev_num,"Insert SIM card",'WARN',15)
        
    #May or maynot come Second step sim card details it just skip
    if tc_details[ui_dev_id](text='Insert SIM card').exists:
	tc_log("It enters into insert sim card section and click skip","INFO")
	tc_details[ui_dev_id](text='Skip').click()
        tc_validate_screentext(dev_num,"Select Wi‑Fi network",'WARN',15)

    #check_for_security_popup(dev_num)
    
    #Second step to select Wi-Fi network
    if tc_details[ui_dev_id](text='Select Wi‑Fi network').exists:
        tc_log("Factory Reset: Skipping Wi-Fi Activation for later","INFO")
        tc_details[ui_dev_id](text='Skip').click()
        tc_validate_screentext(dev_num,"Skip anyway",'WARN',15)
        tc_details[ui_dev_id](text='Skip anyway').click()
        time.sleep(5)
        tc_validate_screentext(dev_num,"Name",'WARN',15)
    time.sleep(2)
        
    #May or maynot come at this point for some devices
    if tc_details[ui_dev_id](text='Name').exists:
    	tc_log("It enters into First & Last Name section and click next","INFO")
     	time.sleep(3)
     	input_text(tc_details[dev_id], tc_details['name'])
     	if tc_details[ui_dev_id](text="Next").exists:
     		tc_details[ui_dev_id](text="Next").click()
     	else:
     		tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
     		tc_details[ui_dev_id](text="Next").click()
     	tc_validate_screentext(dev_num,"Date & time",'WARN',15)
    time.sleep(2)
    #Third step To select Date & time
    if tc_details[ui_dev_id](text= 'Date & time').exists:
        tc_log("It select Date & time and click Next","INFO")
        tc_details[ui_dev_id](className='android.widget.TextView',resourceId='android:id/text1').click()
        tc_validate_screentext(dev_num,tc_details['time_zone'],'WARN',5)
        tc_details[ui_dev_id](scrollable=True).scroll.to(text=tc_details['time_zone'])
        tc_details[ui_dev_id](text=tc_details['time_zone']).click()
        tc_details[ui_dev_id](text="Next").click()  
        
    #check_for_security_popup(dev_num)
    
    #Fourth step Waiting  for Text May come or may not come
    ret_val_1=tc_validate_screentext(dev_num,"Got another device?",'WARN',50)
    ret_val_2=tc_validate_screentext(dev_num,"Have another device?",'WARN',10)
    
    if ret_val_1==1 or ret_val_2==1:
    	tc_log("Factory Reset: Skipping device backup","INFO")
    	tc_log("It enters Got another device setp","INFO")
    	tc_validate_screentext(dev_num,"No thanks",'WARN',15)
     	tc_details[ui_dev_id](text='No thanks').click()
     	tc_validate_screentext(dev_num,"Next",'WARN',15)
     	tc_details[ui_dev_id](text='Next').click()
     	
     	tc_log("Factory Reset: Skipping adding Google account","INFO")
        tc_validate_screentext(dev_num,"Add your account",'WARN',50)
        tc_validate_screentext(dev_num,"MORE",'WARN',15)
        tc_details[ui_dev_id](description='MORE',className='android.widget.Button',resourceId='more').click()
        tc_validate_screentext(dev_num,"SKIP",'WARN',15)
        tc_details[ui_dev_id](description='SKIP',className='android.widget.Button',resourceId="skip").click()
        tc_validate_screentext(dev_num,"SKIP",'WARN',15)
        tc_log("Factory Reset: Google accout sign in skipped","INFO")        
        tc_details[ui_dev_id](description='SKIP',className="android.widget.Button",resourceId="skipdialog-skip").click()
        tc_validate_screentext(dev_num,"Name",'WARN',15)
    #Fifth step Name section    
    if tc_details[ui_dev_id](text='Name').exists:
    	tc_log("It enters into First & Last Name section and click next","INFO")
     	time.sleep(5)
     	input_text(tc_details[dev_id], tc_details['name'])
     	if tc_details[ui_dev_id](text="Next").exists:
     	    tc_details[ui_dev_id](text="Next").click()
     	else:
     	    tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
     	    tc_details[ui_dev_id](text="Next").click()
     	
     	tc_validate_screentext(dev_num,"Set up email",'WARN',15)
    
    #May or maynot come Set up email 
    if tc_details[ui_dev_id](text='Set up email').exists:
    	tc_details[ui_dev_id](text="Not now").click()
    	tc_validate_screentext(dev_num,"Next",'WARN',15)
        tc_details[ui_dev_id](text="Next").click()
        tc_validate_screentext(dev_num,"Protect your phone",'WARN',15)
     	
    #Sixth step Google services or Protect your phone
    if tc_details[ui_dev_id](text='Protect your phone').exists:
    	tc_log("Factory Reset: Skipping Protect your phone section","INFO")
        tc_details[ui_dev_id](text='Protect this device and require a PIN, pattern, or password to unlock the screen').click()
        tc_validate_screentext(dev_num,"Skip",'WARN',15)
        tc_details[ui_dev_id](text='Skip').click()
	tc_validate_screentext(dev_num,"Skip anyway",'WARN',15)
        tc_details[ui_dev_id](text='Skip anyway').click()
        time.sleep(5)
        tc_log("Factory Reset: It enters into Google services section and click next","INFO")
        tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
        tc_validate_screentext(dev_num,"Next",'WARN',15)
        tc_details[ui_dev_id](text="Next").click()
        tc_validate_screentext(dev_num,"GOT IT",'WARN',15)
        tc_details[ui_dev_id](text='GOT IT').click()
        tc_log("********************Initial Setup completed:*******************","INFO")
    else:
        tc_log("Factory Reset: It enters into Google services section and click next","INFO")
        if tc_details[ui_dev_id](text="Next").exists:
     	    tc_details[ui_dev_id](text="Next").click()
     	else:
     	    tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
     	    tc_validate_screentext(dev_num,"Next",'WARN',15)
     	    tc_details[ui_dev_id](text="Next").click()
     	    tc_validate_screentext(dev_num,"GOT IT",'WARN',15)
        tc_details[ui_dev_id](text='GOT IT').click()
        tc_log("********************Initial Setup completed:*******************","INFO")  
     	
    return 	


    
# Function to Enable Stay awake and Developer option
#Usage: enable_stayAwake_developerOptions(dev_num)

def enable_stayAwake_developerOptions(dev_num):    
    dev_id = 'dev' + str(dev_num)
    ui_dev_id= 'ui_dev' + str(dev_num)
    #To Enable stay awake on the device
    cmd = "shell svc power stayon usb"
    Run_Adb_Cmd(tc_details[dev_id], cmd)
    tc_log("Stay awake Enabled on the device","INFO")
    open_settings(tc_details[dev_id], "Settings" )
    tc_validate_screentext(dev_num,"Settings",'WARN',15)
    tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
    tc_details[ui_dev_id](text='About phone').click()
    time.sleep(3)
    tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
    time.sleep(2)
    for i in range(8):
	    tc_details[ui_dev_id](text='Build number').click()
	    time.sleep(1)
    tc_log("Developer option Enabled on the device","INFO")	
    # Clear all recent apps - hardcoded to 6 apps currently
    Run_Adb_Cmd(tc_details[dev_id], "shell input keyevent KEYCODE_APP_SWITCH")
    Run_Adb_Cmd(tc_details[dev_id], "shell input keyevent 20")
    Run_Adb_Cmd(tc_details[dev_id], "shell input keyevent 20")
    for i in range (3):
    	    Run_Adb_Cmd(tc_details[dev_id], "shell input keyevent DEL")
    	    
    #clear_package(tc_details[dev_id], "com.android.settings")
    goto_home_screen(tc_details[dev_id])
    
    return  
            
#-----------------------------------------------------------------------------------------------------------------------------#


# Function to do factory Reset Device
#Usage: factory_reset_device(0)
#Function to launch factory reset it will erase everything in your device(such as apps,contacts etc.,)

def factory_reset_device(dev_num, status='True'):
    dev_id = 'dev' + str(dev_num)
    ui_dev_id= 'ui_dev' + str(dev_num)
    tc_log("********** Factory reset the device %s **********" % tc_details[dev_id], 'INFO')    
    goto_home_screen(tc_details[dev_id])
    open_settings(tc_details[dev_id], "Settings")
    tc_validate_screentext(dev_num,"Settings",'WARN',15)
    if tc_details[ui_dev_id](text='Backup & reset').exists:
    	    tc_details[ui_dev_id](text='Backup & reset').click()
    else:
    	    tc_details[ui_dev_id](scrollable=True).scroll.to(text='Backup & reset')
    	    tc_details[ui_dev_id](text='Backup & reset').click()
    tc_validate_screentext(dev_num,"Factory data reset",'WARN',15)
    tc_details[ui_dev_id](text='Factory data reset').click()
    tc_validate_screentext(dev_num,"Reset phone",'WARN',15)
    tc_details[ui_dev_id](text='Reset phone').click()
    tc_validate_screentext(dev_num,"Erase everything",'WARN',15)
    tc_details[ui_dev_id](text='Erase everything').click()
    tc_log("****************************************factory reset started:***************************************","INFO")
    # This is time to allow the device to reboot
    tc_log("This is time to allow the device to started factory reset", 'INFO')
    time.sleep(180) #time to start factory reset(some devices take time to start)

    # Start the thread to respond to security popups
    #popup_thread_exit = False
    #popup_thread = threading.Thread(target=check_for_security_popup, args=(0,))
    #popup_thread.start()
    tc_log('Starting thread to handle popups', 'INFO')
    tc_details['popup_thread']=popup_thread("popup thread", dev_num)
    tc_details['popup_thread'].start()

    while True:
        return_val = list_device(tc_details[dev_id])
	search_str = tc_details[dev_id] + "	device"
	if return_val.find(search_str) != -1 :
	    while True:	  
	    	    try:
	    	    	    tc_log ("try: Welcome screen not up yet...", 'INFO')
	    	    	    # Recreate the UIAutomator instance
                            tc_details[ui_dev_id] = Device(tc_details[dev_id])
	    	    	    #check_for_security_popup(dev_num)
	    	    	    start_coord = tc_validate_image(tc_details[dev_id], "../images/Factory_reset_start_button.png", 'WARN', 3)
	    	    	    if start_coord != (-1, -1):
	    	    	    #if (tc_details[ui_dev_id](text="Welcome").exists) or (tc_details[ui_dev_id](resourceId='com.google.android.setupwizard:id/welcome_title', className='android.widget.TextView', packageName='com.google.android.setupwizard').exists):
	    	    	    	    #check_for_security_popup(dev_num)
	    	    	    	    tc_log( "Welcome screen up!",'INFO')
	    	    	    	    #check_for_security_popup(dev_num)
	    	    	    	    
	    	    	    	    #Disable mobile data to avoid the security popup
	    	    	    	    cmd = "shell svc data disable"
	    	    	    	    Run_Adb_Cmd(tc_details[dev_id], cmd)

	    	    	    	    #Enable stay awake option to keep the device screen on
	    	    	    	    cmd = "shell svc power stayon usb"
	    	    	    	    Run_Adb_Cmd(tc_details[dev_id], cmd)

	    	    	    	    #To Enable unknown Sources
	    	    	    	    cmd = "shell settings put secure install_non_market_apps 1"
	    	    	    	    Run_Adb_Cmd(tc_details[dev_id], cmd)
	    	    	    	    time.sleep(3)		    		
	    	    	    	    break
	    	    	    else:
	    	    	    	    tc_log("Welcome string NOT FOUND!", "INFO")
	    	    	    	    time.sleep(30)
	    	    	    	    
	    	    except Exception as e:
	    	    	    tc_log("except: Device Welcome screen not yet up...",'INFO')
	    	    	    #Enable stay awake option
	    	    	    cmd = "shell svc power stayon usb"
	    	    	    Run_Adb_Cmd(tc_details[dev_id], cmd)
	    	    	    #Disable mobile data
	    	    	    cmd = "shell svc data disable"
	    	    	    Run_Adb_Cmd(tc_details[dev_id], cmd)
	    	    	    #os.system('adb kill-server')
	    	    	    #time.sleep(5)
	    	    	    #os.system('adb start-server')
	    	    	    time.sleep(50)#This for Welcome screen not yet up message will display every 60 sec
	    	    	    pass
	    	    	
	    	    	    
	    break
	time.sleep(60)#This for reboot device message 
            
    #tc_validate_screentext(self.tc_details['dev0'],"Welcome",2100)   
    
    initial_setup(dev_num)
    
    enable_stayAwake_developerOptions(dev_num)
    
    #To disable google security popup (ACCEPT or CONTINUE)
    cmd = "shell settings put global package_verifier_enable 0"
    Run_Adb_Cmd(tc_details[dev_id], cmd)
    
    #connecting wi-fi:
    tc_wifi_connect(dev_num)
    
    #Add a google account into the device
    if status == 'True':
    	    add_google_account(dev_num)
    	    #Disable contact_sync on the device
    	    disable_contact_sync(dev_num)
    	    #Disable auto_updates app from google play store
    	    disable_auto_app_updates(dev_num)
    else:
    	    tc_log("Account not added",'INFO')
    	    pass
    #Disable contact_sync on the device
    #disable_contact_sync(dev_num)
    
    #Disable auto_updates app from google play store
    #disable_auto_app_updates(dev_num)
    
    tc_log("********************Factory reset completed:*******************","INFO")
    

#-----------------------------------------------------------------------------------------------------------------------------------


# Usage: usb_options(self.tc_details['dev0'])
# Function to open USB options on DUT
def usb_options(dev_id):
    cmd = "shell am start -n com.android.settings/.deviceinfo.UsbModeChooserActivity"
    Run_Adb_Cmd(dev_id, cmd)
    return


# Usage: copy_in_dut(self.tc_details['dev0'], "/sdcard/Download/song.mp3", "/sdcard/Misc")
# Function to copy files in DUT
def copy_in_dut(dev_id, from_path, to_path):
    cmd = "shell cp -r " + from_path + " " + to_path
    status = Run_Adb_Cmd(dev_id, cmd)
    return status


# Function to list files in DUT
# Usage: list_files_dut(self.tc_details['dev0'], "Misc")
def list_files_dut(dev_id, directory_name):
    cmd = "shell ls /sdcard/" + directory_name
    val = Run_Adb_Cmd(dev_id, cmd)
    return val


# Usage: view_contents(self.tc_details['dev0'], "/sdcard/Misc/", "readme")
# Function to view SD Card storage file contents
def view_contents(dev_id, path, file_name):
    root_device(dev_id)
    time.sleep(4)
    cmd = "shell cat " + path + file_name
    content = Run_Adb_Cmd(dev_id, cmd)
    return content




 # Function to remove SD Card directory
# Usage: remove_sdcard_dir(self.tc_details['dev0'], "/sdcard/Misc/delete_this/")
def remove_sdcard_dir(dev_id, dir_name):
    cmd = "shell rm -r " + dir_name
    status = Run_Adb_Cmd(dev_id, cmd) 
    return status

    

    
#Usage: encrypt_device('0')
#Function to encrypt device
def encrypt_device(dev_num):
    tc_log("**********************FOR ENCRYPTION DEVICE MUST BE FULLY CHARGED AND CHARGER SHOULD BE CONNECTED*************************", "INFO")
    #Pre-condition: to encrypt device, device should be fully charged and charger/usb must be connected
    #Launch settings and from security option navigate to encryption option.
    open_settings(tc_details['dev' + str(dev_num)], "Settings" ) 
    tc_details['ui_dev' + str(dev_num)](scrollable=False).scroll.to(text="Security")
    tc_details['ui_dev' + str(dev_num)](text="Security").click()
    time.sleep(2)
    if tc_details['ui_dev' + str(dev_num)](text='Encrypted').exists:
        tc_log("Device is already encrypted", "INFO")
    elif tc_details['ui_dev' + str(dev_num)](text="Encrypt phone").click():
        time.sleep(3)
        tc_details['ui_dev' + str(dev_num)](className="android.widget.Button").click()
        time.sleep(3)
        tc_details['ui_dev' + str(dev_num)](text="Encrypt phone").click()
        while True:
            return_val = list_device(tc_details['dev' + str(dev_num)])
            search_str = tc_details['dev' + str(dev_num)]
            if return_val.find(search_str) != -1 :
                while True:	        
                	try:
                		screen_unlock(tc_details['dev' + str(dev_num)])
                		goto_home_screen(tc_details['dev' + str(dev_num)])
                		time.sleep(3)		    			
                		if tc_details['ui_dev' + str(dev_num)](description="Apps").exists:
                			tc_log("Home screen up!", "INFO")
			                tc_log("Signal the loganalyzer to restart the adb logcat capture", "INFO")
			                loganalyzer[int(dev_num)].restart_adb = True
                			time.sleep(3)		    			
                			break
                	except Exception as e:
                                tc_log("Device home screen not yet up...", "INFO")
                		time.sleep(1)
                		pass		    		 
                break
            time.sleep(1)  
        #time.sleep(5) 
        Run_Adb_Cmd(tc_details['dev' + str(dev_num)],"shell input keyevent 82")
        tc_log("********************Encryption Completed:*******************","INFO")
        time.sleep(10)
    return

# Function to clear logcat
# Usage: clear_logs('0')
def clear_logs(dev_id):
    tc_log("Clearing Logcat", 'INFO')
    cmd =' -s ' + tc_details['dev' + str(dev_id)] + ' logcat -c'
    Run_Adb_Cmd(dev_id, cmd)
    return


# Usage: move_in_dut(self.tc_details['dev0'], "/sdcard/Download/temp_files", "/sdcard/Misc")
# Function to move files in DUT
def move_in_dut(dev_id, from_path, to_path):
    cmd = "shell mv " + from_path + " " + to_path
    status = Run_Adb_Cmd(dev_id, cmd)
    return status




# Usage: read_file(self.tc_details['dev0'], "/sdcard/Misc/", "readme")
# Function to read file contents
def read_file(dev_id, path, file_name):
    root_device(dev_id)
    time.sleep(4)
    cmd = "shell cat " + path + file_name
    content = Run_Adb_Cmd(dev_id, cmd)
    return content


# Usage: view_dut_files(self.tc_details['dev0'], "/ipsm/media/logger")
# Function to view DUT's file system
def view_dut_files(dev_id, path):
    root_device(dev_id)
    time.sleep(4)
    remount_dut(dev_id)	
    cmd = "shell ls " + path
    ls = Run_Adb_Cmd(dev_id, cmd)
    return ls



# Usage: create_file(self.tc_details['dev0'], "/system/app/persistent.txt")
# Function to create file in the DUT's file system
def create_file(dev_id, path):
    root_device(dev_id)
    time.sleep(4)
    remount_dut(dev_id)	
    cmd = "shell touch " + path
    Run_Adb_Cmd(dev_id, cmd)
    return 



# Usage: delete_dut_file(self.tc_details['dev0'], "/system/app/persistent.txt")
# Function to delete file in the DUT's file system
def delete_dut_file(dev_id, path):
    #root_device(dev_id)
    #remount_dut(dev_id)	
    cmd = "shell rm " + path
    Run_Adb_Cmd(dev_id, cmd)
    return 

    


# Usage: check_disk_space(self.tc_details['dev0'])
# Function to check disk space in the DUT
def check_disk_space(dev_id):    
    cmd = "shell df"
    space = Run_Adb_Cmd(dev_id, cmd)
    return space





'''# Usage: check_sdcard_space(self.tc_details['dev0'])
# Function to check SD Card space in the DUT
def check_sdcard_space(dev_id):    
    cmd = "shell df"
    space = Run_Adb_Cmd(dev_id, cmd)
    return space '''



# Usage: remount_dut(self.tc_details['dev0'])
# Function to remount DUT
def remount_dut(dev_id):
    cmd = "remount"
    Run_Adb_Cmd(dev_id, cmd)
    return 
    




#Usage: initial_setup_fac(dev_num)
#Function to do initial setup

def initial_setup_fac(dev_num):

    dev_id = 'dev' + str(dev_num)
    ui_dev_id= 'ui_dev' + str(dev_num)
                   
    #First step to do click Start
    tc_log("It selects Start button","INFO")
    tc_details[ui_dev_id](description='Start').click()
          
    #Second step sim card details it just skip
    tc_log("It enters into insert sim card section and click skip","INFO")
    tc_details[ui_dev_id](text='Skip').click()
            
    #Third step To select Wi-Fi network in the list
    tc_log("It enters Wi-Fi section and click skip","INFO")
    tc_details[ui_dev_id](text='Skip').click()
    tc_details[ui_dev_id](text='Skip anyway').click()
    time.sleep(2)
            
    #Fourth step To select Date & time
    tc_log("It select Date & time and click Next","INFO")
    tc_details[ui_dev_id](className='android.widget.TwoLineListItem').click()
    time.sleep(5)
    #tc_details[ui_dev_id](text= tc_details['date_time']).click()
    tc_details[ui_dev_id](scrollable=True).scroll.to(text=tc_details['country'])
    tc_details[ui_dev_id](text=tc_details['country']).click()
    tc_details[ui_dev_id](text="Next").click()
            
    #Fifth step To give First & Last Name for the device
    tc_log("It enters into First & Last Name section and click next","INFO")
    input_text(tc_details[dev_id], tc_details['name'])
    tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
    tc_details[ui_dev_id](text="Next").click()
    time.sleep(8)
    #Sixth step Google services or Protect your phone
    if tc_details[ui_dev_id](text='Protect your phone').exists:
        tc_details[ui_dev_id](text='Protect this device and require a PIN, pattern, or password to unlock the screen').click()
        time.sleep(3)
        tc_details[ui_dev_id](text='Skip').click()
        time.sleep(5)
        tc_details[ui_dev_id](text='Skip anyway').click()
        time.sleep(3)
        tc_log("It enters into Google services section and click next","INFO")
        tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
        tc_details[ui_dev_id](text="Next").click()
        tc_details[ui_dev_id](text='GOT IT').click()
        tc_log("********************Initial Setup completed:*******************","INFO")
    else:
        tc_log("It enters into Google services section and click next","INFO")
        tc_details[ui_dev_id](scrollable=True).scroll.toEnd()
        tc_details[ui_dev_id](text="Next").click()
        tc_details[ui_dev_id](text='GOT IT').click()
        tc_log("********************Initial Setup completed:*******************","INFO")                         
    return 



#---------------------------------------------------------------------------------------------------------------------#

# Usage : left_scan(self.tc_details['ui_dev0'])
# Function to use left scan keyremap
def left_scan(dev_id):

    tc_log("*******************Entry point of left_scan function*****************",'INFO')
    if tc_details['dev0_type'] == "cn51" or tc_details['dev0_type'] == "CN51":
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 1 257 1")
        time.sleep(3)
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 0 0 0")  
        time.sleep(3)
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 1 257 0")
        time.sleep(3)
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 0 0 0")  
        time.sleep(3)
    elif tc_details['dev0_type'] == "ct50" or tc_details['dev0_type'] == "CT50":
    	Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 1 87 1")
    	time.sleep(3)
    	Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 0 0 0")
    	time.sleep(3)
    	Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 1 87 0")
    	time.sleep(3)
    	Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 0 0 0")
    	time.sleep(3)
        tc_log("*******************Exit point of left_scan function******************",'INFO')
    else:
    	tc_log("Unknown device type",'INFO')

    return 
   
   

    

# Usage : right_scan(self.tc_details['dev0'])
# Function to use middle scan keyremap
def right_scan(dev_id):    
    tc_log("*******************Entry point of middle_scan function*****************",'INFO')
    if tc_details['dev0_type'] == "cn51" or tc_details['dev0_type'] == "CN51": 
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 1 256 1")
        time.sleep(3)
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 0 0 0")  
        time.sleep(3)
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 1 256 0")
        time.sleep(3)
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 0 0 0")   
        time.sleep(3)
    elif tc_details['dev0_type'] == "ct50" or tc_details['dev0_type'] == "CT50":
    	Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 1 88 1")
    	time.sleep(3)
    	Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 0 0 0")
    	time.sleep(3)
    	Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 1 88 0")
    	time.sleep(3)
    	Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/event3 0 0 0")
    	time.sleep(3)
    else:
    	tc_log("Unknown device type",'INFO')
    	
    tc_log("*******************Exit point of middle_scan function******************",'INFO')
    return 


# Usage : long_right_scan(self.tc_details['ui_dev0'])
# Function to long press middle scan button
def long_right_scan(dev_id):    
    tc_log("********************Entry point of long press middle_scan function*******************",'INFO')
    time.sleep(5)
    tc_log("********************Exit point of long press middle_scan function*********************",'INFO')
    return 



# Usage : power_on(self.tc_details['dev0'])
# Function to power on the device
def power_on(dev_id):    
    tc_log("*************************Entry point of Power ON function**************************",'INFO')
    time.sleep(5)
    tc_log("*************************Exit point of Power ON function***************************",'INFO')
    return 




# Function to pull ipsm contents
# Usage: pull_ipsm_contents(self.tc_details['dev0'], "../images/tmp")
def pull_ipsm_contents(dev_id, tmp_path):
    cmd = "pull /storage/IPSM/Test" + " " + tmp_path
    Run_Adb_Cmd(dev_id, cmd)



# Function to delete internal sdcard contents
# Usage: rm_sdcard_contents(self.tc_details['dev0'])
def rm_ipsm_contents(dev_id):
    cmd = "shell rm -r /storage/IPSM"
    Run_Adb_Cmd(dev_id, cmd)

# Function to send sms to specific contact with message
# Usage: message_intent(self.tc_details['dev1'], self.tc_details['contact_number_0'], self.tc_details['message'])
def message_intent(dev_id, number, message):
    cmd = "shell am start -a android.intent.action.SENDTO -d sms:%s"%(number) + " --es sms_body \"%s\"" %(message) + " --ez exit_on_sent true"     
    Run_Adb_Cmd(dev_id, cmd)

# Usage: open_BT_GUI_settings(dev_id)
# Enable Bluetooth Settings
def open_BT_GUI_settings(dev_id):
    cmd = "shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings"
    Run_Adb_Cmd(dev_id, cmd)

# Function to play any music file
# Usage: play_music(self.tc_details['dev0'], "song.mp3", "mp3")
def play_music(dev_id, music_file, file_ext):
    cmd = "shell am start -a android.intent.action.VIEW -d file:/sdcard/Music/%s -t audio/%s" % (music_file, file_ext)
    Run_Adb_Cmd(dev_id, cmd)
    return


# Function to turn on Stay awake
# Usage: stay_awake(self.tc_details['dev0'])
def stay_awake(dev_id):
    cmd = "shell svc power stayon usb"
    Run_Adb_Cmd(dev_id, cmd)
    return
    

# Function to take a screenshot of the device
# Usage:take_screenshot(self.tc_details['dev0'],"home.png")
def take_screenshot(dev_id,image_name):
    tc_log("taking screenshot of the device", 'INFO')
    cmd ="shell /system/bin/screencap -p /sdcard/"+image_name
    Run_Adb_Cmd(dev_id, cmd)
    return



# Function to get the Device property information(User Information)
# Usage: get_dut_prop(self.tc_details['dev0'])
def get_dut_prop(dev_id):
    tc_log("Get Device Property", 'INFO')
    cmd = "shell getprop"
    prop = Run_Adb_Cmd(dev_id, cmd)
    return prop



# Function to Long press power button
# Usage: long_press_pwr_button(self.tc_details['dev0'])
def long_press_pwr_button(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    tc_log("Entry point of long press power button",'INFO')
    for i in range(4):
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['long_press_pwr_%d' % i])
    	time.sleep(1)    
    return 


# Function to get the Device Finger print information(User Information)
# Usage: finger_print_info(self.tc_details['dev0'])
def finger_print_info(dev_id):
    cmd = "shell getprop ro.build.fingerprint"
    prop = Run_Adb_Cmd(dev_id, cmd)
    return prop



# Function to simulate button press 	
# Usage: back_button_press(0)
def back_button_press(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    if tc_details['dev0_type'] == "cn51":
	tc_log("Simulating back button press ",'INFO')
        for i in range(6):
            Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['back_but_press_%d' % i])
            time.sleep(1) 
    elif tc_details['dev0_type'] == "ct50":  
        tc_log("Simulating touch screen back",'INFO')
        for i in range(26):
            Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['ts_back_%d' % i])
            time.sleep(1)  
    return


# Function to simulate touch screen back
# Usage: ts_back(0)
def ts_back(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    if tc_details['dev0_type'] == "ct50":
        tc_log("Simulating touch screen back",'INFO')
        for i in range(26):
            Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['ts_back_%d' % i])
            time.sleep(1)    
    return


# Function to Turn on/off Stay awake
# Usage: stay_awake_on_off(0, "on/off")
def stay_awake_on_off(dev_num, status):
    dev_id = tc_details['dev' + str(dev_num)]
    ui_dev_id = tc_details['ui_dev' + str(dev_num)]

    tc_log("Turn %s Stay Awake" % status, 'INFO')
    Run_Adb_Cmd(dev_id, "shell am start -n com.android.settings/.DevelopmentSettings")  
    time.sleep(3)
    awake_status = ui_dev_id(text="Stay awake").right(className='android.widget.Switch').checked
    if awake_status == True and status == "off":
        ui_dev_id(text="Stay awake").right(className='android.widget.Switch').click()
	tc_log("Stay Awake turned OFF",'INFO')
    elif awake_status == True and status == "on":
	tc_log("Stay Awake already turned ON",'INFO')
    elif awake_status == False and status == "on":
        ui_dev_id(text="Stay awake").right(className='android.widget.Switch').click()
	tc_log("Stay Awake turned ON",'INFO')
    elif awake_status == False and status == "off":
	tc_log("Stay Awake already turned OFF",'INFO')
    time.sleep(2)
    close_package(dev_id, "settings")
    return


# Function to clear the set Keyremap
# Usage: clear_keyremap(0)
def clear_keyremap(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    ui_dev_id = tc_details['ui_dev' + str(dev_num)]
    open_direct_settings(dev_id, "SETTINGS" )
    ui_dev_id(scrollable=True).scroll.to(textContains='Key')
    ui_dev_id(textContains='Key').click()   
    ui_dev_id(text='Clear All Key Remap').click()
    go_back(dev_id)
    close_package(dev_id, "settings")
    return prop




# Function to check if Screen is on/off
# Usage: check_screen()
def check_screen():
    time.sleep(2)
    status=Run_Adb_Cmd(tc_details['dev0'], "shell dumpsys input_method | grep mInteractive")
    temp=status.split("=")
    return temp[2].strip()


# Function to enable/disable wifi
# Usage: wifi_enable_disable(0, "on/off")
def wifi_enable_disable(dev_num, status):
    dev_id = tc_details['dev' + str(dev_num)]
    ui_dev_id = tc_details['ui_dev' + str(dev_num)]

    tc_log("Turn %s Wi-Fi" % status, 'INFO')
    Run_Adb_Cmd(dev_id, "shell am start -n com.android.settings/.Settings")  
    time.sleep(2)
    if ui_dev_id(text='Wi‑Fi').exists == False:
	ui_dev_id(scrollable=True).scroll.to(text="Wi‑Fi")
    ui_dev_id(text='Wi‑Fi').click()
    time.sleep(2)	
    wifi_status = ui_dev_id(className="android.widget.Switch", resourceId="com.android.settings:id/switch_widget").checked
    if wifi_status == True and status == "off":
        ui_dev_id(className="android.widget.Switch", resourceId="com.android.settings:id/switch_widget").click()
	tc_log("Wi-Fi turned OFF",'INFO')	
    elif wifi_status == True and status == "on":
	tc_log("Wi-Fi already turned ON",'INFO')	
	pass
    elif wifi_status == False and status == "on":
        ui_dev_id(className="android.widget.Switch", resourceId="com.android.settings:id/switch_widget").click()
	tc_log("Wi-Fi turned ON",'INFO')
    elif wifi_status == False and status == "off":
	tc_log("Wi-Fi already turned OFF",'INFO')
	pass
    time.sleep(2)
    close_package(dev_id, "settings")
    return



# Function to enable/disable bluetooth
# Usage: bluetooth_enable_disable(0, "on/off")
def bluetooth_enable_disable(dev_num, status):
    dev_id = tc_details['dev' + str(dev_num)]
    ui_dev_id = tc_details['ui_dev' + str(dev_num)]

    tc_log("Turn %s Bluetooth" % status, 'INFO')
    Run_Adb_Cmd(dev_id, "shell am start -n com.android.settings/.Settings")  
    time.sleep(2)
    if ui_dev_id(text='Bluetooth').exists == False:
	ui_dev_id(scrollable=True).scroll.to(text="Bluetooth")
    ui_dev_id(text='Bluetooth').click()
    time.sleep(2)	
    bt_status = ui_dev_id(className="android.widget.Switch", resourceId="com.android.settings:id/switch_widget").checked
    if bt_status == True and status == "off":
        ui_dev_id(className="android.widget.Switch", resourceId="com.android.settings:id/switch_widget").click()
	tc_log("Bluetooth turned OFF",'INFO')
    elif bt_status == True and status == "on":
	tc_log("Bluetooth already turned ON",'INFO')
	pass
    elif bt_status == False and status == "on":
        ui_dev_id(className="android.widget.Switch", resourceId="com.android.settings:id/switch_widget").click()
	tc_log("Bluetooth turned ON",'INFO')
    elif bt_status == False and status == "off":
	tc_log("Bluetooth already turned OFF",'INFO')
	pass
    time.sleep(2)
    close_package(dev_id, "settings")
    return



# Function to enable/disable airplane mode
# Usage: airplane_enable_disable(0, "on/off")
def airplane_enable_disable(dev_num, status):
    dev_id = tc_details['dev' + str(dev_num)]
    ui_dev_id = tc_details['ui_dev' + str(dev_num)]

    tc_log("Turn %s Airplane mode" % status, 'INFO')
    Run_Adb_Cmd(dev_id, "shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")  
    time.sleep(2)    	
    am_status=ui_dev_id(text='Airplane mode').right(className='android.widget.Switch').checked
    if am_status == True and status == "off":
        ui_dev_id(text='Airplane mode').right(className='android.widget.Switch').click()
	tc_log("Airplane mode turned OFF",'INFO')
	time.sleep(10)
    elif am_status == True and status == "on":
	tc_log("Airplane mode already turned ON",'INFO')
	pass
    elif am_status == False and status == "on":
        ui_dev_id(text='Airplane mode').right(className='android.widget.Switch').click()
	tc_log("Airplane mode turned ON",'INFO')
	time.sleep(5)
    elif am_status == False and status == "off":
	tc_log("Airplane mode already turned OFF",'INFO')
	pass
    time.sleep(2)
    close_package(dev_id, "settings")
    return


# Function to draw full screen pattern
# Usage: draw_full_pattern(0)
def draw_full_pattern(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]    
    tc_log("Draw full screen pattern",'INFO')	
    time.sleep(3)       
    for i in range(21):		# 21 to draw pattern with 4 dots
       Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['draw_full_pattern_%d' % i])
       time.sleep(1)  
    return


# Function to draw full screen UNLOCK pattern
# Usage: draw_unlock_pattern(0)
def draw_unlock_pattern(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]    
    tc_log("Draw full screen Unlock pattern",'INFO')	
    time.sleep(3)       
    for i in range(21):		# 21 to draw pattern with 4 dots
       Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['draw_unlock_pattern_%d' % i])
       time.sleep(1)  
    return



# Function to draw screen pattern(3 dots)
# Usage: draw_pattern(0)
def draw_pattern(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]    
    tc_log("Draw screen pattern(3 dots)",'INFO')	
    time.sleep(3)       
    for i in range(17):		# 17 to draw pattern with 3 dots
       Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['draw_pattern_%d' % i])
       time.sleep(1)  
    return


# Function to draw full screen wrong pattern
# Usage: draw_wrong_pattern(0)
def draw_wrong_pattern(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]    
    tc_log("Draw full screen wrong pattern",'INFO')	
    time.sleep(3)       
    for i in range(21):		# 21 to draw pattern with 4 dots
       Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['draw_wrong_pattern_%d' % i])
       time.sleep(1)  
    return



# Function to draw full screen pattern
# Usage: draw_full_pattern(0)
def draw_full_patt(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]    
    tc_log("Draw full screen pattern",'INFO')	
    time.sleep(3)       
    for i in range(21):		# 21 to draw pattern with 4 dots
       Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['draw_full_pattern_%d' % i])
       time.sleep(7)  
    return


# Function to draw screen pattern(3 dots)
# Usage: draw_pattern(0)
def draw_patt(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]    
    tc_log("Draw screen pattern(3 dots)",'INFO')	
    time.sleep(2)       
    for i in range(17):		# 17 to draw pattern with 3 dots
       Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['draw_pattern_%d' % i])
       time.sleep(1)  
    return


# Function to draw full screen wrong pattern
# Usage: draw_wrong_pattern(0)
def draw_wrong_patt(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]    
    tc_log("Draw full screen wrong pattern",'INFO')	
    time.sleep(2)       
    for i in range(21):		# 21 to draw pattern with 4 dots
       Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['draw_wrong_pattern_%d' % i])
       time.sleep(1)  
    return



# Function to simulate Home button press 	
# Usage: press_home_btn(0)
def press_home_btn(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    tc_log("Simulating Home button press ",'INFO')
    time.sleep(3)  
    for i in range(4):
        Run_Adb_Cmd(dev_id, "shell sendevent /dev/input/" + key_press['dev' + str(dev_num)]['press_home_btn_%d' % i])
        time.sleep(1)    
    return









# Media Preamble function for Audio-Codec Test Cases'
# Usage: media_preamble(0)
def media_preamble(dev_num):
    tc_log("Media Preamble", 'INFO')
    dev_id = tc_details['dev' + str(dev_num)] 

    # Remove the directory if it already exists
    remove_dir(dev_id, "/sdcard/AC_files/")

    # Delete all the music files in /sdcard/Music
    delete_dut_file(dev_id, "/sdcard/Music/*")

    # Make a directory to push media files to DUT
    make_dir(dev_id, "/sdcard/AC_files")
    return



# Media Postamble function for Audio-Codec Test Cases'
# Usage: media_postamble(0)
def media_postamble(dev_num):
    tc_log("Media Postamble", 'INFO')
    dev_id = tc_details['dev' + str(dev_num)] 
    # Stop the Music player
    pause_media(dev_id)
    close_package(dev_id, "settings")
	
    # Delete the pushed music files
    tc_log("Delete the pushed music files", 'INFO')
    delete_dut_file(dev_id, "/sdcard/Music/*")

    # Remove the created directory
    remove_dir(dev_id, "/sdcard/AC_files/")
    return



# Function to push all media in a directory to the DUT
# Usage: push_media_files(0)
def push_media_files(dev_num):  
    dev_id = tc_details['dev' + str(dev_num)] 
    dir_loc = '../music/' + tc_details['tc_name'] + '/'
    media_list = []	# Create an empty list to store media file names
    count = 0
    for root, dirs, filenames in os.walk(dir_loc):
    	filenames.sort()
    	for f in filenames:	
	    count += 1
	    
	    ret_val = push(dev_id, '../music/' + tc_details['tc_name'] + '/' + f, "/sdcard/AC_files/")
	    if ret_val == "error":
		tc_log("Failed to copy the media file %s" % f, 'INFO')
		raise TCFailureError
		break	   
	    # Add media files to a list 	    
	    media_list.append(f) 
    # If NO Media Files in the respective TC Music directory, Fail the TC
    if len(media_list) == 0:		
	tc_log("No Media Files in the TC Directory", 'INFO')
	raise TCFailureError
    return (media_list, count)




# Function to play all media in the DUT directory
# Usage: play_media_files(0, media_tracks)
def play_media_files(dev_num, media_tracks):
    dev_id = tc_details['dev' + str(dev_num)] 
    ui_dev_id = tc_details['ui_dev' + str(dev_num)] 

    open_settings(dev_id, "Settings")  
    if ui_dev_id(text='Storage & USB').exists == False:
	ui_dev_id(scrollable=True).scroll.to(text="Storage & USB")
    ui_dev_id(text='Storage & USB').click()
    tc_validate_screentext(dev_num, "Internal storage", 'WARN', 6)
    if ui_dev_id(text="Internal storage").exists:
	ui_dev_id(text="Internal storage").click()			    
    if ui_dev_id(text='Explore').exists == False:
	ui_dev_id(scrollable=True).scroll.to(text="Explore")
    ui_dev_id(text='Explore').click()	
    if ui_dev_id(text='AC_files').exists == False:
 	ui_dev_id(scrollable=True).scroll.to(text="AC_files")	
    ui_dev_id(text='AC_files').click()

    
    for track in media_tracks:
	tc_log("\nPlaying %s track\n" % track, 'INFO')
	ui_dev_id(text=track).click()
	tc_log("Time to let the media play", 'INFO')
	time.sleep(2)
	# Verify media track can be played successfully without any issues
	tc_log("Verify media track can be played successfully without any issues", 'INFO')
	tc_validate_string(0, 'valid_point_0', 'FAIL', 30)			    		    
	tc_log("Media playing correctly", 'INFO')
	coord = tc_validate_image(dev_id, "../images/full_screen.png", 'WARN', 12, silent=True)
	if coord != (-1, -1):
	    tc_log("Viewing full screen pop up appeared", 'INFO')
	    ATF_Touch_Tuple(coord, dev_id)

	# Pause the media
	tc_log("Pause the media", 'INFO')
	pause_media(dev_id)
	time.sleep(3)
	tc_validate_screentext(0, 'Play', 'WARN', 5)
	# Verify Media paused successfully
        tc_log("Verify Media paused successfully", 'INFO')
    	if (ui_dev_id(descriptionContains="Play").exists):		    		    
            tc_log("Media paused successfully", 'INFO')
    	else:
            tc_log("Media did NOT pause successfully", 'INFO')
            raise TCFailureError
	# Play it again to forward/rewind the media
	tc_log("Play it again to forward/rewind the media", 'INFO')
 	ui_dev_id(descriptionContains="Play").click()
	time.sleep(2)


	# Check if the media is video or audio
	# Video Track
	if ui_dev_id(packageName="com.google.android.apps.photos").exists:
	    tc_log("Video track", 'INFO')
	    ui_dev_id(packageName="com.google.android.apps.photos").click()

	    # Rewind the play
            tc_log("Rewind the play", 'INFO')
 	    ui_dev_id(resourceId="com.google.android.apps.photos:id/video_player_progress").click.topleft()
     	    time.sleep(2)		
            # Verify Media has rewinded
            tc_log("Verify Media has rewinded", 'INFO')
	    tc_validate_string(0, 'valid_point_1', 'FAIL', 20)
	    tc_log("Media got rewinded", 'INFO')
   	    time.sleep(4)

	    if ui_dev_id(descriptionContains="Pause").exists == False:
		ui_dev_id(packageName="com.google.android.apps.photos").click()
		time.sleep(0.5)
	    
    	
	    # Forward the play
            tc_log("Forward the play", 'INFO')
 	    ui_dev_id(resourceId="com.google.android.apps.photos:id/video_player_progress").click()
   	    time.sleep(2)
            # Verify Media has Forwarded
            tc_log("Verify Media has Forwarded", 'INFO')
	    tc_validate_string(0, 'valid_point_2', 'FAIL', 20)
	    tc_log("Media got forwarded", 'INFO')	

	    # Stop the Media
	    tc_log("Stop the Media", 'INFO')
	    pause_media(dev_id)
	    go_back(dev_id)



	# Audio Track
	else:
	    tc_log("Audio track", 'INFO')	    
	    # Rewind the play
            tc_log("Rewind the play", 'INFO')
 	    ui_dev_id(className="android.widget.SeekBar", resourceId="com.google.android.music:id/progress").click.topleft()
     	    time.sleep(2)		
            # Verify Media has rewinded
            tc_log("Verify Media has rewinded", 'INFO')
	    tc_validate_string(0, 'valid_point_1', 'FAIL', 20)
	    tc_log("Media got rewinded", 'INFO')
    	
	    # Forward the play
            tc_log("Forward the play", 'INFO')
 	    ui_dev_id(className="android.widget.SeekBar", resourceId="com.google.android.music:id/progress").click()
   	    time.sleep(2)
            # Verify Media has Forwarded
            tc_log("Verify Media has Forwarded", 'INFO')
	    tc_validate_string(0, 'valid_point_2', 'FAIL', 20)
	    tc_log("Media got forwarded", 'INFO')	

	    # Stop the Media
	    tc_log("Stop the Media", 'INFO')
	    stop_media(dev_id)

	tc_validate_screentext(0, 'AC_files', 'FAIL', 20)
	    	
    go_back(dev_id)
    go_back(dev_id)
    close_package(dev_id, "settings")
    return  




# Function to check data connectivity
# Usage: networkType_status(0)
def networkType_status(dev_num):
    dev_id = tc_details['dev' + str(dev_num)] 
    cmd = "shell dumpsys connectivity | grep '0 NetworkAgentInfo'"
    info = Run_Adb_Cmd(dev_id, cmd)    
    info = info.split()
    netType = info[3]
    netStatus = info[6]     
    netType = netType.replace('(', "")
    netType = netType.replace(')', "")
    netStatus = netStatus.replace('/', " ")
    netStatus = netStatus.split()
    netStatus = netStatus[0]
    return (netType, netStatus)



def check_network_connection(dev_num, timeout=60):	
    tc_log("Check the DUT's Network Type and its Connection status", 'INFO')	
    init_time = time.time()
    while True:
	try:
	    info = networkType_status(dev_num)
    	    tc_log("Network Type and Connection status now: %s" % str(info), 'INFO') 
	    netType = info[0]
	    netStatus = info[1]
	    if (netType == "EDGE") and (netStatus == "CONNECTED"):
		return 0	 	
		break
	    elif (netType == "HSPA" or "HSDPA" or "HSUPA" or "UMTS" or "WCDMA" ) and (netStatus == "CONNECTED"):
		return 1	 	
		break
	    else:
	        tc_log("\nWaiting for successful Network connection...", 'INFO')
	except Exception as e:		
	    tc_log("\nWaiting for successful Network connection", 'INFO')
	    time.sleep(5)
	    		
	# If Time exceeds given timeout, break out of loop
        cur_time = time.time()
        if (cur_time - init_time) > timeout:
	    return -1		
            break  
	time.sleep(3)          
    time.sleep(5)	
    return



# Function to Turn ON Stay Awake
# Usage: enable_stayAwake(0)
def enable_stayAwake(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    Run_Adb_Cmd(dev_id, "shell svc power stayon true")
    time.sleep(4)
    return


# Function to Turn OFF Stay Awake
# Usage: disable_stayAwake(0)
def disable_stayAwake(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    Run_Adb_Cmd(dev_id, "shell svc power stayon false")
    time.sleep(4)
    return

# Function to Turn OFF contact sync
# Usage: disable_contact_sync(0)
def disable_contact_sync(dev_num):
    dev_id = 'dev' + str(dev_num)
    ui_dev_id= 'ui_dev' + str(dev_num)
    open_settings(tc_details[dev_id], "Settings" )
    tc_validate_screentext(dev_num,"Settings",'WARN',15)
    tc_details[ui_dev_id](scrollable=True).scroll.to(text='Accounts')
    tc_details[ui_dev_id](text='Accounts').click()
    tc_validate_screentext(dev_num,"Google",'WARN',15)
    if tc_details[ui_dev_id](text='Google').exists:
        tc_details[ui_dev_id](text='Google').click()
    tc_validate_screentext(dev_num,"Contacts",'WARN',15)
    if tc_details[ui_dev_id](text='Contacts').right(className="android.widget.Switch").checked==True:
    	    tc_details[ui_dev_id](text='Contacts').click()
    	    tc_log("Contact sync Turned off",'INFO')
    close_package(dev_id, "settings")
    
    return





# Function to bring the device to Reboot Recovery mode
# Usage: dut_recovery_mode(0)
def dut_recovery_mode(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    tc_log("DUT Goes to Reboot Recovery mode", 'INFO')
    cmd = "reboot recovery"
    Run_Adb_Cmd(dev_id, cmd)
    return


# Function to open device notification
# Usage: open_notification(0)
def open_notification(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    tc_log("Open Notifications tab", 'INFO')
    cmd = "shell service call statusbar 1"
    Run_Adb_Cmd(dev_id, cmd)
    time.sleep(3)
    return

# Function to close device notification
# Usage: close_notification(0)
def close_notification(dev_num):
    dev_id = tc_details['dev' + str(dev_num)]
    tc_log("Close Notifications tab", 'INFO')
    cmd = "shell service call statusbar 2"
    Run_Adb_Cmd(dev_id, cmd)
    time.sleep(2)
    return


# Function to activate and deactivate DND on the DUT
# Usage: enable_disable_DND(0, "enable/disable")
def enable_disable_DND(dev_num, dnd_status):
    dev_id = tc_details['dev' + str(dev_num)]
    ui_dev_id = tc_details['ui_dev' + str(dev_num)] 
    tc_log("%s DND" % dnd_status, 'INFO')
    open_notification(dev_num)
    tc_validate_screentext(dev_num, "Current user Owner", 'WARN', 5)
    ui_dev_id(descriptionStartsWith='Current user').click()
    check_DND(dev_num)

    if dnd_status == "enable":
        tc_validate_screentext(dev_num, "Do not disturb", 'FAIL', 15)
   	ui_dev_id(text='Do not disturb').click()
        tc_validate_screentext(dev_num, "Total\nsilence", 'FAIL', 15)	
    	ui_dev_id(text='Total\nsilence').click()
        tc_validate_screentext(dev_num, "Until you turn this off", 'WARN', 5)
    	dnd_duration_status = ui_dev_id(text='Until you turn this off').left(className='android.widget.RadioButton').checked
	print dnd_duration_status
	if dnd_duration_status == False:
	    ui_dev_id(text='Until you turn this off').left(className='android.widget.RadioButton').click()
	    time.sleep(3) 
        tc_log("DND Enabled", 'INFO')
    	
    elif dnd_status == "disable":
        check_DND(dev_num)
        tc_log("DND Disabled", 'INFO') 	
   	
    go_back(dev_id)
    go_back(dev_id)
    close_notification(dev_num)
    goto_home_screen(dev_id)	        
    return



# Function to check DND
# Usage: check_DND(0)
def check_DND(dev_num):
    ui_dev_id = tc_details['ui_dev' + str(dev_num)] 
    if tc_validate_screentext(dev_num, "Do not disturb", 'WARN', 5) == 0:
	if tc_validate_screentext(dev_num, "Total silence", 'WARN', 5):
            ui_dev_id(text='Total silence').click()
	elif tc_validate_screentext(dev_num, "Alarms only", 'WARN', 5):
            ui_dev_id(text='Alarms only').click()
	elif tc_validate_screentext(dev_num, "Priority only", 'WARN', 5):
            ui_dev_id(text='Priority only').click()
    time.sleep(3)
    return








