## 함수 ##

def open_account():   # 함수는 정의만 해주지 호출하기전까지는 실행하진 않는다.
    print("새로운 계좌가 생성되었습니다.")

# open_account()

## 전달값과 반환값 ##

def deposit(balance, money) : # 잔액 , 입금하는 돈
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))  # 함수 설정
    return balance + money # 반환

def withdraw(balance, money) : # 출금
    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money) : # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 두개의 값을 , 로 구분해서 반환해준다. 여러개의 값 가능!

balance = 0 # 잔액
balance = deposit(balance, 1000)  # 호출
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
