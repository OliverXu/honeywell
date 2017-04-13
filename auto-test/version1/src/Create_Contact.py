# -*- coding: utf-8 -*-

'''
Test Case Name : Create contract Management
Description    : Tests adding contacts then send contact message then delete contacts
		 Validates phone create and delete contact correctly.

'''

import threading
import time
import sys
import os

# HATF imports
sys.path.insert(0, '../../../framework/common')
import log_analyzer
from tc_common import *
from tc_adb_commands import *
import random
import string

global testcase
global loganalyzer
loganalyzer = []


class test_case(threading.Thread):
    def __init__(self, threadID, name, tc_details):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.tc_details = tc_details

    # Function performs initial settings
    def test_case_preamble(self):
        tc_common_preamble()
        # To clear all contacts
        clear_contacts(self.tc_details['dev0'])
        return

    # Function that brings back the device to its initial condition
    def test_case_postamble(self):
        # To clear all contacts
        clear_contacts(self.tc_details['dev0'])

        tc_log("Clean message for dev0 in postamble", 'INFO')
        open_app(self.tc_details['dev0'], 'messaging_v1')
        time.sleep(5)

        #print config_strings['dev0']['recv_mes_number']
        phonenumber = self.tc_details['contact_number_1']
        recv_mes_number = "("+phonenumber[1:4]+") "+phonenumber[4:7]+"-"+phonenumber[7:11]
        tc_log("find the recv sms number","INFO")
        if self.tc_details['ui_dev0'](text=recv_mes_number,
                                      className='android.widget.TextView').exists:
            self.tc_details['ui_dev0'](text=recv_mes_number,
                                       className='android.widget.TextView').click()
        else:
            tc_log("Can not found recv sms number", 'INFO')

        time.sleep(2)

        if self.tc_details['ui_dev0'](description="More options", className='android.widget.ImageView').exists:
            self.tc_details['ui_dev0'](description="More options", className='android.widget.ImageView').click()
        else:
            tc_log("Can not found More options", 'INFO')
        time.sleep(2)
       
        if self.tc_details['ui_dev0'](text="Delete").exists:
            tc_log("start click delete button","INFO")
            self.tc_details['ui_dev0'](text="Delete").click()
        time.sleep(2)

        if self.tc_details['ui_dev0'](className='android.widget.Button', resourceId='android:id/button1').exists:
            self.tc_details['ui_dev0'](className='android.widget.Button', resourceId='android:id/button1').click()
        time.sleep(10)

        goto_home_screen(self.tc_details['dev0'])
        return

    def run(self):
        result = 'FAIL'
        try:

            print "Starting " + self.name
            print "Running test case thread"

            self.test_case_preamble()

            #get the width for drag 
            width = self.tc_details['ui_dev0'].info.get('displayWidth')
 
            #prepare the watch for Pixel
            # tc_details['ui_dev0'].watcher("Pixel Launcher popup").when(text="Pixel Launcher has stopped").click(text="Close app")
            #time.sleep(2)

            '''
            #we should use these code if we run on 7.1 version
            tc_log("start open search app list", 'INFO')
            self.tc_details['ui_dev0'](description="Apps list", className="android.widget.ImageView").drag.to(width / 2,0,100)
            time.sleep(2)

            tc_log("input p to list", 'INFO')
            if self.tc_details['ui_dev0'](textContains="Search Apps", className="android.widget.EditText").exists:
                self.tc_details['ui_dev0'](textContains="Search Apps", className="android.widget.EditText").set_text(
                    'p')
            time.sleep(5)

            if self.tc_details['ui_dev0'](description="Google Search", className="android.widget.ImageView").exists:
                self.tc_details['ui_dev0'](description="Google Search", className="android.widget.ImageView").click()
            time.sleep(5)

            '''
            #we should use these code if we run on 7.0 version
            tc_log("start open search app list", 'INFO')
            open_app(self.tc_details['dev0'], 'google_quick_search')
            time.sleep(2)

            if self.tc_details['ui_dev0'](resourceId="com.google.android.googlequicksearchbox:id/text_container",
                                          className="android.widget.FrameLayout").exists:
                self.tc_details['ui_dev0'](resourceId="com.google.android.googlequicksearchbox:id/text_container",
                                          className="android.widget.FrameLayout").click()

            time.sleep(5)

            if self.tc_details['ui_dev0'](textContains="Search", className="android.widget.EditText").exists:
                self.tc_details['ui_dev0'](textContains="Search", className="android.widget.EditText").set_text('p')
            time.sleep(5)
            #end for 7.0 version

            tc_log("click phone", 'INFO')
            if self.tc_details['ui_dev0'](text="Phone", className="android.widget.TextView").exists:
                self.tc_details['ui_dev0'](text="Phone", className="android.widget.TextView").click()
            time.sleep(5)

            tc_log("click close if pop-up Pixel launcher issue", 'INFO')
            if self.tc_details['ui_dev0'](text="Pixel Launcher has stopped",
                                          className="android.widget.TextView").exists:
                self.tc_details['ui_dev0'](text="Mute until device restarts", resourceId="android:id/aerr_mute").click()
            time.sleep(5)

            tc_log("enter the add contact tab", 'INFO')
            if self.tc_details['ui_dev0'](description="Contacts", className="android.widget.ImageView").exists:
                self.tc_details['ui_dev0'](description="Contacts", className="android.widget.ImageView").click()
            time.sleep(2)

            tc_log("start create new contact", 'INFO')
            if self.tc_details['ui_dev0'](description="Create new contact",
                                          className="android.widget.ImageButton").exists:
                self.tc_details['ui_dev0'](description="Create new contact",
                                           className="android.widget.ImageButton").click()
            time.sleep(2)

            tc_log("enter the name", 'INFO')
            if self.tc_details['ui_dev0'](text="Name", className="android.widget.EditText").exists:
                self.tc_details['ui_dev0'](text="Name", className="android.widget.EditText").set_text(self.tc_details['name'])
            time.sleep(2)

            press_enter(self.tc_details['dev0'])
            time.sleep(2)

            tc_log("enter the phone number", 'INFO')
            phonenumber = self.tc_details['contact_number_1']
            tc_log("phonenumber is "+phonenumber,"INFO")
            if self.tc_details['ui_dev0'](text="Phone", className="android.widget.EditText").exists:
                self.tc_details['ui_dev0'](text="Phone", className="android.widget.EditText").set_text(phonenumber)
            time.sleep(2)

            press_enter(self.tc_details['dev0'])
            time.sleep(2)

            tc_log("click save button", 'INFO')
            if self.tc_details['ui_dev0'](description="Save", className="android.widget.TextView").exists:
                self.tc_details['ui_dev0'](description="Save", className="android.widget.TextView").click()
            time.sleep(2)

            tc_log("start validate phone number", 'INFO')
            recv_number = phonenumber[0:1]+" "+phonenumber[1:4]+"-"+phonenumber[4:7]+"-"+phonenumber[7:11]
            tc_log("format the phonenumber "+recv_number,"INFO")
            tc_validate_screentext(0, recv_number, 'FAIL', 10)

            tc_log("start send message", 'INFO')
            if self.tc_details['ui_dev0'](resourceId="com.android.contacts:id/icon_alternate",
                                          className="android.widget.ImageView").exists:
                self.tc_details['ui_dev0'](resourceId="com.android.contacts:id/icon_alternate",
                                          className="android.widget.ImageView").click()
            time.sleep(2)

            tc_log("input the message text", 'INFO')
            if self.tc_details['ui_dev0'](text="Send message", className="android.widget.EditText").exists:
                self.tc_details['ui_dev0'](text="Send message", className="android.widget.EditText").set_text(
                    self.tc_details['name'])
            time.sleep(2)

            tc_log("send message", 'INFO')
            # if (self.tc_details['ui_dev0'](resourceId='com.google.android.apps.messaging:id/send_message_button').exists):
            #    self.tc_details['ui_dev0'](resourceId='com.google.android.apps.messaging:id/send_message_button').click()
            if (self.tc_details['ui_dev0'](resourceId='com.google.android.apps.messaging:id/self_send_icon').exists):
                self.tc_details['ui_dev0'](resourceId='com.google.android.apps.messaging:id/self_send_icon').click()
            time.sleep(2)

            tc_log("start validate message", 'INFO')
            tc_validate_screentext(0, self.tc_details['name'], 'FAIL', 10)

            tc_log("start to go back contact page", 'INFO')
            if self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").exists:
                self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").click()
            time.sleep(2)

            '''
            #we should use these code if we run on 7.1 version
            go_back(self.tc_details['dev0'])
            time.sleep(2)
            '''
            #we should use these code if we run on 7.0 version
            open_app(self.tc_details['dev0'],'contacts')
            time.sleep(2)

            if (self.tc_details['ui_dev0'](description=self.tc_details['name']).exists):
                self.tc_details['ui_dev0'](description=self.tc_details['name']).click()
            time.sleep(2)
            #end for 7.0 version
            if (self.tc_details['ui_dev0'](description='More options').exists):
                self.tc_details['ui_dev0'](description='More options').click()
            time.sleep(2)

            tc_log("cick delete", 'INFO')
            if self.tc_details['ui_dev0'](text="Delete", className="android.widget.TextView").exists:
                self.tc_details['ui_dev0'](text="Delete", className="android.widget.TextView").click()
            time.sleep(2)

            tc_log("press delete button", 'INFO')
            if self.tc_details['ui_dev0'](text="DELETE", className="android.widget.Button").exists:
                self.tc_details['ui_dev0'](text="DELETE", className="android.widget.Button").click()
            time.sleep(2)

            cmd = "shell am start -n com.android.contacts/.activities.PeopleActivity"
            Run_Adb_Cmd(self.tc_details['dev0'], cmd)
            time.sleep(2)

            self.tc_details['ui_dev0'](text="ALL", className="android.widget.TextView").click()
            tc_log("start validate message", 'INFO')
            tc_validate_screentext(0, "No contacts", 'FAIL', 10)

            result = 'PASS'

        except TCFailureError:
            tc_log("TCFailure Exception Raised", 'INFO')
            result = 'FAIL'

        finally:
            self.test_case_postamble()

            tc_verdict(result)
            tc_details['verdict'] = result
            tc_cleanup()

            print "Completed test steps for " + self.name


if __name__ == "__main__":

    try:
        session_name = sys.argv[1] 

        tc_details, loganalyzer = tc_initialize(session_name, sys.argv[0])
        print loganalyzer

        # Start the new test case thread
        testcase = test_case(1, tc_details['tc_name'], tc_details)
        testcase.start()
        tc_details['testcasethread'] = testcase

        tc_timer_testcase(int(tc_details['tc_duration']))


    finally:
        print "Test Case Thread Exits"

        if tc_details['verdict'] == 'PASS':
            sys.exit(0)
        else:
            sys.exit(1)
