from src.api import HH
from  src.db_creater import DBCreater
import json
from src.config import config

# vacancies = HH.load_vacancies("740")
# employer = HH.load_employer_data("740")
#
# print(json.dumps(vacancies, indent=4, ensure_ascii=False))
# print(json.dumps(employer, indent=4, ensure_ascii=False))
# print(len(vacancies))

params = config()

db = DBCreater("hh_parser", params)
db.create_database()
db.create_tables()
