import config.settings
from utils.json_utils import write_to_json_file
import random


class GroupGenerator:

    def create_team(self, n_of_teams) -> dict:
        teams: dict = {}
        for i in range(n_of_teams):
            teams[f"equipe {i + 1}"] = {"membros": []}

        return teams

    def populate_team(
        self,
        teams: dict,
        h_skill: list,
        s_skill: list,
        general: list,
        persons_per_team: int,
    ) -> dict:

        n_of_teams: int = len(teams)

        # Adicionando as pessoas com hard skills
        for i, person_h in enumerate(self.shuffle_team(h_skill)):
            teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person_h)

        # Adicionando as pessoas com soft skills
        for i, person_s in enumerate(self.shuffle_team(s_skill)):
            teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person_s)

        general = self.shuffle_team(general)
        for team_name, team_data in teams.items():
            while len(team_data["membros"]) < persons_per_team and general:
                team_data["membros"].append(general.pop())

        return teams

    @staticmethod
    def shuffle_team(team: list) -> list:
        random.shuffle(team)
        return team


# teams: dict = create_team(hard_skill, soft_skill)
# write_to_json_file(populate_team(teams, general, team_size))
