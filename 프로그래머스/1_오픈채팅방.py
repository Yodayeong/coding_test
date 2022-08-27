def solution(record):
    record_list = dict()
    for i in record:
        now = i.split()

        if now[0] == 'Enter' or now[0] == 'Change':
            record_list[now[1]] = now[2]
    
    final = []
    for i in record:
        order = i.split()
        
        if order[0] == 'Enter':
            final.append(f'{record_list[order[1]]}님이 들어왔습니다.')
        elif order[0] == 'Leave':
            final.append(f'{record_list[order[1]]}님이 나갔습니다.')
    
    return final