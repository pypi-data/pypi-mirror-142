# whop-python-sdk

## Installation
```
pip install whop
```

## Usage
```
import whop

bearer = "<Bearer Token>"
client = whop.Whop(bearer=bearer)

# client_id = "<client ID>"
# client = whop.Whop(client_id=client_id)

# Create a password protected link for your product.
client.create_link(
    product_id=123,
    password="secretpassword"
    stock=10
)

# Retrieve all links.
resp = client.get_links()
print(resp)
```
