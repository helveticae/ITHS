import sys, os
import unittest
"""A test case is the individual unit of testing.
It checks for a specific response to a particular set of inputs.
unittest provides a base class, TestCase, which may be used to create new test cases."""

print(__file__)

# change dir to where this file is
os.chdir(os.path.dirname(__file__))

# we define path that is up one step
# in this path: vector.py, plotter.py and manual_testing.ipynb
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)
print(path_to_vector_module)

from vector import Vector


class TestVector(unittest.TestCase):
    def test_create_2D_vector(self):
        v = Vector(1,2)
        self.assertEqual(v.numbers,(1,2))


if __name__ == "__main__":
    unittest.main()