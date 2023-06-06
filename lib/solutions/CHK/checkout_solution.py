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


def checkout(skus):
    sku_dict = {}
    total_price = 0
    sku_pattern = r"[A-Z]"

    # Count occurenses of each sku
    for sku in skus:
        sku_exist = re.match(sku_pattern, sku)
        if not sku_exist:
            return -1
        sku_dict[sku] = sku_dict.get(sku, 0) + 1

    # Calculate total price based on prices and special offers
    for sku, quant in sku_dict.items():

        price = prices[sku]["price"]
        special_offer = prices[sku]["special_offer"]

        # Check if there is any special offer applicable
        for offer in special_offer:
            offer_quant = offer.get("quant",0)
            offer_price = offer.get("price",0)
            free_item = offer.get("free_item", None)

            if offer_quant > 0:
                offer_items = quant // offer_quant
                offer_price = offer_items * offer_price
                sku_dict[sku] =
        # if sku == "A":
        #     total_price += (quant // 5) * 200 + ((quant % 5) // 3)*130 + ((quant % 5) % 3) * 50
        # elif sku == "B":
        #     total_price += (quant // 2) * 45 + (quant % 2) * 30
        # elif sku == "C":
        #     total_price += quant * 20
        # elif sku == "D":
        #     total_price += quant * 15
        # elif sku == "E":
        #     total_price += quant * 40
        # elif sku == "F":
        #     total_price += quant * 10


    return total_price



print(checkout("AAAAA"))


