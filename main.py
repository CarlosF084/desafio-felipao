from random import randint


heroes = [
    ["Vi", randint(0, 11000)],
    ["Jinx", randint(0, 11000)],
    ["Ekko", randint(0, 11000)],
    ["Caitlyn", randint(0, 11000)],
    ["Jayce", randint(0, 11000)],
    ["Viktor", randint(0, 11000)],
    ["Heimerdinger", randint(0, 11000)],
]

for hero in heroes:
    nome = hero[0]
    xp = hero[1]
    level = (
        "Ferro" if xp < 1000
        else "Bronze" if 1001 < xp < 2000
        else "Prata" if 2001 < xp < 5000
        else "Ouro" if 5001 < xp < 7000
        else "Platina" if 7001 < xp < 8000
        else "Ascendente" if 8001 < xp < 9000
        else "Imortal" if 9001 < xp < 10000
        else "Radiante" 
    )
    print(f"O Herói de nome {nome} está no nível de {level}.")
