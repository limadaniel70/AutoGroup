import json


def write_to_json_file(data: dict, filename: str = "teams.json") -> None:
    """
    Escreve todos os times em um arquivo json.
    :param data: Dados que serão escrito no arquivo json.
    :param filename: Nome de arquivo (padrão = teams01.json).
    """
    with open(filename, "wt") as f:
        json_data = json.dumps(data, indent=4)
        f.write(json_data)
