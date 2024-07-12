import json
import random

class Characters:
    def __init__(self, name, Health, strength, defense, intelligence, agility):
        self.name = name
        self.Health = Health
        self.strength = strength
        self.defense = defense
        self.intelligence = intelligence
        self.agility = agility
        
    def check(self):
        print(f"\n--------------------------------------------------------------------\nname: {self.name}\nHP: {self.Health}\nSTR: {self.strength}\nDEF: {self.defense}\nINT: {self.intelligence}\nAGI: {self.agility}\n--------------------------------------------------------------------\n")

    def Edit(self):
        x = self.name
        name = input("Enter character Name:")
        self.name = name
        print(f"{x} name has changed to {name}")

class Monster(Characters):
    def __init__(self, name, Health, strength, defense, intelligence, agility, grade):
        super().__init__(name, Health, strength, defense, intelligence, agility)
        self.grade = grade
        self.exp = int((self.Health*0.75) + ((self.strength + self.defense + self.intelligence + self.agility)/2))

    def check(self, x):
        print(f"name: {self.name}\nGrade: {self.grade}\nHP: {self.Health}\nSTR: {self.strength}\nDEF: {self.defense}\nINT: {self.intelligence}\nAGI: {self.agility}")
        choice = int(input("\n1.Edit\n2.Remove from List\n0. Back\n\nSelect an Action: "))
        if choice == 1:
            self.Edit()
        elif choice == 2:
            del game.Monster[x-1]
            print(f"Monster was permanently removed from the 'Monster Encyclopedia'")
            return
        elif choice == 0:
            return

    def Edit(self):
        name = input("Enter the name of the Monster:")
        Health = int(input("Enter the monster's amount of Health: "))
        if Health > 0 & Health < 1000000:
            Strength = int(input("Enter the Strenght of the monster: "))
            if Strength > 0 & Strength < 10000:
                Defense = int(input("Enter the Defense of the monster: "))
                if Defense > 0 & Defense < 10000:
                    Intelligence = int(input("Enter the Intelligence of the monster: : "))
                    if Intelligence > 0 & Intelligence < 10000:
                        Agility = int(input("Enter the Agility of the monster: : "))
                        if Agility > 0 & Agility < 10000:
                            Level = int((Strength + Defense + Intelligence + Agility)/4)
                            if Level <= 19:
                                Grade = 'F'
                            elif Level <= 99:
                                Grade = 'E'
                            elif Level <= 199:
                                Grade = 'D'
                            elif Level <= 299:
                                Grade = 'C'
                            elif Level <= 499:
                                Grade = 'B'
                            elif Level <= 999:
                                Grade = 'A'
                            elif Level <= 2499:
                                Grade = 'S'
                            elif Level <= 5499:
                                Grade = 'SS'
                            elif Level <= 7499:
                                Grade = 'SSS'
                            elif Level <= 9999:
                                Grade = 'Transcended'
                            print("{name} was Recorded as a {Grade} Rank Monster")
                            self.name = name
                            self.Health = Health
                            self.strength = Strength
                            self.defense = Defense
                            self.intelligence = Intelligence
                            self.agility = Agility
                            self.grade = Grade
                            return
                        else:
                            print("No such Monster Exist. Try Again\n")
                            self.record_monster()
                    else:
                        print("No such Monster Exist. Try Again\n")
                        self.record_monster()
                else:
                    print("No such Monster Exist. Try Again\n")
                    self.record_monster()
            else:
                print("No such Monster Exist. Try Again\n")
                self.record_monster()
        else:
            print("No such Monster Exist. Try Again\n")
            game.record_monster()

class Player(Characters):
    def __init__(self, name, Health, strength, defense, intelligence, agility, level):
        super().__init__(name, Health, strength, defense, intelligence, agility)
        self.level = level
        self.limit = 50
        self.current = 0

    def check(self, x):
        print("_____________________________________________________________________")
        print(f"name: {self.name}\nLevel: {self.level}\nHP: {self.Health}\nSTR: {self.strength}\nDEF: {self.defense}\nINT: {self.intelligence}\nAGI: {self.agility}")
        action = input("\nWhat would you like to do?\n1.Rename\n2.Kick from Party\n0.Back\n:")
        if action == '1':
            self.Edit()
        elif action =='2':
            if len(game.Player) > 1:
                print(f"{game.Player[x-1].name} was permanently removed from the 'Party'")
                del game.Player[x-1]
                return
            else:
                print("Party Cannot be Empty")
        elif action == '0':        
            return

    def exp(self, points):
        self.current += points
        while True:
            calculate = self.limit - self.current
            if calculate <= 0:
                self.limit += (self.limit * 1.5)
                self.current = abs(calculate)
            else:
                break


