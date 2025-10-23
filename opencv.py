import cv2

# 키 입력 대기 시간 설정 (33ms)
WAIT_KEY_MS = 33

# 1. 사진 파일 읽기
image_path = "/home/snue990318nsh/Desktop/screen.png" # 준비한 사진 파일 경로로 변경하세요.
img = cv2.imread(image_path)

# 2. 이미지 로드 성공 확인
if img is None:
    print(f"오류: '{image_path}' 파일을 읽을 수 없습니다. 경로와 파일명을 확인하세요.")
else:
    # 3. 사진 출력
    cv2.imshow("Image Viewer", img)
    print("사진을 출력했습니다. 키 입력 대기 중...")
    
    # 4. 키 입력 대기 및 창 닫기
    # waitKey(0)은 무한 대기하며, 어떤 키를 누르면 다음 줄로 넘어갑니다.
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    print("창을 닫았습니다.")