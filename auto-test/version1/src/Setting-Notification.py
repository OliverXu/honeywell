# -*- coding: utf-8 -*-

'''
Test Case Name : Set notification 
Description    : Tests if able to set notification on the device.
		 Validates device has been setting or not

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

        return

    # Function that brings back the device to its initial condition          
    def test_case_postamble(self):
        # clear_package(self.tc_details['dev0'], "com.android.settings")
        goto_home_screen(self.tc_details['dev0'])
        return

    def run(self):
        result = 'FAIL'
        try:

            print "Starting " + self.name
            print "Running test case thread"

            self.test_case_preamble()

            # open setting app
            cmd = "shell am start -n com.android.settings/.Settings"
            Run_Adb_Cmd(self.tc_details['dev0'], cmd)
            tc_log("open setting page", "INFO")
            time.sleep(2)

            tc_log("scroll settings", "INFO")
            self.tc_details['ui_dev0'](scrollable=True).scroll.to(text="Notifications")
            if self.tc_details['ui_dev0'](text="Notifications").exists:
                self.tc_details['ui_dev0'](text="Notifications").click()
            time.sleep(2)

            tc_log("click close if pop-up Pixel launcher issue", 'INFO')
            if self.tc_details['ui_dev0'](text="Pixel Launcher has stopped",
                                          className="android.widget.TextView").exists:
                self.tc_details['ui_dev0'](text="Mute until device restarts", resourceId="android:id/aerr_mute").click()
            time.sleep(5)

            tc_log("scroll notifications", "INFO")
            self.tc_details['ui_dev0'](className="android.widget.ListView", scrollable=True).scroll.to(text="Messenger")
            if self.tc_details['ui_dev0'](text="Messenger").exists:
                self.tc_details['ui_dev0'](text="Messenger").click()
            time.sleep(2)

            tc_log("start validate string and checked", 'INFO')
            tc_validate_screentext(0, "Override Do Not Disturb", 'FAIL', 10)
            if (self.tc_details['ui_dev0'](text='Override Do Not Disturb').right(
                    className="android.widget.Switch").checked):
                raise TCFailureError

            tc_log("click Notification settings", "INFO")
            if (self.tc_details['ui_dev0'](description="Notification settings").exists):
                self.tc_details['ui_dev0'](description="Notification settings").click()
            time.sleep(2)

            tc_log("click show silently", "INFO")
            if not (self.tc_details['ui_dev0'](text='Vibrate').right(className="android.widget.Switch").checked):
                raise TCFailureError

            tc_log("on to off notification", "INFO")
            if (self.tc_details['ui_dev0'](text='Notifications').right(text='ON').exists):
                self.tc_details['ui_dev0'](text='Notifications').right(text='ON').click()
            time.sleep(2)

            if not (self.tc_details['ui_dev0'](text='Vibrate').right(className="android.widget.Switch").checked):
                raise TCFailureError

            if self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").exists:
                self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").click()
            time.sleep(2)

            tc_log("off to on show silently", "INFO")
            if (self.tc_details['ui_dev0'](text='Show silently').right(text='OFF').exists):
                self.tc_details['ui_dev0'](text='Show silently').right(text='OFF').click()
            time.sleep(2)

            tc_log("start validate string and checked again", 'INFO')
            if tc_validate_screentext(0, "Override Do Not Disturb", 'WARN', 10) == 1:
                raise TCFailureError

            tc_log("go back through click Navigate up", "INFO")
            if self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").exists:
                self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").click()
            time.sleep(2)

            tc_log("start click All apps", "INFO")
            if (self.tc_details['ui_dev0'](text="All apps", resourceId="android:id/text1").exists):
                self.tc_details['ui_dev0'](text="All apps", resourceId="android:id/text1").click()
            time.sleep(2)

            tc_log("start click shown silently", "INFO")
            if (self.tc_details['ui_dev0'](text='Shown silently').exists):
                self.tc_details['ui_dev0'](text='Shown silently').click()
            time.sleep(20)

            tc_log("start validate the messenger is or not exist", "INFO")
            tc_validate_screentext(0, "Messenger", 'FAIL', 10)
            tc_log("the messenger is exist", "INFO")
            time.sleep(5)

            tc_log("click messenger", "INFO")
            if self.tc_details['ui_dev0'](text="Messenger").exists:
                self.tc_details['ui_dev0'](text="Messenger").click()
            time.sleep(2)

            tc_log("on to off  show silently", "INFO")
            if (self.tc_details['ui_dev0'](text='Show silently').right(text='ON').exists):
                self.tc_details['ui_dev0'](text='Show silently').right(text='ON').click()
            time.sleep(2)

            tc_log("start validate the string Override Do Not Disturb", "INFO")
            tc_validate_screentext(0, "Override Do Not Disturb", 'WARN', 10)

            if (self.tc_details['ui_dev0'](description="Notification settings").exists):
                self.tc_details['ui_dev0'](description="Notification settings").click()
            time.sleep(2)

            tc_log("off to on notification", "INFO")
            if (self.tc_details['ui_dev0'](text='Notifications').right(text='OFF').exists):
                self.tc_details['ui_dev0'](text='Notifications').right(text='OFF').click()
            time.sleep(2)

            tc_log("go back through click Navigate up", "INFO")
            if self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").exists:
                self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").click()
            time.sleep(2)

            tc_log("go back through click Navigate up", "INFO")
            if self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").exists:
                self.tc_details['ui_dev0'](description="Navigate up", className="android.widget.ImageButton").click()
            time.sleep(2)

            tc_log("start validate the messenger is or not exist", "INFO")
            if (self.tc_details['ui_dev0'](text='Messenger').exists):
                raise TCFailureError

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
