import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

import unittest
import ocr

class TestOCR(unittest.TestCase):
    def test_read_text(self):
        expected_keywords = ["12 point text", "test the ocr code", "quick brown dog jumped over the lazy fox"]
        reader = ocr.initialize_ocr()
        result_text = ocr.read_text(reader, 'testing/images/testocr.png')
        
        for keyword in expected_keywords:
            self.assertIn(keyword, result_text)


if __name__ == '__main__':
    unittest.main()
