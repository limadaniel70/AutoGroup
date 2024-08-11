from config.settings import *
from utils.json_utils import write_to_json_file
import random


def create_team(h_skill: list, s_skill: list) -> dict:
    """
    Cria os times baseado na quantidade de pessoas com hard skills.
    :param h_skill: Lista de pessoas com habilidades tecnicas.
    :param s_skill: Lista de pessoas com habilidades sociais.
    :return: Retorna um dicionário com todos os grupos criados.
    """
    all_teams = {}
    random.shuffle(s_skill)
    
    # Como a quantidade de grupos é em função das pessoas com conhecimento técnico
    # os grupos são inicados com uma pessoa com conhecimento técnico.
    for i in range(len(h_skill)):
        all_teams.update({f"equipe {i + 1}": {
            "membros": [h_skill[i]]
        }})

    # Depois de inicializar os grupos, são adicionadas as pessoas com soft skills
    for i, person_s in enumerate(s_skill):
        all_teams[f"equipe {i % len(h_skill) + 1}"]["membros"].append(person_s)


    return all_teams

def populate_team(teams: dict, general: list, persons_per_team: int = 6) -> dict:
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
