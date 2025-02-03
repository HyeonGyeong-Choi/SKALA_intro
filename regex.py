# 요청사항: 파이썬3로 정규 표현식을 사용하여 비밀번호를 검증하는 코드를 작성: 비밀번호의 조건은 최소 하나의 영문 소문자, 영문 대문자, 숫자 및 기호가 포함되어야 함.
import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern, password):
        return "유효한 비밀번호입니다."
    else:
        return "비밀번호가 조건을 충족하지 않습니다."

user_input = input("비밀번호를 입력하세요: ")
print(validate_password(user_input))

