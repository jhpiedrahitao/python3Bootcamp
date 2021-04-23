import unittest 
import cap

class TestCap(unittest.TestCase):
	"""docstring for TestCap"unittest.TestCasef __init__(self, arg):
		super(TestCap,unittest.TestCase.__init__()
		self.arg = arg
	"""
	def test_one_word(self):
		text='python' 
		result= cap.cap_text(text)
		self.assertEqual(result,'Python')
	def test_multiple_wordsCap(self):
		text='monty python' 
		result= cap.cap_text(text)
		self.assertEqual(result,'Monty Python')

if __name__=='__main__':
	unittest.main()