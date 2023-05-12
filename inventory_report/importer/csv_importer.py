import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.endswith(".csv"):
            with open(file_path, encoding="utf8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        else:
            raise ValueError("Arquivo inválido")
