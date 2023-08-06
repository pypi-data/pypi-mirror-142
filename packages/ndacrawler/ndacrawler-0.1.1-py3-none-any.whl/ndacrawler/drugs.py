import csv
import functools
from ._internal_utils import get_page_content
from bs4 import BeautifulSoup
import lxml
import cchardet


class DataExtractor:

    def processed_data_required(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            if not self._is_data_processed:
                self.process_data()
                self._is_data_processed = True

            return func(self, *args, **kwargs)
        return wrap

    def __init__(self, table):
        self._is_data_processed = False
        self._table = table
        self._headers = []
        self._data = []

    def get_table_headers(self):
        return [
            header.text
            for header in self._table.find("thead").find_all("th")
        ]

    def process_data(self):
        if self._is_data_processed:
            # Prevent processing the data multiple times
            return
        # Get the headers
        self._headers = self.get_table_headers()
        # Get the data
        for table_row in self._table.find("tbody").find_all("tr"):
            self._data.append(
                [column.text for column in table_row.find_all("td")]
            )

    @processed_data_required
    def to_csv(self, file_path):
        with open(file_path, 'w', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self._headers)
            writer.writerows(self._data)

    @property
    def data(self):
        self.process_data()
        return self._data

    @property
    def headers(self):
        self.process_data()
        return self._headers


class TableExtractor:

    def __init__(self, soup):
        self.tables = soup.find_all(
            "table", {"class": "tablepress"}
        )

    def __getitem__(self, table_name):
        # TODO Get from the actual table
        table_names = ["Herbal Human", "Herbal Vet",
                       "Human", "Vet", "Local Traditional Human Herbal"]
        if table_name not in table_names:
            return None

        # table = self.soup.select(
        #     f"table:nth-of-type({table_names.index(table_name)+1})"
        # )[0]
        table_index = table_names.index(table_name)
        table = self.tables[table_index]

        return DataExtractor(table)


def drugs_extractor(soup):
    return TableExtractor(soup)


def get_drugs():
    url = "https://www.nda.or.ug/drug-register"
    page_content = get_page_content(url)
    soup = BeautifulSoup(page_content, "lxml")

    return drugs_extractor(soup)
