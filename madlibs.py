
#  concatenação de strings (também conhecido como juntar strings)
# suponha que queremos criar uma string que diz "subscribe to _______"
# youtuber = "Eduardo Henrique" # alguma variável string

# algumas maneiras de fazer isso
# print("subscribe to" + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person:")

madlib = f"A programação de computadores é tão {adj}! Isso me deixa tão animado o tempo todo porque \
    Eu amo {verb1}. Mantenha-se hidratado e {verb2} como você é {famous_person}!"

print(madlib)

