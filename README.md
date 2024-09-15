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
number_of_teams: int = 5

# A quantidade de pessoas em cada equipe.
# Note que, se o número de pessoas em cada equipe não for suficiente para alocar todas as pessoas, o excesso ficará sem grupo.
team_size: int = 6

# pessoas com conhecimento técnico.
hard_skill: list = [
    "pessoa 1",
    "pessoa 2",
    ...
]

# pessoas com habilidades em liderança ou comunicação
soft_skill: list = [
    "pessoa 1",
    "pessoa 2",
    ...
]

# pessoas com outras habilidades
general: list = [
    "pessoa 1",
    "pessoa 2",
    ...
]
```

---

Com isso feito, basta apenas executar o arquivo main.py e ele irá gerar um arquivo json com todos os grupos.

Exemplo de arquivo gerado pelo programa:

```json
{
    "equipe 1": {
        "membros": [
            "Pete Anthony",
            "Lucille Steele",
            "Geoffrey Lambert",
            "Beatrice Griffin",
            "Silvia Simms",
            "Kenny Ewing"
        ]
    },
    "equipe 2": {
        "membros": [
            "Taylor Delaney",
            "Sally Knapp",
            "Betty Blackburn",
            "Carl Hawkins",
            "Myra Page",
            "Hugh Holland"
        ]
    },
    "equipe 3": {
        "membros": [
            "Candy Shea",
            "Rafael Grimes",
            "Michele McConnell",
            "Darryl Ogden",
            "Cameron Mills",
            "Miranda Elder"
        ]
    }
}
```

*Todos os nomes foram criados por um gerador aleatório.

---

## Como funciona

Inicialmente, o programa inicia criando grupos vazios para serem preenchidos em outro momento:

```python
teams: dict[str, dict[str, list[str]]] = { 
    f"equipe {x+1}": {"membros": []} 
    for x in range(settings.number_of_teams + 1)
}
```

Essa função retorna um dicinário neste formato:

```json
{
    "equipe 1" : {
        "membros" : []
    },
    "equipe 2" : {
        "membros" : []
    },
    "equipe 3" : {
        "membros" : []
    },

    ...
}
```

O segundo é preencher os grupos. Esse processo é realizado pelas seguintes funções:

```python
def add_skilled(
    n_of_teams: int, 
    persons: list[str],
    teams: dict[str, dict[str, list[str]]]
) -> None:
    for i, person in enumerate(persons):
        teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person)


def add_general(
    team_size: int,
    persons: list[str], 
    teams: dict[str, dict[str, list[str]]]
) -> None:
    for team in teams:
        # Em python, uma lista vazia retorna false
        # se a list tiver ao menos um lemento, ela retorna true
        while len(teams[team]["membros"]) < team_size and persons:
            teams[team]["membros"].append(persons.pop())
```

É percepitivel que a distribuiçãos dos membros ocorre em três fases distintas: primeiro são adicionados os membros de com habilidades, de forma ciclíca, e,após isso, são adicionados os membros com outros tipos de habilidades de uma forma diferente das demais.

### Primeira forma de distribuição

```python
def add_skilled(n_of_teams: int, persons: list[str], teams: dict[str, dict[str, list[str]]]) -> None:
    for i, person in enumerate(persons):
        teams[f"equipe {i % n_of_teams + 1}"]["membros"].append(person)
```

Para garantir que a distribuição não concentre pessoas com habilidades técnicas e sociais em um único grupo, essas pessoas são distribuídas em vários grupos de forma cíclica.

Este é um exemplo de como funciona:

![Primeira distribuição](img/distribuição-1.gif)

### Segunda forma de distribuição

```python
def add_general(team_size: int, persons: list[str], teams: dict[str, dict[str, list[str]]]) -> None:
    for team in teams:
        # Em python, uma lista vazia retorna false
        # se a list tiver ao menos um lemento, ela retorna true
        while len(teams[team]["membros"]) < team_size and persons:
            teams[team]["membros"].append(persons.pop())
```

Essa forma de distribuição funciona adicionando os membros ao grupo até o grupo ficar cheio e então passa para o próximo. Fazendo isso até acabarem os membros ou acabarem os grupos.

![Segunda distribuição](img/distribuição-2.gif)