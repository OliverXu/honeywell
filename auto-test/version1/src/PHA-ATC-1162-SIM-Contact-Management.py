# -*- coding: utf-8 -*-

'''
Test Case Name : PHA-ATC-1162 SIM Contact Management
Description    : Tests adding 100 contacts then deleting 20 contacts then adding 5 more contacts
		 Validates after rebooting devices the contacts are saved correctly.

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


class test_case (threading.Thread):

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
		goto_home_screen (self.tc_details['dev0'])
		return

	def add_contact(self, name, number):
		# Click the Add Contact button in the right bottom of screen
		self.tc_details['ui_dev0'](description="add new contact").click()
		time.sleep(2)
		# Handle the saving option pop-up window
		if self.tc_details['ui_dev0'](text="Keep local").exists:
			self.tc_details['ui_dev0'](text="Keep local").click()
		# Input Contact name
		self.tc_details['ui_dev0'](text="Name").click()
		time.sleep(2)
		self.tc_details['ui_dev0'](text="Name").set_text(name)
		time.sleep(2)
		go_back(tc_details['dev0'])

		# Input Phone number
		self.tc_details['ui_dev0'](text="Phone").click()
		time.sleep(2)
		self.tc_details['ui_dev0'](text="Phone").set_text(number)
		time.sleep(2)
		go_back(tc_details['dev0'])

		# Click Save to save the contact
		self.tc_details['ui_dev0'](description="Save").click()
		time.sleep(2)
		# Get back to Contact list
		go_back(tc_details['dev0'])
		time.sleep(2)
		# Fling to the top of contact list
		self.tc_details['ui_dev0'](scrollable=True).fling.vert.toBeginning()
		time.sleep(2)
		return

	def delete_contact(self, name):
		# scroll to the contact name
		self.tc_details['ui_dev0'](scrollable=True).scroll.to(text=name)
		time.sleep(2)
		# Click the contact
		self.tc_details['ui_dev0'](text=name).click()
		time.sleep(2)
		# Delete the contact
		self.tc_details['ui_dev0'](description="More options").click()
		time.sleep(2)
		self.tc_details['ui_dev0'](text="Delete").click()
		time.sleep(2)
		self.tc_details['ui_dev0'](text="OK").click()
		time.sleep(2)
		# Fling to the top of contact list
		self.tc_details['ui_dev0'](scrollable=True).fling.vert.toBeginning()
		time.sleep(2)
		return

	def validate_contact(self, name, validation_type):
		error_flag = 0
		if validation_type == "exist":
			if self.tc_details['ui_dev0'](scrollable=True).scroll.to(text=name):
				tc_log("Adding contact " + name + " is added sucessfully",'INFO')
			else:
				tc_log("error: contact " + name + " IS NOT added", 'INFO')
				error_flag += 1
		else:
			if self.tc_details['ui_dev0'](scrollable=True).scroll.to(text=name):
				tc_log("error: Deleting contact " + name + " IS NOT deleted", 'INFO')
				error_flag += 1
			else:
				tc_log("Deleting contact " + name + " is deleted sucessfully", 'INFO')
		return error_flag

	def run(self):
		result = 'FAIL'
		try:

			print "Starting " + self.name
			print "Running test case thread"
			self.test_case_preamble()

			# Open Contact app and select "ALL CONTACTS" tab
			cmd = "shell am start -n com.android.contacts/.activities.PeopleActivity"
			Run_Adb_Cmd(self.tc_details['dev0'], cmd)
			time.sleep(2)
			self.tc_details['ui_dev0'](text="All contacts", className="android.widget.TextView").click()

			# Contact adding list and deleting list
			contact_name_arr = []
			delete_name_arr = []

			# List for creating random name and phone number
			letter_sample = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
			number_sample = ['0','1','2','3','4','5','6','7','8','9']

			# Indicate the adding and deleting is correct or not
			test_error_flag = 0

			# Add 100 contacts
			for i in range(5):
				contact_name = string.join(random.sample(letter_sample,8)).replace(" ","")
				contact_name_arr.append(contact_name)
				phone_number = string.join(random.sample(number_sample,10)).replace(" ","")
				self.add_contact(contact_name, phone_number)
				test_error_flag += self.validate_contact(contact_name, "exist")
			# Erase 20 contacts
			for i in range(1):
				delete_name = string.join(random.sample(contact_name_arr, 1))
				contact_name_arr.remove(delete_name)
				delete_name_arr.append(delete_name)
				self.delete_contact(delete_name)
				test_error_flag += self.validate_contact(delete_name, "non-exist")
			# Add 5 more contacts
			for i in range(2):
				contact_name = string.join(random.sample(letter_sample,8)).replace(" ","")
				contact_name_arr.append(contact_name)
				phone_number = string.join(random.sample(number_sample,10)).replace(" ","")
				self.add_contact(contact_name, phone_number)
				test_error_flag += self.validate_contact(contact_name, "exist")

			# Reboot the device
			reboot_device(self.tc_details['dev0'])
			tc_log("Sleep 300 seconds for device reboot", 'INFO')
			time.sleep(300)

			# Light and unlock the screen after reboot
			Run_Adb_Cmd(tc_details['dev0'], "shell input keyevent 26")
			Run_Adb_Cmd(tc_details['dev0'], "shell input keyevent 82")

			# Open Contact app and select "ALL CONTACTS" tab
			cmd = "shell am start -n com.android.contacts/.activities.PeopleActivity"
			Run_Adb_Cmd(self.tc_details['dev0'], cmd)
			time.sleep(2)
			self.tc_details['ui_dev0'](text="All contacts", className="android.widget.TextView").click()

			# Check the contacts after reboot
			for i in range(len(contact_name_arr)):
				test_error_flag += self.validate_contact(contact_name_arr[i], "exist")

			# Validate adding and deleting warnings
			if test_error_flag != 0:
				tc_log("Test has " + str(test_error_flag) + " error(s)",'INFO')
				raise TCFailureError
			else:
				result = 'PASS'
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
		session_name = "contactmanagement"

		tc_details, loganalyzer = tc_initialize(session_name, "PHA-ATC-1162-SIM-Contact-Management.py")
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
	  
