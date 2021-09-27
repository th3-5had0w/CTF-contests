#!/usr/bin/python3
import socket
import json
import struct
import logging

# Cấu hình tập tin lưu log của server
logging.basicConfig(filename='./log/kid_server.log', format='%(asctime)s %(message)s')

class KidServer:
    def __init__(self, host, port):
        # Khởi tạo UDP socket và lắng nghe kết nối
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((host, port))
        self.fileList = ["intro.txt", "flag.txt"]

    def start(self):
        # Vòng lặp vô hạn xử lý các gói tin nhận được
        while(True):
            try:
                rawPacket, clientIP = self.socket.recvfrom(4096)
                data = self.handle(rawPacket)
                self.response(data, clientIP)
            except KeyboardInterrupt:
                exit()
            except:
                logging.exception("")

    # Xử lý gói tin nhận được
    def handle(self, rawPacket):
        try:
            kidPacket = KidPacket(rawPacket)
            action = getValue(kidPacket.body, "action")
            inputFile = getValue(kidPacket.body, "file")

            if action == "read":
                if inputFile in self.fileList:
                    file = inputFile
                else: 
                    file = "intro.txt"

                with open(file, "r") as f:
                    return f.read()

            return "Wrong action"
        except Exception as e:
            return str(e)

    # Gửi phản hồi về cho client
    def response(self, data, clientIP):
        self.socket.sendto(bytes(data, encoding="utf8"), clientIP)
    
def getValue(object, key):
    try:
        return object[key]
    except KeyError:
        raise Exception("Missing '%s' param" % key)

class KidPacket:
    def __init__(self, rawPacket):
        self.parse(rawPacket)

    # Hàm xử lý / kiểm tra cấu trúc gói tin
    def parse(self, rawPacket):
        #
        #   Dòng code bên dưới đang chuyển đổi 2 bytes đầu của gói tin
        # từ dạng little endian về dạng số, đây là phần contentLength.
        # Em có thể tìm hiểu thêm hàm struct.pack(), nó sẽ giúp em 
        # chuyển đổi theo chiều ngược lại.
        #
        self.contentLength = struct.unpack("<H", rawPacket[0:2])[0]

        # Các bytes còn lại của gói tin được xem là phần dữ liệu
        data = rawPacket[2:]

        if self.contentLength != len(data):
            raise Exception("Bad content-length")

        # Chuyển đổi dữ liệu nhận được thành JSON object
        try:
            self.body = json.loads(data)
        except:
            raise Exception("Bad format")

def main():
    # Khởi tạo server lắng nghe trên 0.0.0.0:3108
    server = KidServer("0.0.0.0", 3108)
    server.start()

main()