import asyncio
import websockets
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
#stock data to plot
stockdata = []
#time data to plot
times = []


async def handel_stock_data(websocket,path):
    try:
        #listen to for messages on the websocket
        async for message in websocket:
            
            #get current date information
            currentdateInfo = datetime.now()
            #format todays date
            today = f"{currentdateInfo.day}-{currentdateInfo.month}-{currentdateInfo.year}"
            #formate current time
            currentTime = f"{currentdateInfo.hour}:{currentdateInfo.minute}:{currentdateInfo.second}"
            
            #prints the stock price received from the stock server
            print(f"Stock Price (CAD): {message} at {currentdateInfo} ")
            
            
            # add stock and time data to respective lists
            stockdata.append(float(message))
            times.append(currentTime)
            
            # ----------- plot ------------
            plt.ion()
            plt.clf()
            plt.plot(times,stockdata,marker='.', markersize=10)
            plt.ylim(0, 10000)
            plt.xticks(times, rotation=90)
            plt.xlabel("Time")
            plt.ylabel("Price (CAD)")
            plt.title(f"Stock Price {today}")
            plt.pause(1) 
            plt.show()
            
            
            
    #handle if the connection is closed      
    except websockets.exceptions.ConnectionClosedOK:
        print(f"Connection closed by {websocket.remote_address}")
    #handle if  there is an error
    except Exception as e:
        print(f"Error occurred: {e}")

#start a websocket server to port using the function
startServer = websockets.serve(handel_stock_data,"localhost",8765)

#start server and have it running
asyncio.get_event_loop().run_until_complete(startServer)
asyncio.get_event_loop().run_forever()