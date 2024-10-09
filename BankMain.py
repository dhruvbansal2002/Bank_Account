import Admin.Admin1 as aa
import user.user1 as uu


print("Welcome to ABCD Bank")
while True:
    print("\n1 for Admin\n2 for customer\n3 for exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        ob=aa.Adminf()
        ob.admin_menu()
    elif ch==2:
        pass
        ob1=uu.user2()
        ob1.user_menu()
    else:
        break

