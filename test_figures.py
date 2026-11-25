import unittest
import math
from lab_python_oop import Cube, Cone, Tetrahedron

class TestFigures(unittest.TestCase):
    def test_cube_volume(self):
        c = Cube(3)
        self.assertEqual(c.volume(), 27)

    def test_cube_error(self):
        with self.assertRaises(ValueError):
            Cube(-5)

    def test_cone_volume(self):
        c = Cone(3, 4)
        self.assertAlmostEqual(c.volume(), (1/3) * math.pi * 9 * 4)

    def test_tetrahedron_area(self):
        t = Tetrahedron(4)
        self.assertAlmostEqual(t.area(), math.sqrt(3) * 16)

if __name__ == '__main__':
    unittest.main()