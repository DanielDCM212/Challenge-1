from requests import request
from collections import Counter
from datetime import datetime


def get_data():
    res = request("GET",
                  "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow")
    res_json = res.json()
    return res_json


def main():
    # point 1
    a = get_data()
    # point 2
    answered = Counter((item["is_answered"] for item in a['items']))
    # point 3
    min_ = min(a['items'], key=lambda x: x["view_count"])
    # point 4
    oldest = min(a['items'], key=lambda x: x["creation_date"])
    newest = max(a['items'], key=lambda x: x["creation_date"])

    oldest_str = datetime.fromtimestamp(oldest["creation_date"]).strftime("%Y-%m-%dT%H:%M:%S")
    newest_str = datetime.fromtimestamp(newest["creation_date"]).strftime("%Y-%m-%dT%H:%M:%S")
    # point 5
    max_reputation = max(a["items"], key=lambda x: x["owner"]["reputation"])

    print(f"Obtener el número de respuestas contestadas y no contestadas")
    print(f"\tRespuestas Contestadas: {answered[True]}")
    print(f"\tRespuestas No Contestadas: {answered[False]}")

    print(f"Obtener la respuesta con menor número de vistas")
    print(f"\tLa respues con menor numero de visitas tiene {min_['view_count']} visitas")
    print(f"\t {min_}")

    print(f"Obtener la respuesta más vieja y más actual")
    print(f"\tRespuesta mas vieja {oldest_str}")
    print(f"\t {oldest}")
    print(f"\tRespuesta mas nueva {newest_str}")
    print(f"\t {newest}")
    print(f"Obtener la respuesta del owner que tenga una mayor reputación")
    print(f"\tLa respuesta del owner con mayor reputacion es")
    print(f"\t {max_reputation}")
    print(f"\tCon una reputacion de {max_reputation['owner']['reputation']}")


if __name__ == '__main__':
    main()
