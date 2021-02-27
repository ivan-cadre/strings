# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goalscorer_one = 'Gullit'
goalscorer_two = 'Van Basten'
goal_0 = 32
goal_1 = 54
scorers = goalscorer_one + " " + str(goal_0), goalscorer_two + " " + str(goal_1)
report = f'{goalscorer_one} scored in the {goal_0}th minute,\n{goalscorer_one} scored in the {goal_1}th minute'
print(report)
player = 'Dimovski Protasov'
first_name = player[:player.find(' ')]
print(first_name)
last_name_len = len(player[(player.find(' ')+1):])
print(last_name_len)
name_short = f'{first_name[0]}. {player[9:]}'
print(name_short)
chant = f'{first_name}! '*len(first_name)
chant = chant[:-1]
print(chant)
good_chant = chant[-1] != ' '
print(good_chant)