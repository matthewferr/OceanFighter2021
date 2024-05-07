# Matthew F
# 4/8/2021
# An RPG-like game based in the console to raise awareness about tech pollution in the ocean. Target audience is kids

from termcolor import colored

import os
os.system('color')

#================================= Classes ====================================

class Player():
  def __init__(self,name,sprite,health,health_max,level,energy,energy_max,health_pot):
    self.name = name
    self.sprite=sprite
    self.health = health
    self.health_max = health_max
    self.level = level
    self.energy = energy
    self.energy_max=energy_max
    self.health_pot=health_pot
  
  def update_health(self,health, damage):
    """Updates the players health"""
    player.health = player.health - damage
    # Makes it so that player is unable to 'overheal'
    if player.health > player.health_max:
      player.health=player.health_max

  def update_energy(self,energy, energy_c):
    """Updates the players energy"""
    player.energy= player.energy - energy_c
    # Makes it so that the player is unable to go over the energy limit
    if player.energy > player.energy_max:
      player.energy=player.energy_max
  
  def update_level(self,level,experience):
    """Updates the players level"""
    player.level = player.level + experience
  

class Attack():
  def __init__(self, name, damage, energy_c):
    self.name = name
    self.damage = damage
    self.energy_c = energy_c

class Enemy():
  def __init__(self,sprite,e_atk_damage,e_health,attribute,name):
    self.sprite = sprite
    self.e_atk_damage = e_atk_damage
    self.e_health=e_health
    # used to detect when the enemy should drop health potions
    self.attribute = attribute
    self.name=name
  
  def update_e_health(self,enemy,damage):
    """Updates the enemies health"""
    enemies[enemy].e_health=enemies[enemy].e_health-damage

#================================= Getting Sprites ====================================
# Setting variables
length_list=[]
enemies_sprite=[]
art=''
player_sprite_temp=''
player_sprite=[]

def get_enemy():
  """Used to get the lengths of the text art"""

  length=0
  with open('txtart.txt', 'r') as file:
    for line in file.readlines():
      length=length+len(line)
      #checks if there is a break in order to seperate the text art
      if line[0:7]=="-break-":
        length_list.append(length)
        continue

def testing():
  """Used to create a list of the enemy art in order to create objects"""
  with open('txtart.txt', 'r') as file:
    i=0
    test=length_list[i]
    # for some reason, I could not directly make the player sprite equal the file.read(the output would be choppy), so I had to append it to a list
    # -8 is to get rid of the '-break-'
    player_sprite_temp=file.read(test-8)
    player_sprite.append(player_sprite_temp)
    while player_sprite:
      # reads 8 characters ahead to get rid of the '-break-'
      file.read(8)
      i=i+1
      # subtracts to get the difference in lengths in order to precisely copy the art to the list
      test=(length_list[i]-8)-length_list[i-1]
      art=file.read(test)
      enemies_sprite.append(art)
      # there are only 9 sprites needed from the file
      if i == 9:
        break

#===================================Classes Setup=========================================

# Player
player=Player('name',player_sprite,10,10,0,10,10,2)

# Enemies (junk)
get_enemy()
testing()
player.sprite=player_sprite[0]

enemies=[]
gameboy=Enemy(enemies_sprite[0],1,5,'junk',"Nintendo GameBoy")
enemies.append(gameboy)
joystick=Enemy(enemies_sprite[1],2,6,'junk',"Joy Stick")
enemies.append(joystick)
mouse=Enemy(enemies_sprite[2],2,9,'junk',"Computer Mouse")
enemies.append(mouse)
keyboard=Enemy(enemies_sprite[3],3,7,'junk',"Keyboard")
enemies.append(keyboard)
macintosh=Enemy(enemies_sprite[4],3,8,'junk',"Macintosh PC")
enemies.append(macintosh)
pc=Enemy(enemies_sprite[5],3,10,'junk',"Computer")
enemies.append(pc)

