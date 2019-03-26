# OTRS libs

A Python 3.x module to interact with OTRS (6.0) REST webservices. Contains various functions for ticket retrieval and manipulation.

## Functions 

### Generic

```python
__init__(self, otrs_user=None, otrs_pass=None, ssl_verify=True)
```
Setup connection to OTRS webservice-based API (REST)

```python
set_url(self, url)
```

Set OTRS address

```python
set_user(self, user)
```

Set OTRS user

```python
set_pass(self, password)
```

Set OTRS password

```python
set_ssl(self, verify)
```

Set SSL verification on/off (takes a boolean input)

### Ticket searching

```python
search_ticket_number(self, searchvalue)
```
Search for a ticket based on ticket number

```python
search_ticket_id(self, searchvalue)
```
Search for a ticket based on ticket id

```python
search_ticket_title(self, searchvalue)
```
Search for a ticket based on ticket title (only)

```python
search_ticket_text(self, searchvalue)
```
Search for a ticket based on text in ticket articles

```python

```
Search for a ticket based on ticket queue

```python

```
Search for a ticket based on ticket owner

### Ticket object manipulation

Create a ticket

Update ticket title

Update ticket free field

Update ticket owner

Update ticket state

Move ticket to queue

### Ticket information retrieval
```python
get_ticket_text(self, ticket)
```
Retrieve a formatted summary of text contained in an article (owner, last article, relevant free fields)

```python

```
Retrieve ticket owner

```python

```
Retrieve ticket time

```python

```
Retrieve ticket JSON
