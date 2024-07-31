import random

ataques = {
    "bite": {
        "dano": 500,
        "tipo": "eletrico",
        "chance_de_acerto": 0.99,
        "velocidade_de_ataque": 5.73
    },
    "choquei": {
        "dano": 500,
        "tipo": "eletrico",
        "chance_de_acerto": 0.99,
        "velocidade_de_ataque": 5.73
    }
}

pokemons = {
    "peppa_pig": {
        "hp_pokemon": 1000,
        "tipo_pokemon": ["grama"],
        "nivel_pokemon": 1,
        "ataques_pokemon": [ataques["bite"]],
    },
    "charmander": {
        "hp_pokemon": 1200,
        "tipo_pokemon": ["fogo"],
        "nivel_pokemon": 5,
        "ataques_pokemon": [ataques["choquei"]],
    },
    "squirtle": {
        "hp_pokemon": 800,
        "tipo_pokemon": ["água"],
        "nivel_pokemon": 3,
        "ataques_pokemon": [ataques["bite"]],
    },
    "bulbasaur": {
        "hp_pokemon": 900,
        "tipo_pokemon": ["grama", "veneno"],
        "nivel_pokemon": 4,
        "ataques_pokemon": [ataques["choquei"]],
    },
    "pikachu": {
        "hp_pokemon": 1100,
        "tipo_pokemon": ["elétrico"],
        "nivel_pokemon": 7,
        "ataques_pokemon": [ataques["bite"]],
    },
    "jigglypuff": {
        "hp_pokemon": 1500,
        "tipo_pokemon": ["normal", "fada"],
        "nivel_pokemon": 9,
        "ataques_pokemon": [ataques["choquei"]],
    }
}

party_jogador = []

print(party_jogador)

def escolher_pokemon_rival():
  poke_ativ_rival = random.choice(list(pokemons.items()))
  print(poke_ativ_rival)
escolher_pokemon_rival()