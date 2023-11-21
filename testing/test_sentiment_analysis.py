import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))
import unittest
import sentiment_analysis

class TestSentimentAnalysis(unittest.TestCase):
    def test_analyze_sentiment(self):
        # Test with a known string
        test_text = "I love sunny days."
        result = sentiment_analysis.analyze_sentiment(test_text)
        self.assertIn("Polarity", result)

if __name__ == '__main__':
    unittest.main()
