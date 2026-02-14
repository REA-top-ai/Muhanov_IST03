'''1'''
# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# print(zodiac_elements['fire'])
'''2'''
# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# new_dict = {'energy': ['Not a Zodiac element']}
# zodiac_elements.update(new_dict)
# print(zodiac_elements)
'''3'''
# caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}
# key_to_check = 'matcha'
# try:
#     print(caffeine_level[key_to_check])
# except KeyError:
#     print('Неизвестный уровень кофеина')
'''4'''
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# tc_id = user_ids.get('teraCoder',10000)
# print(tc_id)
# stack_id = user_ids.get('superStackSmash',10000)
# print(stack_id)
'''5'''
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# for users in user_ids.keys():
#     print(users)
# for classes in num_exercises.keys():
#     print(classes)
'''6'''
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# total_exercises = 0
# for exercises in num_exercises.values():
#     total_exercises += exercises
# print(total_exercises)
# print()

'''7'''
# tarot = {1: "The Magician",2: "The High Priestess",3: "The Empress",4: "The Emperor",\
#          5: "The Hierophant",6: "The Lovers",7: "The Chariot",8: "Strength",9: "The Hermit",\
#          10: "Wheel of Fortune",11: "Justice",12: "The Hanged Man",13: "Death",14: "Temperance",\
#          15: "The Devil",16: "The Tower",17: "The Star",18: "The Moon",19: "The Sun",\
#          20: "Judgement",21: "The World",22: "The Fool"}
#
# spread = {}
# spread["past"] = tarot[13]
# spread["present"] = tarot[22]
# spread["future"] = tarot[10]
#
# print(spread)