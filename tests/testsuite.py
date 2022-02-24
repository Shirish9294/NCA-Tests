import unittest
from tests.unitTest_Login import NCACMS_ATS1
from tests.unitTest_addStaff import NCACMS_ATS2
from tests.unitTest_addVolunteer import NCACMS_ATS3
from tests.unitTest_Staff import NCACMS_ATS4
from tests.unitTest_StaffLogin import NCACMS_ATS5
from tests.unitTest_StaffActivity import NCACMS_ATS6
from tests.unitTest_StaffVolunter import NCACMS_ATS7
from tests.unitTest_StaffLocation import NCACMS_ATS8
from tests.unitTest_StaffVictims import NCACMS_ATS9
from tests.unitTest_StaffNotifications import NCACMS_ATS11
from tests.unitTest_VolunteerLogin import NCACMS_ATS12
from tests.unitTest_VolunteerActivity import NCACMS_ATS13
from tests.unitTest_VolunteerVictims import NCACMS_ATS14
from tests.unitTest_VolunteerAccount import NCACMS_ATS15
from tests.unitTest_VolunteerRequest import NCACMS_ATS16
from tests.unitTest_VolunteerApproved import NCACMS_ATS17
from tests.unitTest_Volunteerjoining import NCACMS_ATS18

login = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS1)
addstaff = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS2)
addvolunteer = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS3)
staff = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS4)
stafflogin = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS5)
staffactivity = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS6)
staffvolunteer = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS7)
stafflocation = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS8)
StaffVictims = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS9)
StaffNotifications = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS11)
VolunteerLogin = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS12)
VolunteerActivity = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS13)
VolunteerVictims = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS14)
VolunteerAccount = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS15)
VolunteerRequest = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS16)
VolunteerApproved = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS17)
Volunteerjoining = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS18)

test_suite = unittest.TestSuite(
    [login, addstaff, addvolunteer, staff, stafflogin, staffactivity, staffvolunteer, stafflocation,StaffVictims,StaffNotifications, VolunteerLogin,
     VolunteerActivity, VolunteerVictims, VolunteerAccount, VolunteerRequest,VolunteerApproved, Volunteerjoining ])

unittest.TextTestRunner().run(test_suite)
