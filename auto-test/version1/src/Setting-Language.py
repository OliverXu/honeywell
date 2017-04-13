# -*- coding: utf-8 -*-

'''
Test Case Name : Test language setting
Description    : Tests if able to do language setting.
		 Validates device setting language added and delete

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

            tc_log("Starting " + self.name, "INFO")
            tc_log("Running test case thread", "INFO")

            self.test_case_preamble()

            tc_log("get width of screen for draging","INFO")
            width = self.tc_details['ui_dev0'].info.get('displayWidth')

            cmd = "shell am start -n com.android.settings/.Settings"
            Run_Adb_Cmd(self.tc_details['dev0'], cmd)
            tc_log("open setting page","INFO")
            time.sleep(2)

            tc_log("scroll to Languages in settings", "INFO")
            self.tc_details['ui_dev0'](scrollable=True).scroll.to(textStartsWith="Languages")
            time.sleep(2)

            tc_log("click Languages & input", "INFO")
            if (self.tc_details['ui_dev0'](textStartsWith="Languages").exists):
                self.tc_details['ui_dev0'](textStartsWith="Languages").click()
            time.sleep(2)

            tc_log("click Languages", "INFO")
            if (self.tc_details['ui_dev0'](text='Languages').exists):
                tc_log("find Languages selection", "INFO")
                self.tc_details['ui_dev0'](text='Languages').click()
            time.sleep(2)

            tc_log("click Add a language", "INFO")
            if (self.tc_details['ui_dev0'](text='Add a language').exists):
                self.tc_details['ui_dev0'](text='Add a language').click()
            time.sleep(2)

            tc_log("click search menu", "INFO")
            if (self.tc_details['ui_dev0'](resourceId='android:id/locale_search_menu').exists):
                self.tc_details['ui_dev0'](resourceId='android:id/locale_search_menu').click()
            time.sleep(2)

            tc_log("Set English Text", "INFO")
            if (self.tc_details['ui_dev0'](resourceId='android:id/search_src_text').exists):
                self.tc_details['ui_dev0'](resourceId='android:id/search_src_text').set_text("English")
            time.sleep(2)

            
            tc_log("press enter key", "INFO")
            press_enter(tc_details['dev0'])
            time.sleep(2)

            tc_log("click select English text", "INFO")
            if (self.tc_details['ui_dev0'](resourceId='android:id/locale', text='English').exists):
                tc_log("find English selection", "INFO")
                self.tc_details['ui_dev0'](resourceId='android:id/locale', text='English').click()
            time.sleep(2)

            tc_log("scroll to macau", "INFO")
            self.tc_details['ui_dev0'](scrollable=True).scroll.to(text="Macau")
            time.sleep(2)

            tc_log("click macau text", "INFO")
            if (self.tc_details['ui_dev0'](text='Macau').exists):
                self.tc_details['ui_dev0'](text='Macau').click()
            time.sleep(2)

            ret1 = tc_validate_screentext(0, 'English (Macau)', 'FAIL', 10)

            tc_log("drag the handle", "INFO")
            if (self.tc_details['ui_dev0'](textContains='Macau').exists):
                self.tc_details['ui_dev0'](textContains='Macau').right(
                    resourceId='com.android.settings:id/dragHandle').drag.to(width / 2, 0, 100)
            time.sleep(2)

            tc_log("click more options", "INFO")
            if (self.tc_details['ui_dev0'](description='More options').exists):
                self.tc_details['ui_dev0'](description='More options').click()
            time.sleep(2)

            tc_log("click remove button", "INFO")
            if (self.tc_details['ui_dev0'](text='Remove').exists):
                self.tc_details['ui_dev0'](text='Remove').click()
            time.sleep(2)

            tc_log("click English(Macau)", "INFO")
            if (self.tc_details['ui_dev0'](textContains="Macau").exists):
                tc_log("find Macau selection", "INFO")
                self.tc_details['ui_dev0'](textContains="Macau").click()
            time.sleep(2)

            tc_log("click remove button", "INFO")
            if (self.tc_details['ui_dev0'](description='Remove').exists):
                self.tc_details['ui_dev0'](description='Remove').click()
            time.sleep(2)

            tc_log("click ok button", "INFO")
            if (self.tc_details['ui_dev0'](text='OK').exists):
                self.tc_details['ui_dev0'](text='OK').click()
            time.sleep(2)

            if not (self.tc_details['ui_dev0'](textContains="Macau").exists):
                tc_log("cannot find Macau selection", "INFO")
                ret2 = 1

            tc_log("back to multi app screen", "INFO")
            press_switch_app(tc_details['dev0'])
            time.sleep(2)

            tc_log("CLEAR ALL", "INFO")
            self.tc_details['ui_dev0'](text="CLEAR ALL").click()
            time.sleep(5)

            if (ret1 == 1 and ret2 == 1):
                tc_log("***********Setting Languages Sucessfully*******************", 'INFO')
            else:
                tc_log("***********Setting Languages  Failed************************", 'INFO')
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

            tc_log("Completed test steps for " + self.name, "INFO")


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
        tc_log("Test Case Thread Exits", "INFO")

        if tc_details['verdict'] == 'PASS':
            sys.exit(0)
        else:
            sys.exit(1)
