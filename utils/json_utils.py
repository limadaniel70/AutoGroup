import json


def write_to_json_file(data: dict, filename: str = "teams.json") -> None:
    """Salva os times em um arquivoo JSON.

    Args:
        data (dict): todos os times criados.
        filename (str, optional): nome do arquivo para salva. Padrão é "teams.json".
    """
    with open(filename, "wt") as f:
        json_data = json.dumps(data, indent=4)
        f.write(json_data)
