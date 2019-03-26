"""

Small Python module built for reusing various OTRS 6.0 api calls

"""

import json
import re
import requests
import structlog

# immediately initialise an error log
log = structlog.get_logger(__name__)

class OTRSApi:
    """
    Encapsulates an OTRS API connection and various functionalities enabled by the API.

    """
    def __init__(self, otrs_url=None, otrs_user=None, otrs_pass=None, ssl_verify=True):
        self.otrs_url = otrs_url
        self.otrs_user = otrs_user
        self.otrs_pass = otrs_pass
        self.ssl_verify = ssl_verify

    def set_url(self, url):
        ''' otrs url setter - expects a url pointing to an OTRS REST webservice'''
        self.otrs_url = url

    def set_user(self, user):
        ''' otrs user setter'''
        self.otrs_user = user

    def set_pass(self, pass_):
        ''' password setter'''
        self.otrs_pass = pass_

    def set_ssl_verification(self, ssl_verify):
        ''' enable or disable ssl verification for otrs requests '''
        self.ssl_verify = ssl_verify

    # def merge_tickets(self, ticket1_id, ticket2_id):
    #     """
    #     Merge ticket 1 into ticket 2 (copy all articles)

    #     In practice this can be combined with closing ticket 1
    #     and (re)opening ticket 2.

    #     """
    #     ticket1 = self.get_ticket(ticket1_id)
    #     ticket2 = self.get_ticket(ticket2_id)


    def update_ticket_state(self, ticket_id, state):
        """
        Update a ticket's state, for example 'open' or 'close succesful'
        """
        try:
            pass
        except Exception as err:
            structlog.get_logger(log).error("Exception during ticket state update: "+err)

    def update_ticket_queue(self, ticket_id, queue):
        """
        Update a ticket's queue id. A queue id is usually a single integer.
        """
        try:
            pass
        except Exception as err:
            structlog.get_logger(log).error("Exception during queue update: "+err)

    def update_ticket_free_field(self, ticket_id, field, text):
        """
        Update a ticket's free field value with a given string

        """
        try:
            pass
        except Exception as err:
            structlog.get_logger(log).error("Exception during ip address update: "+err)

    def search_ticket_id(self, searchvalue):
        """
        Search for a ticket in OTRS using a specific ticket _number_
        """
        # check if we actually have something to search for
        if searchvalue:
            try:
                req = requests.post(f'{self.otrs_url}SearchTicket/',
                                    json={"UserLogin":self.otrs_user,
                                          "Password":self.otrs_pass,
                                          "DynamicFields":"1",
                                          "TicketID":searchvalue},
                                    # SSL verification
                                    verify=self.ssl_verify)
            except Exception as err:
                raise err

            # if we get something cool, jsonify & return it
            if not req.raise_for_status():
                return json.loads(req.content.decode('utf-8'))
            # otherwise return the error code
            return req.status_code()
        structlog.get_logger(log).info("Invalid search query")

    def search_ticket_number(self, searchvalue):
        """
        Search for a ticket in OTRS using a specific ticket _number_
        """
        # check if we actually have something to search for
        if searchvalue:
            try:
                req = requests.post(f'{self.otrs_url}SearchTicket/',
                                    json={"UserLogin":self.otrs_user,
                                          "Password":self.otrs_pass,
                                          "DynamicFields":"1",
                                          "TicketNumber":searchvalue},
                                    # SSL verification
                                    verify=self.ssl_verify)
            except Exception as err:
                raise err

            if req.raise_for_status():
                    return req.status_code()

            # no ticketID implies the json is invalid
            if "TicketID" in json.loads(req.content.decode('utf-8')):
                return json.loads(req.content.decode('utf-8'))

            return None

        structlog.get_logger(log).info("Invalid search query")

    def search_ticket_title(self, searchvalue):
        """
        Search for a ticket in OTRS using the ticket title.

        Can return matching tickets in json, a request status code (if not 200), or None.
        """

        # do a length check to prevent returning an excessive number of tickets
        if searchvalue:
            if len(searchvalue) > 3:
                searchstring = f'*{searchvalue}*'

                try:
                    req = requests.post(f'{self.otrs_url}SearchTicket/',
                                        json={"UserLogin":self.otrs_user,
                                              "Password":self.otrs_pass,
                                              "Title":searchstring,},
                                        # SSL verification
                                        verify=self.ssl_verify)
                except Exception as err:
                    raise err

                if req.raise_for_status():
                    return req.status_code()

                # no ticketID implies the json is invalid
                if "TicketID" in json.loads(req.content.decode('utf-8')):
                    return json.loads(req.content.decode('utf-8'))

                return None

        structlog.get_logger(log).info("Invalid search query")

    def search_ticket_description(self, searchvalue):
        """
        Search for a ticket in OTRS using the ticket description.

        Can return matching tickets in json, a request status code (if not 200), or None.
        """

        # do a length check to prevent returning an excessive number of tickets
        if searchvalue:
            if len(searchvalue) > 3:
                searchstring = f'*{searchvalue}*'

                try:
                    req = requests.post(f'{self.otrs_url}SearchTicket/',
                                        json={"UserLogin":self.otrs_user,
                                              "Password":self.otrs_pass,
                                              "DynamicFields":"1",
                                              "DynamicField_LaaSta" : {
                                                  "Like":searchstring}
                                             },
                                        # SSL verification
                                        verify=self.ssl_verify)
                except Exception as err:
                    raise err

                if req.raise_for_status():
                    return req.status_code()

                if "TicketID" in json.loads(req.content.decode('utf-8')):
                    return json.loads(req.content.decode('utf-8'))

                return None

        structlog.get_logger(log).info("Invalid search query: "+searchvalue)

    def search_ticket_text(self, searchvalue):
        """
        Search in ticket articles

        Can return matching tickets in json, a request status code (if not 200), or None.
        """

        # do a length check to prevent returning an excessive number of tickets
        if searchvalue:
            if len(searchvalue) > 5:
                searchstring = "%"+searchvalue+"%"

                try:
                    req = requests.post(f'{self.otrs_url}SearchTicket/',
                                        json={"UserLogin":self.otrs_user,
                                              "Password":self.otrs_pass,
                                              # use this to set a hard limit on search results
                                              # "Limit":5,
                                              "MIMEBase_Body": searchstring,
                                             },
                                        # SSL verification
                                        verify=self.ssl_verify)
                except Exception as err:
                    raise err

                # break on error codes
                if req.raise_for_status():
                    return req.status_code()

                if "TicketID" in json.loads(req.content.decode('utf-8')):
                    return json.loads(req.content.decode('utf-8'))

        structlog.get_logger(log).info("Invalid search query: "+searchvalue)

    def search_ticket_queue(self, searchvalue):
        """
        Search a ticket queue

        Can return matching tickets in json, a request status code (if not 200), or None.
        """

        # do a length check to prevent returning an excessive number of tickets
        if searchvalue:
            try:
                req = requests.post(f'{self.otrs_url}SearchTicket/',
                                    json={"UserLogin":self.otrs_user,
                                          "Password":self.otrs_pass,
                                          # use this to set a hard limit on search results
                                          # "Limit":5,
                                          "QueueID": searchvalue,
                                         },
                                    # SSL verification
                                    verify=self.ssl_verify)
            except Exception as err:
                raise err

            # break on error codes
            if req.raise_for_status():
                return req.status_code()

            if "TicketID" in json.loads(req.content.decode('utf-8')):
                return json.loads(req.content.decode('utf-8'))

        structlog.get_logger(log).info("Invalid search query: "+searchvalue)

    def get_ticket_text(self, ticket):
        """
        Concat all relevant information contained in an OTRS ticket object and return it as a string
        with HTML line breaks.

        """
        descriptionstring = ""

        # add the ticket owner
        if 'Owner' in ticket['Ticket'][0]:
            descriptionstring = descriptionstring + "Current ticket owner: " \
                                + ticket['Ticket'][0]['Owner'] + "<br />"

        descriptionstring = descriptionstring + "Link to the original ticket here: " + "https://" \
                            + self.otrs_url + "/otrs/index.pl?Action=AgentTicketZoom;TicketID=" \
                            + ticket['Ticket'][0]['TicketID'] + "<br />"

        # add any text from dynamic (also known as free) fields
        for field in ticket['Ticket'][0]['DynamicField']:
            descriptionstring = descriptionstring + "Dynamic field "+str(field['Name']) \
                                +" content: <br />" + str(field['Value']) + "<br />"

        # add text of latest article
        if 'Article' in ticket['Ticket'][0]:
            if 'Body' in ticket['Ticket'][0]['Article'][-1]:
                descriptionstring = descriptionstring + "Laatste artikel: " \
                + ticket['Ticket'][0]['Article'][-1]['Body'] + "<br />"


        return descriptionstring

    def get_ticket(self, ticketid):
        """
        Get a ticket from OTRS based on the OTRS ticket id (e.g. 34568)
        Note the difference between ticket id and ticket number.
        """
        # check if we have a ticketID
        if ticketid:
            try:
                req = requests.post(f'{self.otrs_url}"GetTicket/{ticketid}',
                                    json={"UserLogin":self.otrs_user,
                                          "Password":self.otrs_pass,
                                          "DynamicFields":"1"},
                                    # DangerZone(tm)
                                    verify=self.ssl_verify)
            except Exception as err:
                raise err

            # if we get a valid response, jsonify & return it.
            if not req.raise_for_status():
                return json.loads(req.content.decode('utf-8'))
            # otherwise return the error code
            return req.status_code()

        structlog.get_logger(log).info("Invalid ticketID query: "+ticketid)
