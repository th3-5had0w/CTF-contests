#!/usr/bin/python3
import socket

# Địa chỉ IP và port của server
IP, PORT = ('167.71.204.85', 20001)

# Hàm này nhận một dòng (line) từ socket
def receive_one_line(s):
    r = b''

    # Lần lượt nhận từng ký tự, nếu là ký tự xuống dòng thì ngưng
    while (True):
        t = s.recv(1)
        if t == b'\n': break
        r = r + t

    # Trả về kết quả dạng string
    return r.decode()

# Hàm này gửi một dòng (line) đến socket
def send_one_line(s, data):
    # Bỏ hết ký tự xuống dòng trong data (nếu có) và gửi đến server
    data = data.strip()
    s.send((data + '\n').encode())

def main():
    # Tạo một socket và kết nối đến server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    # Nhận và in dòng đầu mà server trả về
    banner = receive_one_line(s)
    print(banner)
    print(receive_one_line(s))
    send_one_line(s, '100')
    print(receive_one_line(s))
    send_one_line(s, '14285')
    print(receive_one_line(s))

    # Các bạn đừng ngần ngại mà chạy file python này.
    # Hãy cố gắng tìm hiểu cách giao tiếp với máy chủ thông qua socket tại đây nhé,
    # Tắt connection đến server
    s.close()

if __name__ == '__main__':
    main()
