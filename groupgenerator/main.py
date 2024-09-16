from json_utils import write_to_json_file
from settings import GENERAL, HARD_SKILLS, N_OF_TEAMS, SOFT_SKILLS, TEAM_SIZE

teams: dict[str, list[str]] = {f"equipe {x+1}": [] for x in range(N_OF_TEAMS + 1)}


def add_skilled(n_teams: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    """
    Adiciona as pessoas que possuem habilidades técnicas ou sociais.

    Args:
        n_teams (int): a quantidade de equipes.
        persons (list[str]): as pessoas que serão adicionadas.
        teams (dict[str, list[str]]): o dicionário com as equipes.
    """
    for i, person in enumerate(persons):
        teams[f"equipe {i % n_teams + 1}"].append(person)


def add_general(team_size: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    """
    Adiciona as pessoas com outros tipos de habilidades.

    Args:
        team_size (int): a quantidade de pessoas em cada equipe.
        persons (list[str]): as pessoas que serão adicionadas.
        teams (dict[str, list[str]]): o dicionário com as equipes.
    """
    for team in teams:
        # Em python, uma lista vazia retorna false
        # se a list tiver ao menos um lemento, ela retorna true
        while len(teams[team]) < team_size and persons:
            teams[team].append(persons.pop())


add_skilled(N_OF_TEAMS, SOFT_SKILLS, teams)
add_skilled(N_OF_TEAMS, HARD_SKILLS, teams)
add_general(TEAM_SIZE, GENERAL, teams)
write_to_json_file(teams)
