from necromancer.version import Version
from tests import *
from tests.helpers import *


class TestVersion(unittest.TestCase):

    def test_set_version(self):
        ver = Version("0.0.2")
        self.assertEqual(ver.number, "0.0.2")

    def test_version_immutable(self):
        ver = Version("0.0.2")
        with pytest.raises(TypeError) as e:
            ver.number = "0.0.2"
