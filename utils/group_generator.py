import random


class GroupGenerator:

    def create_empty_teams(self, n_of_teams: int) -> dict[str, dict[str, list[str]]]:
        """
        Cria um dicionário que representa as equipes, onde cada equipe é inicializada
        com uma lista vazia para os membros.

        Args:
            n_of_teams (int): O número de equipes a serem criadas.

        Returns:
            dict: Um dicionário onde as chaves são os nomes das equipes no formato
                "equipe 1", "equipe 2", etc., e os valores são dicionários contendo
                uma chave "membros" associada a uma lista vazia.
        """

        teams: dict = {}
        for i in range(n_of_teams):
            teams[f"equipe {i + 1}"] = {"membros": []}

        return teams

    def distribute_members(
        self,
        teams: dict[str, dict[str, list[str]]],
        h_skill: list[str],
        s_skill: list[str],
        general: list[str],
        persons_per_team: int,
    ) -> dict[str, dict[str, list[str]]]:
        """
        Preenche as equipes com membros baseados em suas habilidades técnicas (hard skills),
        habilidades interpessoais (soft skills) e uma lista geral. A distribuição dos membros
        é feita de forma cíclica entre as equipes.

        Args:
            teams (dict): Um dicionário que contém as equipes a serem preenchidas. As chaves
                        são os nomes das equipes e os valores são dicionários com uma chave
                        "membros", que é uma lista dos membros da equipe.
            h_skill (list): Lista de membros com habilidades técnicas (hard skills) que serão
                            distribuídos primeiro entre as equipes.
            s_skill (list): Lista de membros com habilidades interpessoais (soft skills) que
                            serão distribuídos após os membros com hard skills.
            general (list): Lista de membros sem uma distinção específica de habilidades, que
                            serão distribuídos após os membros com hard e soft skills.
            persons_per_team (int): O número máximo de membros permitido em cada equipe.

        Returns:
            dict: O dicionário `teams` atualizado, onde cada equipe foi preenchida com membros
                da lista de habilidades técnicas, habilidades interpessoais e lista geral.
        """
        n_of_teams: int = len(teams)

        # Adicionando as pessoas com hard skills
        for i, person_h in enumerate(self.shuffle_team(h_skill)):
            teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person_h)

        # Adicionando as pessoas com soft skills
        for i, person_s in enumerate(self.shuffle_team(s_skill)):
            teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person_s)

        # TODO: essa parte precisa ser revisada e reescrita
        general = self.shuffle_team(general)
        for team_name, team_data in teams.items():
            while len(team_data["membros"]) < persons_per_team and general:
                team_data["membros"].append(general.pop())

        return teams

    @staticmethod
    def shuffle_team(team: list[str]) -> list[str]:
        """
        Embaralha a ordem dos membros em uma lista de forma aleatória.

        Args:
            team (list): A lista de membros a ser embaralhada.

        Returns:
            list: A mesma lista de entrada, mas com a ordem dos membros embaralhada aleatoriamente.
        """
        random.shuffle(team)
        return team
