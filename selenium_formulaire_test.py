import time
from seleniumbase import BaseCase

class TestContactForm(BaseCase):
	def test_submit_contact_form(self):
		self.open("http://localhost/formulaire.php")
		self.type("#name", "Linus Torvalds")
		time.sleep(5) # Temporisation de 5 secondes
		self.type("#email", "linus.torvalds@linux.com")
		time.sleep(5) # Temporisation de 5 secondes

		self.type("#message", "Ce message est un test")
		time.sleep(5) # Temporisation de 5 secondes
