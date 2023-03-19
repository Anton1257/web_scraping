from vacancies import get, django_flask, usd_salaries, write_json_file, vacancies_from_page, City


if __name__ == '__main__':
    # задание 1. получаем вакансии
    vacancies_from_page_3 = {City.Moscow: [],
                             City.Saint_Petersburg: []}
    vacancies_from_page(3, vacancies_from_page_3)
    # задание 2. отбираем те вакансии в которых есть ключевые слова Django и Flask
    django_flask_vacancies = []
    for city in vacancies_from_page_3: django_flask_vacancies += get(django_flask, vacancies_from_page_3[city])
    # задание 3.(необязательное) получить вакансии только с ЗП в долларах(USD)
    vacancies_usd_salaries = []
    for city in vacancies_from_page_3: vacancies_usd_salaries += get(usd_salaries, vacancies_from_page_3[city])
    # задание 4. записываем в json файл информацию о каждой вакансии - ссылка, вилка зп, название компании, город
    for city in vacancies_from_page_3: write_json_file(vacancies_from_page_3[city])
