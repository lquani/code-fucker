### 223
https://leetcode.com/problems/rectangle-area/

### 难度
Medium

### 思考情况
bug free

#### 思路


#### code
```cpp
int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
    
        int x1 = max(ax1, bx1);
        int y1 = max(ay1, by1);
        int x2 = min(ax2, bx2);
        int y2 = min(ay2, by2);
        
        int w = max(0, x2 - x1);
        int h = max(0, y2 - y1);
        
        int area1 = (ax2 - ax1) * (ay2 - ay1);
        int area2 = (bx2 - bx1) * (by2 - by1);
        return area1 + area2 - w * h;
    }
```