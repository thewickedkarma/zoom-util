#importing all  the libraries required
import numpy as np
from pyfiglet import Figlet 
import sys,time
from datetime import datetime,date,timedelta
import os
from colorama import Fore
import pandas as pd
from tabulate import tabulate



#A function to animate the characters to make it look surreal
def animate(char,x):
        for letter in char:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(x)

#A function to display banner
def banner():
    banner=Figlet(font='kban').renderText('Zoom-utils') #Banner-text here
    print('\n')
    animate(banner,0.003)
    animate(' '*20,0.003)
    animate('A reliable zoom meeting scheduler',0.05)
    print('\n')


#Using csv file to create and store data
file='meetings.csv'
meet= pd.read_csv(file)
df=pd.DataFrame(meet)
df.index = np.arange(1, len(df)+1) #starts index from 1 

def caution():
    print('\n')
    animate('Disclaimer:Updating the database will delete all the outdated meetings.',0.005)
    print('\n')
    print('┌─[ '+Fore.WHITE +'Do you still want to update the database? [y/n]'+Fore.CYAN +':]─[~]')
    opn=input(Fore.CYAN + '└──╼ ~ ')
    if opn=='y' or opn == 'Y':
            update()
            print('Database updated')
            time.sleep(3)
            print('\n')

    elif opn=='n' or opn=='N':
        start.tasklist()
    


def update():
    today_date=datetime.today().strftime('%H:%M %d/%m/%y')
    today_date_format=datetime.strptime(today_date, '%H:%M %d/%m/%y')
    lst=[]
    
    for i in range(1,len(df)+1):
        time_df=df.loc[i,'Meeting Time']
        date_df=df.loc[i,'Meeting Date']
        datetime_df=time_df+' '+date_df
        datetime_df_format=datetime.strptime(datetime_df, '%H:%M %d/%m/%y')
        if today_date_format>datetime_df_format:
            lst.append(i)
        newdf=df.drop(index=lst)
        newdf.to_csv('meetings.csv',index=False,index_label=False)



#A function to display information about this tool
def utilinfo():
    animate('\033[0;36;48m ::\033['*25,0.003)
    print('\n'+ "\033[0;36;48m ::\033[0;37;48m This is a zoom meeting management tool useful for automation if you  \033[0;36;48m::\033[")
    print("\033[0;36;48m ::\033[0;37;48m are too lazy to click the meeting link! Hope it's helpful to you     \033[0;36;48m::\033[")
    print("\033[0;36;48m ::\033[0;37;48m                 Follow @The-Burning on github                        \033[0;36;48m::\033[")
    animate('\033[0;36;48m ::'*25,0.003)
    print('\n')

#A function to display pandas dataframe in form of a mysql-like table...also task no. 1
def table(df,x):
    if x==1:
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=True))
    elif x==2:
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

#A function to display updated database. needs to be called wherever required.
def shownew(file):
    print('\n')
    print('┌─[ '+Fore.WHITE +'Do you want to see the updated database? [y/n]'+Fore.CYAN +':]─[~]')
    opn=input(Fore.CYAN + '└──╼ ~ ')
    if opn=='y' or opn == 'Y':
        new_file=pd.read_csv(file)
        new_df=pd.DataFrame(new_file)
        table(new_df,2)
        print('\n')
    elif opn=='n'or opn=='N':
        start.tasklist()
        print('\n')
    else:
        shownew()
    
    

#Ask question to the user after completion of certain query . Exit or not
def ask():
    print('┌─[ '+Fore.WHITE +'Type E to exit or C to continue'+Fore.CYAN +':]─[~]')
    res=input(Fore.CYAN + '└──╼ ~ ')
    if res=='e' or res=='E':
        exit()
    elif res=='c' or res=='C':
        print('\n')
        start.tasklist()
    else:
        ask()


