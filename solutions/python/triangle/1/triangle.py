def equilateral(sides):
    a, b, c = sides
    return a == b == c and a > 0


def isosceles(sides):
    a, b, c = sides
    # 检查是否能构成三角形
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    # 检查等腰（至少两边相等）
    return a == b or a == c or b == c
    

def scalene(sides):
    a, b, c = sides
    return (a != b != c != a) and (a + b > c) and (a + c > b) and (b + c > a) and a > 0
