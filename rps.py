import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

img = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
user_choice = int(input("Qual voce escolhe? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura.\n"))

print("Voce escolheu:\n", img[user_choice])
print("Computador escolheu:\n", img[computer_choice])

if user_choice >2 or user_choice <0:
    print("Número inválido, voce perdeu!")
elif computer_choice ==2 and user_choice ==0:
    print("Voce ganhou!.")
elif computer_choice == 0 and user_choice == 2:
    print("Voce perdeu.")
elif computer_choice > user_choice:
    print("Voce perdeu.")
elif user_choice > computer_choice:
    print("Voce ganhou!")
elif computer_choice == user_choice:
    print("Empate.")