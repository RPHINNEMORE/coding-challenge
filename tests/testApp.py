import unittest
import sys


from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from view.appView import AppView
from model.appModel import AppModel


class TestView(unittest.TestCase):
    def test_view(self):
        view = AppView()
        self.assertEqual(view.opening_message(), 0)
        self.assertEqual(view.display_menu(), 0)
        self.assertEqual(view.quit_program(), 0)
        self.assertEqual(view.display_bad_request_error(), 0)
        self.assertEqual(view.invalid_input_error_message(), 0)

class TestModel(unittest.TestCase):
    # happy path test for single ticket
    def test_single_ticket_request(self):
        model = AppModel()
        ticket = model.get_ticket(1)
        self.assertEqual(len(ticket), 1)
        self.assertEqual(ticket['ticket']['id'], 1)
    # happy path test for all tickets
    def test_all_tickets_request(self):
        model = AppModel()
        all_tickets = model.get_all_tickets()
        self.assertEquals(len(all_tickets), 101)

if __name__ == '__main__':
    unittest.main()