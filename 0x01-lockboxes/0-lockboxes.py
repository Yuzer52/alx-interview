def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is unlocked

    keys = [0]  # Starting with the keys in the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)

# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  

boxes = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))  

boxes = [[1, 2, 3], [], [1, 3], [2]]
print(canUnlockAll(boxes))  

