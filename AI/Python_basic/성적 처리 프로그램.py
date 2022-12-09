import sys
if len(sys.argv) > 1: # command 창에서 프로그램 실행 시 파일명을 입력했을 경우
    args=sys.argv[1]
    f_sys = open(args, 'r') #읽기모드로 파일을 연다
    line=f_sys.readlines() 
    f_sys.close()
# command 창에서 프로그램 실행 시 파일명을 입력하지 않았을 경우, default로 students.txt를 읽어온다
else: 
    f = open('students.txt', 'r') 
    line=f.readlines()
    f.close()

# 명령어 (1) - show
def show() :
    data.sort(key=lambda e: e[4], reverse=True) # 평균 점수를 기준으로 내림차순으로 정렬
    # 학생 성적 정보 출력
    print('%8s\t%8s     Midterm   Final  Average  Grade' %('Student','Name'))
    print('-'*60)
    for i in range(0,len(data)) :
        print('{}\t{:>12}\t{}\t{}\t{}\t{}'.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))

# 명령어 (2) - search
def search() :
    search_id=input('Student ID: ') # 찾을 학번 입력
    if search_id not in student_id : # 만약 찾을 학번을 가진 학생이 없다면, no search person 출력
        print('NO SUCH PERSON.')
    else : # 찾을 학번을 가진 학생이 있다면 해당 학생의 성적 정보 출력
        for i in range(0,len(data)) :
            if data[i][0] == search_id:
                print('%8s\t%8s     Midterm   Final  Average  Grade' %('Student','Name'))
                print('-'*60)
                print('{}\t{:>12}\t{}\t{}\t{}\t{}'.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
            else :
                continue

#명령어 (3) - changescore       
def changescore() : 
    changescore_id=input('Student ID: ') # 성적을 바꿀 학생의 학번 입력
    if changescore_id not in student_id : # 만약 해당 학번을 가진 학생이 없다면 no search person 출력
        print('NO SUCH PERSON.')
    else :
        change_test = input('Mid/Final? ') # 중간고사를 바꿀지 기말고사를 바꿀지 입력
        if change_test in ['mid', 'final'] : 
            change_score=int(input('Input new score: ')) # 새로 바꿀 성적 입력
            # 새로 바꿀 성적이 0점부터 100점 사이일 때 성적 정보 list를 새로운 성적으로 update하고 성적 바꾸기 전과 후의 결과를 출력
            if 0 <= change_score <= 100 : 
                for i in range(0,len(data)) :
                    if data[i][0] == changescore_id:
                        for i in range(0,len(data)) :
                            if data[i][0] == changescore_id: # 바꾸기 전의 성적 정보
                                print('%8s\t%8s     Midterm   Final  Average  Grade' %('Student','Name'))
                                print('-'*60)
                                print('{}\t{:>12}\t{}\t{}\t{}\t{}'.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
                                print('Score changed.') # 성적 정보를 새롭게 update하며 평균 점수와 학점을 다시 계산한다
                                if change_test=='mid' :
                                    data[i][2] = change_score
                                    data[i][4] = (float(data[i][2]) + float(data[i][3]))/2
                                    if data[i][4] >= 90 :
                                        data[i][5]='A'
                                    elif data[i][4] >=80 :
                                        data[i][5]='B'
                                    elif data[i][4] >=70 :
                                        data[i][5]='C'
                                    elif data[i][4] >=60 :
                                        data[i][5]='D'
                                    else :
                                        data[i][5]='F'
                                print('%8s\t%8s     Midterm   Final  Average  Grade' %('Student','Name')) #바꾼 후의 성적 정보 출력
                                print('-'*60)
                                print('{}\t{:>12}\t{}\t{}\t{}\t{}'.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))                                  
                            else :
                                continue

# 명령어 (4) - add
def add() :
    add_id=input('Student ID: ') # 새롭게 추가할 학번 입력
    if add_id in student_id : # 만약 해당 학번을 가진 학생이 이미 있다면 already exists 출력
        print('ALREADY EXISTS.')
    # 해당 학번을 가진 학생이 없다면 순서대로 이름, 중간고사 성적, 기말고사 성적을 입력받음
    else :
        student_id.append(add_id)
        add_name=input('Name: ') 
        add_mid = int(input('Midterm Score: '))
        add_final = int(input('Final Score: '))
        print('Student added.')
        add_avg= float((add_mid + add_final) / 2) # 새로운 성적 정보로 평균점수와 학점을 계산
        if add_avg>= 90 :
            add_grade='A'
        elif add_avg>=80 :
            add_grade='B'
        elif add_avg>=70 :
            add_grade='C'
        elif add_avg >=60 :
            add_grade='D'
        else :
            add_grade='F'
        data.append([add_id, add_name, add_mid, add_final, add_avg, add_grade]) # 성적 정보 list에 새로운 학생 성적 정보 추가

# 명령어 (5) - searchgrade
def searchgrade() :
    search_grade = input('Grade to search: ') # 찾을 학점 입력
    grade_list=[]
    if search_grade in ['A', 'B', 'C', 'D', 'F'] : 
        for i in range(0,len(data)) :
            grade_list.append(data[i][5])  # 현재 성적 정보에 저장된 학생들의 학점 정보를 리스트에 저장
        if search_grade not in grade_list : # 만약 찾을 학점을 가진 학생이 현재 없다면 no results출력
            print('NO RESULTS.')
        else : # 찾을 학점이 있다면 해당 학점을 가진 학생들의 성적정보를 출력
            print('%8s\t%8s     Midterm   Final  Average  Grade' %('Student','Name'))
            print('-'*60)
            for i in range(0,len(data)) :
                if data[i][5]==search_grade :
                    print('{}\t{:>12}\t{}\t{}\t{}\t{}'.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))                                  

