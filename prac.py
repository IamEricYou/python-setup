from tqdm import tqdm
 
class TestClass:
    variable: str = ""
    
    def __init__(self, variable: str) -> None:
        self.variable = variable
        
def test(arg1: int) -> None:
    test_list_appended = list()
    test_list = [i for i in range(0,100000)]
    for i in tqdm(test_list, desc="Looping now"):
        test_list_appended.append(i)
        
test(arg1=1)        