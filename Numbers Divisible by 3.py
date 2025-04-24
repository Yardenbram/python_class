start = int(input("Enter start: "))
end = int(input("Enter end: "))
devisor = int(input("Enter divisor: "))
ln = []
for i in range(start, end + 1):
    if i % devisor == 0:
        print(i, end=" ")
        ln.append(i)
print("/n")
print("The number of elements in the list is: ", len(ln))