# Enemies (robots)
robot_one=Enemy(enemies_sprite[6],5,13,'robot',"Shy Robot")
enemies.append(robot_one)
robot_two=Enemy(enemies_sprite[7],6,12,'robot',"Laser Robot")
enemies.append(robot_two)
robot_three=Enemy(enemies_sprite[8],5,20,'robot',"Ping Robot")
enemies.append(robot_three)

# Attacks
flail = Attack('flail',1,1)
headbutt = Attack('headbutt',5,4)
watergun = Attack('watergun',2,2)
rest= Attack('rest',0,-5)
heal = Attack('heal',-5,0)
block= Attack('block',1,-1)

#================================= Methods ====================================

def resume():
  """Made to ensure that user has time to read the story, like a mini pause"""
  print(colored("Press enter to continue...",'blue'))
  input()

def clear():
  """Clears Console"""
  print("\033c")

def death():
  """Death message for when the player dies. Ensures that the game stops running"""
  clear()
  print(colored('''
                                        uuuuuuu
                                    uu$$$$$$$$$$$uu
                                  uu$$$$$$$$$$$$$$$$$uu
                                u$$$$$$$$$$$$$$$$$$$$$u
                                u$$$$$$$$$$$$$$$$$$$$$$$u
                              u$$$$$$$$$$$$$$$$$$$$$$$$$u
                              u$$$$$$$$$$$$$$$$$$$$$$$$$u
                              u$$$$$$"   "$$$"   "$$$$$$u
                              "$$$$"      u$u       $$$$"
                                $$$u       u$u       u$$$
                                $$$u      u$$$u      u$$$
                                "$$$$uu$$$   $$$uu$$$$"
                                  "$$$$$$$"   "$$$$$$$"
                                    u$$$$$$$u$$$$$$$u
                                    u$"$"$"$"$"$"$u
                          uuu        $$u$ $ $ $ $u$$       uuu
                        u$$$$        $$$$$u$u$u$$$       u$$$$
                          $$$$$uu      "$$$$$$$$$"     uu$$$$$$
                        u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
                        $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
                        """      ""$$$$$$$$$$$uu ""$"""
                                  uuuu ""$$$$$$$$$$uuu
                          u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
                          $$$$$$$$$$""""           ""$$$$$$$$$$$"
                          "$$$$$"                      ""$$$$""
                            $$$"                         $$$$"
     ''','red'))

  print("")
  print("Fish and wildlife can only do so much before they, too, are defeated...")
  print("Do what you can to stop the pollution and destruction of the ocean and wildlife...")
  print("Buy computer parts from greener companies, dispose of technology properly and responsibly, and reuse, reduce, and recycle...")
  print("Check online to see how your city deals with technotrash so you can inform yourself and others on how to safely and properly dispose of your old technology to prevent pollution.")
  print("After all, it is up to you,",player.name,"to make sure you are doing your part to help make the ocean a better place for the wildlife.")
  exit()

def screen(enemy): 
  """Prints the playing board with all attributes needed"""
  print(enemies[enemy].sprite)
  e_healthbar=''
  for i in range(enemies[enemy].e_health):
    e_healthbar=e_healthbar+'▉ '
  print("")
  print(colored("                                                                Health: ",'red'),colored(e_healthbar,'red'))
  print("")
  print(colored(player.sprite,'yellow'))
  print("")
  healthbar=''
  for i in range(player.health):
    healthbar=healthbar+'▉ '
  print(colored("Health: ",'green'),colored(healthbar,'green'))
  energybar=''
  for i in range(player.energy):
    energybar=energybar+'▉ '
  print(colored("Energy: ",'cyan'),colored(energybar,'cyan'))
  print("Health Potions: ",colored(player.health_pot,'red'))
  print("")
  print("")
  # player information
  print("1.Flail:      Damage:",colored(flail.damage,'red'), "  Energy Cost:",colored(flail.energy_c,'cyan'))
  print("2.Water Gun:  Damage:",colored(watergun.damage,'red'), "  Energy Cost:",colored(watergun.energy_c,'cyan'))
  print("3.Headbutt:   Damage:",colored(headbutt.damage,'red'), "  Energy Cost:",colored(headbutt.energy_c,'cyan'))
  print("4.Rest: ", "     Restores",colored("3 energy",'cyan'))
  print("5.Heal: ", colored("     Heals for 5","green"),"at the cost of 1 health potion")
  print("6.Block:      Reduces",colored("damage taken to 1",'red'),"and restores",colored("1 energy",'cyan'))
  print("")

