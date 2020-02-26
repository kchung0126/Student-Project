def show_menu():
    print('+----------------------------------+')
    print('| 1) 添加學生訊息                   |')
    print('| 2) 查看所有學生訊息               |')
    print('| 3) 修改學生的成績                 |')
    print('| 4) 刪除學生訊息                   |')
    print('| 5) 成績由高到低排列               |')
    print('| 6) 成績由低到高排列               |')
    print('| 7) 年齡由大到小排列               |')
    print('| 8) 年齡由小到大排列               |')
    print('| q) 退出                           |')
    print('+----------------------------------+')

def main():
    docs = []
    while True:
        show_menu()
        s = input("請選擇下列選項:")
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':
            modify_student_info(docs)
        elif s == '4':
            delete_student_info(docs)
        elif s == '5':
            print_by_score_desc(docs)
        elif s == '6':
            print_by_score_asc(docs)
        elif s == '7':
            print_by_age_desc(docs)
        elif s == '8':
            print_by_age_asc(docs)
        elif s == 'q':
            return

def input_student(): #選項1
    L = []
    while True:
        name = input("請輸入學生姓名:")
        if not name:
            break
        age = int(input("請輸入學生年齡:"))
        score = int(input("請輸入學生成績:"))
        d = {}
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L

def output_student(L): #選項2
    print('+--------------+---------+---------+')
    print('|    name      |   age   |  score  |')
    print('+--------------+---------+---------+')
    for d in L:
        t = (d['name'].center(14),
        str(d['age']).center(9),
        str(d['score']).center(9))
        line = "|%s|%s|%s|" %t
        print(line)
    print('+--------------+---------+---------+')

def modify_student_info(lst): #選項3
    name = input('請輸入要修改的學生姓名:')
    for d in lst:
        if d['name'] == name:
            score = int(input("請輸入新的成績:"))
            d['score'] = score
            print('修改',name,'的成績為',score)
            return
        else:
            print('沒有找到',name,'的學生資料')

def delete_student_info(lst): #選項4
    name = input('請輸入要刪除資料的學生姓名:')
    for i in range(len(lst)):
        if lst[i]['name'] == name:
            del lst[i]
            print('已成功刪除',name)
            return True
        else:
            print('沒有找到',name,'的學生資料') 

def print_by_score_desc(lst): #選項5
    L = sorted(lst, key=lambda d:d['score'], reverse=True)
    output_student(L)

def print_by_score_asc(lst): #選項6
    L = sorted(lst, key=lambda d:d['score'])
    output_student(L)

def print_by_age_desc(lst): #選項7
    L = sorted(lst, key=lambda d:d['age'], reverse=True)
    output_student(L)

def print_by_age_asc(lst):
    L = sorted(lst, key=lambda d:d['age'])
    output_student(L)
        

main()
