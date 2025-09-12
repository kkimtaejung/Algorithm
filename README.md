# Algorithm

<details>

 <img width="1180" height="694" alt="image" src="https://github.com/user-attachments/assets/9e764324-973d-40ce-9f4b-fcd871888458" />
 
 <summary> 백준 - 소수 구하기(완) </summary>
 
  * [1929 - 2025.09.09](1929_s3_20250909.py)
  
    생각의 흐름은 다음과 같음.
    
    a 부터 b 까지의 범위니 for 문 하나 필요, a부터 i까지 탐색하며 소수를 찾아야 하니 for 문 하나 더 필요
    > 시간초과
      
    소수가 아닐 때는 바로 break 하여 탈출하기
    > 시간초과
      
    2번째 for문에서 루트 i만큼만 탐색하면 됨
    > 틀림: a=1,2 일때의 예외처리
      
    a=1,2 일때 조건문으로 바로 2가 출력되도록하여 예외처리 해결
    > 틀림: b=1 일때의 예외 조건을 생각하지 못함
      
    b!=1 일때만 반복문 실행되도록 수정
    > 정답

</details>

<details>

 <img width="984" height="1241" alt="image" src="https://github.com/user-attachments/assets/c4e87db8-31e4-4bf8-b4b7-8f6d1a4bf650" />

 
 <summary> 백준 - 소수 구하기(도전 중) </summary>
 
  * [18110 - 2025.09.10](18110_s4_20250910.py)
  
    생각의 흐름은 다음과 같음.
    
    예제 2번이 잘 이해가 되지 않음, N 에 대한 좌우 15% 씩 제외하고 더한 값들을 나누면 12가 나옴, 13이 어떻게 나오지?
    > 문제못품

    문제를 잘못 이해함, 15%의 기준은 가장 큰/작은 점수를 기준으로 하는 것이었음 + 0일때 에외처리 추가 (sort, pop 등을 활용)
    > 33% 에서 시간초과

    반올림 정수 표기법, 슬라이싱 기법으로 연상량 대폭 감소
    > 33% 여전히 시간초과
    
    가장 큰 연산량은 값을 입력받을 때였고 sys.stdin.buffer.read()로 해결 (입력 구조 외워두고 활용하기)

    추가적으로 if 조건문에서 종료시키고 싶을 때 raise SystemExit 사용
    > 정답
    

</details>
