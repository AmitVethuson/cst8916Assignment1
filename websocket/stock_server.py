import asyncio
import websockets
import random

#function that sends data 
async def sendStockData():
    #URI of the websocket
    uri = "ws://localhost:8765"
    
    #connect to the websocket server
    async with websockets.connect(uri) as websocket:
        while True:
            #generate random prices between 0, 100000
            simulatedStockData = random.uniform(0,10000)
            #send data to the server
            await websocket.send(f"{simulatedStockData:.2f}")
            #wait 5 seconds before sending the next peice of data
            await asyncio.sleep(5)


#start the sending simulator
asyncio.get_event_loop().run_until_complete(sendStockData())