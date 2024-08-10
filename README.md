# Como utilizar

O primeiro passo é preencher o arquivo de configuração (config/settings.py) com os nomes e a quantidade de pessoas em cada time/equipe:

```python
# quantidade de pessoas em cada equipe
team_size: int = 6

# pessoas com conhecimento técnico
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

<p style="font-size:70%">*A quantidade de grupos é em função da quantidade de pessoas com conhecimento técnico.</p>

---

Com isso feito, basta apenas executar o arquivo main.py e ele irá gerar um arquivo json com todos os grupos; exemplo de arquivo gerado pelo programa:
```json
{
    "group1": {
        "membros": [
            "Vivian Rodgers",
            "Pete Anthony",
            "Lucille Steele",
            "Carl Hawkins",
            "Betty Blackburn",
            "Taylor Delaney",
            "Myra Page",
            "Dianne Shields"
        ]
    },
    "group2": {
        "membros": [
            "Pat Hahn",
            "Brandy Brennan",
            "Geoffrey Lambert",
            "Miranda Elder",
            "Silvia Simms",
            "Terry James",
            "Roman Hawley",
            "Beatrice Griffin"
        ]
    },
    "group3": {
        "membros": [
            "Candy Shea",
            "Gwen Tracy",
            "Darryl Ogden",
            "Rosa Roberts",
            "Rafael Grimes",
            "Claire Montoya",
            "Hugh Holland",
            "Kayla Potter"
        ]
    }
}
```
<p style="font-size:70%">*Todos os nomes foram criados por um gerador aleatório.</p>
