# -*- coding: utf-8 -*-

'''
Test Case Name : PHA-TSTRN-11459-250-CALLS
Description    : To verify the device can make and receive 250 calls.
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

    def clear_call_log(self, dev_num):
        # Step 1 Navigate to Start Phone and move to the Call Log tab.
        open_app(self.tc_details['dev' + str(dev_num)], 'phone')
        # self.tc_details['ui_dev' + str(dev_num)](className='android.view.View', description='Recents').click()

        self.tc_details['ui_dev' + str(dev_num)](className='android.widget.ImageView',
                                                 description='Call History').click()
        time.sleep(2)

        # Step 2 Press Menu
        self.tc_details['ui_dev' + str(dev_num)](className='android.widget.ImageButton',
                                                 description='More options').click()
        time.sleep(2)
        self.tc_details['ui_dev' + str(dev_num)](text='Call History').click()
        time.sleep(2)
        # self.tc_details['ui_dev' + str(dev_num)](className='android.widget.ImageButton',
        # description='More options').click()
        self.tc_details['ui_dev' + str(dev_num)](className='android.widget.ImageView',
                                                 description='More options').click()
        time.sleep(2)
        self.tc_details['ui_dev' + str(dev_num)](text='Clear call history').click()
        time.sleep(2)

        # Step 3 Click OK when prompted
        self.tc_details['ui_dev' + str(dev_num)](text='OK').click()

    # Function that brings back the device to its initial condition
    def test_case_postamble(self):

        # self.clear_call_log(0)
        clear_contacts(self.tc_details['dev0'])
        clear_contacts(self.tc_details['dev1'])
        return

    def run(self):
        result = 'FAIL'
        try:
            tc_log("Starting " + self.name, 'INFO')
            tc_log("Running test case thread", 'INFO')

            # self.test_case_preamble()

            if self.tc_details['call_times']:
                tc_log("Total Call times: " + self.tc_details['call_times'], 'INFO')

            tc_log("********Start call progress********", 'INFO')

            for i in range(int(self.tc_details['call_times'])):
                # action: dev0 call dev1, dev1 receive call, dev0 end call
                if i > 0:
                    tc_log("Sleep "+str(self.tc_details['sleep_time'])+" seconds to wait device`s environment ready...",
                           'INFO')
                    time.sleep(int(self.tc_details['sleep_time']))
                call_intent(self.tc_details['dev0'], self.tc_details['dev1_number'])
                tc_log("Sleep "+str(self.tc_details['sleep_time'])+" seconds...", 'INFO')
                time.sleep(int(self.tc_details['sleep_time']))
                receive_call(self.tc_details['dev1'])
                tc_log("Sleep " + str(self.tc_details['sleep_time']) + " seconds...", 'INFO')
                time.sleep(int(self.tc_details['sleep_time']))
                end_call(self.tc_details['dev0'])
                tc_log("Current call times is: " + str(i+1), 'INFO')

            tc_log("********End call progress********", 'INFO')

            # verify dev0 call history message
            tc_log("********Verify "+self.tc_details['dev0']+" call history message start********", 'INFO')

            cmd = "shell am start -n com.android.dialer/.DialtactsActivity"
            Run_Adb_Cmd(self.tc_details['dev0'], cmd)
            time.sleep(2)

            if self.tc_details['ui_dev0'](description='Call history').exists:
                self.tc_details['ui_dev0'](description='Call history').click()
            elif self.tc_details['ui_dev0'](description='Call History').exists:
                self.tc_details['ui_dev0'](description='Call History').click()
            elif self.tc_details['ui_dev0'](description='Recents').exists:
                self.tc_details['ui_dev0'](description='Recents').click()
            time.sleep(2)

            if self.tc_details['ui_dev0'](text='View full call history').exists:
                self.tc_details['ui_dev0'](text='View full call history').click()

                tc_log("Scroll call history page", 'INFO')

                _target_dial_number = str(self.tc_details['dev1_number'])
                _target_dial_len = len(_target_dial_number)
                _scroll_target = _target_dial_number[_target_dial_len-4:_target_dial_len]

                self.tc_details['ui_dev0'](scrollable=True).scroll.to(textContains=_scroll_target)
                tc_log("Focus to the detail", 'INFO')

                if self.tc_details['ui_dev0'](textContains=_scroll_target).exists:
                    tc_log("List the dev0 info", 'INFO')

                    _call_info = self.tc_details['ui_dev0'](textContains=_scroll_target).sibling(
                        className="android.widget.LinearLayout").child(
                        resourceId="com.android.dialer:id/call_location_and_date").info
                    tc_log(_call_info, 'INFO')

                    _count_str = _call_info['text'].encode("utf-8")
                    _call_times = int(_count_str[_count_str.index('(')+1:_count_str.index(')')])

                    if (_call_times != int(self.tc_details['call_times'])) and \
                            (_call_times < int(self.tc_details['call_times']) * 0.98):
                        tc_log("********Call "+self.tc_details['call_times']+" Times. FAIL********",
                               'INFO')
                        raise TCFailureError
                else:
                    tc_log("********Can't get the text contains "+_scroll_target+". FAIL********"
                           , 'INFO')
                    raise TCFailureError

            tc_log("********Device " + self.tc_details['dev0'] + " call history verify end********", 'INFO')
            goto_home_screen(self.tc_details['dev0'])

            time.sleep(2)

            # verify dev1 call history message
            tc_log("********Verify device "+self.tc_details['dev1']+" call history message start********", 'INFO')

            Run_Adb_Cmd(self.tc_details['dev1'], cmd)
            time.sleep(2)

            if self.tc_details['ui_dev1'](description='Call history').exists:
                self.tc_details['ui_dev1'](description='Call history').click()
            elif self.tc_details['ui_dev1'](description='Call History').exists:
                self.tc_details['ui_dev1'](description='Call History').click()
            elif self.tc_details['ui_dev1'](description='Recents').exists:
                self.tc_details['ui_dev1'](description='Recents').click()
            time.sleep(2)

            if self.tc_details['ui_dev1'](text='View full call history').exists:
                self.tc_details['ui_dev1'](text='View full call history').click()

                tc_log("Scroll call history page", 'INFO')

                _receive_dial_number = str(self.tc_details['dev0_number'])
                _receive_dial_len = len(_receive_dial_number)
                _scroll_target = _receive_dial_number[_receive_dial_len-4:_receive_dial_len]

                self.tc_details['ui_dev1'](scrollable=True).scroll.to(textContains=_scroll_target)

                tc_log("Focus to the detail", 'INFO')
                if self.tc_details['ui_dev1'](textContains=_scroll_target).exists:
                    tc_log("List the dev1 info", 'INFO')

                    _call_info = self.tc_details['ui_dev1'](textContains=_scroll_target).sibling(
                        className="android.widget.LinearLayout").child(
                        resourceId="com.android.dialer:id/call_location_and_date").info

                    _count_str = _call_info['text'].encode("utf-8")
                    _receive_call_times = int(_count_str[_count_str.index('(')+1:_count_str.index(')')])
                    tc_log("Receive call times: " + str(_receive_call_times), 'INFO')

                    _call_times = int(_count_str[_count_str.index('(')+1:_count_str.index(')')])
                    if (_call_times != int(self.tc_details['call_times'])) and \
                            (_call_times < int(self.tc_details['call_times']) * 0.98):
                        tc_log("********Receive Call " + self.tc_details['call_times']+" Times. FAIL********",
                               'INFO')
                        raise TCFailureError
                else:
                    tc_log("********Can't get the text contains " + _scroll_target + ". FAIL********"
                           , 'INFO')
                    raise TCFailureError

            tc_log("********Device " + self.tc_details['dev1'] + " call history verify end********", 'INFO')
            goto_home_screen(self.tc_details['dev1'])

            tc_log("********Verify device "+self.tc_details['dev0']+" connect Internet start********", 'INFO')

            _cmd_line_value = os.popen("adb -s "+tc_details['dev0']+" shell ping -c 5 " +
                                       str(self.tc_details['target_website'])+"")
            _ping_return_str = _cmd_line_value.read()
            tc_log("Ping return str:\n " + str(_ping_return_str), 'INFO')
            _ping_success_times = _ping_return_str[_ping_return_str.find(',')+1:_ping_return_str.find('received')]
            tc_log("Ping "+str(self.tc_details['target_website'])+" success times: " + str(_ping_success_times),
                   'INFO')
            if _ping_success_times and int(_ping_success_times) > 0:
                tc_log("Device "+self.tc_details['dev0']+" could connect the internet.", 'INFO')
            else:
                tc_log("********Device "+self.tc_details['dev0']+" could not connect the internet. FAIL********",
                       'INFO')
                raise TCFailureError

            tc_log("********Verify device " + self.tc_details['dev0'] + " connect Internet end********", 'INFO')

            result = 'PASS'

        except TCFailureError:
            tc_log("TCFailure Exception Raised", 'INFO')
            result = 'FAIL'

        finally:
            # self.test_case_postamble()

            tc_verdict(result)
            tc_details['verdict'] = result
            tc_cleanup()

            tc_log("Completed test steps for " + self.name, 'INFO')


if __name__ == "__main__":

    try:
        session_name = sys.argv[1]
        # session_name = "250_call"

        tc_details, loganalyzer = tc_initialize(session_name, sys.argv[0])
        # tc_details, loganalyzer = tc_initialize(session_name, "PHA-TSTRN-11459-250-CALLS.py")
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
