import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path, encoding="utf8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
            if report_type == "simples":
                return SimpleReport.generate(data)
            return CompleteReport.generate(data)
