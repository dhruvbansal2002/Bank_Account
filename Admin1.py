import connect.connect1 as cc


class Adminf:
    def validate(self):
        userid=input("Enter userid:")
        passwd=input("Enter password:")
        if userid=="admin" and passwd=="123456":
            return 1
        else:
            return 0
    def create_newaccount(self):
        accno=int(input("Enter new account no:"))
        name=input("Enter name:")
        address=input("Enter address:")
        phno=input("Enter phno:")
        email=input("Enter email:")
        aadhaar=input("Enter aadhaarid")
        password=input("Enter password:")
        amt=int(input("Enter initial amount:"))
        dt=input("Enter date")
        ob=cc.connect2() #create an object of connect2 class
        con=ob.conn()     #call conn() method for connection
        q="insert into cust_info values('%d','%s','%s','%s','%s','%s','%s')"\
           %(accno,name,address,phno,email,aadhaar,password)#to create a query
        stm=con.cursor()#curor() is a predefined method used as carier
                        #between python and mysql
        stm.execute(q) #execute a query
        con.commit()   #save the data into the database

        tid=1
        deposit=amt
        withdrawl=0
        bal=amt
        q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"\
           %(accno,tid,dt,deposit,withdrawl,bal)
        stm.execute(q1)
        con.commit()
        print("Acoount created successfully")
        con.close()#close the connection
        
    def deposit(self):
        accno=int(input("Enter account no:"))
        damt=int(input("Enter deposit amount:"))
        dt=input("Enter date:")
        ob=cc.connect2()
        con=ob.conn()
        q="select tid,bal from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"\
           %(accno,accno)
        stm=con.cursor()
        stm.execute(q)
        '''
        results=
        tid  bal
         1    8000
        '''
        results=stm.fetchall() #fetchAll() is predefined method used to
                               #fetch the data from database and
                               #store it in results variable
        (tid,bal)=(0,0)
        for r in results:
            tid=r[0]
            bal=r[1]
        tid=tid+1
        deposit=damt
        withdrawl=0
        bal=bal+damt

        q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"\
            %(accno,tid,dt,deposit,withdrawl,bal)
        stm.execute(q1)
        con.commit()
        print("Deposited successfully and your bal is",bal)
        con.close()
    def withdrawl(self):
        accno=int(input("Enter account no:"))
        wamt=int(input("Enter withdrawl amount"))
        dt=input("Enter date")
        ob=cc.connect2()
        con=ob.conn()
        q="select tid,bal from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"\
           %(accno,accno)
        stm=con.cursor()
        stm.execute(q)
        '''
        results=
        tid  bal
      r=[ 1    8000]
        '''
        results=stm.fetchall() #fetchAll() is predefined method used to
                               #fetch the data from database and
                               #store it in results variable
        (tid,bal)=(0,0)
        for r in results:
            tid=r[0]
            bal=r[1]
        tid=tid+1
        deposit=0
        if wamt>bal:
            print("Withdrawl not possible")
        else:
            withdrawl=wamt
            bal=bal-wamt
            q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"\
            %(accno,tid,dt,deposit,withdrawl,bal)
            stm.execute(q1)
            con.commit()
            print("Withdrawl successfully and your bal is",bal)
        con.close()
    def balance_check(self):
        accno=int(input("Enter account no"))
        ob=cc.connect2()
        con=ob.conn()
        q="select tid,bal from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"\
           %(accno,accno)
        stm=con.cursor()
        stm.execute(q)
        '''
        results=
        tid  bal
      r=[ 1    8000]
        '''
        results=stm.fetchall() #fetchAll() is predefined method used to
                               #fetch the data from database and
                               #store it in results variable
        (tid,bal)=(0,0)
        for r in results:
            tid=r[0]
            bal=r[1]
        print("Your balance is ",bal)
        con.close()
    def ministmt(self):
        accno=int(input("Enter account no"))
        ob=cc.connect2()
        con=ob.conn()
        q="select * from transaction where accno='%d'"%(accno)
        stm=con.cursor()
        stm.execute(q)
        results=stm.fetchall()
        '''
        accno      tid        dt    deposit    withdrwal   bal
     r=   1              1     4/7    8000        0         8000
        1              2         .. 2000       0        10000
        ....
        
         '''
        for r in results:
            print(r[1],r[2],r[3],r[4],r[5])
        con.close()
    def admin_menu(self):
        t=self.validate()
        if t==0:
            print("Invalid userid or password")
        else:
            while True:
                print("1 for create new account")
                print("2 deposit")
                print("3 withdrawl")
                print("4 check balance")
                print("5 ministatement")
                print("6 for exit")
                ch=int(input("Enter your choice:"))
                if ch==1:
                    self.create_newaccount()
                elif ch==2:
                    self.deposit()
                elif ch==3:
                    self.withdrawl()
                elif ch==4:
                    self.balance_check()
                elif ch==5:
                    self.ministmt()
                elif ch==6:
                    break


