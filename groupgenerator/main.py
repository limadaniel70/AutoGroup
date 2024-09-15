from . import settings, json_utils

teams: dict[str, dict[str, list[str]]] = {f"equipe {x+1}": {"membros" : []} for x in range(settings.number_of_teams + 1)}

print(teams)