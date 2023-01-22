import mysql.connector as mysql
mydb=mysql.connect(host='localhost',user='root', password='pspy',database='ZOMATO')
query='create table restaurant(
dict={}
def existing_details()
def register():
    for i in dict:
        name=input("Enter your name:")
        uname=input("Enter your username:")
        passwd=input("Enter your password:")
        dict={'Name':name,'User_name':uname,'Password':passwd}
def login():
    uname=input("Enter your username:")
    passwd=input("Enter your login password:")
    if dict['User_name']==uname and dict['Password']==passwd:
        print("______________________________________________WELCOME________________________________________________________")
        def view_profile():
            print("1. for updation")
            print("2. to exit")
            ch=int(input("Enter your choice:"))
            if ch==1:
                update()
            elif ch==2:
                break
        def food_list():
            ##database fetched foodlist
            FID=int(input("Enter the item no."))
            ##IF FID IN THE TABLE FETCH REQUIRED DETAILS OF YOUR FOOD AND PERFORM THE FOLLOWING
            def ch==1:
                ##appending the food item in the database
            def ch==2:
                print("Enter your mode of payment")
                ch=int(input("Enter your choice:"))
                print("1. UPI/PhonPe")
                print("2. Net Banking")
                print("3. App Wallet")
                print("4. Cash on delivery")
            print("1. To add the food item in the cart")
            print("2. To buy the food item")
            print("3. EXIT")
            ch=int(input("Enter your choice:"))
                if ch==1:
                    add_item()
                elif ch==2:
                    buy_item()
                elif ch==3:
                    print("THANY YOU!!PLEASE VISIT AGAIN")
        def cart():
            ##database fetched cart
        def offers():
            ##database fetched offers
        
        print("1. To view profile")
        print("2. To view food_list")
        print("3. To view items in the cart")
        print("4. To view offers available")
        print("5. EXIT")
        ch=int(input("Enter your choice:"))
        if ch==1:
            view_profile()
        elif ch==2:
            view_foodlist()
        elif ch==3:
            view_cart()
        elif ch==4:
            view_offers()
        elif ch==5:
            print("THANK YOU FOR VISITING")
        else:
            break
while True:
    print("1.To fetch existing details")
    print("2.To register new customer details")
    print("3.To log into")
    print("4. Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        existing_details()
    elif ch==2:
        register()
    elif ch==3:
        login()
    elif ch==4:
        print("THANK YOU FOR VISITING")
    else:
        break
