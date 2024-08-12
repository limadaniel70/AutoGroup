from config.settings import *
from utils.json_utils import write_to_json_file
import random


def create_team(h_skill: list, s_skill: list) -> dict:
    """Inicializa os times com uma pessoa que possui habilidades técnicas e então
    adiciona as times criados pessoas com habilidades sociais.

    Args:
        h_skill (list): pessoas com habilidades técnicas.
        s_skill (list): pessoas com habilidades sociais.

    Returns:
        dict: retorna um dicionário contendo as pessoas que possuem alguma habilidade.
    """
    all_teams = {}
    random.shuffle(s_skill)
    
    # Como a quantidade de grupos é em função das pessoas com conhecimento técnico
    # os grupos são inicados com uma pessoa com conhecimento técnico.
    for i in range(len(h_skill)):
        all_teams[f"equipe {i + 1}"] = {
            "membros" : [h_skill[i]]
        }

    # Depois de inicializar os grupos, são adicionadas as pessoas com soft skills
    for i, person_s in enumerate(s_skill):
        all_teams[f"equipe {i % len(h_skill) + 1}"]["membros"].append(person_s)


    return all_teams

def populate_team(teams: dict, general: list, persons_per_team: int = 6) -> dict:
    """Adiciona pessoas com outras habilidades aos times criados.

    Args:
        teams (dict): times criados anteriormente.
        general (list): pessoas que serão alocadas nos times.
        persons_per_team (int, optional): quantidade de pessoas em cada time. 
        Padrão é 6.

    Returns:
        dict: retorna os grupos preenchidos.
    """
    random.shuffle(general)

    for team_name, team_data in teams.items():
        while len(team_data["membros"]) < persons_per_team and general:
            team_data["membros"].append(general.pop())

    return teams


teams: dict = create_team(hard_skill, soft_skill)
write_to_json_file(populate_team(teams, general, team_size))
