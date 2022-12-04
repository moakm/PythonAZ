from lib.utils.util_console_mgmt import cls


def import_web_api_nbp():
    import requests
    url=r"http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
    try:
        response = requests.get(url)
        response_json = response.json()
        currency_data = response_json[0].get("rates")
        for v in currency_data:
            print(f"{v.get('code')} : {v.get('mid')}")
    except:
        print("Something went wrong.")


    cls()

