from typing import List
from main import check_type, rule


@check_type
def test(name: List[str]):
    print(name)

@rule(target=[], dependencies="test")
def test_2():
    print("just for testing, test-2")

if __name__ == "__main__":
    #test(name=["2", "3"])
    test_2()