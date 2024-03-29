import unittest

import imaginar

class unit_imaginar(unittest.TestCase):
        
        def test_suma(self):
                self.assertEqual(imaginar.suma((2,5),(3,2)),(5,7))

        def test_resta(self):
                self.assertEqual(imaginar.resta((2,5),(3,2)),(-1,3))

        def test_multiplicacion(self):
                self.assertEqual(imaginar.multiplicacion((2,3),(4, 5)),(-7,22))

        def test_division(self):
                self.assertEqual(imaginar.division((3,2),(-1, 2)),(0.2,-1.6))

        def test_fase(self):

                self.assertEqual(imaginar.fase((3,2)),0.59)

        def test_modulo(self):
                
                self.assertEqual(imaginar.modulo((3,2)),3.61)

        def test_cartesiano_polar(self):


                self.assertEqual(imaginar.cartesiano_polar((3,2)),(3.61, 0.59))

        def test_polar_cartesiano(self):
                self.assertEqual(imaginar.polar_cartesiano((3,60)),(-2.86, -0.91))

        def test_conjugado(self):
                self.assertEqual(imaginar.conjugado((6,-5)),(6,5))

    
     
if True:
    unittest.main()
