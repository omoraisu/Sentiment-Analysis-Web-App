from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        res1 = sentiment_analyzer("I love working with Python")
        res2 = sentiment_analyzer("I hate working with Python")
        res3 = sentiment_analyzer("I am neutral on Python")

        self.assertEqual(res1['label'], 'SENT_POSITIVE')
        self.assertEqual(res2['label'], 'SENT_NEGATIVE')
        self.assertEqual(res3['label'], 'SENT_NEUTRAL')

unittest.main()
