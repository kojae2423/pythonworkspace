## 슬라이싱 ## : 필요한 정보만 잘라서 가져온다.

jumin = "990120-1234576" # 컴퓨터의 시작은 0부터 시작한다.

print("성별 : " + jumin[7]) # []는 내가 원하는 자리의 값을 가져온다.
print("연 : " + jumin[0:2]) # : 은 0 부터 2직전까지 (0,1) 을 가져온다.
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지
# 맨 뒤는 -1 부터 시작해서 세자!