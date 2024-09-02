import psycopg2


class DBUpdater():
    """Класс для добавления данных в базу данных"""

    def __init__(self, db_name: str, params: dict) -> None:
        """Инициализируем базу данных"""

        self.__db_name = db_name
        self.__params = params

    def insert_data(self, employers: list[dict], vacancies: list[dict]) -> None:
        """Добавляет данные в таблицу employers."""

        conn = psycopg2.connect(dbname=self.__db_name, **self.__params)
        conn.autocommit = True
        cur = conn.cursor()

        for employer in employers:
            cur.execute(
                """
                INSERT INTO employers (employer_id, company_name, open_vacancies, accredited_it_employer, site_url, description)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (int(employer["id"]), employer["name"], int(employer["open_vacancies"]), bool(employer["accredited_it_employer"]), employer["site_url"], employer["description"])
            )

        for vacancy in vacancies:
            try:
                cur.execute(
                    """
                    INSERT INTO vacancies (vacancy_id, employer_id, vacancy_name)
                    VALUES (%s, %s, %s)
                    """,
                    (int(vacancy["id"]), vacancy["employer"]["id"], vacancy["name"])
                )
            except psycopg2.errors.UniqueViolation:
                pass

        conn.close()
