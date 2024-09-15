import settings
import json_utils

N_OF_TEAMS = settings.number_of_teams
TEAM_SIZE = settings.team_size
HARD_SKILLS = settings.hard_skill
SOFT_SKILLS = settings.soft_skill
GENERAL = settings.general

teams: dict[str, dict[str, list[str]]] = {
    f"equipe {x+1}": {"membros": []} for x in range(settings.number_of_teams + 1)
}

def add_skilled(
    n_of_teams: int, persons: list[str], teams: dict[str, dict[str, list[str]]]
) -> None:
    for i, person in enumerate(persons):
        teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person)


def add_general(
    team_size: int, persons: list[str], teams: dict[str, dict[str, list[str]]]
):
    for team in teams:
        # Em python, uma lista vazia retorna false
        # se a list tiver ao menos um lemento, ela retorna true
        while len(teams[team]["membros"]) < team_size and persons:
            teams[team]["membros"].append(persons.pop())


add_skilled(N_OF_TEAMS, SOFT_SKILLS, teams)
add_skilled(N_OF_TEAMS, HARD_SKILLS, teams)
add_general(TEAM_SIZE, GENERAL, teams)
json_utils.write_to_json_file(teams)
