y = 0
while True:
    start = input("Enter Starting Pop Size: ")
    if start:
        start = int(start)
        if start < 9:
            print("Minimum Is 9!")
        elif start >= 9:
            end = int(input("Enter Ending Pop Size: "))
            if end < start:
                while end < start:
                    print("Should Be More Than Starting Size!")
                    end = int(input("Enter Ending Pop Size Again!: "))
                while end > start:
                    start += ((start / 3) - (start / 4))
                    y += 1
                while end == start:
                    start += ((start / 3) - (start / 4))
                    y += 0
            elif end > start:
                while end > start:
                    start += ((start / 3) - (start / 4))
                    y += 1
            elif end == start:
                y += 0
            break
    else:
        print("Please enter a valid number!")
print(f"Year: {y}")
