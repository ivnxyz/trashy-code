def addBorder(picture):
    length = len(picture)
    final_picture = ["*" * (len(picture[0]) + 2)]

    for i, str in enumerate(picture):
        final_picture.append("*" + picture[i] + "*")
    
    final_picture.append("*" * len(final_picture[-1]))
   
    return final_picture


print(addBorder(["a"]))