# AutoGroup

> [!NOTE]
> AutoGroup é um software que gera equipes de forma aleatória levando em consideração as habilidades de cada membro. Assim, evitando que uma única equipe possua muitos membros com habilidades técnicas e as outros com poucos.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Sumário

1. [Introdução](#introdução)
2. [Como utilizar](#como-utilizar)
3. [Como funciona](#como-funciona)
    1. [Primeira forma de distribuição](#primeira-forma-de-distribuição)
    2. [Segunda forma de distribuição](#segunda-forma-de-distribuição)

## Introdução

Este projeto foi criado como forma de tornar mais fácil a criação de equipes com membros aleatórios com a garantia de que as pessoas com conhecimento técnico ou habilidades sociais não fiquem concentradas em poucos grupos, mas distribuídas em vários grupos.

## Como utilizar

O primeiro passo é preencher o arquivo de configuração (`settings.py`) com os nomes e a quantidade de pessoas em cada time/equipe:

```python
# quantidade de equipes.
N_OF_TEAMS: int = 5

# A quantidade de pessoas em cada equipe.
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

> [!WARNING]
> Caso a matemática dos grupos estiver errada, podem ocorrer erros. Se, por exemplo, houverem 36 pessoas e essas pessoas forem alocadas em 6 grupos de 5 pessoas, 6 pessoas ficarão sem grupo.

---

Com isso feito, basta apenas executar o arquivo main.py e ele irá gerar um arquivo YAML (por padrão, o nome do arquivo é `teams.yml`) com todos os grupos.

Exemplo de arquivo gerado:

```yaml
equipe 1:
- Vivian Rodgers
- April Whitehead
- Pete Anthony
- Silvia Simms
- Katy McFarland
- Lucille Steele
equipe 2:
- Pat Hahn
- Jorge Hester
- Taylor Delaney
- Darryl Ogden
- Nathan Shaw
- Dianne Shields
equipe 3:
- Brandy Brennan
- Betty Blackburn
- Candy Shea
- Kenny Ewing
- Sally Knapp
- Cameron Mills
```

> [!IMPORTANT]
> Todos os nomes foram criados por um gerador aleatório.

---

## Como funciona

Inicialmente, o programa inicia criando um dicionário vazio, no qual a chave é o nome da equipe e o valor é a lista com os membros da equipe:

```python
teams: dict[str, list[str]] = { 
    f"equipe {x+1}": []
    for x in range(N_OF_TEAMS)

}
```
> [!NOTE]
> No índice da equipe adicionamos 1 para que não exista uma "equipe 0".

O código anterior retorna um dicinário neste formato:

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

O segundo passo é preencher os grupos. Esse processo é realizado pelas seguintes funções:

```python
def add_skilled(n_teams: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    for i, person in enumerate(persons):
        teams[f"equipe {i % n_teams + 1}"].append(person)


def add_general(team_size: int, persons: list[str], teams: dict[str, list[str]]) -> None:
    for team in teams:
        while len(teams[team]) < team_size and persons:
            teams[team].append(persons.pop())
```

A primeira função distribui as pessoas com habilidades técnicas ou sociais de forma cíclica, para que não haja várias pessoas em um único grupo. A segunda função distribui as pessoas com outras habilidades de uma forma mais simples, apenas verificando se a equipe está com a quantidade de mebros definida pela configuração `TEAM_SIZE`.

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

Essa forma de distribuição funciona adicionando os membros à equipe até a quantidade de membros desta ser igual ao valor definida pela variável `TEAM_SIZE` e após isso passa para a próxima equipe. A função repete esse processo até não haver mais membros para serem adicionados ou acabarem os grupos.

![Segunda distribuição](img/distribuição-2.gif)
