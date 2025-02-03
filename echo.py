# 요청사항: 파이썬3로 사용자가 입력하는 문장을 그대로 출력하는 프로그램을 작성해줘.
def main():  
    user_input = input("문장을 입력하세요: ")
    print("입력한 문장:", user_input)

if __name__ == "__main__":
    main()


# 추가 요청사항: 사용자가 문장을 반복적으로 입력할 수 있도록 하고, 끝내고 싶을 때는 !quit을 입력하면 프로그램이 종료되도록 변경해줘
def main():
    while True:
        user_input = input("문장을 입력하세요 (!quit 입력 시 종료): ")

        if user_input == "!quit":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break 
        
        print("입력하신 문장은:", user_input)

    if __name__ == "__main__":
        main()