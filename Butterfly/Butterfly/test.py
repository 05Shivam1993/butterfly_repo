import random
print('---------------------------------')
print('WELCOME TO CRAZY NUMBERS')
print('---------------------------------')
n = int(input('Press 1 to start the game'))
def numbers():
    initialize_value = []
    for i in range(10):
        initialize_value.append(random.randint(1,999))
    return initialize_value
if n == 1:
    player1 = numbers()
    player2 = numbers()
    # print('---------------------------------')
    # print('Tokens for player one ',player1)
    # print('---------------------------------')
    # print('Tokens for player two ',player2)
    # print('---------------------------------')
    toss_input = input(' Choose Head or Tail ').upper()
    print('---------------------------------')
    print('player1 calls for ',toss_input)
    print('---------------------------------')
    list = ['HEAD','TAIL']
    sys_toss = random.choice(list)
    list = ['HEAD','TAIL']
    sys_toss = random.choice(list)
    print('---------------------------------')
    print('Toss Result ',sys_toss)
    print('---------------------------------')
    count = 0
    if toss_input == sys_toss:
        print('---------------------------------')
        print('player1 start the game')
        print('---------------------------------')
        count = 1
    else:
        print('---------------------------------')
        print('player2 start the game')
        print('---------------------------------')
    if count == 1:
        iteration_start = 0
        iteration_end = 19
    else:
        iteration_start = 1
        iteration_end = 20
    player1_index = 0
    player2_index = 0
    player1_points = 0
    player2_points = 0
    player1_chance = 0 #player1[0]
    player2_chance = 0 #player2[0]
    while iteration_start <= iteration_end:
        if iteration_start % 2 == 0:
            n = int(input(' Press 1 Take your turn'))
            if n == 1:
                player1_chance = player1[player1_index]
                print('---------------------------------')
                print('PLAYER1_CHANCE ',player1_chance)
                print('---------------------------------')
                player1_index = player1_index + 1
                if player2_chance in player2:
                    if player1_chance > player2_chance:
                        player1_points = player1_points + 1
                    else:
                        player2_points = player2_points + 1
                    player1_chance = 0
                print('---------------------------------')
                print('PLAYER1_POINTS ',player1_points)
                print('PLAYER2_POINTS ',player2_points)
                print('---------------------------------')
        else:
            player2_chance = player2[player2_index]
            print('---------------------------------')
            print('PLAYER2_CHANCE ',player2_chance)
            print('---------------------------------')
            player2_index = player2_index + 1
            if player1_chance in player1:
                if player1_chance > player2_chance:
                    player1_points = player1_points + 1
                else:
                    player2_points = player2_points + 1
                player2_chance = 0
            print('---------------------------------')
            print('PLAYER1_POINTS ',player1_points)
            print('PLAYER2_POINTS ',player2_points)
            print('---------------------------------')
        iteration_start = iteration_start + 1

    if player1_points == player2_points:
        print('Match Draw')

    if player1_points > player2_points:
        print('---------------------------------')
        print('Player1 Win')
        print('---------------------------------')
    else:
        print('---------------------------------')
        print('Player2 Win')
        print('---------------------------------')
#-----------------------------------------------------------------------------------------------------------------------------
import random
player_1 = 0
player_2 = 0
player_1_val = 0
player_2_val = 0
count_1 = 0
count_2 = 0
dead_cells = [8,18,26,39,51,54,56,60,75,90,85,83,92,97,99]
print('\n')
print('RULES OF THE GAME !')
print('\n')
print('If your current value lies in this range than it will change and become anything but less than your current value, that is snake bitting')
print('\n')
print(dead_cells)
print('\n')
print('If your partner kills you than your current value becomes 0 but you can begin your journey without waiting for 6')
print('\n')
print('To begin your journey, you must got 6 for the first time only')
print('\n')
while player_1 <100 and player_2<100:
    print('\n')
    player_1_value = int(input('player one press 1 to play your turn'))
    print('\n')
    if player_1_value == 1:
        player_1_val = random.randint(1,6)
        print('you got this time ', player_1_val)
        if count_1 == 0:
            if player_1_val == 6:
                print('\n')
                print('Great player one.you got 6, now you can begin your journey.All the best !')
                print('\n')
                count_1 = 1
        if count_1 == 1:
            player_1 = player_1 + player_1_val
            if player_1 in dead_cells:
                print('\n')
                print('Oops player 1, Snake bites you !')
                print('\n')
                player_1 = random.randint(1,player_1-1)
            if player_1 == player_2:
                print('\n')
                print('Oops player 2, player 1 kills you !')
                print('\n')
                player_2 = 0
    print('\n')
    player_2_value = int(input('player two press 2 to play your turn'))
    print('\n')
    if player_2_value == 2:
        player_2_val = random.randint(1,6)
        print('you got this time ', player_2_val)
        if count_2 == 0:
            if player_2_val == 6:
                print('\n')
                print('Great player two.you got 6, now you can begin your journey.All the best !')
                print('\n')
                count_2 = 1
        if count_2 == 1:
            player_2 = player_2 + player_2_val
            if player_2 in dead_cells:
                print('\n')
                print('Oops player 2,Snake bites you !')
                print('\n')
                player_2 = random.randint(1,player_2-1)
            if player_2 == player_1:
                print('\n')
                print('Oops player 1, player 2 kills you !')
                print('\n')
                player_1 = 0
    print('--------------------------------')
    print('player one value',player_1)
    print('\n')
    print('player two value',player_2)
    print('--------------------------------')
if player_1 >= 100:
    print('player 1 win')
    print('\n')
else:
    print('player 2 win')
    print('\n')





{% extends 'ButterflyApp/base.html' %}
{% block childblock %}
<title>General Knowledge</title>
<div class="container">
    <section>
        <div class="page-header" id="faq">
            <center>
                <h2><small style='color:orange; font-family:Serif; font-weight:bold; font-size:25px;'>Enhance Your General Knowledge</small></h2>
            </center>
        </div>
        <!--end page header-->
        <div class="panel-group" id="accordian">
          {% if que_data %}
          {% for que in que_data %}
            <div class="panel panel-default">
                <div class="panel-heading">
                    <div class="panel-title">
                        <a href="#collapse-{{forloop.counter}}" data-toggle="collapse" data-parent="#accordian">
{{que.question}}
</a>
                    </div>
                    <!--end panel title-->
                    <div id="collapse-{{forloop.counter}}" class="panel-collapse collapse ">
                        <div class="panel-body">
                            {{que.answer}}
                        </div>
                    </div>
                    <!--end panel collapse-->
                </div>
            </div>
{% endfor %}
{% endif %}
</div>
    </section>
</div>
</br></br></br></br>
{% endblock %}
