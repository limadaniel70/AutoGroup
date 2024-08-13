# Introdução

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
# ! a quantidade de grupos é baseada na quantidade de pessoas com hard skills.
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
