import unittest
import ndio.remote.neurodata as neurodata
import test_settings

neurodata_token = "1524d74ec9a915536061af8fd5b51f2cde7de9a5"
test_token = "b1876fab697e519e0cfe4acc9ca0496bf2889e17"
Default_token = ""
HOSTNAME = hostname=test_settings.HOSTNAME

class TestgetURL(unittest.TestCase):

    def setUp(self):
        self.neurodata = neurodata(user_token = neurodata_token, hostname=HOSTNAME)
        self.public = neurodata(hostname=HOSTNAME)
        self.test = neurodata(user_token = Default_token, hostname=HOSTNAME)
        self.private_project = "https://{}/sd/private_neuro/info/".format(HOSTNAME)
        self.public_project = "https://{}/sd/public_neuro/info/".format(HOSTNAME)
        self.private_test_project = "https://{}/sd/private_test_neuro/info/".format(HOSTNAME)
    def test_masterToken(self):
        try:
            req = self.neurodata.getURL(self.private_project)
            print(req.content)
            self.assertEqual(req.status_code, 200)
        except ValueError as e:
            print(req.content)
        try:
            req2 = self.neurodata.getURL(self.public_project)
            self.assertEqual(req2.status_code, 200)
        except ValueError as e:
            print(e)
            
        try:
            req3 = self.neurodata.getURL(self.private_test_project)
            self.assertEqual(req3.status_code, 200)
        except ValueError as e:
            print(e)
    
    def test_testToken(self):
        try:
            req = self.test.getURL(self.private_project)
            self.assertEqual(req.status_code, 403)
        except ValueError as e:
            print(e)
        try:
            req2 = self.test.getURL(self.public_project)
            self.assertEqual(req2.status_code, 200)
        except ValueError as e:
            print(e)
        try:
            req3 = self.test.getURL(self.private_test_project)
            self.assertEqual(req3.status_code, 200)
        except ValueError as e:
            print(e)


    def test_publicToken(self):
        try:
            req = self.public.getURL(self.private_project)
            self.assertEqual(req.status_code, 403)
        except ValueError as e:
            print(req.content)
        try:
            req2 = self.public.getURL(self.public_project)
            self.assertEqual(req2.status_code, 200)
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    unittest.main()
