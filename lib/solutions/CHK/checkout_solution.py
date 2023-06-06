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
            {"quant": 3, "free_item": "F"}
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
        "price": 70,
        "special_offer":[
            {"quant": 2, "price":120}
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
        "price": 20,
        "special_offer":{"quant": 3, "price": 45 ,"bundle": "STXYZ"}
    },
    "T":{
        "price": 20,
        "special_offer":{"quant": 3, "price": 45 ,"bundle": "STXYZ"}
    },
    "U":{
        "price": 40,
        "special_offer":[
            {"quant": 4, "free_item": "U"}
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
        "price": 17,
        "special_offer":{"quant": 3, "price": 45 ,"bundle": "STXYZ"}
    },
    "Y":{
        "price": 20,
        "special_offer":{"quant": 3, "price": 45 ,"bundle": "STXYZ"}
    },
    "Z":{
        "price": 21,
        "special_offer":{"quant": 3, "price": 45 ,"bundle": "STXYZ"}
    }
}


def checkout(skus):
    sku_dict = {}
    total_price = 0
    sku_pattern = r"[A-Z]"
    sku_bundles = ["STXYZ"]

    # Count occurenses of each sku
    for sku in skus:
        sku_exist = re.match(sku_pattern, sku)
        if not sku_exist:
            return -1
        sku_dict[sku] = sku_dict.get(sku, 0) + 1

    # Check offers for free items and reduce list
    for sku in sku_dict:

        price = prices[sku]["price"]
        special_offer = prices[sku]["special_offer"]

        for offer in special_offer:
            quant = sku_dict[sku]
            print(sku_dict)
            offer_quant = offer.get("quant",0)
            sku_free_item = offer.get("free_item", None)

            if quant >= offer_quant and "free_item" in offer:
                free_items = quant // offer_quant
                diff = sku_dict.get(sku_free_item,0) - free_items
                free_items_to_substract = free_items if diff >= 0 else 0
                if free_items_to_substract > 0:
                    sku_dict[sku_free_item] -= free_items_to_substract


    for sku_bundle in sku_bundles:
        bundle_dict = {}
        for sku in sku_bundle:
            bundle_dict[sku] = {
                "quant": sku_dict.get(sku,0),
                "price": prices[sku]["price"]
            }
        sorted_bundle_dict = sorted(bundle_dict.items(), key=lambda x: x[1]["quant"], reverse=True)
        print(sorted_bundle_dict)


    # Calculate total price for each sku considering offers
    for sku in sku_dict:
        price = prices[sku]["price"]
        special_offer = prices[sku]["special_offer"]

        # Check if there is any special offer applicable
        for offer in special_offer:
            quant = sku_dict[sku]
            offer_quant = offer.get("quant",0)
            offer_price = offer.get("price",0)

            if quant >= offer_quant and offer_quant > 0:
                offer_total_price = quant//offer_quant * offer_price
                if offer_total_price > 0:
                    sku_dict[sku] -= offer_quant * (quant//offer_quant)
                    total_price += offer_total_price
        total_price += sku_dict[sku] * price

    return total_price

print(checkout("STXYZ"))






