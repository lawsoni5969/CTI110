int1 = int(input())
int2 = int(input())

if int2 < int1:
    print("Second integer can't be less than the first.")

while int1 <= int2:
    print(int1, end=' ')
    int1 = int1 + 5
    if int1 > int2:
        print('')