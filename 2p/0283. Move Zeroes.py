def moveZeroes(self, nums):
    # fillPointer代表将被填充的指针，指向将被非0数填充的位置
    # movePointer代表将被前移的指针，指向被前移的非0数
    fillPointer, movePointer = 0, 0
    
    # 如果前移指针没有越界，一直循环
    while movePointer < len(nums):
        if nums[movePointer] != 0:
            # 只有填充指针 ！= 前移指针时，两指针交换
            # 如果两指针相等，同时移动
            if fillPointer != movePointer:
                nums[fillPointer], nums[movePointer] = nums[movePointer], nums[fillPointer]
            fillPointer += 1
        # 每次循环都要移动前移指针
        movePointer += 1
    # 把后续所有数字全部置零
    while fillPointer < len(nums):
        if nums[fillPointer] != 0:
            nums[fillPointer] = 0
        fillPointer += 1
