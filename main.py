from src.api import HH
import json

vacancies = HH.load_vacancies("740")
employer = HH.load_employer_data("740")

print(json.dumps(vacancies, indent=4, ensure_ascii=False))
print(json.dumps(employer, indent=4, ensure_ascii=False))
print(len(vacancies))
