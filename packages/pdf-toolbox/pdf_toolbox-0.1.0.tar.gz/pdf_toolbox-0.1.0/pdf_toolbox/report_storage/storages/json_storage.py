import json

from ..domain.storage import Storage


class JSONStorage(Storage):
    def __init__(self, filepath: str):
        self.__filepath = filepath

    def save(self, report: dict, report_id: str):
        json_data = self.__load_json()
        json_data[report_id] = report
        self.__write_json(json_data)

    def __load_json(self) -> dict:
        data = {}
        try:
            with open(self.__filepath) as jsonfile:
                data = json.loads(jsonfile.read())
        except FileNotFoundError:
            pass
        return data

    def __write_json(self, data: dict):
        with open(self.__filepath, "wt") as jsonfile:
            jsonfile.write(json.dumps(data))
