def solution(bandage, health, attacks):
    # 1초마다 x 만큼 체력회복
    # t초 동안 연속으로 붕대를 감는데 성공하면 y만큼의 체력을 추가로 회복

    # 최대 체력 보다 체력이 커지는건 X

    # 몬스터에게 공격을 당하거나 기술이 끝나면 '붕대 감기' 재시전 + 연속 성공시간 0초기화

    # 체력이 0 이하가 되면 캐릭터 사망 후 회복 X
    # 만약에 공격받고 죽으면 -1 리턴

    # 입력 : 붕대감기 기술정보(시전 시간, 1초당 회복량, 추가 회복량), 최대 체력, 몬스터의 공격 패턴
    # 출력 : 모든 공격을 받고 난 후 남은 체력

    max_time = attacks[-1][0] # 몬스터의 마지막 공격시간

    attack_list = [0]*(max_time+1) # 공격 목록을 리스트화

    for time, dam in attacks:
        attack_list[time] = dam
    
    heal_time = bandage[0] # 회복 진행 시간
    sec_heal = bandage[1] # 초당 회복량
    bonus_heal = bandage[2] # 추가 회복량
    
    current = health # 실시간 체력

    time = 0 # 시간
    contin = 0 # 연속 성공 시간

    while current > 0 and time < (max_time+1):
        if attack_list[time] != 0: # 공격당하는 경우
            current -= attack_list[time] # 현재 체력 - 데미지
            contin = 0 # 연속 성공 시간 0 초기화

        else: # 공격 당하지 않는 경우
            current += sec_heal # 초당 회복
            contin += 1 # 연속 성공 시간 + 1

            if contin == heal_time: # 연속으로 붕대를 감는데 성공하면 추가 회복
                current += bonus_heal # 추가 회복
                contin = 0 # 연속 성공 시간 0 초기화
            
            if current > health: # 최대 체력보다 체력이 높아질 수는 없음
                current = health
        
        time += 1
    
    if current <= 0:
        return -1
    else:
        return current
    