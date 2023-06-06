# noinspection PyUnusedLocal
# skus = unicode string

import re

prices ={
    "A":{
        "price": 50,
        "special_offer":[
            {"quant": 3, "price":130},
            {"quant": 5, "price": 200}
        ]
    },
    "B": {
        "price": 50,
        "special_offer":[
            {"quant": 2, "price":45},
        ]
    },
    "C": {
        "price": 20,
        "special_offer":[]
    },
    "D": {
        "price": 15,
        "special_offer":[]
    },
    "E": {
        "price": 40,
        "special_offer":[
            {"quant": 2, "free_item": "B"}
        ]
    },
    "F": {
        "price": 10,
        "special_offer":[
            {"quant": 2, "free_item": "F"}
        ]
    },
    "G":{
        "price": 20,
        "special_offer":[]
    },
    "H":{
        "price": 10,
        "special_offer":[
            {"quant": 5, "price":45},
            {"quant": 10, "price": 80}
        ]
    },
    "I":{
        "price": 35,
        "special_offer":[]
    },
    "J":{
        "price": 60,
        "special_offer":[]
    },
    "K":{
        "price": 80,
        "special_offer":[
            {"quant": 2, "price":150}
        ]
    },
    "L":{
        "price": 90,
        "special_offer":[]
    },
    "M":{
        "price": 15,
        "special_offer":[]
    },
    "N":{
        "price": 40,
        "special_offer":[
            {"quant": 3, "free_item": "M"}
        ]
    },
    "O":{
        "price": 10,
        "special_offer":[]
    },
    "P":{
        "price": 50,
        "special_offer":[
            {"quant": 5, "price":200}
        ]
    },
    "Q":{
        "price": 30,
        "special_offer":[
            {"quant": 3, "price":80}
        ]
    },
    "R":{
        "price": 50,
        "special_offer":[
            {"quant": 3, "free_item": "Q"}
        ]
    },
    "S":{
        "price": 30,
        "special_offer":[]
    },
    "T":{
        "price": 20,
        "special_offer":[]
    },
    "U":{
        "price": 40,
        "special_offer":[
            {"quant": 3, "free_item": "U"}
        ]
    },
    "V":{
        "price": 50,
        "special_offer":[
            {"quant": 2, "price":90},
            {"quant": 3, "price":130}
        ]
    },
    "W":{
        "price": 20,
        "special_offer":[]
    },
    "X":{
        "price": 90,
        "special_offer":[]
    },
    "Y":{
        "price": 10,
        "special_offer":[]
    },
    "Z":{
        "price": 50,
        "special_offer":[]
    }
}

print(prices)

item_dict = {}
total_price = 0
pattern = r"[A-Z]"
def checkout(skus):
    for item in skus:
        item_exist = re.match(pattern, item)
        if not item_exist:
            return -1
        item_dict[item] = item_dict.get(item, 0) + 1


    # Reduce Quantity of Free Items
    if item_dict.get("E",0) >= 2 and item_dict.get("B",0) > 0:
        to_reduce = item_dict["E"]//2
        item_dict["B"] = item_dict["B"] - to_reduce if to_reduce <= item_dict["B"] else 0
    if item_dict.get("F",0) >= 3:
        to_reduce = item_dict["F"]//3
        item_dict["F"] -= to_reduce

    # Calculate Checkout
    for item, quant in item_dict.items():
        if item == "A":
            sum += (quant // 5) * 200 + ((quant % 5) // 3)*130 + ((quant % 5) % 3) * 50
        elif item == "B":
            sum += (quant // 2) * 45 + (quant % 2) * 30
        elif item == "C":
            sum += quant * 20
        elif item == "D":
            sum += quant * 15
        elif item == "E":
            sum += quant * 40
        elif item == "F":
            sum += quant * 10

    return sum


print(checkout("AAAAA"))







