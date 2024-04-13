import json
import os


def load_student_data() -> list:
    """
    Load student data from JSON file.
    """
    file_path = 'students.json'
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        raise FileNotFoundError("找不到 students.json 檔案")

def get_student_info(student_id: str) -> dict:
    """
    Get student information by student ID.
    """
    student_data = load_student_data()
    for student in student_data:
        if student['student_id'] == student_id:
            return student
    raise ValueError(f"學號 {student_id} 找不到")

def add_course(student_id: str, course_name: str, course_score: str) -> None:
    """
    Add a course and its score for a specific student.
    """
    assert course_name!="" and course_score!="", "課程名稱或分數不可空白"
    course_score=float(course_score)
    student_data = load_student_data()
    for student in student_data:
        if student['student_id'] == student_id:
            student['courses'].append({'name': course_name, 'score': course_score})
            with open('students.json', 'w', encoding='utf-8') as file:
                json.dump(student_data, file, ensure_ascii=False, indent=2)
            print("課程已成功新增。")
            return
    raise ValueError(f"學號 {student_id} 找不到")

def calculate_average_score(student_data: dict) -> float:
    """
    Calculate the average score of a student.
    """
    total_score = sum(course['score'] for course in student_data['courses'])
    num_courses = len(student_data['courses'])
    if num_courses == 0:
        return 0.0
    else:
        return total_score / num_courses
while True:
    print("***************選單***************")
    print("1. 查詢指定學號成績")
    print("2. 新增指定學號的課程名稱與分數")
    print("3. 顯示指定學號的各科平均分數")
    print("4. 離開")
    print("**********************************")
    choice = input("請選擇操作項目：")
    if choice == '1':
        student_id = input("請輸入學號: ")
        try:
            student_info = get_student_info(student_id)
            print("=>學生資料:", json.dumps(student_info, ensure_ascii=False, indent=2))
        except ValueError as e:
            print("=>發生錯誤:", e)
    elif choice == '2':
        student_id = input("請輸入學號: ")
        course_name = input("請輸入要新增課程的名稱: ")
        course_score = (input("請輸入要新增課程的分數: "))
        try:
            add_course(student_id, course_name, course_score)
        except ValueError as e:
            print("=>其它例外:", e)
        except AssertionError as e:
            print("=>其它例外:", e)
    elif choice == '3':
        student_id = input("請輸入學號: ")
        try:
            student_info = get_student_info(student_id)
            avg_score = calculate_average_score(student_info)
            print("=>各科平均分數:", avg_score)
        except ValueError as e:
            print("=>發生錯誤:", e)
    elif choice == '4':
        print("=>程式結束。")
        break
    else:
        print("=>請輸入有效的選項。")