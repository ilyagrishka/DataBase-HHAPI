import requests
import os

company = ['Газпром', 'Роснефть', 'Сбербанк', 'Альфабанк', 'Яндекс', 'VK', 'X5 Group', 'Тинькофф', 'Ozon', 'Авито']

for company_name in company:
    url = 'https://api.hh.ru/employers'
    company_params = {
        'text': company_name,
        'per_page': 5  # в чём смысл цифры?
    }

    response = requests.get(url, params=company_params)

    if response.status_code == 200:
        company_data = response.json()
        if company_data.get('items'):
            company_id = company_data['items'][0]['id']
            print(f'Информация о работодателе {company_name}:')
            print('ID работодателя:', company_id)
            print('\nВакансии работодателя:')
            vacancies_url = f'https://api.hh.ru/vacancies?employer_id={company_id}'
            vacancies_response = requests.get(vacancies_url)
            if vacancies_response.status_code == 200:
                vacancies_data = vacancies_response.json()
                for vacancy in vacancies_data['items']:
                    print('Название вакансии:', vacancy['name'])
                    print('ID вакансии:', vacancy['id'])
                    print('-----------------------------')
            else:
                print('Ошибка при получении данных о вакансиях')
        else:
            print(f'Работодатель {company_name} не найден')
    else:
        print(f'Ошибка при получении данных о работодателе {company_name}')
