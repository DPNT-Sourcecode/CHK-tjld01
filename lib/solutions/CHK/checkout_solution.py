

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    item_dict = {}
    for item in skus:
        if item not in "ABCDE":
            return -1
        if item == "A":
            item_dict["A"] = item_dict.get("A", 0) + 1
        elif item == "B":
            item_dict["B"] = item_dict.get("B", 0) + 1
        elif item == "C":
            item_dict["C"] = item_dict.get("C", 0) + 1
        elif item == "D":
            item_dict["D"] = item_dict.get("D", 0) + 1
        elif item == "E":
            item_dict["E"] = item_dict.get("E", 0) + 1

    for key, quant in item_dict.items():
        if key == "A":
            sum += (quant // 5) * 200 + ((quant % 5) // 3)*130 ((quant % 5) % 3) * 50
        elif key == "B":
            sum += (quant // 2) * 45 + (quant % 2) * 30
        elif key == "C":
            sum += quant * 20
        elif key == "D":
            sum += quant * 15
        elif key == "E":
            sum += quant * 40
            if 

    return sum





