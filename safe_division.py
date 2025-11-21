"""
安全除法模組 (Safe Division Module)

這個模組提供一個防呆的除法函式，確保不會因為除以零而導致程式錯誤。
"""


def safe_division(a, b):
    """
    安全的除法函式，防止除以零的錯誤。
    
    參數：
        a (float or int): 被除數
        b (float or int): 除數
    
    返回值：
        float: 除法結果，如果除數為零則返回 None
    
    範例：
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(-10, 2)
        -5.0
    """
    if b == 0:
        return None
    return a / b
