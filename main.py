from timetable import*


def main():
    file=open("schedule.txt","r")
    s=file.readlines()
    text=""
    for elem in s:
        text+=elem
    b=[]
    for i in range(len(s)):
        b.append(s[i][:-1])
    #print(b)
    c=[]
    for i in range(len(b)):
        if i%2==0:
            c.append(b[i])
        else:
            #print(b[i].split(","))
            c.append(b[i].split(","))
    file.close()
    menu(c,s,text)
    return c,s

def menu(c,s,text):
    x=0
    while x!=5:
        print("Меню")
        print("1.Посмотреть данные в файле")
        print("2.Сформировать и посмотреть расписание всей недели")
        print("3.Посмотреть расписание конкретного дня")
        print("4.Добавить расписание этой группы в список всех расписаний НГУ")
        print("5.Выход")
        x=int(input())
        if x==1:
            print(text)

        if x==2:
            e=[]
            #print('fs')
            for n in range(0,len(c),2):
                #print('fs')
                a=Day(c[n],c[n+1][0],c[n+1][1],c[n+1][2],c[n+1][3])
                print(a)
                e.append(str(a))
                #print(e)
            #print(e)
            for i in range(len(e)):
                print(e[i])
        if x==3:
            n=int(input("Введите номер дня(1-Понедельник. 2-Вторник...)"))
            print(e[n-1])
        if x==4:
            days=[]
            days.append(e)
            #print("Список е",e)
            c=All(days)
            print(c)
            
    return

main()

    
                
