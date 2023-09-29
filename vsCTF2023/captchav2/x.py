import asyncio
import websockets
from PIL import Image
import io
def calc():
    img = Image.open('img.png')
    pxl = img.load()
    count = 0
    for i in range(200):
        for j in range(200):
            # print(pxl[i,j])
            if pxl[i,j]!=(240,240,240):
                count+=1
    s = (count/40000)*0.99348*100
    return s

async def main():
    uri = "ws://172.86.96.174:8000/echo"
    async with websockets.connect(uri) as websocket:
        await websocket.send("0")
        message = await websocket.recv()

        N = 101
        for _ in range(N):

            image = await websocket.recv() # image byte
            # print(image)
            with open('img.png','wb') as f:
                f.write(image)
                f.close()

            ans = str(calc())
            await websocket.send(ans)
            
            check = await websocket.recv() # check

            print(check)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
