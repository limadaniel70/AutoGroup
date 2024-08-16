import json


def write_to_json_file(data: dict, filename: str = "teams.json") -> None:
    """
    Salva os times em um arquivoo JSON.

    Args:
        data (dict): todos os times criados.
        filename (str, optional): nome do arquivo para salva. Padrão é "teams.json".
    """

    with open(filename, "wt") as f:
        json_data = json.dumps(data, indent=4)
        f.write(json_data)


def read_config_from_json_file() -> dict[int, int, list, list, list]:
    # TODO: para uma futura implementação de interface ou cli
    pass
