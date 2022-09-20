# Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron
# contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
# Cada raza tiene asociado un "valor" entre 1 y 8:
# - Razas bondadosas: Pelosos (1), Humanos (2), Enanos (3), Elfos (4)
# - Razas malvadas: Humanos (2), Orcos (5), Goblins (6), Huargos (7), Trolls (8)
# Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
# - El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la
#   suma del valor del ejército y el número de integrantes.
# - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
# - Tienes total libertad para modelar los datos del ejercicio.

class Soldier:
    def __init__(self, ide, name, vitality, damage):
        self.id = ide
        self.name = name
        self.vitality = vitality
        self.damage = damage

    def get_vitality(self):
        return self.vitality

    def get_damage(self):
        return self.damage


class Army():
    def __init__(self, soldiers):
        self.soldiers = soldiers

    def calculate_power(self):
        vitality = 0
        attack_power = 0
        for soldier, qty in self.soldiers.items():
            vitality += (soldier.get_vitality() * qty)
            attack_power += (soldier.get_damage() * qty)

        return vitality, attack_power


def main():
    good_army = Army(
        {
            Soldier(1, "Hobbit", 10, 5): 10,
            Soldier(2, "Human", 50, 40): 4000,
            Soldier(3, "Dwarf", 60, 30): 3000,
            Soldier(4, "Elf", 40, 50): 4500
        }
    )

    bad_army = Army(
        {
            Soldier(2, "Humans", 50, 40): 1000,
            Soldier(5, "Orc", 60, 40): 5000,
            Soldier(6, "Goblin", 30, 25): 2500,
            Soldier(7, "Warg", 30, 40): 2000,
            Soldier(8, "Troll", 80, 80): 200
        }
    )

    good_vit, good_atk = good_army.calculate_power()
    bad_vit, bad_atk = bad_army.calculate_power()

    r1 = good_vit - bad_atk
    r2 = bad_vit - good_atk

    if r1 > r2:
        print("Good army wins!")
    elif r1 == r2:
        print("Tie!")
    else: 
        print("Bad army wins!")
        

if __name__ == "__main__":
    main()