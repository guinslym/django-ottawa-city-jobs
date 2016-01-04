import sqlite3

CreateDataBase = sqlite3.connect('jobs.db')

QueryCurs = CreateDataBase.cursor()

def CreateTable():
    QueryCurs.execute('''CREATE TABLE Jobs
    (id INTEGER PRIMARY KEY, Position TEXT, JobRef TEXT, JobUrl TEXT,PostDate TEXT,ExpiryDate TEXT, SalaryMax TEXT, Title REAL)''')

def AddEntry(Position,JobRef,JobUrl,PostDate,ExpiryDate,SalaryMax,Title):
    QueryCurs.execute('''INSERT INTO Jobs (Position,JobRef,JobUrl,PostDate,ExpiryDate,SalaryMax,Title)
    VALUES (?,?,?,?,?,?,?)''',(Position,JobRef,JobUrl,PostDate,ExpiryDate,SalaryMax,Title))

#If I want to create the Database
#CreateTable()

for job in job_list:
	AddEntry(job['position'],job['jobref'],job['joburl'],job['postdate'],job['expirydate'],job['salarymax'],job['name'])


CreateDataBase.commit()

QueryCurs.execute('SELECT * FROM Jobs')

for i in QueryCurs:
    print ("\n")
    for j in i:
        print (j)


QueryCurs.close()
print(len(job_list))