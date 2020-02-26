from menu import show_menu
from student_info import *

#主要函數，用來選取操作選項並實現設定功能
def main():
    docs = [] #這個列表是用來儲存所輸入的學生資料
    while True:
        show_menu()
        s = input("請選擇下列選項:")
        if s == '1': #添加學生資料(姓名,年齡,成績)
            docs += input_student()
        elif s == '2': #查看所輸入的學生資料列表
            output_student(docs)
        elif s == '3': #修改學生成績
            modify_student_info(docs)
        elif s == '4': #刪除學生資料
            delete_student_info(docs)
        elif s == '5': #成績由高到低排列
            print_by_score_desc(docs)
        elif s == '6': #成績由低到高排列
            print_by_score_asc(docs)
        elif s == '7': #年齡由高到低排列
            print_by_age_desc(docs)
        elif s == '8': #年齡由低到高排列
            print_by_age_asc(docs)
        elif s == 'q': #退出
            return
main()