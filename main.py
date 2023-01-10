from functions import *

global connect
connect = create_connection()
create_tables(connect)
#add_courier_boys_data(connect)

order_id = ''
for i in range(2):
    order_id += choice(alphabets).upper()
for i in range(2):
    order_id += str(randrange(0,10))

#__main__
print("Welcome to QUICK SHIP EXPRESS")
user_choice = input("Press Enter to begin your Courier Journey : ")
time.sleep(1)
print("(1) Type 1 for Customer")
print("(2) Type 2 for Company Head")
print("(3) Type 3 for Delivery Boy")
print('\n')
user_choice = int(input("Enter your user_choice : "))
if user_choice == 1:
    time.sleep(1)
    voice = input("Are you a new customer? : ").lower()
    for i in range(1):
        if voice == 'yes':
            print("You need to create an account first")
            time.sleep(1)
            choose = input("Wanna create an account? : ").lower()
            if choose == 'yes':
                data = signup(connect)
                user_id = data[0]
                username = data[1]
                password = data[2]
                print(existing_user_id(connect, username), "IS YOUR USER ID")
                print("What do you want to do? : ")
                while True:
                    print("(1) Add a package to be delivered")
                    print("(2) Get Details of my package")
                    print("(3) View all my packages")
                    print("(4) Update my package information")
                    print("(5) Cancel my package")
                    print("(6) Settings")
                    print("(7) Exit the Program")
                    choose = int(input("Press from (1,2,3,4,5,6,7) to continue : "))
                    if choose == 1:
                        global package
                        package = []
                        sender = username
                        receipient = input("Please enter who you want to send : ")
                        address = input("Where to send the package : ")
                        weight = input("Enter weight of the package : ")
                        date = input("Enter till when to send the package(YYYY-MM-DD) : ")
                        status = "NOT DELIVERED YET"
                        delivery_boy_id = "YOUR PACKAGE IS SEARCHING THE BEST DELIVERY BOY FOR HIM"
                        print('\n')
                        print(order_id, "is your Package_ID to access your details of the package")
                        print("Please remember if for future purposes")
                        print('\n')
                        package.append(order_id)
                        package.append(sender)
                        package.append(receipient)
                        package.append(address)
                        package.append(weight)
                        package.append(date)
                        package.append(status)
                        package.append(delivery_boy_id)
                        package = tuple(package)
                        customer_add_package(connect, package)
                    elif choose == 2:
                        package_id = input("Enter your package id which was provided : ")
                        print("This is your order details")
                        print(customer_get_package(connect, package_id))
                    elif choose == 3:
                        print("Here are all of your packages")
                        print(customer_get_all_package)
                    elif choose == 4:
                        package_id = input("Enter the Package Id of the order of which details need to be changed : ")
                        package = list(customer_get_package(connect, package_id))
                        print("(1) Change the Receiver's Name")
                        print("(2) Change the address to be delivered")
                        print("(3) Change the weight of the package")
                        print("(4) Change the date of the package to be sent")
                        user_choice = int(input("Enter what do you change (1,2,3)? : "))
                        package = list(package)
                        if user_choice == 1:
                            receipient = input("Please add new receiver's name : ")
                            package[2] = receipient
                            package = tuple(package)
                            customer_update_package(connect, package)
                        elif user_choice == 2:
                            address = input("Please add the new address to be delivered : ")
                            package[3] = address
                            package = tuple(package)
                            customer_update_package(connect, package)
                        elif user_choice == 3:
                            weight = input("Please enter the new weight of the package : ")
                            package[4] = weight
                            package = tuple(package)
                            customer_update_package(connect, package)
                        elif user_choice == 4:
                            date = input("Please enter the new date to send the package : ")
                            package[5] = date
                            package = tuple(package)
                            customer_update_package(connect, package)
                        else:
                            break
                    elif choose == 5:
                        package_id = input("Enter the Package Id of the order of which details need to be changed : ")
                        customer_delete_package(connect, package_id)
                        print('\n')
                        print("Your package delivery has been cancelled")
                    elif choose == 6:
                        print("You need Log-In everytime whenever you use the settings.\nThis is order to ensure the security of the data of our customers")
                        customer = login(connect)
                        id = customer[0]
                        username = customer[1]
                        password = customer[2]
                        print(customer)
                        print("(1) View my data")
                        print("(2) View my User ID")
                        print("(3) Generate me a new User ID")
                        print("(3) Change my password")
                        print("(4) Delete my account")
                        user_choice = int(input("What do you want to do(1,2,3) : "))
                        if user_choice == 1:
                            customer_id = input("Enter your Customer-ID : ")
                            print(get_customer(connect, customer_id))
                        elif user_choice == 2:
                            print(existing_user_id(connect, username), "IS YOUR USER ID")
                        elif user_choice == 3:
                            ask = input("Enter your User Name to change your User ID : ")
                            a = new_user_id()
                            update_user_id(connect, a, ask)
                            print(a,"is your new User-ID")
                            print("Your new User Id has been gener")
                        elif user_choice == 4:
                            new_password = input("Enter your new password : ")
                            update_customer(connect, new_password, username)
                            print(new_password,"is your new Password")
                            print("Your password has been changed")
                        elif user_choice == 5:
                            ask = input("Are you sure you want to delete your account? : ").lower()
                            if ask == 'yes':
                                delete_customer(connect, id)
                                print("Your account has been deleted")
                                break
                            else:
                                print("Your account was not deleted")
                        else:
                            break
                    elif choose == 7:
                        print("Thank you for using our service")
                        break
                    else:
                        break
            else:
                print("You denied the request")
                break

        if voice == 'no':
            print("Login in to your account")
            data = login(connect)
            user_id = data[0]
            username = data[1]
            password = data[2]
            print(existing_user_id(connect, username), "IS YOUR USER ID")
            print("What do you want to do? : ")
            while True:
                print("(1) Add a package to be delivered")
                print("(2) Get Details of my package")
                print("(3) View all my packages")
                print("(4) Update my package information")
                print("(5) Cancel my package")
                print("(6) Settings")
                print("(7) Exit the Program")
                choose = int(input("Press from (1,2,3,4,5,6) to continue : "))
                if choose == 1:
                    package = []
                    sender = username
                    receipient = input("Please enter who you want to send : ")
                    address = input("Where to send the package : ")
                    weight = input("Enter weight of the package : ")
                    date = input("Enter till when to send the package(YYYY-MM-DD) : ")
                    status = "NOT DELIVERED YET"
                    delivery_boy_id = "YOUR PACKAGE IS SEARCHING THE BEST DELIVERY BOY FOR HIM"
                    print('\n')
                    print(order_id, "is your Package_ID to access your details of the package")
                    print("Please remember if for future purposes")
                    package.append(order_id)
                    package.append(sender)
                    package.append(receipient)
                    package.append(address)
                    package.append(weight)
                    package.append(date)
                    package.append(status)
                    package.append(delivery_boy_id)
                    package = tuple(package)
                    print(package)
                    customer_add_package(connect, package)
                elif choose == 2:
                    package_id = input("Enter your package id which was provided : ")
                    print("This is your order details")
                    print(customer_get_package(connect, package_id))
                elif choose == 3:
                    print("Here are all of your packages")
                    print(customer_get_all_package)
                elif choose == 4:
                    package_id = input("Enter the Package Id of the order of which details need to be changed : ")
                    package = list(customer_get_package(connect, package_id))
                    print("(1) Change the Receiver's Name")
                    print("(2) Change the address to be delivered")
                    print("(3) Change the weight of the package")
                    print("(4) Change the date of the package to be sent")
                    user_choice = int(input("Enter what do you change (1,2,3)? : "))
                    package = list(package)
                    if user_choice == 1:
                        receipient = input("Please add new receiver's name : ")
                        package[2] = receipient
                        package = tuple(package)
                        customer_update_package(connect, package)
                    elif user_choice == 2:
                        address = input("Please add the new address to be delivered : ")
                        package[3] = address
                        package = tuple(package)
                        customer_update_package(connect, package)
                    elif user_choice == 3:
                        weight = input("Please enter the new weight of the package : ")
                        package[4] = weight
                        package = tuple(package)
                        customer_update_package(connect, package)
                    elif user_choice == 4:
                        date = input("Please enter the new date to send the package : ")
                        package[5] = date
                        package = tuple(package)
                        customer_update_package(connect, package)
                    else:
                        break
                elif choose == 5:
                    package_id = input("Enter the Package Id of the order of which details need to be changed : ")
                    customer_delete_package(connect, package_id)
                    print('\n')
                    print("Your package delivery has been cancelled")
                elif choose == 6:
                    print("You need Log-In everytime whenever you use the settings.\nThis is order to ensure the security of the data of our customers")
                    customer = login(connect)
                    id = customer[0]
                    username = customer[1]
                    password = customer[2]
                    print(customer)
                    print("(1) View my data")
                    print("(2) View my User ID")
                    print("(3) Generate me a new User ID")
                    print("(3) Change my password")
                    print("(4) Delete my account")
                    user_choice = int(input("What do you want to do(1,2,3) : "))
                    if user_choice == 1:
                        customer_id = input("Enter your Customer-ID : ")
                        print(get_customer(connect, customer_id))
                    elif user_choice == 2:
                        print(existing_user_id(connect, username), "IS YOUR USER ID")
                    elif user_choice == 3:
                        ask = input("Enter your User Name to change your User ID : ")
                        a = new_user_id()
                        update_user_id(connect, a, ask)
                        print(a,"is your new User-ID")
                        print("Your new User Id has been generated")
                    elif user_choice == 4:
                        new_password = input("Enter your new password : ")
                        update_customer(connect, new_password, username)
                        print(new_password,"is your new password")
                        print("Your password has been changed")
                    elif user_choice == 5:
                        delete_customer(connect, id)
                        print("Your account has been deleted")
                        break
                    else:
                        break
                elif choose == 7:
                    print("Thank you for using our service")
                    break
                else:
                    break
        else:
            print("You denied the request")
            break

