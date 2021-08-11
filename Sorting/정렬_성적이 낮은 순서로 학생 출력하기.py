# n을 입력받기
n = int(input())

# n명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')

# 리스트명.sort() - 리스트형의 메소드, 리스트 원본값을 직접 수정
# sorted(리스트명) - 내장함수, 리스트 우너본 값은 그대로이고 정렬 값을 반환
