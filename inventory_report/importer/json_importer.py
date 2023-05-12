import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.endswith(".json"):
            with open(file_path) as json_file:
                return json.load(json_file)
        else:
            raise ValueError("Arquivo inválido")
