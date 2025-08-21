import pygame
import random






def atakeskese(ataque, defesa):
    return {
                'scratch': 1*(ataque/defesa),
                'quick attack': 2*(ataque/defesa),
                'flamethrower': 2*(ataque/defesa),
                'surf': 2*(ataque/defesa),
                'razor leaf': 2*(ataque/defesa)
            }

fogo = ['flamehrower']
agua = ['surf']
planta = ['razor leaf']

class pokemon:
    def __init__(self, tipo, movimentos, velocidade, ataque, defesa, vida, nome):
        self.tipo = tipo
        self.movimentos = movimentos
        self.velocidade = velocidade
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida
        self.nome = nome
    def atacar(self):
        print('')
        for j in range(len(self.movimentos)):
            print(self.movimentos[j])
        escl = input('escolha um ataque: ')
        for k in range(len(self.movimentos)):
            if escl == self.movimentos[k]:
                if fogo.count(escl) > 0:
                    b.vida -= int(atakeskese(self.ataque, b.defesa)[escl]*elemento('fogo', b))
                elif agua.count(escl) > 0:
                    b.vida -= int(atakeskese(self.ataque, b.defesa)[escl]*elemento('agua', b))
                elif planta.count(escl) > 0:
                    b.vida -= int(atakeskese(self.ataque, b.defesa)[escl]*elemento('planta', b))
                else:
                    b.vida -= int(atakeskese(self.ataque, b.defesa)[escl])
                print(f'Você usou: {escl}')
    
    # def elemento(self, tipo_do_ataque):
    #     if b.tipo == 'agua':
    #         match tipo_do_ataque:
    #             case 'agua':
    #                 return 1
    #             case 'fogo':
    #                 return 2
    #             case 'planta':
    #                 return 0.5
    #     if b.tipo == 'fogo':
    #         match tipo_do_ataque:
    #             case 'agua':
    #                 return 0.5
    #             case 'fogo':
    #                 return 1
    #             case 'planta':
    #                 return 2
    #     if b.tipo == 'planta':
    #         match tipo_do_ataque:
    #             case 'agua':
    #                 return 2
    #             case 'fogo':
    #                 return 0.5
    #             case 'planta':
    #                 return 1



class inimigo(pokemon):
    def atacar(self):
        escl = random.choice(self.movimentos)
        if fogo.count(escl) > 0:
            a.vida -= int(atakeskese(self.ataque, a.defesa)[escl]*elemento('fogo', a))
        elif agua.count(escl) > 0:
            a.vida -= int(atakeskese(self.ataque, a.defesa)[escl]*elemento('agua', a))
        elif planta.count(escl) > 0:
            a.vida -= int(atakeskese(self.ataque, a.defesa)[escl]*elemento('planta', a))
        else:
            a.vida -= int(atakeskese(self.ataque, a.defesa)[escl])
        print(f'O seu adversário usou: {escl}')
        


charizardattack = ['scratch', 'quick attack', 'flamethrower']
blastoizeattack = ['scratch', 'quick attack', 'surf']
venossauroattack = ['scratch', 'quick attack', 'razor leaf']
blastoize = pokemon('agua', blastoizeattack, 2, 2, 2, 10, 'Blastoize')
charizard = pokemon('fogo', charizardattack, 2, 2, 2, 10, 'Charizard')
venossauro = pokemon('planta', venossauroattack, 2, 2, 2, 10, 'Venossauro')
pokemuns = [blastoize, charizard, venossauro]
a = pokemuns[random.randint(0,len(pokemuns)-1)]
x = random.randint(0,len(pokemuns)-1)
b = inimigo(pokemuns[x].tipo, pokemuns[x].movimentos, pokemuns[x].velocidade, pokemuns[x].ataque, pokemuns[x].defesa, pokemuns[x].vida, pokemuns[x].nome)
print(f'Seu pokemon é: {a.nome}\nO pokemon do seu adversário é: {b.nome}')

def elemento(tipo_do_ataque, a_ou_b):
        if a_ou_b.tipo == 'agua':
            match tipo_do_ataque:
                case 'agua':
                    return 1
                case 'fogo':
                    return 0.5
                case 'planta':
                    return 2
        if a_ou_b.tipo == 'fogo':
            match tipo_do_ataque:
                case 'agua':
                    return 2
                case 'fogo':
                    return 1
                case 'planta':
                    return 0.5
        if a_ou_b.tipo == 'planta':
            match tipo_do_ataque:
                case 'agua':
                    return 0.5
                case 'fogo':
                    return 2
                case 'planta':
                    return 1



while True:
    a.atacar()
    print(b.vida)
    b.atacar()
    print(a.vida)
    if a.vida <= 0:
        print('você perdeu')
        break
    elif b.vida <= 0:
        print('você ganhou')
        break