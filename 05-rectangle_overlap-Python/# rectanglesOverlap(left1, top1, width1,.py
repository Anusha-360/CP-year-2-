# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, or height. This function 
# takes two rectangles described this way, or returns True if the rectangles 
# overlap at all (even if just at a point), or False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, or while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    f1 = ((left2>left1)or(left2>left1+width1))
    f2 = ((left2>left1)or(left2>left1+width2))
    f3 = ((top1>top2) or (top1>top2+height1))
    f4 = ((top1>top2) or (top1>top2+height2))
    if (f1 or f2 or f3 or f4):
        return True
    else:
        return False

k = fun_rectangle_overlap(0,2,1,4,1,6,8,4)
print (k)