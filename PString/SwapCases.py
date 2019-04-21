def SwapCases(str):
    swapped = ""
    for ch in str:
        if ch.islower():
            swapped+=ch.upper()
        elif ch.isupper():
            swapped+=ch.lower()
        else:
            swapped+=ch

    return swapped;


if __name__ == "__main__" :
    input = input("Enter something : ")
    swapped = SwapCases(input)
    print(swapped)
