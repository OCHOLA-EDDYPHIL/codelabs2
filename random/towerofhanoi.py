counter = 0


def tower_of_hanoi(number_of_disks, source, target, spare):
    global counter
    if number_of_disks == 1:
        counter += 1
        print("Move disk 1 from peg", source, "to peg", target, "= Move ", counter)
        return
    else:
        tower_of_hanoi(number_of_disks - 1, source, spare, target)

        counter += 1
        print("Move disk", number_of_disks, "from peg", source, "to peg", target, "= Move ", counter)

        tower_of_hanoi(number_of_disks - 1, spare, target, source)


num_disks = int(input("Enter number of disks: "))
tower_of_hanoi(num_disks, 'A', 'C', 'B')
# print("Total Moves: " ,counter)
