from faker import Faker
from random import randint
from random import choices
import sqlite3
from datetime import datetime

#function to generate the db name
def GenerateFileName(custom=''):
    if custom:
        return custom
    else:
        now = str(datetime.now().strftime("%d-%m-%Y %H-%M-%S"))
        return now
    
dbFileName = GenerateFileName(input('Enter the name of the db file (press enter to use the current date and time as the name): '))
tableName = input('Enter the name of the table: ')

#create the db
conn = sqlite3.connect(f"{dbFileName}.db")
cursor = conn.cursor()

#delete the db if it already exists
cursor.execute(f"DROP TABLE IF EXISTS {tableName}")
conn.commit()

#ask the user to choose the columns and add them to the db
print("""available columns (primary key is username):
password, name, age, phone,
gender, job, city, address, bank, 
email, credit_card, compony""")
OptionalColumns = {'password':False, 'name':False,
           'age':False, 'phone':False,'gender':False, 'job':False, 'city':False,
           'address':False, 'bank':False, 'email':False, 'credit_card':False, 'compony':False}
while 1:
    column = input('Enter the name of the column (press enter to stop): ')
    if column == '':
        break
    elif column in OptionalColumns:
        OptionalColumns[column] = True
    else:
        print('Invalid column name. Try again.')

create_table_query = f"CREATE TABLE IF NOT EXISTS {tableName} (username TEXT PRIMARY KEY"
for column, is_selected in OptionalColumns.items():
    if is_selected:
        create_table_query += f", {column} TEXT"
create_table_query += ")"
cursor.execute(create_table_query)
conn.commit()

#ask the user to choose the language
while 1:
    lang = input('Enter the language ("English" or "Persian" or "both"): ').lower()
    if lang == 'persian':
        f = Faker("fa_IR")
        break
    elif lang == 'english':
        f = Faker("en_US")
        break
    elif lang == 'both':
        f = Faker(["fa_IR", "en_US"])
        break
    else:
        print('Invalid language. Try again.')

#ask the user to enter the number of rows
number = int(input('Please enter the number of rows you want to generate: '))

#generate the data and insert it into the db
usernames = []
added_columns = [column for column, is_selected in OptionalColumns.items() if is_selected]

for i in range(number):
    insert_query = f"INSERT INTO {tableName} (username"

    username = f.user_name()
    while username in usernames:
        username = f.user_name()
    usernames.append(username)

    row_values = [username]  

    gender = f.passport_gender()

    for column in added_columns:
        insert_query += f", {column}"

        if column == 'age':
            row_values.append(randint(18, 70))
        elif column == 'name':
            if gender == 'M':
                row_values.append(f.name_male())
            else:
                row_values.append(f.name_female())
        elif column == 'job':
            if gender == 'M':
                row_values.append(f.job_male())
            else:
                row_values.append(f.job_female())
        elif column == 'password':
            row_values.append(f.password(8))
        elif column == 'bank':
            row_values.append(f.bank())
        elif column == 'credit_card':
            row_values.append(f.credit_card_number())
        elif column == 'phone':
            row_values.append(f.phone_number())
        elif column == 'city':
            row_values.append(f.city())
        elif column == 'address':
            row_values.append(f.address())
        elif column == 'email':
            row_values.append(f.email())
        elif column == 'compony':
            row_values.append(f.company())
        elif column == 'gender':
            row_values.append(gender)

    placeholders = ", ".join(["?"] * len(row_values))
    insert_query += f") VALUES ({placeholders})"

    cursor.execute(insert_query, tuple(row_values))
    conn.commit()


print(f"Data created successfully in {dbFileName}.db inside table '{tableName}'.")
