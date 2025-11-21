"""
安全除法單元測試 (Safe Division Unit Tests)

這個模組包含 safe_division 函式的完整單元測試。
測試涵蓋正常情況、邊界值、負數、以及除以零的情境。
"""
import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """safe_division 函式的測試類別"""
    
    def test_normal_division(self):
        """測試正常的數值相除"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(100, 4), 25.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_negative_numbers(self):
        """測試負數相除"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_by_zero(self):
        """測試除以零的情況（防呆機制）"""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(0, 0))
        self.assertIsNone(safe_division(-10, 0))
    
    def test_zero_dividend(self):
        """測試被除數為零的情況"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -5), 0.0)
    
    def test_boundary_values(self):
        """測試邊界值"""
        self.assertEqual(safe_division(1, 1), 1.0)
        self.assertAlmostEqual(safe_division(0.1, 0.1), 1.0)
        self.assertEqual(safe_division(1000000, 1), 1000000.0)
    
    def test_float_division(self):
        """測試浮點數相除"""
        self.assertAlmostEqual(safe_division(10.5, 2.5), 4.2)
        self.assertAlmostEqual(safe_division(1.0, 3.0), 0.333333, places=5)
    
    def test_very_small_numbers(self):
        """測試非常小的數值"""
        self.assertAlmostEqual(safe_division(0.001, 0.1), 0.01)
        self.assertIsNotNone(safe_division(1, 0.0001))


if __name__ == '__main__':
    unittest.main()
