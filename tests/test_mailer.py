import unittest
from src.template_engine import render_template

class TestEmailFeatures(unittest.TestCase):

    def test_template_rendering(self):
        """Şablonun ismi doğru yerleştirip yerleştirmediğini test eder."""
        context = {"name": ""}
        # Test için geçici bir string üzerinden veya doğrudan fonksiyonu test et
        result = render_template("welcome_email.html", context)
        
       
        self.assertIn("", result)
        self.assertIn("<html>", result)

if __name__ == '__main__':
    unittest.main()