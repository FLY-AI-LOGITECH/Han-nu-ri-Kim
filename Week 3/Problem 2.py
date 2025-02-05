def solution(array, commands):
    answer = []
    for command in commands: 
        i, j, k = command # command의 세 원소에 대해 변수를 부여.
        sliced_array = array[i-1:j] # array 에서 i-1 번째 숫자에서 j까지 슬라이싱 
        sorted_array = sorted(sliced_array) # 슬라이싱 한 부분을 오름차순으로 정렬
        answer.append(sorted_array[k-1]) # sorted_array 의 k-1 번째 숫자를 answer에 추가 
    return answer
