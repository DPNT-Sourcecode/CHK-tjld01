

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    item_dict = {}
    for item in skus:
        if item not in "ABCD":
            return -1
        if item == "A":
            item_dict["A"] = item_dict.get("A", 0) + 1
        elif item == "B":
            item_dict["B"] = item_dict.get("B", 0) + 1
        elif item == "C":
            item_dict["C"] = item_dict.get("C", 0) + 1
        elif item == "D":
            item_dict["D"] = item_dict.get("D", 0) + 1

    for key, value in item_dict.items():
        if key == "A":
            sum += (value // 3) * 130 + (value % 3) * 50
        elif key == "B":
            sum += (value // 2) * 45 + (value % 2) * 30
        elif key == "C":
            sum += value * 20
        elif key == "D":
            sum += value * 15

    return sum



