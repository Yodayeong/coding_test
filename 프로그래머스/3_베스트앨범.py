#문제
#베스트 앨범 만듬
#1. 많이 재생된 노래가 있는 '장르' 먼저 수록 (각 장르별 2개씩)
#2. 장르 내에서도 '많이 재생된 순'으로 수록
#3. 재생 횟수가 같다면, 고유번호가 낮은 노래 먼저 수록
#return 베스트 앨범 내 노래 고유번호 순서대로

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    best_album = []

    while True:
        if len(plays) == 0:
            break
        
        #가장 큰 수가 들어있는 장르를 찾아주고
        #그 장르에 해당되는 id 값들을 찾아주자.
        largest = max(plays)
        for i in range(len(plays)):
            if plays[i] == largest:
                genre = genres[i]
        
        id = []
        for i in range(len(genres)):
            if genres[i] == genre:
                id.append(i)
        
        #이제, 장르 내에서 순서를 정해주자.
        if plays[id[0]] >= plays[id[1]]:
            temp = [id[0], id[1]]
        elif plays[id[0]] < plays[id[1]]:
            temp = [id[1], id[0]]
        
        for i in range(2, len(id)):
            if plays[id[i]] > plays[temp[0]]:
                temp.pop(0)
                temp.insert(0, id[i])
            elif plays[id[i]] == plays[temp[0]]:
                if id[i] < temp[0]:
                    temp.pop(0)
                    temp.insert(0, id[i])
                else:
                    temp.pop()
                    temp.append(id[i])
            elif plays[id[i]] > plays[temp[1]]:
                temp.pop()
                temp.append(id[i])
            elif plays[id[i]] == plays[temp[1]]:
                if id[i] < temp[1]:
                    temp.pop()
                    temp.append(id[i])
        
        #best앨범에 장르별 순서를 합쳐주기
        best_album.append(temp)

        print(id)
        #해당 장르의 plays 없애주기
        #pop으로 하자니까, index 값 계속 변함

        return best_album
    

print(solution(genres, plays))