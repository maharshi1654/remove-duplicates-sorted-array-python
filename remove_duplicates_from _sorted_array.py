nums=[1,1,2]
numn=[]
numn.append(nums[0])
j=0
for i in range(1,len(nums)):
    if nums[i]==numn[j]:
        continue
    else:
        numn.append(nums[i])
        j+=1
nums[:]=numn
print(nums)