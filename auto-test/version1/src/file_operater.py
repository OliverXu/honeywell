# -*- coding: utf-8 -*-

'''
Test Case Name : file_operate
Description    : upload and download file

'''
# HATF imports
import threading
import time
import sys
import os


# HATF imports
sys.path.insert(0, '../../../framework/common')
import log_analyzer
from tc_common import *
from tc_adb_commands import *
from file_operater_res import FileOperaterRes
global testcase
global loganalyzer
loganalyzer = []


class test_case(threading.Thread):

    def __init__(self, threadID, name, tc_details):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.tc_details = tc_details
        self.selector = FileOperaterRes()

    # Function performs initial settings
    def test_case_preamble(self):
        tc_common_preamble()
        # clear_contacts(tc_details['dev0'])
        return

    # Function that brings back the device to its initial condition
    def test_case_postamble(self):
        # clear_package(self.tc_details['dev0'], "com.android.settings")

        # clear_contacts(tc_details['dev0'])
        goto_home_screen(self.tc_details['dev0'])
        return

    def run(self):
        result = 'FAIL'
        try:

            print "Starting " + self.name
            print "Running test case thread"

            self.test_case_preamble()

            # Launch Contacts app

            open_settings(self.tc_details['dev0'], "Settings")
            time.sleep(2)
            if self.tc_details['ui_dev0'](text="Wi‑Fi").exists:
                self.tc_details['ui_dev0'](text="Wi‑Fi").click()
                time.sleep(2)
                cmd = "shell am start -n com.baidu.netdisk/.ui.MainActivity"
                Run_Adb_Cmd(self.tc_details['dev0'], cmd)
                time.sleep(5)
                # upload
                # if self.selector.upload:
                tc_log("****************start upload****************", 'INFO')
                if self.tc_details['ui_dev0'](resourceId=self.selector.upload_id).exists:
                    self.tc_details['ui_dev0'](resourceId=self.selector.upload_id).click()
                    time.sleep(2)
                    self.tc_details['ui_dev0'](text=self.selector.upload_type).click()
                    self.tc_details['ui_dev0'](text=r'0').click()
                    self.tc_details['ui_dev0'](scrollable=True).scroll.to(text="Download")
                    self.tc_details['ui_dev0'](text="Download").click()
                    self.tc_details['ui_dev0'](text=self.selector.upload_files_name).click()
                    self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/button_select_ok").click()
                    self.upload_start_time = datetime.datetime.now()
                    print self.upload_start_time
                    time.sleep(5)
                    self.tc_details['ui_dev0'](resourceId=self.selector.transfer_list).click()
                    time.sleep(1)

                    if self.tc_details['ui_dev0'](text=self.selector.upload_files_name).exists:
                        self.upload_end_time = datetime.datetime.now()

                        go_back(self.tc_details['dev0'])

                        self.tc_details['ui_dev0'](
                            resourceId="com.baidu.netdisk:id/button_search").click()
                        time.sleep(3)
                        self.tc_details['ui_dev0'](
                            resourceId="com.baidu.netdisk:id/search_text").click()
                        time.sleep(2)
                        self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/search_text"). \
                            set_text("")
                        time.sleep(2)
                        self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/search_text"). \
                            set_text(self.selector.upload_files_name)
                        time.sleep(2)
                        self.tc_details['ui_dev0'](
                            resourceId="com.baidu.netdisk:id/search_button").click()
                        # file_size
                        upload_file_size = self.tc_details['ui_dev0'](
                            resourceId="com.baidu.netdisk:id/filesize").text

                        go_back(self.tc_details['dev0'])

                        if 'GB' in upload_file_size:
                            upload_file_size = float(upload_file_size.replace("GB", "").strip()) * 1024 * 1024
                        elif 'MB' in upload_file_size:
                            upload_file_size = float(upload_file_size.replace("MB", "").strip()) * 1024
                        else:
                            upload_file_size = float(upload_file_size.replace("KB", "").strip())

                        upload_file_speed = int(upload_file_size) / (
                        int((self.upload_end_time - self.upload_start_time).seconds) - 5)
                        print str(upload_file_speed)
                        tc_log("****************Upload Speed :"+str(int(upload_file_speed))+"kB/S*****************", 'INFO')
                        # validate files
                        tc_log("****************Successful Upload****************", 'INFO')
                # download
                # else:
                time.sleep(5)
                tc_log("****************start download****************", 'INFO')
                if self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/button_search").exists:
                    self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/button_search").click()
                    time.sleep(3)
                    self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/search_text").click()
                    time.sleep(2)
                    self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/search_text"). \
                        set_text("")
                    time.sleep(2)
                    self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/search_text").\
                        set_text(self.selector.down_files_name)
                    time.sleep(2)
                    self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/search_button").click()
                    time.sleep(5)
                    if self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/checkable_layout").exists:
                        if self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/checkable_layout").\
                                child(index=3).exists:
                            self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/checkable_layout"). \
                                child(index=3).click()
                            # file_size
                            file_size = self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/filesize").text
                        else:
                            self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/checkable_layout").click()

                        if self.tc_details['ui_dev0'](resourceId=self.selector.download_id).exists:
                            self.tc_details['ui_dev0'](resourceId=self.selector.download_id).click()
                            self.start_time = datetime.datetime.now()
                            self.origin_time = self.start_time

                            time.sleep(5)
                            go_back(self.tc_details['dev0'])
                            time.sleep(4)
                            self.tc_details['ui_dev0'](
                                resourceId=self.selector.transfer_list).click()
                            time.sleep(2)
                            self.tc_details['ui_dev0'](text=u"下载列表").click()
                            flg = 0
                            cnt = 0
                            while flg == 0:
                                info = Run_Adb_Cmd(self.tc_details['dev0'],
                                            'ls /storage/emulated/0/BaiduNetdisk/')
                                file_name = self.selector.down_files_name+'.'
                                if file_name in info.decode('utf8'):
                                    time.sleep(1)
                                    cnt + 1
                                else:
                                    self.courrent_time = datetime.datetime.now()
                                    if 'GB' in file_size:
                                        file_size = float(file_size.replace("GB", "").strip()) * 1024 * 1024
                                    elif 'MB' in file_size:
                                        file_size = float(file_size.replace("MB","").strip()) * 1024
                                    else:
                                        file_size = float(file_size.replace("KB", "") .strip())
                                    download_file_speed = file_size / (int((self.courrent_time - self.start_time).seconds) - cnt)
                                    print str(download_file_speed)
                                    tc_log("****************download Speed :"+str(int(download_file_speed))+"kB/S****************", 'INFO')
                                    if int((self.courrent_time - self.origin_time).seconds)/3600 < 1:
                                        time.sleep(2)
                                        self.tc_details['ui_dev0'](text=self.selector.down_files_name).long_click()
                                        self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/edit_tools_delete_btn").click()
                                        self.tc_details['ui_dev0'](text=u"确定").click()

                                        go_back(go_back(self.tc_details['dev0']))

                                        self.tc_details['ui_dev0'](
                                            resourceId="com.baidu.netdisk:id/button_search").click()
                                        time.sleep(3)
                                        self.tc_details['ui_dev0'](
                                            resourceId="com.baidu.netdisk:id/search_text").click()
                                        time.sleep(2)
                                        self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/search_text"). \
                                            set_text("")
                                        time.sleep(2)
                                        self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/search_text"). \
                                            set_text(self.selector.down_files_name)
                                        time.sleep(2)
                                        self.tc_details['ui_dev0'](
                                            resourceId="com.baidu.netdisk:id/search_button").click()
                                        self.tc_details['ui_dev0'](resourceId="com.baidu.netdisk:id/checkable_layout"). \
                                            child(index=3).click()
                                        # file_size
                                        file_size = self.tc_details['ui_dev0'](
                                            resourceId="com.baidu.netdisk:id/filesize").text
                                        self.tc_details['ui_dev0'](resourceId=self.selector.download_id).click()
                                        self.start_time = datetime.datetime.now()
                                        cnt = 0
                                        time.sleep(5)
                                        go_back(self.tc_details['dev0'])
                                        time.sleep(2)
                                        self.tc_details['ui_dev0'](
                                            resourceId=self.selector.transfer_list).click()
                                        time.sleep(2)
                                    else:
                                        flg = 1
                                        tc_log("****************Successful download****************", 'INFO')

                                        open_chrome = "shell am start -n com.android.chrome/com.google.android.apps.chrome.Main"
                                        Run_Adb_Cmd(self.tc_details['dev0'], open_chrome)
                                        self.tc_details['ui_dev0'](
                                            resourceId="com.android.chrome:id/url_bar").click()
                                        time.sleep(2)
                                        self.tc_details['ui_dev0'](
                                            resourceId="com.android.chrome:id/url_bar").set_text("www.baidu.com")
                                        time.sleep(5)
                                        self.tc_details['ui_dev0'](text="www.baidu.com", index=0).click()
                                        if self.tc_details['ui_dev0'](description="百度一下").exists:
                                            tc_log("****************WI-FI Successful****************", 'INFO')

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

    def makeCall(self):
        call_intent(self.tc_details['dev0'], '10086')
        print "sleep 3 seconds..."
        time.sleep(3)
        end_call(self.tc_details['dev0'])

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

