import requests

def get_github_user_info(username):
    """
    주어진 GitHub 계정의 사용자 정보를 반환하는 함수.
    :param username: GitHub 계정 사용자 이름
    :return: 사용자 정보 딕셔너리 또는 오류 메시지 딕셔너리
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    # 상태 코드가 200일 경우 사용자 정보를 반환
    if response.status_code == 200:
        return response.json()
    # 상태 코드가 200이 아닐 경우 오류 메시지 반환
    else:
        return {"error": "사용자 정보를 가져올 수 없습니다."}

import unittest

class TestGitHubUserInfo(unittest.TestCase):
    
    def test_valid_user(self):
        """
        정상적인 GitHub 사용자 이름을 입력하여 사용자 정보를 확인
        """
        valid_user = "octocat"  # GitHub 공식 테스트 계정
        response = get_github_user_info(valid_user)
        self.assertIn("login", response, "정상 사용자 정보 검증 실패")
        self.assertEqual(response.get("login"), valid_user, "사용자 이름이 일치하지 않습니다.")
    
    def test_invalid_user(self):
        """
        존재하지 않는 GitHub 사용자 이름을 입력하여 오류 메시지 확인
        """
        invalid_user = "nonexistentuser12345"
        response = get_github_user_info(invalid_user)
        self.assertIn("error", response, "비정상 사용자 정보 검증 실패")
        self.assertEqual(response.get("error"), "사용자 정보를 가져올 수 없습니다.", "오류 메시지가 예상과 다릅니다.")
    
    def test_empty_username(self):
        """
        빈 GitHub 사용자 이름을 입력하여 오류 메시지 확인
        """
        response = get_github_user_info("")
        self.assertIn("error", response, "빈 사용자 이름 처리 실패")
        self.assertEqual(response.get("error"), "사용자 정보를 가져올 수 없습니다.", "빈 사용자 이름 처리 오류가 발생했습니다.")
    
    def test_special_character_username(self):
        """
        특수 문자가 포함된 GitHub 사용자 이름을 입력하여 오류 메시지 확인
        """
        response = get_github_user_info("!@#$%^&*")
        self.assertIn("error", response, "특수 문자 포함 사용자 이름 처리 실패")
        self.assertEqual(response.get("error"), "사용자 정보를 가져올 수 없습니다.", "특수 문자가 포함된 사용자 이름 처리 오류가 발생했습니다.")
    
if __name__ == "__main__":
    unittest.main()
