import asyncio
from .pururin import get_pur, input

class Tomoe():
    def __init__(self, Pururin: str = input().pururin):
        self.pururin = Pururin

Api = Tomoe()

def main():
    async def main_pururin():
        await asyncio.gather(get_pur())

    if Api.pururin is not None:
        asyncio.run(main_pururin())

    else: 
        print("No arguments was given")

if __name__ == '__main__':
    main()
    