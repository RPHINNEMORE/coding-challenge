import sys

from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from model.appModel import AppModel
from view.appView import AppView


class AppController:
    def __init__(self):
        self.model = AppModel()
        self.view = AppView()
        self.input = ""
        self.current_page = 1
        self.ticket_id = ""

    def run(self):
        self.view.opening_message()
        self.display_main_menu()

    def get_user_input(self):
        self.input = raw_input()

    def get_total_ticket_list(self):
        total_ticket_list = self.model.get_all_tickets()
        if total_ticket_list == 0:
            self.view.display_bad_request_error()
        else:
            return total_ticket_list

    def handle_search(self):
        total_ticket_list = self.get_total_ticket_list()
        self.manage_search_single_ticket(total_ticket_list)

    def handle_view(self):
        total_ticket_list = self.get_total_ticket_list()
        self.view_all_tickets(total_ticket_list)

    def display_main_menu(self):
        while True:
            self.get_user_input()
            if self.input == "menu":
                self.view.display_menu()
            elif self.input == "view":
                self.handle_view()
            elif self.input == "search":
                self.handle_search()
            elif self.input == "quit":
                sys.exit(self.view.quit_program())
            else:
                self.view.invalid_input_error_message()
            self.input = ""

    def manage_view_all_tickets(self, total_ticket_list, pages):
        while True:
            self.get_user_input()
            if self.input == "next":
                if (self.current_page + 1) <= pages:
                    self.current_page = self.current_page + 1
                    self.view_all_tickets(total_ticket_list)
                else:
                    print("\nYou are at the end of the ticket list\n")
            elif self.input == "previous":
                if (self.current_page - 1) >= 1:
                    self.current_page = self.current_page - 1
                    self.view_all_tickets(total_ticket_list)
                else:
                    print("\nYou are at the beginning of the ticket list\n")
            elif self.input == "menu":
                self.view.display_menu()
                self.display_main_menu()
            elif self.input == "quit":
                sys.exit(self.view.quit_program())
            else:
                self.view.invalid_input_error_message()
            self.input = ""

    def view_all_tickets(self, total_ticket_list):
        pages = self.model.calculate_total_pages(total_ticket_list)
        page_dict = self.model.paginate_tickets(total_ticket_list, pages)
        paginated_ticket_list = page_dict[self.current_page]
        self.view.display_tickets(self.current_page, pages, paginated_ticket_list)
        self.manage_view_all_tickets(total_ticket_list, pages)

    def manage_search_single_ticket(self, total_ticket_list):
        self.view.display_ticket_search_options(total_ticket_list)
        while True:
            self.get_user_input()
            if (self.input).isdigit():
                self.ticket_id = self.input
                ticket = self.model.get_ticket(self.ticket_id)
                self.view.display_single_ticket(ticket, total_ticket_list)
            elif self.input == "menu":
                self.view.display_menu()
                self.display_main_menu()
            elif self.input == "quit":
                sys.exit(self.view.quit_program())
            self.input = ""


if __name__ == "__main__":
    c = AppController()
    c.run()
