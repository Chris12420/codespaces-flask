import json

# 步驟 2：讀取 JSON 文件
with open('students.json', 'r') as file:
    data = json.load(file)

# 步驟 3：訪問 JSON 數據
students = data['students']

# 步驟 4：處理 JSON 數據
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()