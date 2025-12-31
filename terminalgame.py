import random

hp = 100
potions = 4
heal = 10
damage = 10
monstruos = 5


while hp != 0 and monstruos != 0:
    hpm = random.randint(10, 30)
    damagem = random.randint(1, 15)
    print('Estas en lo profundo de un boque oscuro, y te encuentras con un monstruo. Tienes tres opciones: 1.luchar  2.cubrirte 3.curarte')

    opciones = input('¿Que deseas hacer? (1, 2, 3): ')

    if opciones == '1':
        while hpm > 0:
            print('Atacas al monstruo y le haces ', damage, ' puntos de daño.')
            hpm -= damage
            print('El monstruo tiene ', hpm, ' puntos de vida restantes.')
            print('El monstruo te ataca y te hace ', damagem, ' puntos de daño.')
            hp -= damagem
            print('Tienes ', hp, ' puntos de vida restantes.')
            if hpm <= 0:
                print('Has derrotado al monstruo.')
                monstruos -= 1
                break   

    elif opciones == '2':
        print('Te cubres y evitas el ataque del monstruo.')
       
    elif opciones == '3':
        print('te curas ', heal, ' puntos de vida.')
        hp += heal
        potions -= 1
        print('Tienes ', hp, ' puntos de vida restantes.')
        

if hp <= 0:
    print('Has sido derrotado por el monstruo.')
elif monstruos <= 0:
    print('Has derrotado a todos los monstruos.')

