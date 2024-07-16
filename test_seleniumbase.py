from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_basic(self):
        self.open("https://www.google.com")
        self.type("input[name='q']", "Selenium")
        self.click("input[type='submit']")
        self.assert_element("h3")
        self.assert_text("Selenium", "h3")

if __name__ == "__main__":
    from pytest import main
    main(['-s', 'test_seleniumbase.py'])

