from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.endswith(".xml"):
            with open(file_path) as xml_file:
                tree = ET.parse(xml_file)
                root = tree.getroot()
                return [
                    {elem.tag: elem.text for elem in record}
                    for record in root.findall("record")
                ]
        else:
            raise ValueError("Arquivo inválido")
