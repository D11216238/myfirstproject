"""
防呆計算機示範程式 (Safe Division Calculator Demo)

這個程式示範 safe_division 函式的使用方式。
"""
from safe_division import safe_division


def main():
    """示範 safe_division 函式的各種使用情境"""
    print("=" * 60)
    print("防呆計算機示範 (Safe Division Calculator Demo)")
    print("=" * 60)
    print()
    
    # 測試案例
    test_cases = [
        (10, 2, "正常相除"),
        (100, 4, "正常相除"),
        (10, 0, "除以零（防呆）"),
        (-10, 2, "負數相除"),
        (10, -2, "負數相除"),
        (0, 5, "零當被除數"),
        (7, 2, "有小數結果"),
        (0, 0, "零除以零（防呆）"),
    ]
    
    print("測試結果：\n")
    for a, b, description in test_cases:
        result = safe_division(a, b)
        if result is None:
            print(f"  {a} ÷ {b} = None (除數為零，已防呆) - {description} ✅")
        else:
            print(f"  {a} ÷ {b} = {result} - {description}")
    
    print("\n" + "=" * 60)
    print("所有計算都安全完成，沒有程式錯誤！")
    print("=" * 60)
    
    # 互動式示範
    print("\n互動式計算器（輸入 'q' 結束）：")
    while True:
        try:
            user_input = input("\n請輸入算式 (例如: 10 / 2) 或 'q' 離開: ").strip()
            if user_input.lower() == 'q':
                print("感謝使用防呆計算機！")
                break
            
            # 解析輸入
            parts = user_input.split('/')
            if len(parts) != 2:
                print("❌ 請使用格式：數字 / 數字")
                continue
            
            a = float(parts[0].strip())
            b = float(parts[1].strip())
            
            result = safe_division(a, b)
            if result is None:
                print(f"⚠️  結果：除數為零！已防呆，返回 None")
            else:
                print(f"✅ 結果：{a} ÷ {b} = {result}")
        
        except ValueError:
            print("❌ 請輸入有效的數字！")
        except KeyboardInterrupt:
            print("\n\n感謝使用防呆計算機！")
            break


if __name__ == "__main__":
    main()
