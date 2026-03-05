import hello
import my_math

def main():
    print("=== 主程式開始 ===")
    hello.say_hello()

    x = int(input("請輸入第一個數字: "))
    y = int(input("請輸入第二個數字: "))
    result = my_math.add_numbers(x, y)
    print(f"{x} + {y} = {result}")

    print("=== 主程式結束 ===")

if __name__ == "__main__":
    main()