def fight(enemy,health_pot):
  """Controls every fight sequence in the game"""
  fight=True
  while fight:
    # counter is used for enemies that only attack every other turn
    counter=0
    attack=player_turn(enemy,player.health_pot,counter)
    resume()
    # checks if player has defeated the enemy
    if enemies[enemy].e_health <= 0:
      if enemy == 8:
        print("Before you defeat Ping Robot, he manages to smack you with his paddle!")
        print("You should have known! It's impossible for a fish to live in this much pollution!")
        fight = False
        resume()
        death()
      # makes sure that robots do not drop health potions
      elif enemies[enemy].attribute != 'robot':
        print("You have defeated",enemies[enemy].name,"!")
        resume()
        clear()
        player.health_pot=player.health_pot+1
        print("You got 1 health potion!")
        resume()
      elif enemies[enemy].attribute == 'robot':
        print("You have defeated",enemies[enemy].name,"!")
        clear()
        resume()
      fight= False
      clear()
      level_up(enemy)
      break
    
    enemy_turn(enemy,attack,counter)
    # checks if player has been defeated after enemy attack
    if player.health <=0:
      print("Oh no! You have been defeated!")
      fight = False
      resume()
      death()
    
    # Counter is set to 1 in order to trigger the skip attack for certain enemies (6 and 7)
    counter=1
    
    attack=player_turn(enemy,player.health_pot,counter)
    resume()
    if enemies[enemy].e_health <= 0:
      if enemy == 8:
        print("Before you defeat Ping Robot, he manages to smack you with his paddle!")
        print("You should have known! It's impossible for a fish to live in this much pollution!")
        fight= False
        resume()
        death()

      elif enemies[enemy].attribute != 'robot':
        print("You have defeated",enemies[enemy].name,"!")
        resume()
        clear()
        player.health_pot=player.health_pot+1
        print("You got 1 health potion!")
        resume()
      elif enemies[enemy].attribute == 'robot':
        print("You have defeated",enemies[enemy].name,"!")
        clear()
        resume()
      fight= False
      clear()
      level_up(enemy)
      break
    
    enemy_turn(enemy,attack,counter)

    if player.health <=0:
      print("Oh no! You have been defeated!")
      fight = False
      resume()
      death()
      
