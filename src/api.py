from typing import Any

import requests

class HH:
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    @staticmethod
    def __connection_to_api(api_method: str, api_params: dict) -> Any:
        """Приватный метод для подключения к API"""

        url = f"https://api.hh.ru/{api_method}"
        headers = {"User-Agent": "HH-User-Agent"}

        response = requests.get(url, headers=headers, params=api_params)

        if response.status_code != 200:
            raise requests.RequestException
        return response

    @classmethod
    def load_vacancies(cls, employer_id: str) -> list:
        """Метод для получения вакансий по ключевому слову"""

        params = {"employer_id": employer_id, "page": 0, "per_page": 100, "area": 113}
        vacancies = []

        print("Загрузка данных ... ", end="")
        # while params.get('page') != 20:
        while params.get("page") != 20:
            print("#", end="")
            vacancies_page = cls.__connection_to_api("vacancies", params).json()["items"]
            # print(type(vacancies_page), len(vacancies_page))
            vacancies.extend(vacancies_page)
            # print(type(vacancies), len(vacancies))
            params["page"] += 1

        # print()
        return vacancies

    @classmethod
    def load_employer_data(cls, employer_id: str) -> dict:
        """Метод для получения вакансий по ключевому слову"""

        params = {}

        print("Загрузка данных ... ")

        employer_data = cls.__connection_to_api(f"employers/{employer_id}", params).json()

        return employer_data
