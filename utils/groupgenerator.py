import random


class GroupGenerator:

    def create_team(self, n_of_teams: int) -> dict:
        """_summary_

        Args:
            n_of_teams (int): _description_

        Returns:
            dict: _description_
        """
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
        """_summary_

        Args:
            teams (dict): _description_
            h_skill (list): _description_
            s_skill (list): _description_
            general (list): _description_
            persons_per_team (int): _description_

        Returns:
            dict: _description_
        """
        n_of_teams: int = len(teams)

        # Adicionando as pessoas com hard skills
        for i, person_h in enumerate(self.shuffle_team(h_skill)):
            teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person_h)

        # Adicionando as pessoas com soft skills
        for i, person_s in enumerate(self.shuffle_team(s_skill)):
            teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person_s)

        # TODO: this part needs to be updated
        general = self.shuffle_team(general)
        for team_name, team_data in teams.items():
            while len(team_data["membros"]) < persons_per_team and general:
                team_data["membros"].append(general.pop())

        return teams

    @staticmethod
    def shuffle_team(team: list) -> list:
        """_summary_

        Args:
            team (list): _description_

        Returns:
            list: _description_
        """
        random.shuffle(team)
        return team
