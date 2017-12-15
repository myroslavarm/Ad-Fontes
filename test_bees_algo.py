from unittest import TestCase
from BeesAlgo import BeesAlgo

b = BeesAlgo()
flowers = [(-1.09, 0.35), (0.785, -1.75), (-0.893, 1.34)]


class TestBeesAlgo(TestCase):
    def test_rand_init_extended(self):
        result = b.rand_init_extended(50, [-2.048, 2.048], [-2.048, 2.048])
        self.assertEquals(50, len(result))

    def test_de_jong(self):
        self.assertEquals(3905.93, b.de_jong([1, 1]))

    def test_fitness(self):
        result = b.fitness(flowers)
        self.assertEquals(True, isinstance(result[0], tuple))

    def test_max_fitness_of_recruits(self):
        result = b.max_fitness_of_recruits(((-1.09, 0.35), (0.785, -1.75)), 2)
        self.assertEquals(True, isinstance(result[0][0], float))

    def test_main(self):
        result = b.main()
        self.assertEquals(True, isinstance(result[0], tuple))
