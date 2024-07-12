import random

class Index():
    """
    random nums are divided by random nums using the function map
    """
    def tryExcept(self):
        list_broke = [random.randint(1,100) for _ in range(10)]
        print(list_broke)
        try:
            transformation = list(map(lambda unit: (unit/random.randint(0,5)), list_broke))
            return transformation
        except ZeroDivisionError as e:
            return "no puedes dividir entre 0 idiota!"

if __name__ == "__main__":
    instances =Index()
    result = instances.tryExcept()
    print(result)