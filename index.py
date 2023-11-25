name = []
phone_number = []
num = int(input("Enter no of contact you want to save:"))
for i in range(num):
    name = input("Name: ")
    phone_number = input("phone number: ")
    name.append(name)
    phone_number.append(phone_number)
    print("\nName\t\t\tphone Number\n")
    for i in range(num):
        print("{}\t\t\t{}" .format(name[i]. phone_number[i]))
        search_term = input("Enter search term: ")
        print("search result: ")
        if search_term in name:
            index = name.index(search_term)
            phone_number = phone_number;{index}
            print("Names {}, phone Number: {}".format(search_term, phone_number))
        else:print("Name not found")
        