# -*- coding: utf-8 -*-

'''
Test Case Name : HELAN-ATC-2921-Encryption
Description    : Tests if able to do Encrypt the device.
		 Validates device has been encrypted or not

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


class test_case (threading.Thread):

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
        #clear_package(self.tc_details['dev0'], "com.android.settings")
    	goto_home_screen (self.tc_details['dev0'])
        return
                  

    def run(self):
	result = 'FAIL'
	try:

	    print "Starting " + self.name				
	    print "Running test case thread"
            
            self.test_case_preamble()

            height = self.tc_details['ui_dev0'].info.get('displayHeight')
            width = self.tc_details['ui_dev0'].info.get('displayWidth')
            print width,height

            #open setting app 
	    cmd = "shell am start -n com.android.settings/.Settings"
	    Run_Adb_Cmd(self.tc_details['dev0'], cmd)
      	    time.sleep(2)

            #prepare validate setting screen
            #Add validate code
            print "scroll settings"
            self.tc_details['ui_dev0'](scrollable=True).scroll.to(textStartsWith="Languages")
            time.sleep(2)

            print "click Languages & input"
            if (self.tc_details['ui_dev0'](textStartsWith="Languages").exists):
                self.tc_details['ui_dev0'](textStartsWith="Languages").click()
            time.sleep(2)
         
            print "click Languages"
            if (self.tc_details['ui_dev0'](text='Languages').exists):
                self.tc_details['ui_dev0'](text='Languages').click()
            time.sleep(2)
            
            '''
            print "click Add a language"
            if (self.tc_details['ui_dev0'](text='Add a language').exists):
                self.tc_details['ui_dev0'](text='Add a language').click()
            time.sleep(2)

            print "click search menu"
            if (self.tc_details['ui_dev0'](resourceId='android:id/locale_search_menu').exists):
                self.tc_details['ui_dev0'](resourceId='android:id/locale_search_menu').click()
            time.sleep(2)
            
            print "Set English Text"
            if (self.tc_details['ui_dev0'](resourceId='android:id/search_src_text').exists):
                self.tc_details['ui_dev0'](resourceId='android:id/search_src_text').set_text("English")
            time.sleep(2)
 
           
            press_enter(tc_details['dev0'])
            time.sleep(2)

            print "click select English text"
            if (self.tc_details['ui_dev0'](resourceId='android:id/locale',text='English').exists):
                self.tc_details['ui_dev0'](resourceId='android:id/locale',text='English').click()
            time.sleep(2)

            print "scroll to macau"
            self.tc_details['ui_dev0'](scrollable=True).scroll.to(text="Macau")
            time.sleep(2)

            print "click macau text"
            if (self.tc_details['ui_dev0'](text='Macau').exists):
                self.tc_details['ui_dev0'](text='Macau').click()
            time.sleep(2)

            '''
            print "drag the handle"
            if (self.tc_details['ui_dev0'](textContains='Macau').exists):
                self.tc_details['ui_dev0'](textContains='Macau').right(resourceId='com.android.settings:id/dragHandle').drag.to(width/2,0,100)
            time.sleep(2)

            print "click more options"
            if (self.tc_details['ui_dev0'](description='More options').exists):
                self.tc_details['ui_dev0'](description='More options').click()
            time.sleep(2)

            print "click remove button"
            if (self.tc_details['ui_dev0'](text='Remove').exists):
                self.tc_details['ui_dev0'](text='Remove').click()
            time.sleep(2)

            print "click English(Macau)"
            if (self.tc_details['ui_dev0'](textContains="Macau").exists):
                self.tc_details['ui_dev0'](textContains="Macau").click()
            time.sleep(2)

            ret1 = tc_validate_screentext(0, "English(Macau)",'FAIL', 10)

            print "click remove button"
            if (self.tc_details['ui_dev0'](description='Remove').exists):
                self.tc_details['ui_dev0'](description='Remove').click()
            time.sleep(2)

            print "click ok button"
            if (self.tc_details['ui_dev0'](description='OK').exists):
                self.tc_details['ui_dev0'](description='OK').click()
            time.sleep(2)

            ret2 = tc_validate_screentext(0, "English(Macau)",'FAIL', 10)

            print "back to multi app screen"
            #press menu(right button on buttom)
            press_switch_app(tc_details['dev0'])
	    time.sleep(2) 	    

            print "CLEAR ALL"
            self.tc_details['ui_dev0'](text="CLEAR ALL").click()
            time.sleep(5) 
             
            print ret1,ret2
            if (ret1==1 and ret2==0):
            	    tc_log("***********Setting Languages Sucessfully*******************",'INFO')
            else:
            	    tc_log("***********Setting Languages  Failed************************",'INFO')
	    	    raise TCFailureError                  
	    #Click the Save button on the right top of screen to save the Contact
	    #self.tc_details['ui_dev0'](resourceId="com.android.contacts:id/menu_save").click()
            #time.sleep(5)
            #Validation for new contact
            '''
            ret1 = tc_validate_screentext(0, "John",'FAIL', 10)
	    ret2 = tc_validate_screentext(0, "1 234-567-89",'FAIL', 10)
            ret3 = tc_validate_screentext(0, "Mobile",'FAIL', 10)          
            if ret1==1 and ret2==1 and ret3==1:
            	    tc_log("***********Create Contact Sucessfully*******************",'INFO')
            else:
            	    tc_log("***********Create Contact Failed************************",'INFO')
	    	    raise TCFailureError                  
                  
	    result = 'PASS'
            '''
	except TCFailureError:
	    tc_log("TCFailure Exception Raised" , 'INFO')
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
	  
