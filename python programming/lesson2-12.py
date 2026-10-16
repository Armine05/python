print("conditionals")
print("match case")
color=input("enter a RGM color name")
match color:
    case"red":
        print("it s red")
    case "green":
        print("it s green")
    case "blue":
        print("it s blue")
    case _:
        print("its other color")
