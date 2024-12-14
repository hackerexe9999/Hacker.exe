# Zaskocz swoich rówieśników!
import random
facts = []
x = int(input("Ile faktów chcesz dodać? : "))
for i in range(x):
    fact = input("Dodaj fakt: ")
    facts.append(fact)
print("twój losowy fakt to: " , random.choice(facts))
