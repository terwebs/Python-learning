from random import choice

nouns = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla"
]

verbs = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles"
]

adjetives = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening"
]

prepositions = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within"
]

adverbs = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously"
]
vowels = "aeiou"

noun1 = choice(nouns)
noun2 = choice(nouns)
noun3 = choice(nouns)

while noun1 == noun2:
    noun2 = choice(nouns)
while noun1 == noun3 or noun2 == noun3:
    noun3 = choice(nouns)

verb1 = choice(verbs)
verb2 = choice(verbs)
verb3 = choice(verbs)

while verb1 == verb2:
    verb2 = choice(verbs)
while verb1 == verb3 or verb2 == verb3:
    verb3 = choice(verbs)
        
adjetive1 = choice(adjetives)
adjetive2 = choice(adjetives)
adjetive3 = choice(adjetives)

while adjetive1 == adjetive2:
    adjetive2 = choice(verbs)
    
while adjetive1 == verb3 or adjetive2 == adjetive3:
    adjetive3 = choice(adjetives)

preposition1 = choice(prepositions)
preposition2 = choice(prepositions)

while preposition1 == preposition2:
    preposition2 = choice(prepositions)

adverb1 = choice(adverbs)

if vowels.find(adjetive1[0]) != -1:
    article = "An"
else:
    article = "A"

print "{} {} {}.".format(article, adjetive1, noun1)
print " "
print "{} {} {} {} {} the {} {}".format(article, adjetive1, noun1, verb1, preposition1, adjetive2, noun2)
print "{}, the {} {}".format(adverb1, noun1, verb2)
print "the {} {} {} a {} {}".format(noun2, verb3, preposition2, adjetive3, noun3)










