#두 개의 실수를 입력 받는다.
inputValue1 = float(input("첫 번째 값을 입력 하세요"))
inputValue2 = float(input("두 번째 값을 입력 하세요"))

#연산자를 입력한다.
inputValue3 = input("연산자를 선택 하세요 (+, -, *, / 중 하나 입력)")

#결과의 자료형을 입력한다.
inputValue4 = input("결과 값 자료형(integer, float, string 중 하나 입력)")

#결과 값을 저장할 변수 선언
res = 0

#입력 한 연산자에 따른 입력 받은 두 값의 연산결과를 저장한다.
if inputValue3 == '+':
    res = inputValue1 + inputValue2
elif inputValue3 == '-':
    res = inputValue1 - inputValue2
elif inputValue3 == '*':
    res = inputValue1 * inputValue2
elif inputValue3 == '/':
    res = inputValue1 / inputValue2

#연산 결과를 입력한 자료형으로 변환한다.
if inputValue4 == "integer":
    res = int(res)
elif inputValue4 == "float":
    res = float(res)
elif inputValue4 == "string":
    res = str(res)

#최종 결과 값을 출력한다.
print("결과 값은 아래와 같습니다.")
print(inputValue1, inputValue3, inputValue2, "=", res)