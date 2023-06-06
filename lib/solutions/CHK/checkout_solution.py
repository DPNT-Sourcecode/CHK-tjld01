# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    item_dict = {}
    for item in skus:
        if item not in "ABCDE":
            return -1
        item_dict[item] = item_dict.get(item, 0) + 1

    # Reduce Quantity of Free Items
    if item_dict.get("E",0) >= 2 and item_dict.get("B",0) > 0:
        to_reduce = item_dict["E"]//2
        item_dict["B"] = item_dict["B"] - to_reduce if to_reduce <= item_dict["B"] else 0
 
    # Calculate Checkout
    for key, quant in item_dict.items():
        if key == "A":
            sum += (quant // 5) * 200 + ((quant % 5) // 3)*130 + ((quant % 5) % 3) * 50
        elif key == "B":
            sum += (quant // 2) * 45 + (quant % 2) * 30
        elif key == "C":
            sum += quant * 20
        elif key == "D":
            sum += quant * 15
        elif key == "E":
            sum += quant * 40

    return sum



