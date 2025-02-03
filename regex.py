import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern, password):
        return "유효한 비밀번호입니다."
    else:
        return "비밀번호가 조건을 충족하지 않습니다."

user_input = input("비밀번호를 입력하세요: ")
print(validate_password(user_input))

