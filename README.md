# OTRS libs

A Python 3.x module to interact with OTRS (6.0) REST webservices. Contains various functions for ticket retrieval and manipulation.

## Functions 

### Generic
Setup connection to OTRS webservice-based API (REST):
```python
__init__(self, otrs_user=None, otrs_pass=None, ssl_verify=True)
```

Set OTRS address:
```python
set_url(self, url)
```

Set OTRS user:
```python
set_user(self, user)
```

Set OTRS password:
```python
set_pass(self, password)
```

Set SSL verification on/off (takes a boolean input):
```python
set_ssl(self, verify)
```

Generic purpose request handler
```python
do_request(self, request_url, json_payload)
```

### Ticket searching
Search for a ticket based on ticket number:
```python
search_ticket_number(self, searchvalue)
```

Search for a ticket based on ticket id:
```python
search_ticket_id(self, searchvalue)
```

Search for a ticket based on ticket title (only):
```python
search_ticket_title(self, searchvalue)
```

Search for a ticket based on text in ticket articles:
```python
search_ticket_text(self, searchvalue)
```

Search for a ticket based on ticket queue:
```python
TODO
```

Search for a ticket based on ticket owner:
```python
TODO
```


### Ticket object manipulation

Create a ticket:
```python
TODO
```

Update ticket title:
```python
TODO
```

Update ticket free field:
```python
update_ticket_free_field(self, ticket_id, field, text)
```

Update ticket owner:
```python
TODO
```

Update ticket state:
```python
update_ticket_state(self, ticket_id, state)
```

Move ticket to queue:
```python
TODO
```

### Ticket information retrieval
Retrieve a formatted summary of text contained in an article (owner, last article, relevant free fields):
```python
get_ticket_text(self, ticket)
```

Retrieve ticket owner:
```python
TODO
```

Retrieve ticket creation timestamp:
```python
TODO
```

Retrieve ticket 'last modified' timestamp:
```python
TODO
```

Retrieve ticket JSON:
```python
get_ticket(self, ticketid)
```
