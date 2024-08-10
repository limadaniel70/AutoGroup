from config.settings import *
from utils.json_utils import write_to_json_file
import random


def create_team(h_skill: list, s_skill: list) -> dict:
    """
    Cria os times baseado na quantidade de pessoas com hard skills.
    :param h_skill: Lista de pessoas com habilidades tecnicas.
    :return: Retorna um dicionário com todos os grupos criados.
    """
    all_teams = {}

    num_teams = min(len(h_skill), len(s_skill))
    for i in range(num_teams):
        all_teams.update({f"group{i + 1}": {
            "membros": [h_skill[i], s_skill[i]]
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
    random.shuffle(general)

    for team_name, team_data in teams.items():
        while len(team_data["membros"]) < persons_per_team and general:
            team_data["membros"].append(general.pop())

    return teams


teams: dict = create_team(hard_skill, soft_skill)
teams = populate_team(teams, general, team_size)
write_to_json_file(teams)
