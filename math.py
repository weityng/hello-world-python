# math.py
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    x = int(input("請輸入第一個數字: "))
    y = int(input("請輸入第二個數字: "))
    print(f"{x} + {y} = {add_numbers(x, y)}")
