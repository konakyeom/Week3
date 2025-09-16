import pyfirmata2
import time

# Arduino 연결
board = pyfirmata2.Arduino('COM4')  # 포트 번호 확인 후 변경

# Iterator 시작 (필수!)
it = pyfirmata2.util.Iterator(board)
it.start()

print("✅ Arduino 연결 성공!")

# LED 출력 테스트
led1 = board.get_pin('d:13:o')  # 디지털 13번, 출력 모드
led2 = board.get_pin('d:3:o')   #디지털 3번

print("LED 테스트 시작...")
for i in range(3):
    led1.write(1)
    led2.write(1)
    print(f"LED ON ({i+1}/3)")
    time.sleep(0.5)
    led1.write(0)
    led2.write(0)
    print(f"LED OFF ({i+1}/3)")
    time.sleep(0.5)

print("✅ 테스트 완료!")
board.exit()