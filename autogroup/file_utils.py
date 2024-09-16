import json

import yaml


def write_to_json_file(
    data: dict[str, list[str]], filename: str = "teams.json"
) -> None:
    """
    Salva os times em um arquivoo JSON.

    Args:
        data (dict): todos os times criados.
        filename (str, optional): nome do arquivo para salva. Padrão é "teams.json".
    """

    with open(filename, "wt") as f:
        json_data = json.dumps(data, indent=4)
        f.write(json_data)


def write_to_yaml_file(data: dict[str, list[str]], filename: str = "teams.yml") -> None:
    """
    Salva as equipes geradas em arquivo YAML.
    * YAML é mais fácil de ler que um JSON.

    Args:
        data (dict[str, list[str]]): as equipes.
        filename (str, optional): nome do arquivo onde os dados serão
        escritos. Padrão é "teams.yml".
    """
    with open(filename, "wt") as f:
        yml_data = yaml.dump(data)
        f.write(yml_data)


# def read_config_from_json_file() -> dict[int, int, list, list, list]:
#    # TODO: para uma futura implementação de interface ou cli
#    pass
