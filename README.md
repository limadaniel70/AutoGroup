# Group Generator

## Sumário

1. [Introdução](#introdução)
2. [Como utilizar](#como-utilizar)
3. [Como funciona](#como-funciona)
    1. [Priemira forma de distribuição](#primeira-forma-de-distribuição)
    2. [Segunda forma de distribuição](#segunda-forma-de-distribuição)
4. [Conclusão](#conclusão)

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
def create_empty_teams(self) -> dict[str, dict[str, list[str]]]:
    teams: dict = {}
        for i in range(self.number_of_teams):
            teams[f"equipe {i + 1}"] = {"membros": []}

        return teams
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

O segundo é preencher os grupos. Esse processo é realizado desta forma:

```python
def distribute_members(self) -> None:
    
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
        while len(self.teams[team]["membros"]) < self.team_size and self.other_skills:
            self.teams[team]["membros"].append(self.other_skills.pop())
```

É percepitivel que a distribuiçãos dos membros ocorre em três fases distintas: primeiro são adicionados os membros de com hard skills de forma ciclíca e após são adicionas os membros com soft skills da mesma forma e, por fim, são adicionados os membros com outros tipos de habilidades de uma forma diferente das demais.

### Primeira forma de distribuição

```python
for i, person_x in enumerate(self.x_skills):
        self.teams[f"equipe {i % self.number_of_teams + 1}"]["membros"].append(
            person_x
        )
```

Para garantir que a distribuição não concentre pessoas com habilidades técnicas e sociais em um único grupo, essas pessoas são distribuídas em vários grupos de forma cíclica.

Este é um exemplo de como funciona:

![Primeira distribuição](img/distribuição-1.gif)

### Segunda forma de distribuição

```python
for team in self.teams:
        while len(self.teams[team]["membros"]) < self.team_size and self.other_skills:
            self.teams[team]["membros"].append(self.other_skills.pop())
```

Essa forma de distribuição funciona adicionando os membros ao grupo até o grupo ficar cheio e então passa para o próximo. Fazendo isso até acabarem os membros ou acabarem os grupos.

![Segunda distribuição](img/distribuição-2.gif)

## Conclusão
