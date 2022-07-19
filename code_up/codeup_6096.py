#바둑알 십자 뒤집기

#바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
#십자 뒤집기 횟수(n)가 입력된다.
#십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

#십자 뒤집기 결과를 출력한다.

locations = [ ]
for i in range(19):
    locations.append([])
    for j in range(19):
        locations[i].append(int(input().split()))

print(locations)