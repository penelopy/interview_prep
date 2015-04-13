def moveTower(height, source, helper, target):
    if height >= 1:
        moveTower(height - 1, source, helper, target)
        moveDisk(source,target)
        moveTower(height - 1, helper, source, target)

def moveDisk(source,target):
    print("moving disk from",source,"to",target)

moveTower(3,"A","B","C")