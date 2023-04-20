from random import randint
import atexit
from os import path
from json import dumps, loads


def read_counter():
    return loads(open("counter.json", "r").read()) + 1 if path.exists("counter.json") else 0


def write_counter():
    with open("counter.json", "w") as f:
        f.write(dumps(counter))


def addtofile(res):
    with open(f'./LogsJuegos/Juego_{counter}', 'a') as f:
        f.write(f'\n{res}')


def joao():
    global valc
    while valc < 17:
        ranc = randint(1, 10)
        valc = valc + ranc
    if valc > 21:
        print("Joao se paso, ganaste")
        addtofile("Joao se paso, ganaste")
    pass


counter = read_counter()
atexit.register(write_counter)
againn = True

while againn:
    hit = True
    val = 0
    valc = 0
    it = 0
    while hit:
        ran = randint(1, 10)
        if it == 0:
            ran = ran + randint(1, 10)
            it = 1
        if ran == 1:
            coppa = int(input("1 / 11"))
            if coppa == 1:
                ran = 1
            elif coppa == 11:
                ran = 11
        val = val + ran
        print(val)
        addtofile(val)
        if val > 21:
            print("te pasaste pa")
            addtofile("te pasaste pa")
            again = input("Queres jugar de vuelta? (S/N)\n")
            addtofile(f"Queres jugar de vuelta? (S/N)\n{again}")
            if again == "N":
                againn = False
            print("\n")
            addtofile("\n")
            break
        elif val == 21:
            print("21 pa 😎")
            addtofile("21 pa 😎")
            again = input("Queres jugar de vuelta? (S/N)\n")
            addtofile(f"Queres jugar de vuelta? (S/N)\n{again}")
            if again == "N":
                againn = False
            print("\n")
            addtofile("\n")
            break

        else:
            sergio = input("Hit or stand? (H/S)\n")
            addtofile(f"Hit or stand? (H/S)\n{sergio}")
            if sergio == "S":
                hit = False
                joao()
                if val < valc <= 21:
                    print(f"Perdiste, joao tenia {valc}")
                    addtofile(f"Perdiste, joao tenia {valc}")
                elif valc == val:
                    print("Empate")
                    addtofile("Empate")
                elif valc < val:
                    print(f"Ganaste, joao tenia {valc}")
                    addtofile(f"Ganaste, joao tenia {valc}")
                again = input("Queres jugar de vuelta? (S/N)\n")
                addtofile(f"Queres jugar de vuelta? (S/N)\n{again}")
                if again == "N":
                    againn = False
                print("\n")
                addtofile("\n")
