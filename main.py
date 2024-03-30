import random
import map, Hero, Enemy, check_input, beg_factory, exp_factory

def main():
  name = input("What is your name, traveler? ")
  difficulty = check_input.get_int_range("Difficulty:\n1. Beginner \n2. Expert\n", 1, 2)

  '''
  Factory Construction Based on Difficulty Choice
  '''
  factory = None
  if difficulty == 1:
    factory = beg_factory.BeginnerFactory()
  else:
    factory = exp_factory.ExpertFactory()
  mapCounter = 1
  hero1 = Hero.Hero(name)
  userChoice = 0
  map1 = map.Map()
  map1.load_map(mapCounter)
  
  '''
  Dictonary to Store Our Prompts for the Encounters
  '''
  prompts = {
    'm': "You encounter a ",
    'o': "You can't move there!",
    'n': 'This room is empty.',
    's': 'You wound up back at the dungeon!',
    'i': 'You found a health potion!',
    'f': 'Congratulations! You found the stairs to the next floor of the dungeon.'
  }

  # Loop not ending when hero dies
  while userChoice != 5 or hero1.hp <= 0:
    if hero1.hp <= 0:
      break
    print() 
    print(hero1)
    map1.reveal(hero1._loc)
    print(map1.show_map(hero1._loc))

    '''
    Menu for the User to Choose what direction to go in 
    '''
    userChoice = check_input.get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit. \nEnter Choice: ", 1, 5)
    map1.reveal(hero1._loc)
    if userChoice == 1:
      letter = hero1.go_north()
    elif userChoice == 2:
      letter = hero1.go_south()
    elif userChoice == 3:
      letter = hero1.go_east()
    elif userChoice == 4:
      letter = hero1.go_west()
    else:
      break

    map1.reveal(hero1._loc)
    print()

    '''
    Monster Fight - Can either choose to attack the monster or run away. Running Away moves the user by one unit in a random direction
    '''
    if letter == 'm':
      map1.reveal(hero1._loc)
      enemy = factory.create_random_enemy()
      print(enemy)
      print(prompts['m'] + enemy.name)
      while True:
        print(f"1. Attack {enemy.name}\n2. Run Away")
        userChoice = check_input.get_int_range("Enter Choice: ", 1, 2)
        print()
        if userChoice == 1:
          hero1.attack(enemy)
          if enemy.hp <= 0:
            print(f"You have slain {enemy.name}")
            map1.remove_at_loc(hero1._loc)
            break
          else:
            print(enemy.attack(hero1))
            if hero1.hp <= 0:
              print(f"You have been slain by {enemy.name}")
              break
        else:
          '''
          Looping through options to make sure the direction we move in is valid (not blocked by boundaries)
          '''
          returned = 'o'
          while returned == "o":
            direction = random.randint(1, 4)
            if direction == 1:
              returned = hero1.go_north()
            elif direction == 2:
              returned = hero1.go_south()
            elif direction == 3:
              returned = hero1.go_east()
            elif direction == 4:
              returned = hero1.go_west()
          map1.reveal(hero1._loc)
          break
    elif letter == 'n':
      print(prompts['n'])
    elif letter == 's':
      print(prompts['s'])
      hero1._loc = [0,0]
    elif letter == 'i':
      hero1.heal()
      print(prompts['i'])
      map1.remove_at_loc(hero1._loc)
    elif letter == 'o':
      print(prompts['o'])
    elif letter == 'f':
      print()
      print(prompts['f'])
      mapCounter += 1
      if mapCounter == 4:
        mapCounter = 1
      map1 = map.Map()
      map1.load_map(mapCounter)
  print("Game Over")

main()