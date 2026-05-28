def score(x, y):
    # 计算平方和，避免重复书写
    dist_sq = x**2 + y**2
    
    # 使用 if-elif-else 保证只会执行其中一个分支
    if dist_sq <= 1**2:      # 内圈
        return 10
    elif dist_sq <= 5**2:    # 中间圈
        return 5
    elif dist_sq <= 10**2:   # 外圈
        return 1
    else:                    # 目标外
        return 0
    
        
