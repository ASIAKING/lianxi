"""
构建一个基本的日历，用户将能够通过命令行与之交互。用户应该能够选择：

查看日历
将事件添加到日历中
更新现有事件
删除现有事件
程序应以下列方式运行：
zip 将多个列表字对应成对
enumerate()为列表元素提供索引循环时
打印一条欢迎信息给用户
提示用户查看、添加、更新或删除日历上的事件。
取决于用户的输入：查看、添加、更新或删除日历上的事件
除非用户决定退出，否则程序永远不会终止。
"""
from time import sleep,strftime
USER_FIRST_NAME='Asia'
calendar={}
def welcome():
    print('Welcome,'+USER_FIRST_NAME+'.')
    print('Calendar starting...')
    sleep(1)
    print('Today is:'+strftime('%A %B %D,%Y'))
    print('Now time is'+strftime('%H:%M:%S'))
    print('What would you like to do?')
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'V':
            if len(calendar.keys())<1:
                print("Calendar empty.")
            else:
                print(calendar)
        elif user_choice == 'U':
            date = input("What date? ")
            update = input("Enter the update: ")
            calendar[date] = update
        elif user_choice == 'A':
            event = input("Enter event:")
            date = input("Enter date (MM/DD/YYYY): ")
            if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print('你输入了无效信息')
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print('添加成功')
                print(calendar)
        elif user_choice == 'D':
                if len(calendar.keys())<1:
                    print("Calendar empty.")
                else:
                    event = input("Enter event:")
                    for date in calendar.keys():
                        if event == calendar[date]:
                            del(calendar[date])
                            print('删除成功')
                            print(calendar)
                        else:
                            print('事件不存在')
        elif user_choice == 'X':
            start = False
        else:
            print('请输入有效字符')
            start=False
start_calendar()
