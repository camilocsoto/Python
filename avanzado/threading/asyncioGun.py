import asyncio
from dataclasses import dataclass, field

@dataclass
class Weapon():
    name:str
    charger:list = field(default_factory=lambda:['⁍' for _ in range(8)]) 
    
    async def dropCasquette(self):
        if not self.charger:
            print('Charger is empty, please reload.')
        await asyncio.sleep(0.5)
        return 'fallin...' 
    
    async def fireGun(self):
        if not self.charger:
            print('no ammunuution, please reload.')
        print(self.charger)
        self.charger.pop(0)
        print(await asyncio.gather(
            self.dropCasquette(),
            self.dropCasquette(),
            self.dropCasquette()
            )
        )
              
        
        
if __name__ == "__main__":
    ak47 = Weapon('AK-47')
    while ak47.charger != []:
        asyncio.run(ak47.fireGun())