import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if ".csv" in path:
            with open(path, encoding="utf8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = [row for row in csv_reader]
        if ".json" in path:
            with open(path) as json_file:
                data = json.load(json_file)
        if ".xml" in path:
            with open(path) as xml_file:
                tree = ET.parse(xml_file)
                root = tree.getroot()
                data = [
                    {elem.tag: elem.text for elem in record}
                    for record in root.findall("record")
                ]
        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
