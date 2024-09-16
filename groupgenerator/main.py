import json_utils
from settings import N_OF_TEAMS, TEAM_SIZE, HARD_SKILLS, SOFT_SKILLS, GENERAL

teams: dict[str, list[str]] = {f"equipe {x+1}": [] for x in range(N_OF_TEAMS + 1)}


def add_skilled(n_teams: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    for i, person in enumerate(persons):
        teams[f"equipe {i % n_teams + 1}"].append(person)


def add_general(team_size: int, persons: list[str], teams: dict[str, list[str]]):
    for team in teams:
        # Em python, uma lista vazia retorna false
        # se a list tiver ao menos um lemento, ela retorna true
        while len(teams[team]) < team_size and persons:
            teams[team].append(persons.pop())


add_skilled(N_OF_TEAMS, SOFT_SKILLS, teams)
add_skilled(N_OF_TEAMS, HARD_SKILLS, teams)
add_general(TEAM_SIZE, GENERAL, teams)
json_utils.write_to_json_file(teams)
