import unittest
import exploit


class TestScript(unittest.TestCase):

    def test_run_no_connection(self):
        try:
            res = exploit.run_exploit(
                target_url="http://localhost",
                target_port="8080",
                target_file="/etc/shadow"
            )
            assert not res
        except:
            assert False

    def test_with_connection_good_file(self):
        res = exploit.run_exploit(
            target_url="http://localhost",
            target_port=3000,
            target_file="/etc/passwd"
        )
        assert res == True


