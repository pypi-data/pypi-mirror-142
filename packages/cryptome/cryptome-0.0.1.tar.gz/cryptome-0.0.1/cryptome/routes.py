import requests

def get_price(short: str):
  short = short.upper()
  try:
    url = f"https://api.nomics.com/v1/currencies/ticker?key=3bee3800772469509690a457b81bf895ee4cb174&ids={short}&per-page=100&page=1"
    data = requests.get(url)
    clean = data.json()
    clean = clean[0]
    return clean['price']
  except:
    return 'Invalid Short Code'

