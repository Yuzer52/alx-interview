def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is unlocked

    keys = [0]  # Start with the keys in the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)


