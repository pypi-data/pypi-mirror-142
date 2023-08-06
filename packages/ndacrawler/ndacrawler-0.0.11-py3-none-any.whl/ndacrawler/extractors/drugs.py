import csv

from .._internal_utils import get_page_content
from bs4 import BeautifulSoup


class CommonDataExtractor:
    headers = [
        "NAME OF DRUG",
        "NDA REGISTRATION NUMBER",
        "MANUFACTURER",
        "COUNTRY OF MANUFACTURE",
        "LOCAL TECHNICAL REPRESENTATIVE",
        "DOSAGE FORM",
        "PACK SIZE"
    ]

    def __init__(self, table):
        self.data = []
        self.table = table
        self.headers_index = self.get_table_headers_indexes()

        self.process_data()

    def get_table_headers_indexes(self):
        return {
            header.text: index
            for index, header in enumerate(self.table.find("thead").find_all("th"))
        }

    def get_common_data(self, row_data):
        return {
            "name": row_data[self.headers_index[self.name_header]],
            "registration_number": row_data[self.headers_index[self.registration_number_header]],
            "license_holder": row_data[self.headers_index[self.license_holder_number_header]],
            "manufacturer": row_data[self.headers_index[self.manufacturer_header]],
            "country_of_manufacture": row_data[self.headers_index[self.country_of_manufacture_header]],
            "local_technical_representative": row_data[self.headers_index[self.local_technical_representative_header]],
            "dosage_form": row_data[self.headers_index[self.dosage_form_header]],
            "pack_size": row_data[self.headers_index[self.pack_size_header]]
        }

    def get_data(self, row_data):
        return {
            header[:-7]: row_data[self.headers_index[getattr(self, header)]]
            for header in self.headers
        }

    def process_data(self):
        # TODO Arrange the data according to the order of the headers
        for table_row in self.table.find("tbody").find_all("tr"):
            row_data = [column.text for column in table_row.find_all("td")]
            self.data.append(
                [
                    row_data[self.headers_index[header]]
                    for header in self.headers
                ]
            )
        return self.data

    def to_csv(self, file_path):
        with open(file_path, 'w', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            writer.writerows(self.data)


class HerbalHumanDataExtractor(CommonDataExtractor):
    headers = CommonDataExtractor.headers + \
        ["S/N", "LICENSE HOLDER", "REGISTRATION DATE"]


class HerbalVetDataExtractor(CommonDataExtractor):
    headers = CommonDataExtractor.headers + \
        ["LICENSE HOLDER", "REGISTRATION DATE"]


class HumanDataExtractor(CommonDataExtractor):
    headers = CommonDataExtractor.headers + \
        ["S/N", "LICENSE HOLDER", "GENERIC NAME OF DRUG",
            "STRENGTH OF DRUG", "REGISTRATION DATE"]


class VetDataExtractor(CommonDataExtractor):
    headers = CommonDataExtractor.headers + \
        ["S/N", "LICENSE HOLDER", "GENERIC NAME OF DRUG",
            "STRENGTH OF DRUG", "REGISTRATION DATE"]


class LocalTraditionalHumanHerbalDataExtractor(CommonDataExtractor):
    headers = CommonDataExtractor.headers + \
        ["S/N", "LICENCE HOLDER"]


def get_drugs():
    url = "https://www.nda.or.ug/drug-register"
    page_content = get_page_content(url)
    soup = BeautifulSoup(page_content, "html.parser")
    herbal_human_table, herbal_vet_table, human_table, vet_table, local_traditional_human_herbal_table = soup.find_all(
        "table", {"class": "tablepress"}
    )
    # TODO Lazy load the extraction of the data for when requested

    return {
        "Herbal Human": HerbalHumanDataExtractor(herbal_human_table),
        "Herbal Vet": HerbalVetDataExtractor(herbal_vet_table),
        "Human": HumanDataExtractor(human_table),
        "Vet": VetDataExtractor(vet_table),
        "Local Traditional Human Herbal": LocalTraditionalHumanHerbalDataExtractor(local_traditional_human_herbal_table)
    }
