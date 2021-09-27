#!/usr/bin/python3

# Cài đặt các thư viện cần thiết, chạy lệnh sau:
# python3 -m pip install -r requirements.txt

import socket
import json
import yaml
import struct
import zlib
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
        while True:
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

            if action == "read":
                inputFile = getValue(kidPacket.body, "file")
                if inputFile not in self.fileList:
                    inputFile = "intro.txt"

                with open(inputFile, "r") as f:
                    return f.read()

            return "Wrong action"
        except KidException as ex:
            return str(ex)
        except Exception:
            return "Bad packet"

    # Gửi phản hồi về cho client
    def response(self, data, clientIP):
        self.socket.sendto(bytes(data, encoding="utf8"), clientIP)

def getValue(object, key, default=None):
    try:
        return object[key]
    except KeyError:
        raise Exception("Missing '%s' param" % key)

class KidException(Exception):
    pass

class KidPacket:
    def __init__(self, rawPacket):
        self.parse(rawPacket)

    def parse(self, rawPacket):
        #
        #   Dòng code bên dưới đang chuyển đổi 2 bytes đầu của gói tin
        # từ dạng little endian về dạng số, đây là phần contentLength.
        # Em có thể tìm hiểu thêm hàm struct.pack(), nó sẽ giúp em
        # chuyển đổi theo chiều ngược lại.
        #
        self.contentLength = struct.unpack("<H", rawPacket[0:2])[0]

        # Bóc tách contentType và checksum từ gói tin
        self.contentType = struct.unpack("<H", rawPacket[2:4])[0]
        self.checksum = struct.unpack("<I", rawPacket[4:8])[0]

        # Các bytes còn lại của gói tin được xem là phần dữ liệu
        data = rawPacket[8:]

        if self.checksum != zlib.crc32(data):
            raise KidException("Bad checksum")
        data = zlib.decompress(data)

        if self.contentLength != len(data):
            raise KidException("Bad content-length")

        # Chuyển đổi dữ liệu từ dạng JSON / Yaml
        try:
            if self.contentType == 0x01:
                self.body = json.loads(data)
            elif self.contentType == 0x02:
                self.body = yaml.load(data)
            else:
                raise KidException("Unsupported contentType")
        except:
            raise KidException("Bad format")
        
def main():
    # Khởi tạo server lắng nghe trên 0.0.0.0:3109
    server = KidServer("0.0.0.0", 3109)
    server.start()

main()