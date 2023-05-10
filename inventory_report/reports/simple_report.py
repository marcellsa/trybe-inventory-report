from collections import Counter
from datetime import date, datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        manucturing_dates = [item["data_de_fabricacao"] for item in data]
        f_manucturing_dates = [
            datetime.strptime(item, "%Y-%m-%d") for item in manucturing_dates
        ]
        oldest_date = date.isoformat(min(f_manucturing_dates))
        expiration_dates = [item["data_de_validade"] for item in data]
        f_expiration_dates = [
            datetime.strptime(item, "%Y-%m-%d") for item in expiration_dates
        ]
        current_date = date.today()
        closest_dates = [
            item
            for item in f_expiration_dates
            if date.isoformat(item) >= current_date.isoformat()
        ]
        closest_date = date.isoformat(min(closest_dates))
        companies = Counter([item["nome_da_empresa"] for item in data])
        return f"""Data de fabricação mais antiga: {oldest_date}
Data de validade mais próxima: {closest_date}
Empresa com mais produtos: {companies.most_common(1)[0][0]}"""
