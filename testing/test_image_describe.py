import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

import unittest
import unittest
from unittest.mock import patch
import image_description

class TestImageDescription(unittest.TestCase):
    @patch('image_description.describe_image')
    def test_describe_image(self, mock_describe):
        # Mocking Azure's Computer Vision response
        mock_describe.return_value = "a cat sitting on a mat"
        result_description = image_description.describe_image(None, 'dummy_image.jpg')
        self.assertEqual(result_description, "a cat sitting on a mat")

if __name__ == '__main__':
    unittest.main()
