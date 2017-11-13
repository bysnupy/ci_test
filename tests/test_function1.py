from unittest import TestCase
from function1 import Function1

class TestFunction1(TestCase):

  def test_hello(self):
    self.assertEqual(Function1.hello(self), 'Hello CI world')

if __name__ == '__main__':
  unittest.main()
