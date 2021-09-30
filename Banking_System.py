import mysql.connector as sql_con
import random
import time
import datetime
import csv
from datetime import date

connection = sql_con.connect(host='localhost', user='root', password='coder_player', db='RBI_db')
mycursor =  connection.cursor()

if connection.is_connected():
    print('''
     ###               ###    ######     ###                    #######          #######      ##########         ######
     ###               ###  #######    ###                  #########    #########  ############    ########
     ###               ###  ##                 ###                  ##             ##    ##               ##  ###     ##    ###    ##
     ###     ##    ###  #####          ###                  ##                      ##               ##  ###     ##     ###   #####
     ###     ##    ###  #####          ###                  ##                      ##               ##  ###     ##     ###   #####
     ###     ##    ###  ##                  ###          ##  ##            ##     ##               ##  ###                ###   ##
     ###########  ########   #########  #########     #########   ###                ###   ########
      ##########      ######       ########     #######            #######     ###                 ###    ######
       ''')
    time.sleep(1)
    print("RBI online banking service\n")
    time.sleep(0.5)
    print(''' This program is created by :-
     ''')
    time.sleep(0.33)
    print('1.Maheep Gupta')
    time.sleep(0.33)
    print('2.Amartya Pratap Singh')
    time.sleep(0.33)
    print('3.Parth Srivastava')
    time.sleep(0.33)
    print('4.Avinash pandey')
    time.sleep(0.33)
    print('5.Rishabh Sharma')
    time.sleep(0.5)
    global t
    t=0
    global ac_num
    global security_code

    # User Working place
    def user_thing():
        #Money Deposit/Withdraw
        def Trasaction( ):
            def trans_ch( ):
                ch = int(input(''' What do tou want to do
                                    1.Money Deposit 
                                    2.Money Withdraw
                                    Enter your Choice:-'''))

                def choice_verification( ):
                    if ch == 1:
                        def Money_deposit( ):
                            global Sr_no, original_avail, str_avail, str_avail_th
                            Amount = int(input("Enter the Amount you want to Deposit :- Rs."))
                            recived_from = 'Self Online Payment'
                            paid_to = "----"
                            deducted = '--'
                            date = datetime.date.today()
                            # A dummy text file to count Sr_no
                            D_write = ac_num + '\n'
                            D_file = open(r"Dummy_trans.txt", "a")
                            D_file.write(D_write)
                            D_file.close()
                            D_file = open(r"Dummy_trans.txt", "r")
                            D_read = D_file.readlines()
                            for x in range(0, len(D_read)):
                                Sr_no = x + 1
                            f_ex = 'select Avail_balance from account_details where Account_number=%s '
                            mycursor.execute(f_ex, (ac_num,))
                            avail_value = mycursor.fetchall()
                            for value_avail in avail_value:
                                global str_avail
                                str_avail = ((str(value_avail).strip('()')).strip(' , ')).strip("  ' ' ")
                            original_avail = int(str_avail)
                            values = (
                                Sr_no, date, datetime.datetime.now(), ac_num, adhaar_no, paid_to, recived_from,
                                (str(original_avail)),
                                deducted, str(Amount), str(original_avail + Amount))
                            am_ex = 'insert into transacation_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            mycursor.execute(am_ex, values)
                            print("Your Amount added Sucessfully, ")
                            theek = 'select Avail_balance from transacation_details where Account_number=%s '
                            mycursor.execute(theek, (ac_num,))
                            avail_value_th = mycursor.fetchall()
                            for value_avail_th in avail_value_th:
                                str_avail_th = ((str(value_avail_th).strip('()')).strip(' , ')).strip("  ' ' ")
                                time.sleep(0.25)
                            print(" Avail Balance:-", str_avail_th)

                        Money_deposit()
                    elif ch == 2:
                        def Money_withdraw( ):
                            global Sr_no, original_avail, str_avail, str_avail_th, str_avail_th_w
                            Amount = int(input("Enter the Amount you want to Withdraw :- Rs."))
                            recived_from = '---'
                            paid_to = "To Self"
                            credited = '--'
                            date = datetime.date.today()
                            # A dummy text file to count Sr_no
                            D_write = ac_num + '\n'
                            D_file = open(r"Dummy_trans_w.txt", "a")
                            D_file.write(D_write)
                            D_file.close()
                            D_file = open(r"Dummy_trans_w.txt", "r")
                            D_read = D_file.readlines()
                            for x in range(0, len(D_read)):
                                Sr_no = x + 1
                            f_ex = 'select Avail_balance from account_details where Account_number=%s '
                            mycursor.execute(f_ex, (ac_num,))
                            avail_value = mycursor.fetchall()
                            for value_avail in avail_value:
                                str_avail = ((str(value_avail).strip('()')).strip(' , ')).strip("  ' ' ")
                                original_avail = int(str_avail)
                            values = (
                                Sr_no, date, datetime.datetime.now(), ac_num, adhaar_no, paid_to, recived_from,
                                str_avail, str(Amount), credited, str(original_avail - Amount))
                            am_w_ex = 'insert into transacation_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            mycursor.execute(am_w_ex, values)
                            print("Your Amount Debited  Sucessfully, ")
                            theek_w = 'select Avail_balance from transacation_details where Account_number=%s '
                            mycursor.execute(theek_w, (ac_num,))
                            avail_value_th_w = mycursor.fetchall()
                            for value_avail_th_w in avail_value_th_w:
                                str_avail_th_w = ((str(value_avail_th_w).strip('()')).strip(' , ')).strip("  ' ' ")
                                time.sleep(0.25)
                            print(" Avail Balance:-", str_avail_th_w)

                        Money_withdraw()
                    else:
                        choice_verification()

                choice_verification()

            def online_bank( ):
                ch = input('''Did you use online banking (y/n) for Yes and No -> ''')
                if ch == 'y' or ch == 'Y':
                    def User_user( ):
                        global t
                        t = t + 1
                        global username
                        username = input(" Username:- ")
                        global ac_num
                        ac_num = input("Enter your account number:-")
                        global adhaar_no
                        adhaar_no = input("Enter your Adhaar_number:-")
                        Users_show = 'select Username from account_details '
                        mycursor.execute(Users_show)
                        u_data = mycursor.fetchall()
                        count = mycursor.rowcount
                        lst_u = [ ]
                        for row in u_data:
                            str_user = ((str(row).strip('()')).strip(' , ')).strip("  ' ' ")
                            if str_user == username:
                                lst_u.append(str_user)
                        if username in lst_u:
                            def User_pass( ):
                                global t
                                t = t + 1
                                password = input(" Password:- ")
                                Users_pass = 'select Pass_word from account_details '
                                mycursor.execute(Users_pass)
                                p_data = mycursor.fetchall()
                                lst = [ ]
                                for prow in p_data:
                                    str_pass = ((str(prow).strip('()')).strip(' , ')).strip("  ' ' ")
                                    if str_pass == password:
                                        lst.append(str_pass)
                                if password in lst:
                                    print("Access Granted ")
                                    admin_file = open(r'Account_logins.csv ', 'a')
                                    cwriter = csv.writer(admin_file)
                                    login_time = datetime.datetime.now()
                                    login_data = [
                                        [ 'Username', 'Time of login' ],
                                        [ username, login_time ] ]
                                    cwriter.writerows(login_data)
                                    admin_file.close()
                                    trans_ch()
                                else:
                                    while t <= 3:
                                        # sir se poochna hai
                                        print(" Wrong password")
                                        User_pass()

                            User_pass()
                        else:
                            while t <= 3:
                                print(" The username you entered is not in our db plz retry")
                                User_user()

                    User_user()
                elif ch == 'n' or ch == 'N':
                    def adhaar( ):
                        global adhaar_no
                        adhaar_no = input(" Adhaar_no:- ")
                        global ac_num
                        ac_num = input("Enter your account number:-")
                        Users_show = 'select Adhaar_Number from account_details'
                        mycursor.execute(Users_show)
                        u_data = mycursor.fetchall()
                        count = mycursor.rowcount
                        lst_ad = [ ]
                        for row in u_data:
                            str_user = ((str(row).strip('()')).strip(' , ')).strip("  ' ' ")
                            if str_user == adhaar_no:
                                lst_ad.append(str_user)
                        if adhaar_no in lst_ad:
                            def User_sec( ):
                                security_code = input(" Security Code:- ")
                                Users_sec = 'select Security_Code from account_details'
                                mycursor.execute(Users_sec)
                                p_data = mycursor.fetchall()
                                lst_sec = [ ]
                                for prow in p_data:
                                    str_pass = ((str(prow).strip('()')).strip(' , ')).strip("  ' ' ")
                                    if str_pass == security_code:
                                        lst_sec.append(str_pass)
                                if security_code in lst_sec:
                                    print("Access Granted ")
                                    admin_file = open(r'account2_logins.csv ', 'a')
                                    cwriter = csv.writer(admin_file)
                                    login_time = datetime.datetime.now()
                                    login_data = [
                                        [ 'Adhaar_no', 'Time of login' ],
                                        [ adhaar_no, login_time ] ]
                                    cwriter.writerows(login_data)
                                    admin_file.close()
                                    trans_ch()
                                else:
                                    while t <= 3:
                                        print(" Wrong password")
                                        User_sec()

                            User_sec()
                        else:
                            while t <= 3:
                                print(" The adhaar_no you entered is not in our db plz retry")
                                adhaar()

                    adhaar()
                else:
                    online_bank()

            online_bank()

        # Account details
        def Account_Details( ):
            print("For security reason we request you to login again from here --->")
            time.sleep(0.5)

            def activity_records_ad( ):
                # getting fetched account details
                ac_ex = 'select account_number from account_details where adhaar_number=%s'
                mycursor.execute(ac_ex, (adhaar_no,))
                ac_val = mycursor.fetchall()
                for Ac_value in ac_val:
                    str_Ac = ((str(Ac_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    time.sleep(0.25)
                    print("Account Number:  ", str_Ac)
                # getting fetched holder name
                holder_ex = 'select account_holder_name from account_details where adhaar_number=%s'
                mycursor.execute(holder_ex, (adhaar_no,))
                holder_val = mycursor.fetchall()
                for Holder_value in holder_val:
                    str_holder = ((str(Holder_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    print("Account Holder Name:  ", str_holder)
                # getting fetched Father's name
                f_name_ex = 'select Account_Holder_Father_name from account_details where adhaar_number=%s'
                mycursor.execute(f_name_ex, (adhaar_no,))
                f_name_val = mycursor.fetchall()
                for F_name_value in f_name_val:
                    str_Ac_f = ((str(F_name_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    time.sleep(0.25)
                    print("Account Holder's Father name:  ", str_Ac_f)
                # getting fetched Mother's name
                m_name_ex = 'select Account_Holder_Mother_name from account_details where adhaar_number=%s'
                mycursor.execute(m_name_ex, (adhaar_no,))
                m_name_val = mycursor.fetchall()
                for M_name_value in m_name_val:
                    str_Ac_M = ((str(M_name_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    time.sleep(0.25)
                    print("Account Holder's Mother name:  ", str_Ac_M)
                # getting fetched Date of birth
                dob_ex = 'select Date_of_Birth from account_details where adhaar_number=%s'
                mycursor.execute(dob_ex, (adhaar_no,))
                dob_val = mycursor.fetchall()
                for Dob_value in dob_val:
                    str_Ac_U = (((str(Dob_value).strip('()')).strip(' , ')).strip("  ' ' ").strip("datetime.date"))
                    time.sleep(0.25)
                    print("Date of Birth:  ", str_Ac_U)
                # Adhaaar number
                print("Adhaar number:  ", adhaar_no)
                # getting fetched Username
                u_name_ex = 'select username from account_details where adhaar_number=%s'
                mycursor.execute(u_name_ex, (adhaar_no,))
                u_name_val = mycursor.fetchall()
                for U_name_value in u_name_val:
                    str_Ac_U = ((str(U_name_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    time.sleep(0.25)
                    print("Account  Username:  ", str_Ac_U)
                # getting fetched Available Balance
                balance_ex = 'select avail_balance from transacation_details where adhaar_number=%s'
                mycursor.execute(balance_ex, (adhaar_no,))
                balance_val = mycursor.fetchall()
                for Balance_value in balance_val:
                    str_Ac_Bal = ((str(Balance_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    time.sleep(0.25)
                    print("Current Account Balance:  ", str_Ac_Bal)

            def activity_records_user( ):
                # getting fetched account details
                ac_ex = 'select account_number from account_details where Account_number=%s'
                mycursor.execute(ac_ex, (Account_number,))
                ac_val = mycursor.fetchall()
                for Ac_value in ac_val:
                    str_Ac = ((str(Ac_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    time.sleep(0.25)
                    print("Account Number:  ", str_Ac)
                # getting fetched holder name
                holder_ex = 'select account_holder_name from account_details where Account_number=%s'
                mycursor.execute(holder_ex, (Account_number,))
                holder_val = mycursor.fetchall()
                for Holder_value in holder_val:
                    str_holder = ((str(Holder_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    print("Account Holder Name:  ", str_holder)
                # getting fetched Father's name
                f_name_ex = 'select Account_Holder_Father_name from account_details where Account_number=%s'
                mycursor.execute(f_name_ex, (Account_number,))
                f_name_val = mycursor.fetchall()
                for F_name_value in f_name_val:
                    str_Ac_f = ((str(F_name_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    time.sleep(0.25)
                    print("Account Holder's Father name:  ", str_Ac_f)
                # getting fetched Mother's name
                m_name_ex = 'select Account_Holder_Mother_name from account_details where Account_number=%s'
                mycursor.execute(m_name_ex, (Account_number,))
                m_name_val = mycursor.fetchall()
                for M_name_value in m_name_val:
                    str_Ac_M = ((str(M_name_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    time.sleep(0.25)
                    print("Account Holder's Mother name:  ", str_Ac_M)
                # getting fetched Username
                dob_ex = 'select Date_of_Birth from account_details where Account_number=%s'
                mycursor.execute(dob_ex, (Account_number,))
                dob_val = mycursor.fetchall()
                for Dob_value in dob_val:
                    str_Ac_U = (((str(Dob_value).strip('()')).strip(' , ')).strip("  ' ' ").strip("datetime.date"))
                    time.sleep(0.25)
                    print("Date of Birth:  ", str_Ac_U)
                # getting fetched Adhaar number
                adhaar_ex = 'select adhaar_number from account_details where Account_number=%s'
                mycursor.execute(adhaar_ex, (Account_number,))
                adhaar_val = mycursor.fetchall()
                for Adhaar_value in adhaar_val:
                    str_Ac_ad = (((str(Adhaar_value).strip('()')).strip(' , ')).strip("  ' ' ").strip("datetime.date"))
                    time.sleep(0.25)
                    print("Date of Birth:  ", str_Ac_ad)
                    # getting fetched Username
                    username_ex = 'select username from account_details where Account_number=%s'
                    mycursor.execute(username_ex, (Account_number,))
                    username_val = mycursor.fetchall()
                    for Username_value in username_val:
                        str_Ac_user = (
                            ((str(Username_value).strip('()')).strip(' , ')).strip("  ' ' ").strip("datetime.date"))
                        time.sleep(0.25)
                    print("Account  Username:  ", str_Ac_user)

            def online_bank( ):
                ch = input('''Did you use online banking (y/n) for Yes and No -> ''')
                if ch == 'y' or ch == 'Y':
                    def User_user( ):
                        global t
                        t = t + 1
                        global username
                        username = input(" Username:- ")
                        global Account_number
                        Account_number=input("Enter your Account number:-")
                        Users_show = 'select Username from account_details '
                        mycursor.execute(Users_show)
                        u_data = mycursor.fetchall()
                        count = mycursor.rowcount
                        lst_u = [ ]
                        for row in u_data:
                            str_user = ((str(row).strip('()')).strip(' , ')).strip("  ' ' ")
                            if str_user == username:
                                lst_u.append(str_user)
                        if username in lst_u:
                            def User_pass( ):
                                global t
                                t = t + 1
                                password = input(" Password:- ")
                                Users_pass = 'select Pass_word from account_details '
                                mycursor.execute(Users_pass)
                                p_data = mycursor.fetchall()
                                lst = [ ]
                                for prow in p_data:
                                    str_pass = ((str(prow).strip('()')).strip(' , ')).strip("  ' ' ")
                                    if str_pass == password:
                                        lst.append(str_pass)
                                    print(lst)
                                if password in lst:
                                    print("Your details:- ")
                                    activity_records_user()
                                    admin_file = open(r'Account_Activity.csv ', 'a')
                                    cwriter = csv.writer(admin_file)
                                    login_time = datetime.datetime.now()
                                    login_data = [
                                        [ 'Username', 'Time of login' ],
                                        [ username, login_time ] ]
                                    cwriter.writerows(login_data)
                                    admin_file.close()

                                else:
                                    while t <= 3:
                                        # sir se poochna hai
                                        print(" Wrong password")
                                        User_pass()
                            User_pass()
                        else:
                            while t <= 3:
                                print(" The username you entered is not in our db plz retry")
                                User_user()

                    User_user()
                elif ch == 'n' or ch == 'N':
                    def adhaar( ):
                        global adhaar_no
                        adhaar_no = input(" Adhaar_no:- ")
                        Users_show = 'select Adhaar_Number from account_details'
                        mycursor.execute(Users_show)
                        u_data = mycursor.fetchall()
                        count = mycursor.rowcount
                        lst_ad = [ ]
                        for row in u_data:
                            str_user = ((str(row).strip('()')).strip(' , ')).strip("  ' ' ")
                            if str_user == adhaar_no:
                                lst_ad.append(str_user)
                        if adhaar_no in lst_ad:
                            time.sleep(0.25)

                            def User_sec( ):
                                security_code = input(" Security Code:- ")
                                Users_sec = 'select Security_Code from account_details'
                                mycursor.execute(Users_sec)
                                p_data = mycursor.fetchall()
                                lst_sec = [ ]
                                for prow in p_data:
                                    str_pass = ((str(prow).strip('()')).strip(' , ')).strip("  ' ' ")
                                    if str_pass == security_code:
                                        lst_sec.append(str_pass)
                                if security_code in lst_sec:
                                    print("Your details are:- ")
                                    admin_file = open(r'account2_logins.csv ', 'a')
                                    cwriter = csv.writer(admin_file)
                                    login_time = datetime.datetime.now()
                                    login_data = [
                                        [ 'Adhaar_no', 'Time of login' ],
                                        [ adhaar_no, login_time ] ]
                                    cwriter.writerows(login_data)
                                    admin_file.close()
                                    activity_records_ad()
                                else:
                                    while t <= 3:
                                        print(" Wrong password")
                                        User_sec()

                            User_sec()
                        else:
                            while t <= 3:
                                print(" The adhaar_no you entered is not in our db plz retry")
                                adhaar()

                    adhaar()
                else:
                    online_bank()

            online_bank()

        # Update Account Section
        def Update( ):
            def ac_num_verification( ):
                global t
                t = t + 1
                ac_num = input("Enter your Account Number->")
                search = 'select Account_number from account_details'
                mycursor.execute(search)
                ac_num_details = mycursor.fetchall()
                lst_ac = [ ]
                for num_value in ac_num_details:
                    str_details = ((str(num_value).strip('()')).strip(' , ')).strip("  ' ' ")
                    if str_details == ac_num:
                        lst_ac.append(str_details)
                if ac_num in lst_ac:
                    def Security_Code_verification( ):
                        global t
                        t = t + 1
                        security_code = input("Enter your Security Code->")
                        search_security_code = 'select Security_Code from account_details'
                        mycursor.execute(search_security_code)
                        search_security_code_details = mycursor.fetchall()
                        lst_secu = [ ]
                        for security_code_value in search_security_code_details:
                            str_ad_details = ((str(security_code_value).strip('()')).strip(' , ')).strip("  ' ' ")
                            if security_code == str_ad_details:
                                lst_secu.append(str_ad_details)
                        if security_code in lst_secu:
                            print(" What do you want to update->")
                            time.sleep(0.5)
                            print("1.Update Account holder name")
                            time.sleep(1)
                            print("2.Update Nominee name")
                            time.sleep(0.5)
                            print("3.Update Your Address")
                            time.sleep(0.5)
                            print("4.Upadte Password")
                            time.sleep(0.5)
                            print("5.New Username")

                            def u_choice( ):
                                up_choice = int(input("Enter your choice:-"))
                                if up_choice == 1:
                                    def ac_holder_name( ):
                                        print("Your Account Details  ")
                                        execution = 'select Account_Holder_name from account_details where Account_number=%s and security_code=%s'
                                        num_1 = (ac_num, security_code)
                                        mycursor.execute(execution, num_1)
                                        ac_holder_details = mycursor.fetchall()
                                        for holder_value in ac_holder_details:
                                            str_ad_details = ((str(holder_value).strip('()')).strip(' , ')).strip(
                                                "  ' ' ")
                                            print("OLD ACCOUNT HOLDER NAME -> ", str_ad_details)
                                            new_holder_name = input("Enter new  account holder name->")
                                            value = 'update account_details set Account_Holder_name=%s where Account_number=%s'
                                            holder_1 = (new_holder_name, ac_num)
                                            mycursor.execute(value, holder_1)
                                            print(" Your Account Holder Name changed Sucessfully")

                                    ac_holder_name()
                                elif up_choice == 2:
                                    def nominee_name( ):
                                        execution = 'select Nominee_name from account_details where Account_number=%s and Security_Code=%s'
                                        ex_value = (ac_num, security_code)
                                        mycursor.execute(execution, ex_value)
                                        ac_nominee_details = mycursor.fetchall()
                                        for nominee_value in ac_nominee_details:
                                            str_ad_details = ((str(nominee_value).strip('()')).strip(' , ')).strip(
                                                "  ' ' ")
                                            print("OLD ACCOUNT NOMINEE NAME -> ", str_ad_details)
                                            new_nominee_name = input("Enter new  account nominee name->")
                                            value = 'update account_details set Nominee_name=%s where Account_number=%s '
                                            nominee_1 = (new_nominee_name, ac_num)
                                            mycursor.execute(value, nominee_1)
                                            print(" Your Account Nominee Name changed Sucessfully")

                                    nominee_name()
                                elif up_choice == 3:
                                    def address( ):
                                        execution = 'select Address from account_details where Account_number=%s and security_code=%s'
                                        ex_ad = (ac_num, security_code)
                                        mycursor.execute(execution, ex_ad)
                                        ac_address_details = mycursor.fetchall()
                                        for address_value in ac_address_details:
                                            str_ad_details = ((str(address_value).strip('()')).strip(' , ')).strip(
                                                "  ' ' ")
                                            print("OLD ACCOUNT ADDRESS  -> ", str_ad_details)
                                            new_address_name = input("Enter new  account address ->")
                                            value = 'update account_details set address=%s where Account_number=%s'
                                            address_1 = (new_address_name, ac_num)
                                            mycursor.execute(value, address_1)
                                            print(" Your Account address changed Sucessfully")

                                    address()
                                elif up_choice == 4:
                                    def password( ):
                                        execution = 'select Pass_word from account_details where Account_number=%s and security_code=%s'
                                        num_1 = (ac_num, security_code)
                                        mycursor.execute(execution, num_1)
                                        ac_Passsword_details = mycursor.fetchall()
                                        for Passsword_value in ac_Passsword_details:
                                            str_ad_details = ((str(Passsword_value).strip('()')).strip(' , ')).strip(
                                                "  ' ' ")
                                            print("OLD ACCOUNT PASSWORD  -> ", str_ad_details)
                                            new_Passsword_name = input("Enter new  account Passsword ->")
                                            value = 'update account_details set pass_word=%s where Account_number=%s'
                                            Passsword_1 = (new_Passsword_name, ac_num)
                                            mycursor.execute(value, Passsword_1)
                                            print(" Your Account Passsword changed Sucessfully")

                                    password()
                                elif up_choice == 5:
                                    def username( ):
                                        execution = 'select Username from account_details where Account_number=%s and security_code=%s'
                                        num_1 = (ac_num, security_code)
                                        mycursor.execute(execution, num_1)
                                        ac_username_details = mycursor.fetchall()
                                        for username_value in ac_username_details:
                                            str_ad_details = ((str(username_value).strip('()')).strip(' , ')).strip(
                                                "  ' ' ")
                                            print("OLD ACCOUNT USERNAME  -> ", str_ad_details)
                                            create = '''123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
                                            for x in range(1):
                                                new_username = " "
                                                for y in range(8):
                                                    new_username += random.choice(create)
                                        value = 'update account_details set username=%s where Account_number=%s'
                                        username_1 = (new_username, ac_num)
                                        mycursor.execute(value, username_1)
                                        print(" Your Account username changed Sucessfully")

                                    username()
                                else:
                                    u_choice()

                            u_choice()
                        else:
                            print(" Wrong Security Code !!!!")
                            while t <= 3:
                                Security_Code_verification()

                    Security_Code_verification()
                else:
                    print("Wrong Account number!!!")
                    while t <= 3:
                        ac_num_verification()

            ac_num_verification()

        #New Account section
        def New_Account( ):
            # Details
            ac_file = open(r'Account.txt', 'r')
            old = ac_file.readlines()
            ac_file.close()
            ac = int(old[ 0 ]) + 1
            ac_file.close()
            ac_file = open(r'Account.txt', 'w')
            ac_file.write(str(ac))
            ac_file.close()
            time.sleep(0.5)
            print("|| Provide your correct details to Create your saving account || ")
            Ac_number = ac
            Ac_holder = input("Enter Account holder name (As on Adhaar Card):-")
            Ac_Fname = input("Enter Account holder\'s father\'s name:-")
            Ac_Mname = input("Enter Account holder\'s mother\'s name:-")
            DOB = input("Enter you DOB yy/mm/dd <-(89/12/30)-> :-")
            Ac_DOB = datetime.datetime.strptime(DOB, '%y/%m/%d')
            Adhaar_number = input("Enter Account holder\'s Adhaar Number (with spaces too):-")
            Address = input("Enter your Adress:-")
            Nominee_name = input("Enter the Nominee name:-")
            Nominee_Ad_number = input(("Enter Nominee\'s Adhaar Number (with spaces too):-"))
            create = '''123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
            for x in range(1):
                code = " "
                for y in range(8):
                    code += random.choice(create)
                Security_code = code

            # A dummy text file to count Sr_no

            D_write = Ac_holder + '\n'
            D_file = open(r"Dummy.txt", "a")
            D_file.write(D_write)
            D_file.close()
            D_file = open(r"Dummy.txt", "r")
            D_read = D_file.readlines()
            for x in range(0, len(D_read)):
                Sr_no = x + 1

            def pay( ):
                ch = input("press Y/y if you agree:-")
                if ch == 'ý' or ch == 'Y':
                    print(''' enter your payment method
                              1.Paytm
                              2.Online Banking
                              3.ATM''')

                    def payment_method( ):
                        c_p = int(input(" Choose your payment method:-"))
                        if c_p == 1:
                            c = 'paytm'
                            upi = input("Enter your upi:-")
                            print("Your form has submitted to our server ")
                        elif c_p == 2:
                            c = 'Online banking'
                            Account_number = int(input("your Account number:-"))
                            Pass = input("your Paasword:-")
                            print("Your form has submitted to our server ")
                        elif c_p == 3:
                            c = 'ATM'
                            ATM = int(input("your ATM number:-"))
                            CVV = int(input("Your CVV"))
                            Expiry_date = int(input("Enter your expiry date(yyyy/mm/dd):-"))
                            print("Your form has submitted to our server ")
                        else:
                            payment_method()

                    payment_method()

                else:
                    print("Your form has not been submitted to our server")

            def online_error_sol( ):
                online_ch = input("Do you want to do online Banking(y/n):-")
                # Yes for online
                if online_ch == 'y' or online_ch == 'Y':
                    Password = input("Enter your password (for online banking only):-")

                    # Username for Bank Account
                    global username, code
                    create = '''123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
                    for x in range(1):
                        username = " "
                        for y in range(8):
                            username += random.choice(create)

                            # Sending value to Sql Database
                    pay()

                    New_account_insert = 'insert into Account_Details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    New_account_value = [ (Sr_no, Ac_number, Ac_holder, Ac_Fname, Ac_Mname, Ac_DOB,
                                           Adhaar_number, Address, username, Password, Nominee_name,
                                           Nominee_Ad_number, 'Not required', '1000') ]
                    mycursor.executemany(New_account_insert, New_account_value)
                    connection.commit()


                elif online_ch == 'n' or online_ch == 'N':
                    pay()

                    New_account_insert = 'insert into Account_Details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    New_account_value = [ (Sr_no, Ac_number, Ac_holder, Ac_Fname, Ac_Mname, Ac_DOB,
                                           Adhaar_number, Address, 'Not used', 'Not used', Nominee_name,
                                           Nominee_Ad_number, Security_code, '1000') ]
                    mycursor.executemany(New_account_insert, New_account_value)
                    connection.commit()
                else:
                    online_error_sol()

            online_error_sol()
            D_file.close()

        #Transaction Details
        def Trans_Details( ):
            print('Hello',username, ''' How do you want transaction 
                                                 1.Date wise
                                                 2.Month wise
                                                 3.Yearly wise''')

            def t_ch( ):
                tr_ch = int(input("Enter your choice:-"))
                if tr_ch == 1:
                    def date_choice( ):
                        d_ch = input('''Do you want your details of present month or of any other year 
                                                           Please reply with 
                                                           p/P:-(Present Date)
                                                           n/N:-(New Date):-''')
                        if d_ch == 'p' or d_ch == 'P':
                            value = 'select * from transacation_details where Date=now'
                            mycursor.execute(value)
                            data = mycursor.fetchall()
                            for row in data:
                                print(row)
                        elif d_ch == 'n' or d_ch == 'N':
                            D_u = input("Enter you desired datein format(yy/mm/dd):- ")
                            Date = datetime.datetime.strptime(D_u, '%y/%m/%d')
                            d_1 = (Date,)
                            value = 'select * from transacation_details where Date=%s'
                            mycursor.execute(value, d_1)
                            data = mycursor.fetchall()
                            for row in data:
                                print(row)
                        else:
                            date_choice()

                    date_choice()
                elif tr_ch == 2:  # month wise
                    def month_choice( ):
                        m_ch = input('''Do you want your details of present month or of any other year 
                                           Please reply with 
                                           p/P:-(Present Month)
                                           n/N:-(New Month):-''')
                        if m_ch == 'p' or m_ch == 'P':
                            m = date.today()
                            Year = m.year
                            D_y = Year[ 2:4:1 ]
                            mon = m.month
                            D_u = str(D_y) + '/' + str(mon) + '/01'
                            Date = datetime.datetime.strptime(D_u, '%y/%m/%d')
                            d_1 = (Date,)
                            value = 'select * from transacation_details where Date=%s'
                            mycursor.execute(value, d_1)
                            data = mycursor.fetchall()
                            for row in data:
                                print(row)
                        elif m_ch == 'n' or m_ch == 'N':
                            Year = input('Enter your desire year:-')
                            mon = input('Enter your desire month:-')
                            D_u = Year[ 2:4:1 ] + '/' + str(mon) + '/01'
                            Date = datetime.datetime.strptime(D_u, '%y/%m/%d')
                            d_1 = (Date,)
                            value = 'select * from transacation_details where Date=%s'
                            mycursor.execute(value, d_1)
                            data = mycursor.fetchall()
                            for row in data:
                                print(row)
                        else:
                            month_choice()

                    month_choice()
                elif tr_ch == 3:  # year wise
                    def year_choice( ):
                        y_ch = input('''Do you want your details of present year or of any other year 
                                           Please reply with 
                                           p/P:-(present year)
                                           n/N:-(New year)''')
                        if y_ch == 'p' or y_ch == 'P':
                            Y = date.today()
                            Year = Y.year
                            D_u = Year[ 2:4:1 ] + '/01/01'
                            Date = datetime.datetime.strptime(D_u, '%y/%m/%d')
                            d_1 = (Date,)
                            value = 'select * from transacation_details where Date=%s'
                            mycursor.execute(value, d_1)
                            data = mycursor.fetchall()
                            for row in data:
                                print(row)
                        elif y_ch == 'n' or y_ch == 'N':
                            Year = input('Enter your desire year:-')
                            D_u = Year[ 2:4:1 ] + '/01/01'
                            Date = datetime.datetime.strptime(D_u, '%y/%m/%d')
                            d_1 = (Date,)
                            value = 'select * from transacation_details where Date=%s'
                            mycursor.execute(value, d_1)
                            data = mycursor.fetchall()
                            for row in data:
                                print(row)
                        else:
                            year_choice()

                    year_choice()
                else:
                    t_ch()

            t_ch()

        #Query Section
        def Query( ):  # Query Section
            print("Choose from the given question to resolve your query")
            ques = open(r"question.txt", 'r')
            z = ques.readlines()
            for x in z:
                print(x)
            ques.close()
            ch = int(input("Enter your question number:-"))
            if ch == 1:
                ans1 = open("ans1.txt", 'r')
                w = ans1.readlines()
                for y in w:
                    print(y)
                ans1.close()
                count = '1'
                Query_file = open(r"sr_no.txt", "r")
                Query_file.write(count)
            elif ch == 2:
                ans2 = open("ans2.txt", 'r')
                w = ans2.readlines()
                for y in w:
                    print(y)
                ans2.close()
                count = '1'
                Query_file = open(r"sr_no.txt", "r")
                Query_file.write(count)
            elif ch == 3:
                ans3 = open("ans3.txt", 'r')
                w = ans3.readlines()
                for y in w:
                    print(y)
                ans3.close()
                count = '1'
                Query_file = open(r"sr_no.txt", "r")
                Query_file.write(count)
            elif ch == 4:
                ans4 = open("ans4.txt", 'r')
                w = ans4.readlines()
                for y in w:
                    print(y)
                ans4.close()
                count = '1'
                Query_file = open(r"sr_no.txt", "r")
                Query_file.write(count)
            elif ch == 5:
                def op( ):
                    new_query = input("Enter your query with word limit of 1000 words:-")
                    if len(new_query) > 1000:
                        print("!!!! Maximum word limit exceeded !!!!")
                    elif len(new_query) <= 1000:
                        new_q_file = open("newq.txt", 'r')
                        new_q_file.write(new_query)
                        new_q_file.close()
                    else:
                        op()
                    op()
            else:
                Query_file = open(r"sr_no.txt", "r")
                Query_read = Query_file.readlines()
                for x in range(0, len(Query_read)):
                    Sr_no = x + 1
                    # Sending value to Sql Database

                    Insert_Qvalue = 'insert into query values(%s,%s,%s)'
                    Query_value = [ (Sr_no, 'Check Query.txt file', datetime.datetime.now()) ]
                    mycursor.executemany(Insert_Qvalue, Query_value)
                    Query_file.close()
                    print("Your Query has been sent to the RBI ")

                    # What will you do today ka choice

        #Make Choice
        def Choice( ):
            print("What do you want to do Today\n ")
            time.sleep(0.5)
            print("1.Open a New Saving Account")
            time.sleep(1)
            print("2.Update Your Account")
            time.sleep(0.5)
            print("3.Transaction Details")
            time.sleep(0.5)
            print("4.Account Details")
            time.sleep(0.5)
            print("5.Trasaction")
            time.sleep(0.5)
            print("6.Others/Query")
            time.sleep(0.5)

            mang = int(input("Enter your choice:-"))

            if mang <= 8:
                ans = 'y'
                while ans == 'y':
                    if mang == 1:
                        New_Account()
                        connection.commit()

                    elif mang == 2:
                        Update()
                        connection.commit()

                    elif mang == 3:
                        Trans_Details()
                        connection.commit()

                    elif mang == 4:
                        Account_Details()
                        connection.commit()

                    elif mang == 5:
                        Trasaction()
                        connection.commit()

                    elif mang == 6:
                        Query()
                        connection.commit()
                    ans = input("Re Run the Program(y/n):-")
                    if ans == 'y':
                        Choice()
                    else:
                        break
            else:
                Choice()
        Choice()

    #User Login
    def user_login( ):
        def online_bank( ):
            ch = input('''Did you use online banking (y/n) for Yes and No -> ''')
            if ch == 'y' or ch == 'Y':
                def User_user( ):
                    global t
                    t = t + 1
                    username = input(" Username:- ")
                    Users_show = 'select Username from account_details '
                    mycursor.execute(Users_show)
                    u_data = mycursor.fetchall()
                    count = mycursor.rowcount
                    lst_u = [ ]
                    for row in u_data:
                        str_user = ((str(row).strip('()')).strip(' , ')).strip("  ' ' ")
                        if str_user == username:
                            lst_u.append(str_user)
                    if username in lst_u:
                        def User_pass( ):
                            global t
                            t = t + 1
                            password = input(" Password:- ")
                            Users_pass = 'select Pass_word from account_details '
                            mycursor.execute(Users_pass)
                            p_data = mycursor.fetchall()
                            lst = [ ]
                            for prow in p_data:
                                str_pass = ((str(prow).strip('()')).strip(' , ')).strip("  ' ' ")
                                if str_pass == password:
                                    lst.append(str_pass)
                                print(lst)
                            if password in lst:
                                print("Access Granted ")
                                user_thing()
                                admin_file = open(r'Account_logins.csv ', 'a')
                                cwriter = csv.writer(admin_file)
                                login_time = datetime.datetime.now()
                                login_data = [
                                    [ 'Username', 'Time of login' ],
                                    [ username, login_time ] ]
                                cwriter.writerows(login_data)
                                admin_file.close()

                            else:
                                while t <= 3:
                                    # sir se poochna hai
                                    print(" Wrong password")
                                    User_pass()
                        User_pass()
                    else:
                        while t <= 3:
                            print(" The username you entered is not in our db plz retry")
                            User_user()

                User_user()
            elif ch == 'n' or ch == 'N':
                def adhaar( ):
                    adhaar_no = input(" Adhaar_no:- ")
                    Users_show = 'select Adhaar_Number from account_details'
                    mycursor.execute(Users_show)
                    u_data = mycursor.fetchall()
                    count = mycursor.rowcount
                    lst_ad = [ ]
                    for row in u_data:
                        str_user = ((str(row).strip('()')).strip(' , ')).strip("  ' ' ")
                        if str_user == adhaar_no:
                            lst_ad.append(str_user)
                    if adhaar_no in lst_ad:
                        def User_sec( ):
                            security_code = input(" Security Code:- ")
                            Users_sec = 'select Security_Code from account_details'
                            mycursor.execute(Users_sec)
                            p_data = mycursor.fetchall()
                            lst_sec = [ ]
                            for prow in p_data:
                                str_pass = ((str(prow).strip('()')).strip(' , ')).strip("  ' ' ")
                                if str_pass == security_code:
                                    lst_sec.append(str_pass)
                            if security_code in lst_sec:
                                print("Access Granted ")
                                user_thing()
                                admin_file = open(r'account2_logins.csv ', 'a')
                                cwriter = csv.writer(admin_file)
                                login_time = datetime.datetime.now()
                                login_data = [
                                    [ 'Adhaar_no', 'Time of login' ],
                                    [ adhaar_no, login_time ] ]
                                cwriter.writerows(login_data)
                                admin_file.close()

                            else:
                                while t <= 3:
                                    print(" Wrong password")
                                    User_sec()

                        User_sec()
                    else:
                        while t <= 3:
                            print(" The adhaar_no you entered is not in our db plz retry")
                            adhaar()

                adhaar()
            else:
                online_bank()

        online_bank()

    #Admin Log out Section
    def LogOut( ):
        z = 3

    #Admin Login Section
    def LogIn( ):
        def Admin_user( ):
            username = input(" Username:- ")
            Admins_show = 'select User_name from Adminstration_Table'
            mycursor.execute(Admins_show)
            u_data = mycursor.fetchall()
            global t
            t = t + 1
            lst_ad = [ ]
            for row in u_data:
                str_user = ((str(row).strip('()')).strip(' , ')).strip("  ' ' ")
                if str_user == username:
                    lst_ad.append(str_user)
            if username in lst_ad:
                def Admin_pass( ):
                    global t
                    t = t + 1
                    password = input(" Password:- ")
                    Admins_pass = 'select Pass_word from Adminstration_Table'
                    mycursor.execute(Admins_pass)
                    p_data = mycursor.fetchall()
                    lst_pass = [ ]
                    for prow in p_data:
                        str_pass = ((str(prow).strip('()')).strip(' , ')).strip("  ' ' ")
                        if str_pass == password:
                            lst_pass.append(str_pass)
                    if password in lst_pass:
                        print("Access Granted ")
                        admin_file = open(r'Adminstration_logins.csv ', 'a')
                        cwriter = csv.writer(admin_file)
                        login_time = datetime.datetime.now()
                        login_data = [
                            [ 'Username', 'Time of login' ],
                            [ username, login_time ] ]
                        cwriter.writerows(login_data)
                        admin_file.close()
                    else:
                        while t <= 3:
                            print(" Wrong password")
                            Admin_pass()
                Admin_pass()
            else:
                while t <= 3:
                    print(" The username you entered is not in our db plz retry")
                    Admin_user()
        Admin_user()

    #1 choice in term of Admin login
    def Admin_login( ):
        print('''Do you want to 1. LogIn 
                     2. LogOut''')
        log_ch = int(input(' Enter your Choice:-'))
        if log_ch == 1:
            LogIn()
        elif log_ch == 2:
            print(" Log Out Sucessfully!!")

    #2 choice in term of user
    def User_login_activity( ):

        print(''' Are  you a
             1.New user
             2.Existing user ''')

        def op_u( ):
            u_ch = int(input("Enter your choice:-"))
            #existing User
            if u_ch == 2:
               user_login()
               connection.commit()

               #New user
            elif u_ch == 1:
                print("What do you want to do Today\n ")
                time.sleep(0.5)
                print("1.Open a New Saving Account")
                time.sleep(1)
                print("2.Update Your Account")
                time.sleep(0.5)
                print("3.Transaction Details")
                time.sleep(0.5)
                print("4.Account Details")
                time.sleep(0.5)
                print("5.Money Deposit")
                time.sleep(0.5)
                print("6.Money Withdrawal")
                time.sleep(0.5)
                print("7.Others/Query")
                time.sleep(0.5)

                # New Account Section

                def New_Account( ):
                    # Details
                    ac_file = open(r'Account.txt', 'r')
                    old = ac_file.readlines()
                    ac_file.close()
                    ac = int(old[ 0 ]) + 1
                    ac_file.close()
                    ac_file = open(r'Account.txt', 'w')
                    ac_file.write(str(ac))
                    ac_file.close()
                    time.sleep(0.5)
                    print("|| Provide your correct details to Create your saving account || ")
                    Ac_number = ac
                    Ac_holder = input("Enter Account holder name (As on Adhaar Card):-")
                    Ac_Fname = input("Enter Account holder\'s father\'s name:-")
                    Ac_Mname = input("Enter Account holder\'s mother\'s name:-")
                    DOB = input("Enter you DOB yy/mm/dd <-(89/12/30)-> :-")
                    Ac_DOB = datetime.datetime.strptime(DOB, '%y/%m/%d')
                    Adhaar_number = input("Enter Account holder\'s Adhaar Number (with spaces too):-")
                    Address = input("Enter your Adress:-")
                    Nominee_name = input("Enter the Nominee name:-")
                    Nominee_Ad_number = input(("Enter Nominee\'s Adhaar Number (with spaces too):-"))
                    create = '''123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
                    for x in range(1):
                        code = " "
                        for y in range(8):
                            code += random.choice(create)
                        Security_code = code

                    # A dummy text file to count Sr_no

                    D_write = Ac_holder + '\n'
                    D_file = open(r"Dummy.txt", "a")
                    D_file.write(D_write)
                    D_file.close()
                    D_file = open(r"Dummy.txt", "r")
                    D_read = D_file.readlines()
                    for x in range(0, len(D_read)):
                        Sr_no = x + 1

                    def pay( ):
                        ch = input("press Y/y if you agree:-")
                        if ch == 'ý' or ch == 'Y':
                            print(''' enter your payment method
                                      1.Paytm
                                      2.Online Banking
                                      3.ATM''')

                            def payment_method( ):
                                c_p = int(input(" Choose your payment method:-"))
                                if c_p == 1:
                                    c = 'paytm'
                                    upi = input("Enter your upi:-")
                                    print("Your form has submitted to our server ")
                                elif c_p == 2:
                                    c = 'Online banking'
                                    Account_number = int(input("your Account number:-"))
                                    Pass = input("your Paasword:-")
                                    print("Your form has submitted to our server ")
                                elif c_p == 3:
                                    c = 'ATM'
                                    ATM = int(input("your ATM number:-"))
                                    CVV = int(input("Your CVV"))
                                    Expiry_date = int(input("Enter your expiry date(yyyy/mm/dd):-"))
                                    print("Your form has submitted to our server ")
                                else:
                                    payment_method()

                            payment_method()

                        else:
                            print("Your form has not been submitted to our server")
                    def online_error_sol( ):
                        online_ch = input("Do you want to do online Banking(y/n):-")
                        # Yes for online
                        if online_ch == 'y' or online_ch == 'Y':
                            Password = input("Enter your password (for online banking only):-")

                            # Username for Bank Account
                            global username, code
                            create = '''123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
                            for x in range(1):
                                username = " "
                                for y in range(8):
                                    username += random.choice(create)



                                    # Sending value to Sql Database
                            pay()

                            New_account_insert = 'insert into Account_Details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            New_account_value = [ (Sr_no, Ac_number, Ac_holder, Ac_Fname, Ac_Mname, Ac_DOB,
                                                   Adhaar_number, Address, username, Password, Nominee_name,
                                                   Nominee_Ad_number, 'Not required','1000') ]
                            mycursor.executemany(New_account_insert, New_account_value)
                            connection.commit()


                        elif online_ch == 'n' or online_ch == 'N':
                            pay()

                            New_account_insert = 'insert into Account_Details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            New_account_value = [ (Sr_no, Ac_number, Ac_holder, Ac_Fname, Ac_Mname, Ac_DOB,
                                                   Adhaar_number, Address, 'Not used', 'Not used', Nominee_name,
                                                   Nominee_Ad_number, Security_code,'1000') ]
                            mycursor.executemany(New_account_insert, New_account_value)
                            connection.commit()
                        else:
                            online_error_sol()

                    online_error_sol()
                    D_file.close()



                def Choice( ):

                    mang = int(input("Enter your choice:-"))

                    if mang <= 8:
                        ans = 'y'
                        while ans == 'y':
                            if mang == 1:
                                New_Account()

                            else:
                                print("please create a account and then login as existing user ")
                            ans=input(" Do you want to re create the account(y/n):-")
                    else:
                        Choice()

                Choice()
            else:
                op_u()
        op_u()


    # 1 and main function
    def User_check( ):

        time.sleep(0.5)
        print('Like Whom you want to login!!!')
        print('''1.Adminstration
                2.Bank_User''')
        ch = int(input(" As whom you want login:-"))
        if ch == 1:
            Admin_login()
            print(" You Sucessfully Login as Admin")

            def User_check_again( ):
                print('Like Whom you want to login Again!!!')
                print(''' 1.Adminstration
                        2.Bank_User''')
                ch_re = int(input("Enter your choice:-"))
                if ch_re == 1:
                    print("You are already login as Admin")
                    User_login_activity()
                elif ch_re == 2:
                    User_login_activity()
                else:
                    User_check_again()

            User_check_again()

            def ac_number( ):
                global z
                z = 1
                if z == 1:
                    def w_admin_login( ):
                        ac = '04022021'
                        ac_file = open('Account.txt', 'w')
                        ac_file.write(ac)
                        ac_file.close()

                    w_admin_login()
                    z = 2
                    ac_number()
                elif z == 2:
                    def a_admin_login( ):
                        ac_file = open(r'Accounz.txt', 'r')
                        old = ac_file.readlines()
                        print("old account", old)
                        ac_file.close()
                        global ac
                        ac = int(old[ 0 ]) + 1
                        print("new account", ac)
                        ac_file.close()
                        ac_file = open(r'Account.txt', 'w')
                        ac_file.write(str(ac))
                        ac_file.close()
                    a_admin_login()
        elif ch == 2:
            User_login_activity()
        else:
            User_check()

    User_check()

else:
    print("!!!!!Server Connection failed  !!!!!! \nPlease wait till we reconnect.............")
    for x in range(0, 5):
        time.sleep(0.5)
        print("Connecting.........")
    connection = sql_con.connect(host='127.0.0.1', user='root', password='coder_player', db='RBI_db')
    time.sleep(1)
    print("Now, Please restart the Program")

connection.commit()
