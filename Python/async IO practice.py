import time
import asyncio
import requests


async def function1():

# downloading a file using request
    url = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(url)
    open("instagram.ico", "wb").write(response.content)

    # await asyncio.sleep(1)
    print("fun 1")
    return "ABC"
    
async def function2():
    url = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(url)
    open("instagram2.ico", "wb").write(response.content)
    # await asyncio.sleep(1)
    print("fun 2")

async def function3():
    url = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(url)
    open("instagram3.ico", "wb").write(response.content)
    # await asyncio.sleep(4)
    print("fun 3")

# async def main():
#     task = asyncio.create_task(function1())
#     # await function1()
#     await function2()
#     await function3()

async def main():
    L = await asyncio.gather(
                            function1(),
                             function2(), 
                             function3(),
                             )
    print(L)


asyncio.run(main())