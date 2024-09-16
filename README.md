# Group Generator

## Sumário

1. [Introdução](#introdução)
2. [Como utilizar](#como-utilizar)
3. [Como funciona](#como-funciona)
    1. [Priemira forma de distribuição](#primeira-forma-de-distribuição)
    2. [Segunda forma de distribuição](#segunda-forma-de-distribuição)

## Introdução

Este projeto foi criado como forma de tornar mais fácil a criação de equipes com membros aleatórios com a garantia de que as pessoas com conhecimento técnico ou habilidades sociais não fiquem concentradas em poucos grupos, mas distribuídas em vários grupos.

## Como utilizar

O primeiro passo é preencher o arquivo de configuração (config/settings.py) com os nomes e a quantidade de pessoas em cada time/equipe:

```python
# quantidade de equipes.
N_OF_TEAMS: int = 5

# A quantidade de pessoas em cada equipe.
# Note que, se o número de pessoas em cada equipe não for suficiente para alocar todas as pessoas, o excesso ficará sem grupo.
TEAM_SIZE: int = 6

# pessoas com conhecimento técnico.
HARD_SKILLS: list[str] = [
    "pessoa 1",
    "pessoa 2",
    ...
]

# pessoas com habilidades em liderança ou comunicação
SOFT_SKILLS: list[str] = [
    "pessoa 1",
    "pessoa 2",
    ...
]

# pessoas com outras habilidades
GENERAL: list[str] = [
    "pessoa 1",
    "pessoa 2",
    ...
]
```

---

Com isso feito, basta apenas executar o arquivo main.py e ele irá gerar um arquivo json com todos os grupos.

Exemplo de arquivo gerado:

```json
{
    "equipe 1": [
        "Vivian Rodgers",
        "April Whitehead",
        "Pete Anthony",
        "Silvia Simms",
        "Katy McFarland",
        "Lucille Steele"
    ],
    "equipe 2": [
        "Pat Hahn",
        "Jorge Hester",
        "Taylor Delaney",
        "Darryl Ogden",
        "Nathan Shaw",
        "Dianne Shields"
    ],
    "equipe 3": [
        "Brandy Brennan",
        "Betty Blackburn",
        "Candy Shea",
        "Kenny Ewing",
        "Sally Knapp",
        "Cameron Mills"
    ]
}
```

*Todos os nomes foram criados por um gerador aleatório.

---

## Como funciona

Inicialmente, o programa inicia criando grupos vazios para serem preenchidos em outro momento:

```python
teams: dict[str, list[str]] = { 
    f"equipe {x+1}": []
    for x in range(settings.number_of_teams + 1)
}
```

Essa função retorna um dicinário neste formato:

```python
{
    'equipe 1': [],
    'equipe 2': [],
    'equipe 3': [], 
    'equipe 4': [], 
    'equipe 5': [], 
    'equipe 6': []
}
```

O segundo é preencher os grupos. Esse processo é realizado pelas seguintes funções:

```python
def add_skilled(n_teams: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    for i, person in enumerate(persons):
        teams[f"equipe {i % n_teams + 1}"].append(person)


def add_general(team_size: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    for team in teams:
        while len(teams[team]) < team_size and persons:
            teams[team].append(persons.pop())
```

É percepitivel que a distribuiçãos dos membros ocorre em três fases distintas: primeiro são adicionados os membros de com habilidades, de forma ciclíca, e,após isso, são adicionados os membros com outros tipos de habilidades de uma forma diferente das demais.

### Primeira forma de distribuição

```python
def add_skilled(n_teams: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    for i, person in enumerate(persons):
        teams[f"equipe {i % n_teams + 1}"].append(person)
```

Para garantir que a distribuição não concentre pessoas com habilidades técnicas e sociais em um único grupo, essas pessoas são distribuídas em vários grupos de forma cíclica.

Este é um exemplo de como funciona:

![Primeira distribuição](img/distribuição-1.gif)

### Segunda forma de distribuição

```python
def add_general(team_size: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    for team in teams:
        while len(teams[team]) < team_size and persons:
            teams[team].append(persons.pop())
```

Essa forma de distribuição funciona adicionando os membros ao grupo até o grupo ficar cheio e então passa para o próximo. Fazendo isso até acabarem os membros ou acabarem os grupos.

![Segunda distribuição](img/distribuição-2.gif)
