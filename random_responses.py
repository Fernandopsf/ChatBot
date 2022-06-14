import random

def random_string():
    random_list = [
        "Desculpa, não entendi",
        "Desculpa, ainda não consigo fazer isso",
        "Lamento eu queria te ajudar, mas ainda não consigo fazer isso"
               
        ]
    list_count = len(random_list)
    random_item = random.randrange(list_count)
    
    return random_list[random_item]

    
    