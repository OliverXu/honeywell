'''
Test Case Name : HELAN-ATC-2953-L1-incoming-call
Description    : Verify that the DUT is able to receive call and call is successfully hunged up, DUT exits the call screen.
'''
import threading
import time
import sys
import os

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

    def test_case_preamble(self):
        tc_common_preamble()
        # Navigates to the main screen
	goto_home_screen(self.tc_details['dev0'])
	return

    def test_case_postamble(self):
        end_call(self.tc_details['dev0'])
        go_back(self.tc_details['dev0'])
        return

    def run(self):
        result = 'FAIL'		
        try:
            print "Starting " + self.name
	    print "Running test case thread"
            
            self.test_case_preamble()
            # Raising call to specific number mentioned in the testcase config file from
	    # device0 to device1
	    call_intent(self.tc_details['dev0'], self.tc_details['contact_number_1'])
            time.sleep(5)
            tc_validate_string(0,'valid_point_1','FAIL', 60)
            if self.tc_details['ui_dev0'](text = "Phone").exists:
                self.tc_details['ui_dev0'](text = "Phone").click()
            time.sleep(3)

            if self.tc_details['ui_dev0'](text = "Always").exists:
                self.tc_details['ui_dev0'](text = "Always").click()
            time.sleep(3) 
	   
	    tc_log("CALL Raised from device: Success", 'INFO')
	    
	    tc_validate_string(1,'valid_point_1','FAIL', 60)

	    # Receiving the call at device1, after waiting for it to ring
	    time.sleep(5)
	    receive_call(self.tc_details['dev1'])
            # Let the conversation continue for some time
	    time.sleep(15)
	    
	    # Hanging up the call at device0
	    end_call(self.tc_details['dev0'])
	    tc_validate_string(0,'valid_point_2','FAIL', 60)
	    time.sleep(5)
	    go_back(self.tc_details['dev0'])

	    result = 'PASS'
	
        except TCFailureError:
	    tc_log("TCFailure Exception Raised" , 'INFO')
	    result = 'FAIL'
			
        finally:
	    self.test_case_postamble()		
	    tc_verdict(result)
	    tc_details['verdict'] = result
	    tc_cleanup()
        
	    tc_log("Completed test steps for " + self.name, 'INFO')


if __name__ == "__main__":
    try:
        session_name = sys.argv[1]
	tc_details, loganalyzer = tc_initialize(session_name, sys.argv[0])

	# Start the new test case thread
	testcase = test_case(1, tc_details['tc_name'], tc_details)
	testcase.start()
	tc_details['testcasethread'] = testcase
	tc_timer_testcase(int(tc_details['tc_duration']))
    except TCFailureError:
	tc_log("TCFailure Exception Raised", 'INFO')
    finally:
	tc_log("Test Case Thread Exits",'INFO')
	if tc_details['verdict'] == 'PASS':
	    sys.exit(0)
	else:
	    sys.exit(1)