elif user_choice == 2:
    ask = input("Verify by providing your Company ID : ")
    if ask == "AB123":
        print("You are verified")
        print("Login to your account via the Company's Email and Password")
        select = company_login()
        while True:
            if select == "none":
                break
            else:
                print("(1) View all current orders which are not delivered yet")
                print("(2) Display all delivery ID's")
                print("(3) Update the status of a specific delivery")
                print("(4) Get the data of a specific package")
                print("(5) Assign delivery to delivery boys")
                print("(6) Delete all deliveries who are delivered")
                print("(7) Exit the system")
                user_choice = int(input("Enter your choice (1,2,3,4,5,6) : "))
                if user_choice == 1:
                    print(display_all_data(connect))
                elif user_choice == 2:
                    print(display_id(connect))
                elif user_choice == 3:
                    order_id = input("Enter the Package_Id you want to change the delivery status : ")
                    update_status(connect, order_id)    
                elif user_choice == 4:
                    order_id = input("Enter the Package_Id to view : ")
                    print(display_one_data(connect, order_id))
                elif user_choice == 5:
                    order_id = input("Enter the Order-ID to assign a delivery boy : ")
                    courier_boy_id = input("Enter the User-Id of the courier boy to assign him a courier : ")
                    assign_boy_to_courier(connect, order_id, courier_boy_id )
                elif user_choice == 6:
                    company_delete_package(connect)
                elif user_choice == 7:
                    print("Leaving the moderation side of the program...")
                    break
elif user_choice == 3:
    user_name = input("Enter your name : ").lower()
    userid = input("Enter your User-ID")
    courier_boy_login(connect, userid, user_name)
    while True:
        print("What do you want to access : ")
        print("(1) To view orders assigned to you")
        print("(2) Exit the program")
        choose = int(input("Enter your choice : "))
        if choose == 1:
            print("Here is your list of packages to complete")
            courier_boy_packages(connect, userid)
        else:
            print("Logging out of the system...")
            break
        
