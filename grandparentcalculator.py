#Raavi Chowdhury
#RIT

def main():
    print("This program tells you what ancestor you and your nth cousin share")
    cousin = int(input("What is your level of cousin-hood with that person? (ex. 2 for 2nd cousin): "))
    grand = ""

    if cousin == 1:
        print("You share a grandparent.")
        return
    elif cousin > 1:
        grand = "great"
        cousin = cousin - 1
        while cousin > 1:
            grand = grand + " great"
            cousin = cousin - 1
        print("You share a ", grand, "grandparent.")


main()
