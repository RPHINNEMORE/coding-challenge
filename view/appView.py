class AppView:
    def __init__(self):
        pass

    def opening_message(self):
        print("\n------------------ Welcome to Zendesk's Ticket Viewer Application ------------------\n")
        print("This application can be used to view all tickets or search for a single ticket\n")
        print("To see a list of options, enter 'menu' or to exit the application, enter 'quit'\n")
        return 0

    def display_menu(self):
        print("\n----------------------------- Ticket Viewer Menu Mode -----------------------------\n")
        print("Here are a list of options for the Ticket Viewer Application: \n")
        print("1) To see all tickets, enter 'view'\n")
        print("2) To search for a single ticket, enter 'search'\n")
        print("Enter your choice here: \n")
        return 0

    def quit_program(self):
        print("\nClosing the Ticket Viewer Application\n")
        print("Goodbye now\n")
        return 0

    def display_tickets(self, current_page, pages, paginated_ticket_list):
        print("\n----------------------------- Ticket Viewer View Mode -----------------------------\n")
        print("Displaying tickets on page: " + str(current_page) + " of " + str(pages) + "\n")
        for ticket in paginated_ticket_list:
            ticket_id = ticket['id']
            ticket_subject = ticket['subject']
            ticket_status = ticket['status']
            print("Ticket ID " + "'" + str(ticket_id) + "'" +
                  " has the subject " + "'" + ticket_subject + "'" +
                  " and status " + "'" + ticket_status + "'" + " \n")
        print("\nTo see the next page, enter 'next' and to see the previous page, enter 'previous'")
        print("\nTo see a list of options, enter 'menu' or to exit the application, enter 'quit'\n")

    def display_ticket_search_options(self, total_ticket_list):
        number_tickets = len(total_ticket_list)
        print("\nTo search for a ticket, enter a ticket ID number between 1 and " + str(number_tickets) + " \n")
        return 0

    def display_bad_request_error(self):
        print("\nUh oh! The service is not functioning presently\n")
        print("Enter 'quit' to exit\n")
        return 0

    def invalid_input_error_message(self):
        print("\nOops you have entered an invalid command\n")
        print("To see a list of options, enter 'menu' or to exit the application, enter 'quit'\n")
        return 0

    def display_single_ticket(self, ticket, total_ticket_list):
        ticket_data = ticket['ticket']
        ticket_id = ticket_data['id']
        ticket_description = ticket_data['description']
        ticket_subject = ticket_data['subject']
        ticket_status = ticket_data['status']
        print("\n---------------------------- Ticket Viewer Search Mode ----------------------------\n")
        print("Ticket ID " + str(ticket_id) +
              " concerning subject " + "'" + ticket_subject + "'" +
              " has the status " + "'" + ticket_status + "'" + "\n")
        print("Ticket Description: \n\n" + ticket_description)
        self.display_ticket_search_options(total_ticket_list)
        print("To see a list of options, enter 'menu' or to exit the application, enter 'quit'\n")
