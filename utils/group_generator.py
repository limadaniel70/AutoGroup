import random


class GroupGenerator:

    def __init__(
        self,
        n_of_teams: int,
        h_skill: list[str],
        s_skill: list[str],
        general: list[str],
        persons_per_team: int,
    ) -> None:
        """
        Inicializa o gerador de grupos com o número de equipes, listas de habilidades
        técnicas, habilidades interpessoais e uma lista geral, além do tamanho máximo de cada equipe.

        Args:
            n_of_teams (int): Número de equipes a serem criadas.
            h_skill (list[str]): Lista de membros com habilidades técnicas.
            s_skill (list[str]): Lista de membros com habilidades interpessoais.
            general (list[str]): Lista de membros sem uma distinção específica de habilidades.
            persons_per_team (int): Número máximo de membros permitido em cada equipe.
        """
        self.number_of_teams = n_of_teams
        self.hard_skills = self.__shuffle_team(h_skill)
        self.soft_skills = self.__shuffle_team(s_skill)
        self.other_skills = self.__shuffle_team(general)
        self.team_size = persons_per_team
        self.teams = self.__create_empty_teams()
        self.__distribute_members()

    def __create_empty_teams(self) -> dict[str, dict[str, list[str]]]:
        """
        Cria um dicionário que representa as equipes, onde cada equipe é inicializada
        com uma lista vazia para os membros.

        Returns:
            dict: Um dicionário onde as chaves são os nomes das equipes no formato
                "equipe 1", "equipe 2", etc., e os valores são dicionários contendo
                uma chave "membros" associada a uma lista vazia.
        """

        teams: dict = {}
        for i in range(self.number_of_teams):
            teams[f"equipe {i + 1}"] = {"membros": []}

        return teams

    def __distribute_members(self) -> None:
        """
        Preenche as equipes com membros baseados em suas habilidades técnicas (hard skills),
        habilidades interpessoais (soft skills) e uma lista geral. A distribuição dos membros
        é feita de forma cíclica entre as equipes.
        """

        # Adicionando as pessoas com hard skills
        for i, person_h in enumerate(self.hard_skills):
            self.teams[f"equipe {i % self.number_of_teams + 1}"]["membros"].append(
                person_h
            )

        # Adicionando as pessoas com soft skills
        for i, person_s in enumerate(self.soft_skills):
            self.teams[f"equipe {i % self.number_of_teams + 1}"]["membros"].append(
                person_s
            )

        # Adicionando as pessoas restantes aos times
        for team in self.teams:
            # Em python, uma lista vazia retorna false
            # se a list tiver ao menos um lemento, ela retorna true
            while len(self.teams[team]["membros"]) < self.team_size and self.other_skills:
                self.teams[team]["membros"].append(self.other_skills.pop())

    def __shuffle_team(self, team: list[str]) -> list[str]:
        """
        Embaralha a ordem dos membros em uma lista de forma aleatória.

        Args:
            team (list): A lista de membros a ser embaralhada.

        Returns:
            list: A mesma lista de entrada, mas com a ordem dos membros embaralhada aleatoriamente.
        """
        random.shuffle(team)
        return team
