import pandas
import time
import re

print('\n\nWelcome To Your Accounts Manager')

while True:
    choice_user = input("\nSelect [""\033[32mAdd\033[0m][""\033[34mSearch\033[0m][""\033[30mEdit\033[0m][""\033[31mDelete\033[0m] or Exit: ").lower()
    #اختيار اضافة حساب
    if choice_user == 'add':
        while True:
            print('<<< You Can Cancel >>>')
            email = input('Enter Your Email: ')
            if email.lower() == 'cancel':
                print('\nCancelled\n')
                break
            else:
                check_email = re.findall(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email)
                #اذا كان ايميل المستخدم يمكن ان يكون ايميل
                if check_email:
                    while True:
                        password = input('Enter Your Password: ')
                        
                        #اذا كان كلمة المرور صالحة
                        if len(password) >= 8:

                            while True:
                                account_name = input('What Is The Account Name? ').lower()
                                    
                                #اذا اضاف اسم للحساب
                                if account_name:
                                        #اذا كان اضاف حساب من قبل
                                        try:
                                            read_file = pandas.read_csv('Accounts.csv')
                                                
                                            if email in read_file['Emails'].values and password in read_file['Passwords'].values and account_name in read_file['Account_name'].values:
                                                print('\nThis Account Is Found Realy\n')
                                                time.sleep(2)
                                                break
                                            elif account_name in read_file['Account_name'].values:
                                                print('This Name Is Found, Please Change This Name')
                                                continue

                                            else:
                                                last_data = pandas.DataFrame({
                                                    'Emails': [email],
                                                    'Passwords': [password],
                                                    'Account_name': [account_name]
                                                })
                                        
                                                new_data = pandas.concat([read_file, last_data], ignore_index=True)
                                                if 'Unnamed: 0' in new_data.columns:
                                                    new_data.drop(columns=['Unnamed: 0'], inplace=True)
                                                new_data.to_csv('Accounts.csv', index=False)
                                        #اذا لم يضف اي حساب من قبل
                                        except:
                                            first_data = pandas.DataFrame({
                                                'Emails': [email],
                                                'Passwords': [password],
                                                'Account_name': [account_name]
                                            })

                                            first_data.to_csv('Accounts.csv', index=False)
                                                
                                        print('\n🎉🎉The Account Added Successfully🎉🎉\n')
                                        break
                                    
                                #اذا لم يضف اسم للحساب
                                else:
                                    print('\nYou cannot change your account name\n')
                                    continue
                            #continue
                        #اذا لم تكن كلمة المرور صالحة
                        else:
                            print('\nIncorrect Password\n')
                            continue
                        break
                    
                #اذا كان ايميل المستخدم لا يمكن ان يكون ايميل
                else:
                    print('This is not an Email')
                    continue
        continue
    #اختيار البحث
    elif choice_user == 'search':
        #اذا كان اضاف حساب من قبل
        try:
            while True:
                read_file = pandas.read_csv('Accounts.csv')

                if read_file['Emails'].empty and read_file['Passwords'].empty and read_file['Account_name'].empty:
                    print('\nYou Deleted All Accounts\n')
                    time.sleep(2)
                    
                    continue
                else:
                    read_file = pandas.read_csv('Accounts.csv')

                    user_search = input('\nEnter Your Email Address, Password or Account Name: ')

                    values_file = read_file[
                    (read_file['Emails'] == user_search) |
                    (read_file['Passwords'] == user_search) |
                    (read_file['Account_name'] == user_search)
                    ]

                    if not values_file.empty:

                        email_searched = values_file['Emails'].item()
                        password_searched = values_file['Passwords'].item()
                        account_name_searched = values_file['Account_name'].item()

                        print('\nThe Account is found:\n')
                        print(f'\nThe Email: {email_searched}')
                        print(f'\nThe Password: {password_searched}')
                        print(f'\nAccount Name: {account_name_searched}')

                    else:
                        print("\nAccount Not Found😢")
                        print('Try Again, But Do It Defferently')
                        continue

        #اذا لم يضف اي حساب من قبل
        except FileNotFoundError:
            print('\nYou not Added any Account😊')
            continue
    elif choice_user == 'edit':
        #اذا اضاف حساب  من قبل
        try:
            read_file = pandas.read_csv('Accounts.csv')

            #اذا تم حذف جميع الحسابات
            if read_file['Emails'].empty and read_file['Passwords'].empty and read_file['Account_name'].empty:
                print('\nYou Deleted All Accounts')
                time.sleep(2)

                continue
            ############################################################################
            # هذا الاعداد لم يكتمل بالكامل
            else:
                read_file = pandas.read_csv('Accounts.csv')
                
                edit_item = input('\nSelect [Emails][Passwords][Accounts Names] To Edit: ').lower()

                while True:
                    if edit_item == 'emails' or edit_item == 'email':
                        old_email = input('\nEnter Old Email: ')

                        if old_email in read_file['Emails'].values:
                            while True:
                                email_edit = input('Enter New Email: ')

                                check_email = re.findall(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email_edit)

                                if check_email:
                                    read_file.loc[read_file['Emails'] == old_email, 'Emails'] = email_edit
                                    read_file.to_csv('Accounts.csv', index=False)

                                    print('Edit Complete')
                                    break
                                else:
                                    print('This is not an Email')
                                    continue
                        #اذا كان الحساب المراد حذفه غير موجود
                        else:
                            print('\nThe Account Is Not Found')
                            continue
                        break
                    elif edit_item == 'passwords' or edit_item == 'password':
                        old_password = input('\nEnter Old Password To Edit: ')
                        
                        if old_password in read_file['Passwords'].values:
                            while True:
                                password_edit = input('Enter New Password: ')

                                if password_edit >= 8:
                                    read_file.loc[read_file['Passwords'] == old_email, 'Passwords'] = password_edit
                                    read_file.to_csv('Accounts.csv', index=False)
                                    print('Edit Complete')
                                    break

                                elif password_edit == False:
                                    print('< Please Enter New Password >')
                                    continue
                                
                                else:
                                    print('\nIncorrect Password\n')
                                    continue

                        else:
                            print('\nPassword Not Found\n')
                            continue
                        break

                    elif edit_item == 'accounts names' or edit_item == 'account name':
                        old_account_name = input('\nEnter Old Account Name To Edit: ')
                        
                        if old_password in read_file['Account_name'].values:
                            while True:
                                account_name_edit = input('Enter New Account Name: ')

                                if account_name_edit:
                                    read_file.loc[read_file['Account_name'] == old_email, 'Account_name'] = account_name_edit
                                    read_file.to_csv('Accounts.csv', index=False)
                                    print('Edit Complete')
                                    break

                                else:
                                    print('\nIncorrect Password\n')
                                    continue

                        else:
                            print('\nAccount Name Not Found')
                            continue
                        break
                    else:
                        pass

                    continue
            ############################################################################
        #اذا لم يضف اي حساب
        except:
            print('Your Is Not Added Any Accounts')
            continue

    #اختيار ازالة حساب
    elif choice_user == 'delete':
        #اذا اضاف حساب  من قبل
        try:
            #اذا اذا اضاف حساب وتم حذفه
            read_file = pandas.read_csv('Accounts.csv')

            if read_file['Emails'].empty and read_file['Passwords'].empty and read_file['Account_name'].empty:
                print('\nYou Deleted All Accounts')
                time.sleep(2)

                continue

            #اذا كان يوجد حساب للحذف
            else:
                read_file = pandas.read_csv('Accounts.csv')
                account_deleted = input('Enter Account name: ')
                #اذا كان الحساب المراد حذفه موجود
                if account_deleted in read_file['Account_name'].values:

                    read_file = read_file[read_file['Account_name'] != account_deleted]
                    read_file.to_csv('Accounts.csv', index=False)
                    
                    print('\nDeleted Complete')
                #اذا كان الحساب المراد حذفه غير موجود
                else:
                    print('\nThe Account Is Not Found')

                continue
        #اذا لم يضف اي حساب
        except:
            print('Your Is Not Added Any Accounts')
            continue

    #اختيار الخروج
    elif choice_user == 'exit':
        print('\nPlease Wait to Exit....\n')
        time.sleep(5)

        break
    elif choice_user == 0:
        print('\nPlease Select Option')
        continue
    
    else:
        print('Option not listed')
        continue
