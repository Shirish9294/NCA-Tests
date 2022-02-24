import unittest

from tests.unitTest_Staff import NCACMS_ATS4
from tests.unitTest_StaffLogin import NCACMS_ATS5
from tests.unitTest_StaffActivity import NCACMS_ATS6
from tests.unitTest_StaffVolunter import NCACMS_ATS7
from tests.unitTest_StaffLocation import NCACMS_ATS8
from tests.unitTest_StaffVictims import NCACMS_ATS9
from tests.unitTest_StaffNotifications import NCACMS_ATS11

staff = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS4)
stafflogin = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS5)
staffactivity = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS6)
staffvolunteer = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS7)
stafflocation = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS8)
StaffVictims = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS9)
StaffNotifications = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS11)

test_suite = unittest.TestSuite(
    [stafflogin, staff, staffactivity, staffvolunteer, stafflocation, StaffVictims, StaffNotifications])

unittest.TextTestRunner().run(test_suite)
