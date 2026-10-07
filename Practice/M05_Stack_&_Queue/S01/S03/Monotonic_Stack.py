#Monotonic Increasing Stack 
#General pattern:
arr=[4,12,5,3,1,2,5,3,1,2,4,6]
stack=[]
for x in arr:
    while stack and stack[-1]>x:
        stack.pop()
    stack.append(x) 

#Monotonic Decreasing Stack
#General pattern:
stack=[]
for x in arr:
    while stack and stack[-1]<x:
        stack.pop()
    stack.append(x)

#Next greater element
def NEXTGreaterElement(arr):
    stack=[]
    res=[-1]*len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]]<arr[i]:
            res[stack.pop()]=arr[i]
        stack.append(i)
    return res
arr=[4,12,5,3,1,2,5,3,1,2,4,6]
#output=[12,-1,6,5,2,5,6,4, 2, 2, 4, 6, -1]
print(NEXTGreaterElement(arr))