#To execute task number 2 of the tool i.e adding new meetings
def newdf():
    print('┌─[ '+Fore.WHITE +'Meeting Name'+Fore.CYAN +':]─[~]')
    meet_name=input(Fore.CYAN + '└──╼ ~ ')
    print('┌─[ '+Fore.WHITE +'Meeting Time (in the form h:m)'+Fore.CYAN +':]─[~]')
    meet_time=input(Fore.CYAN + '└──╼ ~ ')
    print('┌─[ '+Fore.WHITE +'Meeting Date(in the form Date/Month/Year, type t for today, to for tomorrow)'+Fore.CYAN +':]─[~]')
    meet_date=input(Fore.CYAN + '└──╼ ~ ')
    if meet_date=='t' or meet_date=='T':
        meet_date=datetime.today().strftime('%d/%m/%y')
    elif meet_date=='to' or meet_date=='TO':
        meet_date=datetime.strptime(datetime.today().strftime('%d/%m/%y'),'%d/%m/%y') + timedelta(days=1)
        meet_date=meet_date.strftime('%d/%m/%y')
    else:
        meet_date=meet_date
    print('┌─[ '+Fore.WHITE +'Meeting ID'+Fore.CYAN +':]─[~]')
    meet_id=input(Fore.CYAN + '└──╼ ~ ')
    print('┌─[ '+Fore.WHITE +'Meeting Password'+Fore.CYAN +':]─[~]')
    meet_pass=input(Fore.CYAN + '└──╼ ~ ')
    dic=[{'Meeting Name':meet_name, 'Meeting Time':meet_time,'Meeting Date': meet_date,'Meeting ID':meet_id,'Meeting Password':meet_pass}]
    newdf=pd.DataFrame(dic)
    new_df=pd.concat([df,newdf],ignore_index=True)
    new_df.to_csv('meetings.csv',index=False,index_label=False)
    shownew(file)


#task number 3
def upcoming():
	newdf=pd.DataFrame(pd.read_csv(file))
	today_date=datetime.today().strftime('%H:%M %d/%m/%y')
	today_date_format=datetime.strptime(today_date, '%H:%M %d/%m/%y')
	lst=[]
	
	for i in range(1,len(df)+1):
		time_df=df.loc[i,'Meeting Time']
		date_df=df.loc[i,'Meeting Date']
		datetime_df=time_df+' '+date_df
		datetime_df_format=datetime.strptime(datetime_df, '%H:%M %d/%m/%y')
		diff=datetime_df_format-today_date_format
		lst.append(diff)
	indices = []
	for each in range(len(lst)):
		if lst[each] == min(lst):
			indices.append(each)

	
	upcoming=newdf.loc[indices]
	table(upcoming,2)
	print('\n')
	print('You can click these links to join the meeting now:\n')
	for i in range(1, len(df)+1):
		name_df=df.loc[i,'Meeting Name']
		id_df=df.loc[i,'Meeting ID']
		pass_df=df.loc[i,'Meeting Password']
		print(str(name_df)+':'+'https://us04web.zoom.us/j/'+str(id_df)+'?pwd='+str(pass_df))
        
def automate():
    newdf=pd.DataFrame(pd.read_csv(file))
    today_date=datetime.today().strftime('%H:%M %d/%m/%y')
    today_date_format=datetime.strptime(today_date, '%H:%M %d/%m/%y')
    lst=[]
    
    for i in range(1,len(df)+1):
        time_df=df.loc[i,'Meeting Time']
        date_df=df.loc[i,'Meeting Date']
        datetime_df=time_df+' '+date_df
        datetime_df_format=datetime.strptime(datetime_df, '%H:%M %d/%m/%y')
    while True:
        if datetime_df_format==today_date_format:
            name_df=df.loc[i,'Meeting Name']
            id_df=df.loc[i,'Meeting ID']
            pass_df=df.loc[i,'Meeting Password']
            os.system('google-chrome'+' https://us04web.zoom.us/j/'+str(id_df)+'?pwd='+str(pass_df))
        
