from config.settings import hard_skill, soft_skill, general

def create_team(h_skill: list, s_skill: list) -> list:
    """
    Cria os times baseado na quantidade de pessoas com hard skills.
    :param h_skill: Lista de pessoas com habilidades tecnicas.
    :param s_skill: Lista de pessoas com habilidades de comunicação e de liderança
    :return: Retorna uma matriz com todos os grupos criados.
    """
    num_of_teams = len(h_skill) // 6
    pass

def populate_team(teams: list, general: list) -> list:
    """
    Adiciona pessoas com outras habilidades ao times criados anteriormente.
    :param teams: Todos os times.
    :param general: Todas as pessoas com outras habilidades.
    :return: Retorna uma matriz contendo todos os participantes de cada time.
    """
    pass

