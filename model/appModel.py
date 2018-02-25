import requests
import math


class AppModel:
    def __init__(self):
        self.org = "rphinn"
        self.login = "13rp46@queensu.ca"
        self.password = "Queens2017"
        self.tickets = []
        self.ticket = []
        self.url = ""
        self.limit = 25
        self.ticket_id = ""

    def get_ticket(self, ticket_id):
        self.ticket_id = ticket_id
        self.url = "https://" + self.org + ".zendesk.com/api/v2/tickets/" + str(self.ticket_id) + ".json"
        try:
            response = requests.get(self.url, auth=(self.login, self.password))
            response_status = response.status_code
            if (response_status != 200):
                return 0
            self.ticket = response.json()
            ticket = self.ticket
        except requests.exceptions.RequestException:
            return 0
        return ticket

    def get_all_tickets(self):
        self.url = "https://" + self.org + ".zendesk.com/api/v2/tickets.json"
        if self.tickets == None or not self.tickets:
            while self.url:
                try:
                    response = requests.get(self.url, auth=(self.login, self.password))
                    response_status = response.status_code
                    if (response_status != 200):
                        return 0
                    data = response.json()
                    self.tickets.extend(data['tickets'])
                    self.url = data['next_page']
                except requests.exceptions.RequestException:
                    return 0
        return self.tickets

    def calculate_total_pages(self, total_ticket_list):
        pages = math.ceil(float(len(total_ticket_list)) / self.limit)
        return int(pages)

    def paginate_tickets(self, total_ticket_list, pages):
        page_dict = {}
        list_per_page = [total_ticket_list[i:i + self.limit] for i in range(0, len(total_ticket_list), self.limit)]
        for page in range(1, pages + 1):
            page_dict[page] = list_per_page[page - 1]
        return page_dict