class Dungeon:
    def __init__(self, name, difficulty, type, loot):
        self.name = name
        self.difficulty = difficulty
        self.type = type
        self.loot = loot

    def combat(self, x, spawn):
            Hp = x.Health
            while True:
                if Hp == 0:
                    input(f"{x.name} has been defeated.")
                    for y in game.Player:
                        y.exp(x.exp)
                    break
                else:
                    dialogue = ["is waiting menacingly", "grows impatient as it sees you struggling to unsheath your weapons", "wants to go back to sleep", "is upset to see your face", "likes to make your face as a mop", "Stares at you, waiting for something to happen"]
                    print(f"{x.name} {random.choice(dialogue)}")
                    print(f"\n|My Team|")
                    for y in game.Player:
                        print(f"\nname: {y.name}\nLevel: {y.level}\nHP: {y.Health}\nSTR: {y.strength}\nDEF: {y.defense}\nINT: {y.intelligence}\nAGI: {y.agility}")
                    action = input(f"""
        ______________________________________________________________________________________
       |          Attack           |           Identify           |            Run            |                                 
       |_____________1_____________|_______________2______________|_____________0_____________|
                        |>""")
                    if action == '1':
                        damage = 0
                        for y in game.Player:
                            damage += int((y.strength + y.intelligence)-x.defense)
                        if damage > 0:
                            if damage <= Hp:
                                Hp = x.Health - damage
                            elif damage > Hp:
                                Hp = 0
                            input(f"{x.name} took {damage} damage")
                        else:
                            Hp = x.Health - 1
                            input(f"{x.name} took 1 damage")

                    elif action == '2':
                        input(f"\n\t\t\tEnemy Info\n\nname: {x.name}\nGrade: {x.grade}\nHP: ({Hp}/{x.Health})\nSTR: {x.strength}\nDEF: {x.defense}\nINT: {x.intelligence}\nAGI: {x.agility}\n\n\nv^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^\n...")
                    elif action == '0':
                        input(f"{x.name} laugh at you as it watch you run with your tails between your legs\n\n")
                        break


    def Detail(self,choice):
        print(f"""
        |-------------------|{self.name}|------------------
        |Dungeon Rank: {self.difficulty}
        |Dungeon Type: {self.type}
        |Available loot:{self.loot}
        |________________________________________
            """)
        action = input("\nWhat would you like to do?\n1.Edit Details\n2.Raid\n3.Remove Dungeon\n0.Back\n:")
        if action == '1':
            self.Edit(choice)
        elif action == '2': #Raid 
            monsters = []
            for x in game.Monster:
                if x.grade == self.difficulty:
                    monsters.append(x)
            if len(monsters) == 0:
                print(f"Warning!!! There are no registered monster with '{self.difficulty}' rank in your 'Monster Encyclopedia'")
                
            else:
                spawn = (random.choices(monsters, k=5))
                for x in spawn:
                    print("_____________________________________________________________________\n")
                    input(f"\nA {x.name} has been spotted")
                    self.combat(x, spawn)
            input("\n|YOUR PARTY HAS RETURNED FROM A LONG EXPEDITION|\n...")

        elif action =='3':
            del game.Dungeon[choice-1]
        elif action == '0':
            game.dungeon_list()

    def Edit(self, choice):
        name = input("\nEnter the name of the Dungeon:")
        difficulty = input("What is the Dungeons Difficulty?: ")
        type = input("what type of dungeon did you explore?: ")
        Loot = input("What loot can be found there?: ")
        confirm = input("Finish Editing Dungeon Details?\n1.Yes\n2.No\n: ")
        if confirm == '1':
            new = Dungeon(name, difficulty, type, Loot)
            game.Dungeon[choice-1] = new
            game.dungeon_list()
        elif confirm == '2':
            self.Edit(choice)
        else:
            print("error input")
            self.Detail(choice)


