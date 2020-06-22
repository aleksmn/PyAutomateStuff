# Get nice string from input

def sentence_maker(phrase):
    interogatives = ('что','где','когда','как','почему')
    capitalized = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    
print(sentence_maker('доброе утро'))

results = []
while True:
    user_input = input("Напишите что-нибудь: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
