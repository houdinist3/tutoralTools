import os
import sys
import time
import imageUtils

update = 3 # 디렉토리를 확인할 주기(초)
repeat = 4 # 디렉토리를 확인할 횟수

path = "" # 감시할 디렉토리 경로
destdir = "" # 저장될폴더 

# 디렉토리 감시 함수
def watchDir(path):
    print(time.ctime()) # 현재 시간 출력
    return os.stat(path).st_mtime # 디렉토리의 최종 수정 시간 반환

initCheck = watchDir(path) # 초기 디렉토리 상태 저장

startTime = time.time() # 시작 시간 저장
counter = 0 # 디렉토리 확인 횟수 초기화
while True:
    check = watchDir(path) # 디렉토리 상태 확인
    if initCheck != check: # 디렉토리 상태가 변경되었을 경우
        print("dir update, run someting") # 메시지 출력
        imageUtils.createProxy(path, destdir, "jpg")
        initCheck = check # 디렉토리 상태 업데이트

    counter += 1 # 디렉토리 확인 횟수 증가

    if counter == repeat: # 디렉토리 확인 횟수가 지정한 값에 도달하면
        sys.exit() # 프로그램 종료

    time.sleep(update - (time.time() - startTime) % update) # 디렉토리 확인 주기에 맞춰 대기
