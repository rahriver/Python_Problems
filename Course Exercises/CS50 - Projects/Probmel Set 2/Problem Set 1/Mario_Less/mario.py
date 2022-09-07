while True:
    height = input("Height: ")
    if height:
        height = int(height)
        if height > 0 and height < 9:
            for i in range(height):
                print(" " * (height - i - 1) + "#" * (i + 1))
            break
    else:
        print("Please enter a number between 1 and 8.")
