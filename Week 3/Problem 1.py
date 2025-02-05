def solution(sizes):
    adjusted_sizes = [(max(size),min(size)) for size in sizes] # 가장 큰 값을 가로에, 가장 작은 값을 세로에 배치
    max_width = max(size[0] for size in adjusted_sizes) # 가로에 저장된 값들 중 가장 큰 값을 저장
    max_height = max(size[1] for size in adjusted_sizes) # 세로에 저장된 값들 중 가장 큰 값을 저장
    answer = max_width * max_height # 넓이 계산
    return answer