class Game():
    def __init__(self, filename = 'Dungeonabyss.json'):
        self.filename = filename
        self.Dungeon = []
        self.Player = []
        self.Monster = []

    def explore(self):
        name = input("Enter the name of the Dungeon:")
        difficulty = input("What is the Dungeons Difficulty?: ")
        type = input("what type of dungeon did you explore?: ")
        Loot = input("What loot can be found there?: ")

        conquer = Dungeon(name, difficulty, type, Loot)
        self.Dungeon.append(conquer)

    def dungeon_list(self):
        print("\nExplored Dungeons:\n")
        print("_____________________________________________")
        for x, y in enumerate(self.Dungeon):
            print(f"{x+1}. {y.name}")
            print("_____________________________________________")
        print("0.Back")
        print("_____________________________________________")

        choice = int(input("\nWhich dungeon would you wish to Invesitgate?: "))
        if choice == 0:
            pass
        elif choice <= len(self.Dungeon):
            self.Dungeon[choice-1].Detail(choice)
        else: 
            print("Dungeon selected does not exist. try again.")
            self.dungeon_list()

    def recruit(self):
        name = input("Enter Character Name:")

        if len(game.Player) < 4:
            member = Player(name, 15, 5, 5, 5, 5, 1)
            print("creating new character")
            game.Player.append(member)
            print(f"{name} joined the party.")
        else:
            print("Party is full, remove a character before you can recruit another.")

    def check_party(self): 
        print(f"\nMy Party:\n")
        for x, y in enumerate(game.Player):
            print(f"\n{x+1}. {y.name}\n")
            print("_____________________________________________")
        print("0.Back")
        print("_____________________________________________")            
        choice = int(input("\nSelect Character to view: "))
        if choice == 0:
            return
        elif choice <= len(game.Player):
            game.Player[choice-1].check(choice)
        else: 
            print("Party member does not exist. try again.")
            self.check_party()


    def record_monster(self):
        name = input("Enter the name of the Monster:")
        Health = int(input("Enter the monster's amount of Health: "))
        if Health > 0 & Health < 1000000:
            Strength = int(input("Enter the Strenght of the monester: "))
            if Strength > 0 & Strength < 10000:
                Defense = int(input("Enter the Defense of the monster: "))
                if Defense > 0 & Defense < 10000:
                    Intelligence = int(input("Enter the Intelligence of the monster: : "))
                    if Intelligence > 0 & Intelligence < 10000:
                        Agility = int(input("Enter the Agility of the monster: : "))
                        if Agility > 0 & Agility < 10000:
                            Level = int((Strength + Defense + Intelligence + Agility)/4)
                            if Level <= 19:
                                Grade = 'F'
                            elif Level <= 99:
                                Grade = 'E'
                            elif Level <= 199:
                                Grade = 'D'
                            elif Level <= 299:
                                Grade = 'C'
                            elif Level <= 499:
                                Grade = 'B'
                            elif Level <= 999:
                                Grade = 'A'
                            elif Level <= 2499:
                                Grade = 'S'
                            elif Level <= 5499:
                                Grade = 'SS'
                            elif Level <= 7499:
                                Grade = 'SSS'
                            elif Level <= 9999:
                                Grade = 'Transcended'
                            Mob = Monster(name, Health, Strength, Defense, Intelligence, Agility, Grade)
                            print(f"\n\n[{name}] has been recorded as --{Grade} Rank Monster--\n")
                            game.Monster.append(Mob)
                            print("\nMonster has been Registered on the 'Monster Encyclopedia'\n\n")
                        else:
                            print("No such Monster Exist. Try Again\n")
                            self.record_monster()
                    else:
                        print("No such Monster Exist. Try Again\n")
                        self.record_monster()
                else:
                    print("No such Monster Exist. Try Again\n")
                    self.record_monster()
            else:
                print("No such Monster Exist. Try Again\n")
                self.record_monster()
        else:
            print("No such Monster Exist. Try Again\n")
            self.record_monster()

    def monster_encyclopedia(self):
        print(f"\n--------------------| Monster Encyclopedia|--------------------\n|\n|\n|")
        for x, y in enumerate(game.Monster):
            print(f"|{x+1}. {y.name}")
            print("|_____________________________________________")
        print("|0.Back")
        print("|_____________________________________________")
        choice = int(input("|\nSelect a Monster to view: "))
        if choice == 0:
            return
        elif choice <= len(game.Monster):
            game.Monster[choice-1].check(choice)
        else: 
            print("Monster does not exist. try again.")
            self.monster_encyclopedia()

    def save_to_json(self):
        Dungeon_data = [{'Name': dungeons.name, 'Difficulty': dungeons.difficulty, 'Type': dungeons.type, 'Loots': dungeons.loot}for dungeons in self.Dungeon]
        Monster_data = [{'Name': monsters.name, 'Health': monsters.Health, 'Strength': monsters.strength, 'Defense': monsters.defense, 'Intelligence': monsters.intelligence, 'Agility': monsters.agility, 'Grade': monsters.grade}for monsters in self.Monster]
        PLayer_data = [{'Name': players.name, 'Health': players.Health, 'Strength': players.strength, 'Defense': players.defense, 'Intelligence': players.intelligence, 'Agility': players.agility, 'Level': players.level}for players in self.Player]
    
        with open(self.filename, 'w') as json_file:
            json.dump({'Dungeons': Dungeon_data, 'Monsters': Monster_data, 'Players': PLayer_data}, json_file, indent =2 )
            input("Game Saved.")


    def load_from_json(self):
        with open(self.filename, 'r') as json_file:
            data = json.load(json_file)
        self.Dungeon = [Dungeon(dungeons['Name'], dungeons['Difficulty'], dungeons['Type'], dungeons['Loots'])for dungeons in data.get('Dungeons', [])]
        self.Monster = [Monster(monsters['Name'], monsters['Health'], monsters['Strength'], monsters['Defense'], monsters['Intelligence'], monsters['Agility'], monsters['Grade'])for monsters in data.get('Monsters',[])]
        self.Player = [Player(players['Name'], players['Health'], players['Strength'], players['Defense'], players['Intelligence'], players['Agility'], players['Level'])for players in data.get('Players',[])]
        input("Game Loaded")

            