# 명령어 (6) - remove
def remove() :
    if len(data) == 0 : # 만약 성적 정보 리스트가 이미 비어있다면, list is empty 출력
        print('List is empty.')
    else :
        remove_id=input('Student ID: ') # 제거할 학생의 학번 입력
        if remove_id not in student_id : # 만약 해당 학번을 가진 학생이 없다면 no such person 출력
            print('NO SUCH PERSON.')
        else : # 해당 학번의 학생 성적 정보 삭제
            for i in range(0,len(data)) :
                if data[i][0] == remove_id :
                    del data[i]
                    student_id.remove(remove_id)
                else :
                    continue
            print('Student removed.')

# 명령어 (7) - quit
def quit() :
    save_data=input('Save data?[yes/no] ') # 저장 여부
    if save_data == 'yes' : # 저장한다면 저장할 파일명 입력받음
        file_name=input('File name: ')
        f_save=open(file_name,'w') 
        data.sort(key=lambda e: e[4], reverse=True) # 평균 점수를 기준으로 내림차순으로 정렬한 이후 파일에 저장
        for i in range(0,len(data)) :
            f_save.write('{}\t{}\t{}\t{}\n'.format(data[i][0], data[i][1], data[i][2], data[i][3]))
        f_save.close()
        sys.exit() # 프로그램 종료
    elif save_data == 'no' :
        sys.exit() # 저장하지 않는다고 했을 때 프로그램 종료

# 프로그램 실행 시, 파일 읽어오기 
data=[] # 성적 정보를 저장할 list
student_id=[] # 학번만을 저장할 list
for i in range(0,len(line)) : # 학번, 이름, 중간고사 성적, 기말고사 성적을 list에 저장
    data.append([line[i].split()[0], line[i].split()[1]+' '+line[i].split()[2], line[i].split()[3], line[i].split()[4]])
    student_id.append(line[i].split()[0]) # 학번만을 list에 저장
for i in range(0,len(line)) : # 중간고사와 기말고사 성적으로 각 학생별 평균을 구한다.
    avg = ((float(line[i].split()[3]) + float(line[i].split()[4])) / 2)
    avg=round(avg,1)
    data[i].append(avg)
    if avg>= 90 : #평균>= 90 일 때, 학점은 A
        grade='A'
    elif avg>=80 : # 평균>=80 일 때, 학점 B
        grade='B'
    elif avg>=70 : # 평균>=70 일 때, 학점 C
        grade='C'
    elif avg >=60 : #평균>=60 일 때, 학점 D
        grade='D'
    else :  
        grade='F' # 평균<60 일 때, 학점 F
    data[i].append(grade) # 성적 정보를 저장해놓은 list에 평균과 학점 정보를 추가한다.
print(); show(); print() # 전체 학생의 성적 정보를 출력한다.

#명령어 입력 및 실행 단계
while True : # quit을 입력받아 프로그램이 종료되기 까지 명령어를 무한으로 입력받는다
    command=input('#') # #뒤에 명령어를 입력한다
    command=command.lower() # 명령어 입력 시, 대소문자 구별하지 않기 위해 모두 소문자로 변환하여 전달한다.
    if command == "show": # 명령어 show 실행
        show(); print()
    elif command=='search' : # 명령어 search 실행
        search(); print()
    elif command == 'changescore' : # 명령어 changescore 실행
        changescore(); print() 
    elif command== 'searchgrade' : # 명령어 searchgrade 실행
        searchgrade(); print()
    elif command=='add' : # 명령어 add 실행
        add(); print()
    elif command=='remove' : # 명령어 remove 실행
        remove(); print()
    elif command=='quit' : # 명령어 quit 실행
        quit(); print()

