import unittest

from tests.unitTest_VolunteerLogin import NCACMS_ATS12
from tests.unitTest_VolunteerActivity import NCACMS_ATS13
from tests.unitTest_VolunteerVictims import NCACMS_ATS14
from tests.unitTest_VolunteerAccount import NCACMS_ATS15

VolunteerLogin = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS12)
VolunteerActivity = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS13)
VolunteerVictims = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS14)
VolunteerAccount = unittest.TestLoader().loadTestsFromTestCase(NCACMS_ATS15)


test_suite = unittest.TestSuite(
    [VolunteerLogin, VolunteerAccount, VolunteerActivity, VolunteerVictims ])

unittest.TextTestRunner().run(test_suite)
