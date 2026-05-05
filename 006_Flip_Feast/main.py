import random

decision_maker = [random.randint(0,1) for i in range(3)]


if decision_maker.count(0) > 1:
    print(f"Opps Sorry🥲! Aj paisy bachao or Ghar ka Khana khao😂")

else:
    print("Wah Wah! Jan chuti 😅 Nikalo Paisa 🤑 or Urao Fast Food pr, Mazy kro😋")