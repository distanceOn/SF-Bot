import requests

class APIException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str) -> float:
        url = f'https://v6.exchangerate-api.com/v6/55b498382c7143777840b335/latest/{base}'
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            raise APIException(f"Ошибка {data['error']['code']}: {data['error']['type']}")
        try:
            price = float(data['conversion_rates'][quote]) * float(amount)
            return round(price, 2)
        except KeyError:
            raise APIException(f"Неверно указаны валюты или количество: {base}, {quote}, {amount}")
