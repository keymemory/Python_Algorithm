# n을 입력받기
n = int(input())

# n개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
    print(i, end=' ')

# 리스트명.sort() - 리스트형의 메소드, 리스트 원본값을 직접 수정
# sorted(리스트명) - 내장함수, 리스트 우너본 값은 그대로이고 정렬 값을 반환
