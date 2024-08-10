from config.settings import hard_skill, soft_skill, general
from utils.json_utils import write_to_json_file


def create_team(h_skill: list) -> list:
    """
    Cria os times baseado na quantidade de pessoas com hard skills.
    :param h_skill: Lista de pessoas com habilidades tecnicas.
    :return: Retorna um dicionário com todos os grupos criados.
    """
    all_teams = {}
    for i, membro in enumerate(h_skill):
        all_teams.update({f"group{i + 1}": {
            "membros": [membro]
        }})

    return all_teams


def populate_team(teams: dict, general: list, persons_per_team: int = 6) -> list:
    """
    Adiciona pessoas com outras habilidades ao times criados anteriormente.
    :param teams: Todos os times.
    :param general: Todas as pessoas com outras habilidades.
    :param persons_per_team: A quantidade de pessoas em cada time (valor padrão = 6).
    :return: Retorna uma matriz contendo todos os participantes de cada time.
    """
    pass


teams = create_team(hard_skill)
write_to_json_file(teams)
