import unittest

import calculadora_matrices
import imaginar

class unit_imaginar(unittest.TestCase):
        
        def test_adicion_vectores(self):
                self.assertEqual(calculadora_matrices.adicion_vectores([(3,1),(2,1),(4,2)],[(3,2),(4,3),(5,2)]),[[(6, 3), (6, 4), (9, 4)]] )

        def test_inversa(self):
                 self.assertEqual(calculadora_matrices.inversa_vectores([(1,-1),(0,0),(1,1)]),[(-1, 1), (0, 0), (-1, -1)])

        def test_multiplicacion_escalar(self):
                self.assertEqual(calculadora_matrices.producto_escalar((2,4),[(2,-9),(0,0),(1,-5)]),[(40, -10), (0, 0), (22, -6)])

        def test_adicion_matrices(self):
                self.assertEqual(calculadora_matrices.adicion_matrices([[(2,1),(0,0),(1,3)],[(1,0),(2,4),(3,5)]],[[(3,2),(4,3),(5,2)],[(3,2),(4,3),(5,2)]]),  [[(5, 3), (4, 3), (6, 5)], [(4, 2), (6, 7), (8, 7)]])

        def test_inversa_matrices(self):
                self.assertEqual(calculadora_matrices.inversa([[(1,0),(0,0),(0,0)],[(0,0),(0,1),(0,2)],[(1,-1),(0,0),(1,1)]]),[[(1.0, 0.0), (0.0, 0.0), (0.0, 0.0)], [(0.0, -2.0), (0.0, -1.0), (-1.0, 1.0)], [(0.0, 1.0), (0.0, 0.0), (0.5, -0.5)]])

        def test_multiplicacion_escalar_matrices(self):
            self.assertEqual(calculadora_matrices.multiplicacion_escalar_matrices((2,4),[[(2,-9),(0,0),(1,-5)],[(3,0),(0,0),(0,3)],[(5,2),(-1,-3),(1,0)]]),[[(40, -10), (0, 0), (22, -6)], [(6, 12), (0, 0), (-12, 6)], [(2, 24), (10, -10), (2, 4)]])

        def test_transpuesta(self):
            self.assertEqual(calculadora_matrices.transpuesta([[(2,-9),(0,0),(1,-5)],[(3,0),(0,0),(0,3)],[(5,2),(-1,-3),(1,0)]]),[[(2, -9), (3, 0), (5, 2)], [(0, 0), (0, 0), (-1, -3)], [(1, -5), (0, 3), (1, 0)]])
        
        def test_conjugado(self):
            self.assertEqual(calculadora_matrices.conjugada([[(2,1),(3,0),(-1,4)],[(4,-1),(5,0),(17,-2)],[(1,0),(3,-1),(1,3)]]),[[(2, -1), (3, 0), (-1, -4)], [(4, 1), (5, 0), (17, 2)], [(1, 0), (3, 1), (1, -3)]])

        def test_adjunta(self):
               self.assertEqual(calculadora_matrices.adjunta([[(1,0),(0,0),(0,0)],[(0,0),(0,1),(0,2)],[(1,-1),(0,0),(1,1)]]),[[(-1, 1), (2, 2), (-1, -1)], [(0, 0), (1, 1), (0, 0)], [(0, 0), (0, -2), (0, 1)]])

        #def test_accion(self):


        #def test_norma_matricial:

           #def test_distancia_entrematrices 

        def test_unitaria(self):
            self.assertEqual(calculadora_matrices.matriz_unitaria([[(1,0),(-1,1)],[(1,1),(1,0)]]),True)

        def test_Hermitian(self):
                self.assertEqual(calculadora_matrices.matriz_hermitiana([[(3,0),(2,1)],[(2,-1),(1,0)]]),True)          

        def test_producto_tensor(self):
                self.assertEqual(calculadora_matrices.producto_tensor([[(2,1),(3,0),(-1,4)],[(4,-1),(5,0),(17,-2)],[(1,0),(3,-1),(1,3)]],[[(4,2),(2,0),(-3,-2)],[(1,0),(0,5),(-2,0)],[(1,0),(-2,0),(4,0)]]),[[(6, 8), (4, 2), (-4, -7), (2, 1), (-5, 10), (-4, -2), (2, 1), (-4, -2), (8, 4)], [(12, 6), (6, 0), (-9, -6), (3, 0), (0, 15), (-6, 0), (3, 0), (-6, 0), (12, 0)], [(-12, 14), (-2, 8), (11, -10), (-1, 4), (-20, -5), (2, -8), (-1, 4), (2, -8), (-4, 16)], [(18, 4), (8, -2), (-14, -5), (4, -1), (5, 20), (-8, 2), (4, -1), (-8, 2), (16, -4)], [(20, 10), (10, 0), (-15, -10), (5, 0), (0, 25), (-10, 0), (5, 0), (-10, 0), (20, 0)], [(72, 26), (34, -4), (-55, -28), (17, -2), (10, 85), (-34, 4), (17, -2), (-34, 4), (68, -8)], [(4, 2), (2, 0), (-3, -2), (1, 0), (0, 5), (-2, 0), (1, 0), (-2, 0), (4, 0)], [(14, 2), (6, -2), (-11, -3), (3, -1), (5, 15), (-6, 2), (3, -1), (-6, 2), (12, -4)], [(-2, 14), (2, 6), (3, -11), (1, 3), (-15, 5), (-2, -6), (1, 3), (-2, -6), (4, 12)]])
unittest.main()

        
        

