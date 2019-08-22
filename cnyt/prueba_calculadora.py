import unittest

import calculadora_matrices
import imaginar

class unit_imaginar(unittest.TestCase):
        
        def test_adicion_vectores(self):
                self.assertEqual(calculadora_matrices.adicion_vectores([[(2,1),(0,0),(1,3)]],[[(3,2),(4,3),(5,2)]]),  [[(4, 2), (0, 0), (2, 6)], [(6, 4), (8, 6), (10, 4)]])

     #   def test_inversion_vectores(self):
       #         self.assertEqual(calculadora_matrices.inversion_vectores([[(2,1),(0,0),(1,3)]],[[(3,2),(4,3),(5,2)]]),  [[(4, 2), (0, 0), (2, 6)], [(6, 4), (8, 6), (10, 4)]])
        def test_matriz_adjunta(self):
                self.assertEqual(calculadora_matrices.matriz_adjunta([[(1,0),(0,0),(0,0)],[(0,0),(0,1),(0,2)],[(1,-1),(0,0),(1,1)]]),[[(-1, 1), (2, 2), (-1, -1)], [(0, 0), (1, 1), (0, 0)], [(0, 0), (0, -2), (0, 1)]])

        def test_determinante(self):
                self.assertEqual(calculadora_matrices.determinante([[(4,2),(2,0),(-3,-2)],[(1,0),(0,5),(-2,0)],[(1,0),(-2,-5),(4,0)]]),(-36, 32)) 
if True:
    unittest.main()
