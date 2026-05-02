import unittest
from src.preprocessing import clean_resume

class TestPreprocessing(unittest.TestCase):
    def test_clean_resume(self):
        raw_text = "This is a   test\nresume  with multiple   spaces."
        expected = "This is a test resume with multiple spaces."
        self.assertEqual(clean_resume(raw_text), expected)

if __name__ == "__main__":
    unittest.main()