def Play():
    while True:
        print("________________________________| HOME |________________________________")
        option = input("1.Check Available Dungeons\n\n2.Check party\n\n3.Recruit New Member\n\n4.Open Monster Encyclopedia\n\n5.Record new monster\n\n6.Generate new Dungeon\n\n0.Exit\n\n|: ")
        print("__________________________________________________________________________")
        if option == '1':
            if not game.Dungeon:
                print("\n\n----------------------No Dungeons Available Generate one first----------------------\n\n\n\n")
            else:
                game.dungeon_list()
        elif option == '2':
            game.check_party()
        elif option == '3':
            game.recruit()
        elif option == '4':
            if not game.Monster:
                print("\n\n----------------------No Monsters Recorded. Add one first----------------------\n\n\n\n")
            else:            
                game.monster_encyclopedia()
        elif option == '5':
            game.record_monster()
        elif option == '6':
            game.explore()
        elif option == '0':
            save = input("Do you wanna save your Progress?\n1.Yes\n2.No\n: ")
            if save == '1':
                game.save_to_json()
                break
            elif save == '2':
                print("save failed.\nExit game.")
                break
            else:
                print("Invalid Input")


def menu():
    while True:
        mainmenu = input("""
                                 #########
                                #  *---*  #
                                #  |-|-|  #                           
                            __________________
                            | DUNGEON ABYSS  |                             
                            |  1. New Game   |                            
                            |  2. Continue   |                            
                            |  0. Exit       |                        
                            |________________|
                                :""")
        if mainmenu == '1':
            try:
                confirm = input("Are you sure?\nAll saved progress and data will be lost.\n1. Yes\n2. No\n: ")
                if confirm == '1': #Bugged
                    game.recruit()
                    game.save_to_json()
                    Play()
                elif confirm == '2':
                    print("\n\n\n\n\n\n\n\n")
            except Exception as e:
                print(f'Error: {e}')
        elif mainmenu == '2':
            print("\n\n\n\n\n\n\n\n")
            try:
                game.load_from_json()
                Play()
            except FileNotFoundError:
                print("No save file available.\n\nLoad failed\n\n.")
        elif mainmenu == '0':
            break


if __name__ == '__main__':
    game = Game()
    menu()