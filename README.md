# keitaro

keitaro is a simple and easy to use API wrapper library for [Keitaro](https://keitaro.io/) Admin API written in Python3 and [aiohttp](https://pypi.org/project/aiohttp/)

## 📄 Official Keitaro resources

-   [Keitaro Website](https://keitaro.io/)
-   [Admin API documentation](https://admin-api.docs.keitaro.io/)
-   [Technical Support](https://t.me/keitarobot)

## 📖 Getting Started

### Installation

Pypi package is not updated, you can build it using setup.py

### Keitaro tracker initialization

Begin by importing Keitaro class from aiokeitaro module and passing Admin API key and URL of Keitaro tracker to it

```python
from aiokeitaro import Keitaro

api = Keitaro('API KEY', 'URL with http or https (if is domain)')
```

## 📚 Examples

If API request was successful, status code 200 will be received and a response in the json format.

```python
import asyncio
from aiokeitaro import Keitaro, Offer

async def main():
    api = Keitaro('API KEY', 'URL with http or https (if is domain)')
    
    # Create an instance of the Offer class
    offer = Offer(api)
    
    # Call the get method on the instance
    ss = await offer.get()
    print(ss)

# run main.py
asyncio.run(main())

```

<details>
  <summary>
    <i>Click to see a response sample</i>
    <a href="https://admin-api.docs.keitaro.io/#tag/Affiliate-Networks/paths/~1affiliate_networks~1{id}/delete">
    Admin API reference</a>
  </summary>
  <p>
    {
      "id": 14,
      "name": "string",
      "postback_url": "string",
      "offer_param": "string",
      "state": "string",
      "template_name": "string",
      "notes": "string",
      "pull_api_options": "string",
      "created_at": "string",
      "updated_at": "string",
      "offers": "string"
    }
  </p>
</details>

### Get all offers or specific one

To get all offers call get() method without any arguments

```python
all_offers = await offer.get()
```

Let's try to get a specific offer by its id

```python
dummy_offer = await offer.get(21)
```

As a result you'll get a response in JSON format

<details>
  <summary>
    <i>Click to see a response sample</i>
  </summary>
  <p>
    [
      {
      "id": 21,
      "name": "string",
      "group_id": 0,
      "action_type": "string",
      "action_payload": "string",
      "action_options": [],
      "affiliate_network_id": 0,
      "payout_value": 0,
      "payout_currency": "string",
      "payout_type": "string",
      "state": "string",
      "created_at": {},
      "updated_at": {},
      "payout_auto": true,
      "payout_upsell": true,
      "country": [],
      "notes": "string",
      "affiliate_network": "string",
      "archive": "string",
      "local_path": "string",
      "preview_path": "string"
      }
    ]
  </p>
</details>

### Campaign creation

To create an advertising campaign, you can simply call create() method of the campaigns resource

```python
payload = {
  'name': 'Dummy campaign',
  'state': 'disabled',
  'cost_type': 'CPC',
  'cost_value': '5',
  'cost_currency': 'USD',
  'cost_auto': True
}

campaign = await campaigns.create(payload)
```

The non-asynchronous module is located here: https://github.com/ysomad/keitaro
