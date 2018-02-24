import unittest
import sys


from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from view.appView import AppView


# note some tests missing in test_view
class TestView(unittest.TestCase):
    def test_view(self):
        view = AppView()
        self.assertEqual(view.opening_message(), 0)
        self.assertEqual(view.display_menu(), 0)
        self.assertEqual(view.quit_program(), 0)
        self.assertEqual(view.display_bad_request_error(), 0)
        self.assertEqual(view.invalid_input_error_message(), 0)



if __name__ == '__main__':
    unittest.main()