def equilateral(sides):
    x, b, c = sides
    return x == b == c and x > 0


def isosceles(sides):
    x, b, c = sides
    # 检查是否能构成三角形
    if x <= 0 or b <= 0 or c <= 0:
        return False
    if x + b <= c or x + c <= b or b + c <= x:
        return False
    # 检查等腰（至少两边相等）
    return x == b or x == c or b == c
    

def scalene(sides):
    x, b, c = sides
    return (x != b != c != x) and (x + b > c) and (x + c > b) and (b + c > x) and x > 0
