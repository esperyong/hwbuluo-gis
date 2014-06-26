import unittest
from hwbuluocontrib.gis.coordinatetransform import wgs2gcj

class CoordinateTransformTest(unittest.TestCase):

    def test_wgs2gcj(self): 
        self.assertEquals(wgs2gcj(39.891082,116.396135),
                          (39.89248436758296, 116.40237600938156))





