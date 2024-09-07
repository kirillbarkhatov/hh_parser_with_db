from src.api import HH
from src.db_creater import DBCreater
from src.db_updater import DBUpdater
from src.db_manager import DBManager
import json
from src.config import config
from src.utils import read_json

# vacancies = HH.load_vacancies("740")
# employer = HH.load_employer_data("740")
#
# print(json.dumps(vacancies, indent=4, ensure_ascii=False))
# print(json.dumps(employer, indent=4, ensure_ascii=False))
# print(len(vacancies))

params = config()

# db = DBCreater("hh_parser", params)
# db.create_database()
# db.create_tables()
#
# companies = read_json("data/companies_settings.json")
#
# employers = []
# vacancies = []
#
# for company in companies:
#     print(company["name"])
#     employers.append(HH.load_employer_data(company["id"]))
#     vacancies.extend(HH.load_vacancies(company["id"]))
#
#
# db = DBUpdater("hh_parser", params)
# db.insert_data(employers, vacancies)

db = DBManager("hh_parser", params)
print(db.get_avg_salary())
