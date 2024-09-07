from typing import Any, Callable

import psycopg2


class DBManager:
    """Класс для получения данных о вакансиях из базы данных"""

    def __init__(self, db_name: str, params: dict) -> None:
        """Инициализируем базу данных"""

        self.__db_name = db_name
        self.__params = params

    def __query_execute(self, query: str) -> list[dict | Any]:
        """Метод для выполнения запроса"""

        with psycopg2.connect(dbname=self.__db_name, **self.__params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                columns = [column[0] for column in cur.description]
                result = cur.fetchall()
                result_in_dict = [dict(zip(columns, i)) for i in result]

        conn.close()

        return result_in_dict

    def get_employers(self) -> Any:
        """Получить данные о работодателях из БД"""

        return self.__query_execute("SELECT * FROM employers")

    def get_companies_and_vacancies_count(self) -> Any:
        """Получает список всех компаний и количество вакансий у каждой компании"""

        query = """
            SELECT employers.company_name, COUNT(*)
            FROM vacancies
            JOIN employers USING(employer_id)
            GROUP BY employers.company_name
            """

        return self.__query_execute(query)