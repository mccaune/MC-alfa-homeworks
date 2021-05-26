import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="pokemon"
)

mycursor = db.cursor()

# mycursor.execute("DESCRIBE player_csv")
# for x in mycursor:
#     print(x)

class Player:
    number_of_players = 0
    
    def __init__(self, name, experience, pokemonSlots):
        self.name= name 
        self.experience = experience
        self.pokemonSlots = pokemonSlots
        self.abilities = []
        self.ownedPokemons = []
        self.wonBattles = 0
        Player.number_of_players += 1
        
    def addAbility(self, abilityName):
        #assigning ability to player
        self.abilities.append(abilityName)

    def addPokemon(self, pokemonName):
        #player can add pokemon only if he have free pokemon slot
        if self.pokemonSlots > len(self.ownedPokemons):
            self.ownedPokemons.append(pokemonName)
        
    def gainExperience(self):
        #for winning single battle player earns 10exp
        i = 0
        while i < self.wonBattles: 
            self.experience += 10
            i += 1
            
        #for acquiring ability player earns 2exp
        for x in self.abilities: 
            self.experience += 2
        
        #based on earned experience player gets additional pokemon slots  
        if self.experience > 10:
            self.pokemonSlots += 1
        if self.experience > 20:
            self.pokemonSlots += 3
        if self.experience > 40:
            self.pokemonSlots += 11
        
        
class Ability:
    def __init__(self, name, a_type, power ):
        self.name = name
        self.a_type = a_type
        self.power = power
        
        
class Pokemon:
    def __init__(self, p_id, p_name, p_type, p_experience):
        self.p_id = p_id
        self.p_name = p_name
        self.p_type = p_type
        self.p_experience = p_experience
        self.moves = []
    
    #currently not used 
    def getMoves(self,name):
        move = Moves(name)
        self.moves.append(move)
        
#currently not used     
class Moves:
    def __init__(self, name):
        self.name = name

#currently not used
class Stats:
    def __init__(self, name):
        self.attack = attack
        self.magicAttack = magicAttack
        self.defence = defence
        self.magicDefence = magicDefence
        self.speed = speed

class Battle:
    def __init__(self, player1Name, player2Name, player1Exp, player2Exp):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Exp = player1Exp
        self.player2Exp = player2Exp
    
    #here the winner of fight will be decided. For now player with most experience wins 
    def decidingWinner(self):
        if self.player1Exp > self.player2Exp:
            print(self.player1Name, ' has WON!!!')
            player1.wonBattles += 1
        else:
            print(self.player2Name, ' has WON!!!')
            player2.wonBattles += 1




#creating players
player1 = Player('Bob', 1, 5)
player2 = Player('Carl', 2, 4)
player3 = Player('Ash', 3, 3)
player4 = Player('Ciri', 4, 2)
player5 = Player('Skye', 5, 1)

#creating player abilities
abilityFire1 = Ability('fire bolt', 'fire', 3)
abilityFire2 = Ability('inferno', 'fire', 6)
abilityWater1 = Ability('water cannon', 'water', 4)
abilityWater2 = Ability('cunami', 'water', 5)
abilityGround1 = Ability('rock rain', 'ground', 2)
abilityGround2 = Ability('earthquake', 'ground', 7)
abilityElectric1 = Ability('sparks', 'electric', 1)
abilityElectric2 = Ability('lightning strike', 'electric', 8)

#crating pokemons
pokemon1 = (1, 'bulabsaur', 'posion', 1)
pokemon2 = (2, 'charmander', 'fire', 1)
pokemon3 = (3, 'squirtle', 'water', 1)
pokemon4 = (4, 'pidgey', 'flying', 1)
pokemon5 = (5, 'pikachu', 'electric', 1)
pokemon6 = (6, 'jigglypuff', 'fairy', 1)
pokemon7 = (7, 'diglett', 'ground', 1)
pokemon8 = (8, 'meowth', 'normal', 1)
pokemon9 = (9, 'hypno', 'psychic', 1)
pokemon10 = (10, 'magnemite', 'electric', 1)

#adding abilities to players
player1.addAbility(abilityGround1)
player1.addAbility(abilityGround2)
player2.addAbility(abilityFire1)
player2.addAbility(abilityFire2)
player3.addAbility(abilityWater1)
player3.addAbility(abilityWater2)
player4.addAbility(abilityElectric1)
player4.addAbility(abilityElectric2)
player5.addAbility(abilityFire1)
player5.addAbility(abilityGround2)

# by running this players gain experience based on their abilities and won battles
player1.gainExperience()
player2.gainExperience()
player3.gainExperience()
player4.gainExperience()
player5.gainExperience()

#adding pokemons to players only after players gain experience (pokemon slots depend on it)
player1.addPokemon(pokemon4)
player1.addPokemon(pokemon3)
player1.addPokemon(pokemon2)

print(player2.name, ' won battles: ',player2.wonBattles)

#simulating fight with player1 and player2. 
fight1 = Battle(player1.name, player2.name, player1.experience, player2.experience)

fight1.decidingWinner()

print(player2.name, ' won battles: ',player2.wonBattles)


"""
#printing some data about players
print('\n', player1.name, ' experience: ', player1.experience )
print('\n', player2.name, ' experience: ', player2.experience )
print('\n', player3.name, ' experience: ', player3.experience )
print('\n', player4.name, ' experience: ', player4.experience )
# print(player1.pokemonSlots)
# print(player2.pokemonSlots)
# print(player3.pokemonSlots)
# print(player4.pokemonSlots)

print('\n', player1.name, ' abilities: ')
for x in player1.abilities: print(x.name)

print('\n', player1.name, ' owned pokemons: ')
for x in player1.ownedPokemons: print(x)

#getting total player count
print('\n', 'Player count: ', Player.number_of_players)

"""

#DB stuff

"""
#adding random players to DB
playerNames = ['Jeramy','Dennise','Kathryne','Stephen','Rosella','Stuart','Mica','Aisha','Ching','Aleshia','Cami','Kacie','Dane','Kenisha','Burl','Mechelle','Kimberlie','Mitch','Reed','Clarissa','Arnold','Keesha','Lourdes','Raylene','Maggie','Megan','Rachell','Quintin','Orval','Robbie','Myrta','Hester','Dorthy','Ethel','Le','My','Bruce','Torie','Dia','Gus','Winter','Myriam','Krissy','Damon','Robby','Reinaldo','Johnathan','Edwin','Lola','Piedad',]

for x in playerNames:
    mycursor.execute("INSERT INTO players (name, status, experience, abilities, pokemonSlots, ownedPokemons, wonBattles) VALUES(%s, %s, %s, %s, %s, %s, %s)", (x, 'active', 0, 0, 1, 0, 0))
    
db.commit()
"""

"""
#selecting random user
randomNumber = random.randint(53,102)


user1 = mycursor.execute("SELECT * FROM players WHERE idPlayer = 66")

print(user1)
for x in mycursor:
    print(x)
    
    
"""

#getting total player count
mycursor.execute("SELECT count(*) FROM player_csv")
players_total = mycursor.fetchone()

#assigning random pokemon to each player
for x in range(players_total[0]+1):
    sql_statement = "UPDATE player_csv SET pokemon_id = %s where player_id = %s"
    data = (random.randint(1,800), x)
    mycursor.execute(sql_statement, data)
db.commit()


