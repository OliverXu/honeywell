# -*- coding: utf-8 -*-

'''
Test Case Name : SMS_message_verify
Description    : Tests if able to do Encrypt the device.
		 Validates device has been encrypted or not

'''

import threading
import time
import sys
import os
import string
import random

# HATF imports
sys.path.insert(0, '../../../framework/common')
import log_analyzer
from tc_common import *
from tc_adb_commands import *

global testcase
global loganalyzer
loganalyzer = []
unfoundsms = []

def clear_app(dev_id):
        Run_Adb_Cmd(tc_details[dev_id], "shell input keyevent KEYCODE_APP_SWITCH")
    	Run_Adb_Cmd(tc_details[dev_id], "shell input keyevent 20")
    	Run_Adb_Cmd(tc_details[dev_id], "shell input keyevent 20")
    	for i in range (3):
    	    	Run_Adb_Cmd(tc_details[dev_id], "shell input keyevent DEL")

class test_case (threading.Thread):

	def __init__(self, threadID, name, tc_details):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.tc_details = tc_details

	# Function performs initial settings
	def test_case_preamble(self):
		tc_common_preamble()
                clear_app('dev0')
                clear_app('dev1')
	# Function that brings back the device to its initial condition
	def test_case_postamble(self):
		tc_log("Clean message for dev0", 'INFO')
		open_app(self.tc_details['dev0'], 'messaging_v')
                time.sleep(5)
                if self.tc_details['ui_dev1'](text=config_strings['dev0']['recv_mes_number'],className='android.widget.ImageView').exists:
                        self.tc_details['ui_dev1'](text=config_strings['dev0']['recv_mes_number'],className='android.widget.ImageView').click()
                else:
                        tc_log("Can not found recv sms number",'INFO')

		if self.tc_details['ui_dev0'](descriptionContains="More options",className='android.widget.ImageView').exists:
			self.tc_details['ui_dev0'](descriptionContains="More options",className='android.widget.ImageView').click()
                else:
                        tc_log("Can not found More options",'INFO')
		time.sleep(2)
		if self.tc_details['ui_dev0'](text="Delete").exists:
			self.tc_details['ui_dev0'](text="Delete").click()
		time.sleep(2)
		if self.tc_details['ui_dev0'](className='android.widget.Button', resourceId='android:id/button1').exists:
			self.tc_details['ui_dev0'](className='android.widget.Button', resourceId='android:id/button1').click()
		time.sleep(10)

		tc_log("Clean message for dev1", 'INFO')
		open_app(self.tc_details['dev1'], 'messaging_v')
                time.sleep(5)
		if self.tc_details['ui_dev1'](descriptionContains="More options").exists:
			self.tc_details['ui_dev1'](descriptionContains="More options").click()
                else:
                        tc_log("Can not found More options",'INFO')
		time.sleep(2)
		if self.tc_details['ui_dev1'](text="Delete").exists:
			self.tc_details['ui_dev1'](text="Delete").click()
		time.sleep(2)
		if self.tc_details['ui_dev1'](className='android.widget.Button', resourceId='android:id/button1').exists:
			self.tc_details['ui_dev1'](className='android.widget.Button', resourceId='android:id/button1').click()

		# clear call history
                clear_contacts(self.tc_details['dev0'])
                clear_contacts(self.tc_details['dev1'])

		goto_home_screen (self.tc_details['dev0'])
		goto_home_screen (self.tc_details['dev1'])

		return

	def run(self):
		result = 'PASS'
		try:

			print "Starting " + self.name
			print "Running test case thread"

			self.test_case_preamble()
			clear_contacts(self.tc_details['dev0'])
			count_send=0
			count_recv=0

			tc_log("Open message page by "+self.tc_details['dev0'], 'INFO')
			open_app(self.tc_details['dev0'], 'messaging_v')
			if self.tc_details['ui_dev0'](resourceId="com.android.messaging:id/start_new_conversation_button").exists:
				self.tc_details['ui_dev0'](resourceId="com.android.messaging:id/start_new_conversation_button").click()
                        elif self.tc_details['ui_dev0'](description="Start new conversation").exists:
                                self.tc_details['ui_dev0'](description="Start new conversation").click()
                                print "can not find add button"
                        time.sleep(5)
			#if self.tc_details['ui_dev0'](text="To").exists:
			self.tc_details['ui_dev0'](text="To").set_text(config_strings['dev0']['recv_phone_number'])
			click_enter(self.tc_details['dev0'])
                        time.sleep(5)

                        letter_sample = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        #count = 2
                        count = int(config_strings['dev0']['count'])
                        message_len = int(config_strings['dev0']['message_len'])
			for index in range(0,count):
				tc_log("Send message by "+ self.tc_details['dev0'], 'INFO')
				#message_intent(tc_details['dev0'], config_strings['dev0']['recv_phone_number'], config_strings['dev0']['message'] + str(index))
                                message_random = string.join(random.sample(letter_sample,message_len)).replace(" ","")
				#self.tc_details['ui_dev0'](text="Send message").set_text(config_strings['dev0']['message'] + str(index))
				self.tc_details['ui_dev0'](text="Send message").set_text(message_random)

				#time.sleep(3)
				if self.tc_details['ui_dev0'](resourceId="com.android.messaging:id/self_send_icon").exists:
					self.tc_details['ui_dev0'](resourceId="com.android.messaging:id/self_send_icon").click()
					count_send+=1
					tc_log("count_send:"+str(count_send),'INFO')

				tc_log("Check conversation page opened for "+self.tc_details['dev1'], 'INFO')
			        open_app(self.tc_details['dev1'], 'messaging_v')
				#open_notification(1)
				time.sleep(int(config_strings['dev0']['time_sleep']))
				if self.tc_details['ui_dev1'](text=config_strings['dev0']['send_mes_number']).exists:
					self.tc_details['ui_dev1'](text=config_strings['dev0']['send_mes_number']).click()
					if self.tc_details['ui_dev1'](text=config_strings['dev0']['send_mes_number']).exists:
						tc_log("Conversation opened successfully", 'INFO')
						#time.sleep(3)
						#if self.tc_details['ui_dev1'](resourceId="android:id/list").child(text=config_strings['dev0']['message']+str(index)).exists:
						if self.tc_details['ui_dev1'](resourceId="android:id/list").child(text = message_random).exists:
							tc_log("Message recevied by device[1]", 'INFO')
							count_recv+=1
							tc_log("count_recv:" + str(count_recv),'INFO')
                                                else:
                                                        time.sleep(60)
                                                        unfoundsms.append(message_random)
                                                        tc_log("add to unfoundsms",'INFO')
                                        else:
                                                unfoundsms.append(message_random)
                                                tc_log("add to unfoundsms",'INFO')
                                else:
                                        unfoundsms.append(message_random)
                                        tc_log("add to unfoundsms",'INFO')

                        tc_log(unfoundsms,'INFO')
                        if not count_send==count_recv and len(unfoundsms)>0 :
                                open_app(self.tc_details['dev1'], 'messaging_v')
                                time.sleep(3)
                                if self.tc_details['ui_dev1'](text=config_strings['dev0']['send_mes_number']).exists:
                                        #self.tc_details['ui_dev1'](text=config_strings['dev0']['send_mes_number']).click()
                                        time.sleep(3)
                                        for index in range(len(unfoundsms)):
                                                if count_recv > 10 :
                                                        self.tc_details['ui_dev1'](scrollable=True).fling.vert.toBeginning()
                                                        time.sleep(3)
                                                        self.tc_details['ui_dev1'](scrollable=True).scroll.to(textContains=unfoundsms[index])

                                                if self.tc_details['ui_dev1'](textContains=unfoundsms[index]).exists:
                                                        print "add recv"
                                                        count_recv+=1
                                                else:
                                                        print "can not find the unfounsms"
                                else:
                                         tc_log("can not find the send_mes_number",'INFO')
 
                                #self.tc_details['ui_dev0'](scrollable=True).fling.vert.toBeginning()
                                #self.tc_details['ui_dev1'](scrollable=True).fling.vert.toBeginning()
                        tc_log("finally count_recv:" + str(count_recv),'INFO')

			tc_log("Send voice call", 'INFO')
			time.sleep(2)
			call_intent(self.tc_details['dev0'], config_strings['dev0']['recv_phone_number'])
			time.sleep(5)
			# Verify the call is success
			if tc_validate_screentext(0, config_strings['dev0']['recv_phone_number_1'], 'FAIL', 10) > 0:
				tc_log("CALL Raised from device: Success", 'INFO')
			else:
				tc_log("CALL Raised from device: Failed", 'INFO')

			# Verify the receiver is get the call
                        open_notification(1)
                        time.sleep(5)
			if tc_validate_screentext(1, config_strings['dev1']['send_phone_number_1'], 'FAIL', 10) > 0:
				tc_log("CALL Answer from device: Success", 'INFO')
			else:
				tc_log("CALL Answer from device: Failed", 'INFO')

			# Receiving the call at device1, after waiting for it to ring
			time.sleep(10)
			receive_call(self.tc_details['dev1'])
			# Let the conversation continue for some time
			time.sleep(10)

			# Hanging up the call at device0
			end_call(self.tc_details['dev0'])

                        close_notification(1)
			time.sleep(2)

			cmd = "shell am start -n com.android.dialer/.DialtactsActivity"

			# print self.tc_details['phone']
			Run_Adb_Cmd(self.tc_details['dev0'], cmd)
			Run_Adb_Cmd(self.tc_details['dev1'], cmd)
			# open_app(self.tc_details['dev0'], self.tc_details['phone'])
			time.sleep(2)
                        
                        if self.tc_details['ui_dev0'](description='Call history').exists:
                                self.tc_details['ui_dev0'](description='Call history').click()
            		elif self.tc_details['ui_dev0'](description='Call History').exists:
                		self.tc_details['ui_dev0'](description='Call History').click()
            		elif self.tc_details['ui_dev0'](description='Recents').exists:
                		self.tc_details['ui_dev0'](description='Recents').click()
			time.sleep(2)

                        if self.tc_details['ui_dev1'](description='Call history').exists:
                                self.tc_details['ui_dev1'](description='Call history').click()
            		elif self.tc_details['ui_dev1'](description='Call History').exists:
                		self.tc_details['ui_dev1'](description='Call History').click()
            		elif self.tc_details['ui_dev1'](description='Recents').exists:
                		self.tc_details['ui_dev1'](description='Recents').click()
			time.sleep(2)

			if self.tc_details['ui_dev0'](text=config_strings['dev0']['recv_phone_number_1']).exists:
				tc_log("Call history verification successfully for dev0", 'INFO')
                        else:
                                result='FAIL'

			if self.tc_details['ui_dev1'](text=config_strings['dev1']['send_phone_number_1']).exists:
				tc_log("Call history verification successfully for dev1", 'INFO')
                        else:
                                result='FAIL'
			# call_intent(tc_details['dev0'], config_strings['dev0']['recv_phone_number'] )
			# time.sleep(5)
			# end_call(tc_details['dev0'])
			if count_recv >= count*0.98 and count_send ==count:#and send_call == recv_call:
				tc_log("Message send verification successfully", 'INFO')
			else:
				tc_log("Message received verification failed", 'INFO')
				result = 'FAIL'
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
		session_name = "messageverify"

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
	  