#function to delete meetings
def rem():
    newdf=df
    table(df,1)
    if df.empty:
        print('Database is empty, can\'t delete anything')
    else:
        print('┌─[ '+Fore.WHITE +'Which meeting do you want to remove?(use \'all\' to delete all, c to cancel )'+Fore.CYAN +':]─[~]')
        ans=input(Fore.CYAN + '└──╼ ~ ')
        if int(ans) in range(0,len(df)+1):
            newdf=df.drop(index=int(ans))
        if ans=='all':
            newdf=df.drop(df.index[0:len(df)])
        if ans=='c' or ans=='C':
            exit()
        newdf.to_csv('meetings.csv',index=False,index_label=False)
        shownew(file)    

#Tool starts with this class run start.tasklist
class start:
#a function to display all the tasks. These Fore.CYAN and Fore.WHITE just impart colors to texts. :)
    def start():
        print('It is advised to update database before running any command. Updating \ndatabase clears old meetings.\n')
        print('┌─[ '+Fore.WHITE +'Do you want to update the database? [y/n]'+Fore.CYAN +':]─[~]')
        opn=input(Fore.CYAN + '└──╼ ~ ')
        if opn=='y' or opn == 'Y':
            caution()
            start.tasklist()
        elif opn=='n'or opn=='N':
            start.tasklist()
        else:
            print('Invalid choice')

    def tasklist():
        
        print(Fore.CYAN + ' [' + Fore.WHITE + '01' + Fore.CYAN + '] Show all meetings')
        print(Fore.CYAN + ' [' + Fore.WHITE + '02' + Fore.CYAN + '] Schedule new meetings')
        print(Fore.CYAN + ' [' + Fore.WHITE + '03' + Fore.CYAN + '] Show upcoming meeting')
        print(Fore.CYAN + ' [' + Fore.WHITE + '04' + Fore.CYAN + '] Edit meeting')
        print(Fore.CYAN + ' [' + Fore.WHITE + '05' + Fore.CYAN + '] Search for a meeting')
        print(Fore.CYAN + ' [' + Fore.WHITE + '06' + Fore.CYAN + '] Delete meetings')
        print(Fore.CYAN + ' [' + Fore.WHITE + '07' + Fore.CYAN + '] Update Database')

        print(Fore.CYAN + ' [' + Fore.WHITE + '08' + Fore.CYAN + '] Run automation')
        print(Fore.CYAN + ' [' + Fore.WHITE + '09' + Fore.CYAN + '] Exit')
        start.takeinput() #proceeds to take input

#funcion to take input
    def takeinput():
        print('\n')
        print('┌─['+Fore.WHITE +'What you wanna do?'+Fore.CYAN +':]─[~]')
        start.takeinput.var= int(input(Fore.CYAN + '└──╼ ~ '))
        start.exct() #proceeds to execute

#function for execution
    def exct():

#for input 1        
        if start.takeinput.var == 1:
            print('\n')
            new_file=pd.read_csv(file)
            new_df=pd.DataFrame(new_file)
            table(new_df,2)
            print('\n')
            time.sleep(3)
            print('\n')
            ask()

#for input 2
        elif start.takeinput.var == 2:
            animate('Here you can add new meetings to the database. Fill the details correctly',0.05)
            print('\n')
            newdf()
            ask()
            
#for input 3
        elif start.takeinput.var == 3:
            upcoming()
            ask()

#for input 4
        elif start.takeinput.var == 4:
            print('Under development')
            ask()

#for input 5
        elif start.takeinput.var == 5:
            print('Under development')
            ask()

#for input 6            
        elif start.takeinput.var == 6:
            update()
            rem()
            ask()

#for input 7
        elif start.takeinput.var == 7:
            update()
            print('Database Updated successfully')
            ask()

#for input 8 
        elif start.takeinput.var == 8:
            automate()
            ask()      

#for input 9
        elif start.takeinput.var == 9:
            exit()
            

#or else do this
        else:
            print('Not a valid choice')
            ask()

banner()
utilinfo()
start.start()

