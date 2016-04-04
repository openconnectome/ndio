import unittest
import ndio.remote.neurodata as neurodata
import ndio.remote.errors
import numpy
import random


class TestXYZZYX(unittest.TestCase):

    def setUp(self):
        self.nd = neurodata()
        self.nd_force_chunk = neurodata(chunk_threshold=0)

    def test_post_get_no_chunk(self):
        token = 'ndio_demos'
        channel = 'image'
        cutout = numpy.ones((10, 10, 10)).astype(int)
        cutout[2, 3, 4] = random.randint(100, 200)
        self.nd.post_cutout(token, channel, 20, 20, 20, cutout, resolution=0)
        pulldown = self.nd.get_cutout(token, channel,
                                      20, 25, 20, 25, 20, 25, resolution=0)
        self.assertEqual(cutout[2, 3, 4], pulldown[2, 3, 4])

    def test_post_get_chunk(self):
        token = 'ndio_demos'
        channel = 'image'
        cutout = numpy.ones((10, 10, 10)).astype(int)
        cutout[2, 3, 4] = random.randint(100, 200)
        self.nd_force_chunk.post_cutout(token, channel,
                                        20, 20, 20, cutout, resolution=0)
        pulldown = self.nd_force_chunk.get_cutout(token, channel,
                                                  20, 25, 20, 25, 20, 25,
                                                  resolution=0)
        self.assertEqual(cutout[2, 3, 4], pulldown[2, 3, 4])


if __name__ == '__main__':
    unittest.main()
