# noinspection PyUnusedLocal
# skus = unicode string

import re

prices ={
    "A":{
        "price": 50,
        "special_offer":[
            {"quant": 5, "price": 200},
            {"quant": 3, "price":130}
        ]
    },
    "B": {
        "price": 30,
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
            {"quant": 10, "price": 80},
            {"quant": 5, "price":45}
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
            {"quant": 3, "price":130},
            {"quant": 2, "price":90}
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
    for sku in sku_dict:

        price = prices[sku]["price"]
        special_offer = prices[sku]["special_offer"]

        # Check if there is any special offer applicable
        for offer in special_offer:
            quant = sku_dict[sku]
            offer_quant = offer.get("quant",0)
            offer_price = offer.get("price",0)
            free_item = offer.get("free_item", None)

            if quant >= offer_quant and offer_quant > 0:
                offer_total_price = quant//offer_quant * offer_price
                if offer_total_price > 0:
                    sku_dict[sku] -= offer_quant * (quant//offer_quant)
                    total_price += offer_total_price
                if free_item:
                    free_items = quant // offer_quant
                    diff = sku_dict[free_item] - free_items
                    sku_dict[free_item] = diff if diff > 0 else 0

        total_price += sku_dict[sku] * price

    return total_price



