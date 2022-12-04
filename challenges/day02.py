from lib.matma.util_matma import is_number_even, double
from lib.utils.util_console_mgmt import cls

# challenge 3
def import_web_api_random_people():
    import requests
    url = r"https://randomuser.me/api/?results=10"
    try:
        response = requests.get(url)
        response_json = response.json()
        simple_data = response_json.get("results")

        for v in simple_data:
            personal_data = v.get("name")
            location_data = v.get("location")
            credentials = v.get("login")
            print(f"{personal_data.get('first')} {personal_data.get('last')}")
            print(f"{location_data.get('city')}")
            print(f"U: {credentials.get('username')}  P: {credentials.get('password')}")
    except:
        print("Something went wrong.")

    cls()


# challenge 4

def countries_search_engine_by_continent():
    import requests
    regions = []
    try:
        url1 = f"https://restcountries.com/v3.1/all"
        response_region = requests.get(url1)
        re_json = response_region.json()
        for v in re_json:
            regions.append(v.get('region'))
        regions = set(regions)  # remove repeated values
        regions = list(regions)  # convert to list
        for i, k in enumerate(regions, start=1):
            print(f"{i} -> {k}")
        user_input = input("Input continent number: ")
        url = f"https://restcountries.com/v3.1/region/{regions[int(user_input) - 1]}"
        try:
            response = requests.get(url)
            resp_js = response.json()
            countries = []
            for c in resp_js:
                countries.append((c.get('cca3'), c.get('name').get('common')))
            countries.sort(key=lambda a: a[1])
            for i, c in enumerate(countries, start=1):
                print(f"{i} -> {c[1]}")

            user_input = input("Input country number: ")
            url = f"https://restcountries.com/v3.1/alpha/{(countries[int(user_input) - 1][0]).lower()}"
            try:
                response = requests.get(url)
                response_json = response.json()
                print(f"{response_json[0].get('name').get('official')} ->")
                for cur in response_json[0].get('currencies').keys():
                    print(cur)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)

    cls()


# challenge 5
# function testing if number is even (parzysta)
# use this function to filter list of integers
# print only even
def numbers_tests():
    values = [23, 56, 43, 54, 67, 87]
    print("Even numbers: ")
    for v in values:
        if is_number_even(v): print(v)

    print("Doubled values: ")
    for v in values:
        print(double(v))
    cls()