def player_turn(enemy,health_pot,counter):
  """The players turn to attack"""
  #Note: Most returns in this function have no real use. They are here for testing purposes only aside from the Block, which returns attack
  while True:
    choice=input("type the number of your choice: ")
    # Flail
    if choice == '1':
      # checks if player has enough energy for the move
      if player.energy < flail.energy_c:
        print("You do not have enough energy! Try resting...")
        continue
      #adjusts player stats accordingly
      player.update_energy(player.energy,flail.energy_c)
      enemies[enemy].update_e_health(enemy,flail.damage)
      clear()
      screen(enemy)
      print("You used flail to deal", flail.damage, "damage to", enemies[enemy].name,"!")
      return 1

    # Water Gun
    elif choice =='2':
      # checks if player has enough energy for the move
      if player.energy < watergun.energy_c:
        print("You do not have enough energy! Try resting...")
        continue
      # adjusts player stats accordingly
      player.update_energy(player.energy,watergun.energy_c)
      enemies[enemy].update_e_health(enemy,watergun.damage)
      clear()
      screen(enemy)
      print("You used water gun to deal", watergun.damage, "damage to", enemies[enemy].name,"!")
      return 2

    # Headbutt
    elif choice == '3':
      # checks if player has enough energy for the move
      if player.energy < headbutt.energy_c:
        print("You do not have enough energy! Try resting...")
        continue
      # adjusts player stats accordingly
      player.update_energy(player.energy,headbutt.energy_c)
      enemies[enemy].update_e_health(enemy,headbutt.damage)
      clear()
      screen(enemy)
      print("You used headbutt to deal", headbutt.damage, "damage to", enemies[enemy].name,"!")
      return 3

    # Rest
    elif choice =='4':
      # adjusts player stats accordingly
      player.update_energy(player.energy,rest.energy_c)
      clear()
      screen(enemy)
      print("You rested and gained 5 energy!")
      return 4

    # Heal
    elif choice =='5':
      # Ensures player can only heal at the cost of a health potion
      player.update_health(player.health,heal.damage)
      if player.health_pot ==0:
        print("You do not have any health potions!")
        continue
      # adjusts player stats accordingly
      player.health_pot=player.health_pot-1
      clear()
      screen(enemy)
      print("You used a health potion to heal 5 health!")
      return 5

    # Block
    elif choice == '6':
      # Enemies 6 and 7 cannot be blocked. This makes sure that happens
      # Counter is taken into account in order to ensure you are not losing health when the enemy is not attacking
      if enemy==6 and counter==0:
        player.update_health(player.health,enemies[enemy].e_atk_damage)
        clear()
        screen(enemy)
        print("Shy robot punched straight through your block!")
        attack='block'
        return attack
      elif enemy==7 and counter==0:
        player.update_health(player.health,enemies[enemy].e_atk_damage)
        clear()
        screen(enemy)
        print("The laser went straight through your block!")
        attack='block'
        # returns attack in order to ensure that the player does not take the enemy damage
        return attack

      # Makes sure you do not lose health for blocking at a turn where the enemy would not attack
      elif enemy==7 or enemy==6:
        attack='block'
        player.update_energy(player.energy,block.energy_c)
        clear()
        screen(enemy)
        print(enemies[enemy].name,"did not attack this round!")
        return attack
      attack='block'
      # Updates player stats accordingly
      player.update_energy(player.energy,block.energy_c)
      player.update_health(player.health,block.damage)
      
      clear()
      screen(enemy)
      print("You blocked the attack!")
      return attack
    else:
      print("Not a valid input, please try again...")

def enemy_turn(enemy,attack,counter):
  """The enemy's turn to attack"""
  #Note: Returns here are used for testing purposes only

  if attack == 'block':
    return "attack blocked!"

  if enemy != 6 and enemy!=7:
    player.update_health(player.health,enemies[enemy].e_atk_damage)
    clear()
    screen(enemy)
    print(enemies[enemy].name,"attacked you for",enemies[enemy].e_atk_damage,"damage!")
    print("")
    return "player was attacked!"

  elif counter ==0:
    player.update_health(player.health,enemies[enemy].e_atk_damage)
    clear()
    screen(enemy)
    print(enemies[enemy].name,"attacked you for",enemies[enemy].e_atk_damage,"damage!")
    print("")
    return "player was attacked!"

  # Makes sure that enemies 6 and 7 only attack every other turn
  elif enemy==6 and counter==1:
    clear()
    screen(enemy)
    print("Shy robot does not feel like attacking right now...")
  elif enemy==7 and counter==1:
    clear()
    screen(enemy)
    print("The laser needs time to recharge!")

