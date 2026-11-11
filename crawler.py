import json
import requests
from bs4 import BeautifulSoup

def crawl_yonsei_programs():
    # 연세대학교 미래캠퍼스 비교과 사이트 URL (기본 목록 페이지)
    url = "https://with.yonsei.ac.kr/with/nsp.htm?ch=1"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.38 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    programs = []
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # HTML 파싱 (BeautifulSoup 활용)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 사이트 구조에 맞춰 목록 요소를 가져오는 로직 
        # (현재는 프로토타입용 샘플 데이터 구조와 연동되도록 기본 틀을 제공합니다)
        # 추후 사이트 상세 태그에 맞춰 정밀 조율할 수 있습니다.
        
        # 임시 예시 데이터 구조 삽입 (크롤링 연결 전 테스트용 기본 데이터)
        sample_data = [
            {
                "program_id": "2546",
                "title": "[비교과] 2026학년도 AI·SW 해커톤 역량 강화 특강",
                "purpose": "학생들의 AI 활용 기획 및 실무 역량 증진",
                "introduction": "아이디어 기획부터 프로토타이핑까지 실무를 배우는 특강",
                "operation_mode": "대면",
                "target_audience": "1~4학년 전체",
                "application_period": "2026.03.01 ~ 2026.03.15",
                "topic_name": "AI/SW",
                "operation_period": "2026.03.20 ~ 2026.03.22",
                "domain": "진로/취업",
                "category": "AI",
                "url": "https://with.yonsei.ac.kr/with/nsp.htm?ch=1&mode=view&tid=2546&ap_page=2"
            },
            {
                "program_id": "2522",
                "title": "[비교과] RC 리더십 세미나 및 공동체 운동 프로그램",
                "purpose": "기숙사 및 캠퍼스 생활 속 리더십 함양",
                "introduction": "리더십을 기르고 체력을 증진하는 야외/실내 활동",
                "operation_mode": "대면",
                "target_audience": "1~2학년",
                "application_period": "2026.03.05 ~ 2026.03.20",
                "topic_name": "운동/건강",
                "operation_period": "2026.03.25 ~ 2026.03.28",
                "domain": "대학생활",
                "category": "운동",
                "url": "https://with.yonsei.ac.kr/with/nsp.htm?ch=1&mode=view&tid=2522&ap_page=2"
            }
        ]
        
        programs = sample_data

    except Exception as e:
        print(f"크롤링 중 오류 발생: {e}")

    # JSON 파일로 저장
    with open("programs.json", "w", encoding="utf-8") as f:
        json.dump(programs, f, ensure_ascii=False, indent=4)
    
    print("programs.json 파일이 성공적으로 업데이트되었습니다!")

if __name__ == "__main__":
    crawl_yonsei_programs()
