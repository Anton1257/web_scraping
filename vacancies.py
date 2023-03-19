import requests
import json
from enum import Enum

URL = 'https://api.hh.ru/vacancies'


class City(Enum):
    Moscow = 1,
    Saint_Petersburg = 2


def get_vacancies(cities: list, text: str, page: int, per_page: int) -> list:
    vacancies = dict()
    for city in cities:
        params = {
            'text': text,
            'area': city.value,
            'page': page,
            'per_page': per_page
        }
        r = requests.get(URL, params)
        success = r.status_code == 200
        vacancies[city] = r.json()['items'] if success else None
    return vacancies


def get(func, city):
    return [vacancy for vacancy in city if func(vacancy)]


def django_flask(vacancy):
    name = vacancy['name'].lower()
    name.lower() if name else ''
    requirement = vacancy['snippet']['requirement']
    requirement.lower() if requirement else ''
    return ('django' or 'flask') in (name or requirement)


def usd_salaries(vacancy):
    currency = vacancy['salary']
    return currency and currency['currency'].lower() == 'usd'


def write_json_file(city):
    json_file = []
    for vacancy in city:
        json_file.append({
            'href': vacancy['alternate_url'],
            'salary': vacancy['salary'],
            'employer_name': vacancy['employer']['name'],
            'city': vacancy['area']['name']
        })
    with open(f"Вакансии {vacancy['area']['name']}.json", "w") as write_file:
        json.dump(json_file, write_file)


def vacancies_from_page(number: int, vacancies_from_page_3: dict):
    for n in range(number):
        vacancies = get_vacancies([City.Moscow,
                                   City.Saint_Petersburg],
                                   'python',
                                   n,
                                   100)
        for city in vacancies:
            vacancies_from_page_3[city] += vacancies[city]