def level_up(enemy):
  """Levels the player up and adjusts stats accordingly"""
  # Because it is a small game, I did not see the point in using a proper experience system. Instead, I just made it so that the player levels up after every other enemy.

  #Note: Returns here are for testing purposes only

  if enemy == 0:
    #Updates players level to ensure proper output
    player.update_level(player.level,1)
    print("You leveled up! You are now level ",player.level)

    # Updates players stats
    player.energy=player.energy+1
    player.energy_max=player.energy_max+1
    player.health=player.health+1
    player.health_max=player.health_max+1
    print("Your max health and energy has increased!")
    print("Max Health:",colored(player.health_max,'green'))
    print("Max Energy:",colored(player.energy_max,'cyan'))
    print("")

    flail.damage = flail.damage+1
    watergun.damage=watergun.damage+1
    print("Flail now does",colored(flail.damage,'red'))
    print("Water gun now does",colored(watergun.damage,'red'))
    return "player is level 1"

  elif enemy == 1:
    player.update_level(player.level,1)
    print("You leveled up! You are now level ",player.level)

    player.energy_max=player.energy_max+2
    player.energy=player.energy+2
    player.health_max=player.health_max+2
    player.health=player.health+2
    print("Your max health and energy has increased!")
    print("Max Health:",colored(player.health_max,'green'))
    print("Max Energy:",colored(player.energy_max,'cyan'))
    print("")
    
    watergun.damage=watergun.damage+1
    headbutt.damage=headbutt.damage+1
    print("Water gun now does",colored(watergun.damage,'red'))
    print("Headbutt now does",colored(headbutt.damage,'red'))
    return "player is level 2"

  elif enemy == 3:
    player.update_level(player.level,1)
    print("You leveled up! You are now level ",player.level)

    player.energy_max=player.energy_max+1
    player.energy=player.energy+1
    player.health_max=player.health_max+2
    player.health=player.health+2
    print("Your max health and energy has increased!")
    print("Max Health:",colored(player.health_max,'green'))
    print("Max Energy:",colored(player.energy_max,'cyan'))

    watergun.damage=watergun.damage+1
    headbutt.damage=headbutt.damage+2
    watergun.energy_c= watergun.energy_c+1
    print("Water gun now does",colored(headbutt.damage,'red'),"and takes",colored(watergun.energy_c,'cyan'))
    print("Headbutt now does",colored(headbutt.damage,'red'))
    return "player is level 3"

  elif enemy == 5:
    player.update_level(player.level,1)
    print("You leveled up! You are now level ",player.level)

    player.energy_max=player.energy_max+2
    player.energy=player.energy+2
    player.health_max=player.health_max+2
    player.health=player.health+2
    print("Your max health and energy has increased!")
    print("Max Health:",colored(player.health_max,'green'))
    print("Max Energy:",colored(player.energy_max,'cyan'))

    
    headbutt.damage=headbutt.damage+1
    headbutt.energy_c= headbutt.energy_c+1
    print("Headbutt now does",colored(headbutt.damage,'red'),"and takes",colored(headbutt.energy_c,'cyan'))
    return "player is level 4"

  elif enemy == 7:
    player.update_level(player.level,1)
    print("You leveled up! You are now level ",player.level)

    player.energy_max=player.energy_max+2
    player.energy=player.energy+2
    player.health_max=player.health_max+2
    player.health=player.health+2
    print("Your max health and energy has increased!")
    print("Max Health:",colored(player.health_max,'green'))
    print("Max Energy:",colored(player.energy_max,'cyan'))
    
    flail.damage = flail.damage+1
    watergun.damage=watergun.damage+1
    headbutt.damage=headbutt.damage+1
    watergun.energy_c= watergun.energy_c+1
    headbutt.energy_c= headbutt.energy_c+1
    print("Flail now does",colored(flail.damage,'red'))
    print("Water gun now does",colored(watergun.damage,'red'),"and takes",colored(watergun.energy_c,'cyan'))
    print("Headbutt now does",colored(headbutt.damage,'red'),"and takes",colored(headbutt.energy_c,'cyan'))
    return "player is level 5"

  else:
    return None

