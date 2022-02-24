import unittest

from tests.unitTest_Login import NCACMS_ATS1
from tests.unitTest_addStaff import NCACMS_ATS2
from tests.unitTest_addVolunteer import NCACMS_ATS3
from tests.unitTest_VolunteerRequest import NCACMS_ATS16
from tests.unitTest_VolunteerApproved import NCACMS_ATS17
from tests.unitTest_Volunteerjoining import NCACMS_ATS18

login = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS1)
addstaff = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS2)
addvolunteer = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS3)
VolunteerRequest = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS16)
VolunteerApproved = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS17)
Volunteerjoining = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS18)

test_suite = unittest.TestSuite(
    [login, addstaff, addvolunteer, Volunteerjoining, VolunteerRequest, VolunteerApproved])

unittest.TextTestRunner().run(test_suite)
