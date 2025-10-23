import cv2
import datetime
import os
import sys # 프로그램 강제 종료 시 자원 해제를 위해 sys 모듈 추가

# --- 설정 ---
# 키 입력 대기 시간 설정 (33ms)
WAIT_KEY_MS = 33

# 비디오 파일 경로 설정 (사용자 경로로 지정)
# NOTE: 이 경로는 사용자 환경에 맞춰 변경해야 합니다.
video_path = "/home/snue990318nsh/Desktop/example.mp4" 

# 출력 파일을 저장할 디렉토리 설정 (선택 사항: 현재 디렉토리에 저장하려면 빈 문자열("") 사용)
OUTPUT_DIR = "opencv_output" 

# --- 함수 정의 ---
def get_timestamp():
    """현재 시간을 'YYYYMMDD_HH-MM-SS' 형식으로 반환합니다."""
    return datetime.datetime.now().strftime("%Y%m%d_%H-%M-%S")

def ensure_output_dir():
    """출력 디렉토리가 없으면 생성합니다."""
    if OUTPUT_DIR and not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"출력 디렉토리가 생성되었습니다: '{OUTPUT_DIR}'")

# --- 메인 실행 ---
def main():
    # 출력 디렉토리 확인 및 생성
    ensure_output_dir()
    
    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)

    # 비디오 로드 확인
    if not cap.isOpened():
        print(f"오류: '{video_path}' 파일을 열 수 없습니다. 경로 또는 코덱을 확인하세요.")
        sys.exit(1)

    print(f"'{video_path}' 재생 시작.")
    print("--- 단축키 안내 ---")
    print("ESC: 프로그램 종료")
    print("z (Ctrl+Z): 화면 캡쳐 (.png)")
    print("x (Ctrl+X): 녹화 시작 (.mp4)")
    print("c (Ctrl+C): 녹화 중지")

    # 녹화 관련 변수 초기화
    is_recording = False
    out = None

    # 비디오 속성 가져오기
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    try:
        while True:
            # 프레임 읽기
            ret, frame = cap.read()

            # 비디오 끝에 도달했거나 프레임을 읽지 못했을 경우
            if not ret:
                print("비디오의 끝에 도달했습니다.")
                break
            
            # ----------------------------------------------------
            # 1. 현재 녹화 중인 경우: 프레임을 비디오 파일에 쓰기
            #    (키 입력 처리 전에 저장하여 프레임 손실 방지)
            if is_recording and out is not None:
                out.write(frame)

            # ----------------------------------------------------
            # 2. 키 입력 대기 및 처리
            key = cv2.waitKey(WAIT_KEY_MS) & 0xFF 

            # ESC: 프로그램 종료 (아스키 코드 27)
            if key == 27:
                print("ESC 키 입력. 프로그램을 종료합니다.")
                break

            # z (Ctrl+Z): 화면 캡쳐
            if key == ord('z'):
                timestamp = get_timestamp()
                filename = os.path.join(OUTPUT_DIR, f"Capture_{timestamp}.png")
                cv2.imwrite(filename, frame)
                print(f"✔️ 화면 캡쳐: {filename}")

            # x (Ctrl+X): 동영상 녹화 시작
            if key == ord('x') and not is_recording:
                timestamp = get_timestamp()
                filename = os.path.join(OUTPUT_DIR, f"Record_{timestamp}.mp4")
                
                # 코덱 설정 (mp4v가 일반적이며, 안될 경우 XVID 시도)
                fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
                # fourcc = cv2.VideoWriter_fourcc(*'XVID') # 대안 코덱
                
                out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))
                
                is_recording = True
                print(f"🔴 녹화 시작: {filename}")
            
            # c (Ctrl+C): 녹화 중지
            if key == ord('c') and is_recording:
                is_recording = False
                if out is not None:
                    out.release() # VideoWriter 객체 해제 (파일 저장 완료)
                    out = None
                    print("⏹️ 녹화 중지.")

            # ----------------------------------------------------
            # 3. 화면 표시 (녹화 상태 반영)
            # 녹화 중일 경우, 현재 프레임에 'RECORDING' 텍스트를 오버레이
            if is_recording:
                cv2.putText(frame, 'RECORDING', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
            # 최종 프레임을 화면에 출력
            cv2.imshow('Video Player', frame)

    except KeyboardInterrupt:
        # 터미널에서 Ctrl+C 강제 종료 시 발생
        print("\nKeyboardInterrupt 감지. 프로그램 종료 중...")
        
    finally:
        # --- 자원 해제 ---
        cap.release()
        if is_recording and out is not None:
            out.release() # 프로그램 종료 전에 녹화 중이었다면 저장하고 해제
        cv2.destroyAllWindows()
        print("프로그램이 완전히 종료되었습니다.")

if __name__ == "__main__":
    main()