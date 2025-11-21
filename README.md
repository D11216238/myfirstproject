# My First Project

這個專案包含兩個 Python 應用程式：

1. **猜數字遊戲 (Number Guessing Game)**
2. **防呆計算機 (Safe Division Calculator)**

---

## 1. 猜數字遊戲 (Number Guessing Game)

### 功能說明 (Features)

這是一個簡單的猜數字遊戲，遊戲規則如下：

1. 程式會隨機產生一個 1 到 100 之間的整數
2. 玩家輸入猜測的數字
3. 程式會提示「太高了」或「太低了」
4. 當猜對時，程式會顯示「恭喜你！」並告知猜測次數
5. 玩家可以隨時輸入 'exit' 離開遊戲

### 如何執行 (How to Run)

```bash
python3 GN.py
```

### 遊戲示例 (Game Example)

```
歡迎來到猜數字遊戲！我已經選好了一個1到100之間的數字。
請輸入你的猜測（或輸入 'exit' 離開遊戲）：50
太低了！再試一次。
請輸入你的猜測（或輸入 'exit' 離開遊戲）：75
太低了！再試一次。
請輸入你的猜測（或輸入 'exit' 離開遊戲）：90
太高了！再試一次。
請輸入你的猜測（或輸入 'exit' 離開遊戲）：82
太低了！再試一次。
請輸入你的猜測（或輸入 'exit' 離開遊戲）：86
恭喜你！你猜對了，數字就是 86。你總共猜了 5 次。
```

### 功能特色 (Features)

- ✅ 隨機產生 1-100 的整數
- ✅ 提供即時提示（太高/太低）
- ✅ 記錄並顯示猜測次數
- ✅ 錯誤輸入處理
- ✅ 可隨時退出遊戲

### 技術實作 (Technical Implementation)

- 使用 Python 3 開發
- 使用 `random.randint()` 產生隨機數字
- 包含完整的錯誤處理機制

---

## 2. 防呆計算機 (Safe Division Calculator)

### 功能說明

這是一個安全的除法計算機，實作了 `safe_division(a, b)` 函式，能夠防止「除以零」錯誤，確保每次計算都安全。

### 功能特色

- ✅ 安全的除法運算
- ✅ 防止除以零錯誤
- ✅ 完整的單元測試覆蓋
- ✅ 支援正數、負數、浮點數運算
- ✅ 包含綠燈/紅燈測試場景驗證

### 檔案說明

- `safe_division.py` - 安全除法函式實作
- `test_safe_division.py` - 完整的單元測試
- `demo_safe_division.py` - 互動式示範程式
- `TEST_REPORT.md` - 詳細的測試報告（包含綠燈/紅燈場景）

### 如何執行

#### 執行單元測試
```bash
python3 -m unittest test_safe_division.py -v
```

#### 執行示範程式
```bash
python3 demo_safe_division.py
```

#### 在程式中使用
```python
from safe_division import safe_division

# 正常相除
result = safe_division(10, 2)  # 返回 5.0

# 除以零（防呆機制）
result = safe_division(10, 0)  # 返回 None，不會出錯
```

### 測試結果

✅ **綠燈（所有測試通過）**：當函式包含完整的防呆機制時，所有 7 個單元測試都通過。

❌ **紅燈（測試失敗）**：當移除防呆機制後，除以零的測試會失敗，程式拋出 `ZeroDivisionError`。

詳細測試報告請參閱 [TEST_REPORT.md](TEST_REPORT.md)

---

## 專案結構

```
.
├── GN.py                    # 猜數字遊戲
├── safe_division.py         # 安全除法函式
├── test_safe_division.py    # 單元測試
├── demo_safe_division.py    # 示範程式
├── TEST_REPORT.md           # 測試報告
└── README.md                # 專案說明（本檔案）
```

## 技術棧

- Python 3.12
- unittest (單元測試框架)
- 防禦性程式設計原則