def main():
  """Starts the game and controls the game until the end"""

  print("")
  print(colored('''
░█████╗░░█████╗░███████╗░█████╗░███╗░░██╗               ████▓▓████  
██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗░██║           ▓▓▓▓▒▒▓▓▓▓▒▒▒▒▓▓▓▓ 
██║░░██║██║░░╚═╝█████╗░░███████║██╔██╗██║          ▓▓░░░░▒▒▓▓░░▒▒▒▒▓▓░░▓▓ 
██║░░██║██║░░██╗██╔══╝░░██╔══██║██║╚████║        ██░░▓▓▒▒░░░░░░▓▓██▓▓░░██ 
╚█████╔╝╚█████╔╝███████╗██║░░██║██║░╚███║       ██▓▓▓▓░░  ░░░░██████▒▒░░██
░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝       ██▒▒░░  ░░░░▒▒████▓▓▓▓░░██''','blue'))
  print(colored(''' ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          ███████╗██╗░██████╗░██╗░░██╗████████╗███████╗██████╗░
▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒▒██╔════╝██║██╔════╝░██║░░██║╚══██╔══╝██╔════╝██╔══██╗
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████╗░░██║██║░░██╗░███████║░░░██║░░░█████╗░░██████╔╝
          ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒██╔══╝░░██║██║░░╚██╗██╔══██║░░░██║░░░██╔══╝░░██╔══██╗
              ▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓    ▓▓▓▓▓▓▓██║░░░░░██║╚██████╔╝██║░░██║░░░██║░░░███████╗██║░░██║
                    ▒▒▒▒▓▓            ▓▓▓╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
                    ▒▒▓▓                   
                    ''','green'))
  print("")
  player.name=input("Type your character's name: ")

  print("The ocean is being attacked by", colored("technotrash!",'red'),"You must use your fish abilities to fight off these enemies and protect your homeland!")
  print("You are told that somewhere near the centre of the ocean, the technotrash's boss awaits for your arrival!")
  print("Protect the ocean and defeat the pollution!")
  print("")
  resume()
  clear()

  print("While swimming along the ocean, you notice an old Nintendo Gameboy!")
  resume()
  clear()

  enemy=0
  screen(enemy)
  fight(enemy,player.health_pot)
  resume()
  clear()
  
  print("After defeating the gameboy, you travel a bit further, looking for more technotrash...")
  print("After a bit, you encounter a joy stick!")
  resume()
  clear()

  enemy=1
  screen(enemy)
  fight(enemy,player.health_pot)
  resume()
  clear()

  print("You keep on swimming along until you are ambushed by a mouse!")
  resume()
  clear()

  enemy=2
  screen(enemy)
  fight(enemy,player.health_pot)
  resume()
  clear()

  print("After defeating the mouse, a keyboard jumps out to attack you!")
  resume()
  clear()

  enemy=3
  screen(enemy)
  fight(enemy,player.health_pot)
  resume()
  clear()

  print("You travel a bit further, getting closer to the center. You consider resting until an old Macintosh comes forth!")
  resume()
  clear()

  enemy=4
  screen(enemy)
  fight(enemy,player.health_pot)
  resume()
  clear()

  print("After defeating the Macintosh, you notice an old PC in the distance. You swim towards it!")
  resume()
  clear()

  enemy=5
  screen(enemy)
  fight(enemy,player.health_pot)
  resume()
  clear()

  print("You are almost at the center! Be cautious! You see a robot coming at you!")
  resume()
  clear()

  enemy=6
  screen(enemy)
  fight(enemy,player.health_pot)
  resume()
  clear()

  print("After swimming a bit closer, you encounter a new robot!")
  resume()
  clear()

  enemy=7
  screen(enemy)
  fight(enemy,player.health_pot)
  resume()
  clear()

  print("You finally reached the center! Get ready to fight the boss!")
  resume()
  clear()

  enemy=8
  screen(enemy)
  fight(enemy,player.health_pot)

main()
