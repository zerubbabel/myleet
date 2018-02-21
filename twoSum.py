# n*lg(n)
# brute force and binary search
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find(L,R,k):#binary search
            ans=-1
            while L<=R:
                mid=(L+R) // 2
                if lst[mid][0]==k:
                    ans=mid
                    break
                elif lst[mid][0]>k:
                    R=mid-1
                else:
                    L=mid+1				
            return ans	


        n=len(nums)-1
        lst=[]
        for i in range(n+1):
            lst.append((nums[i],i))

        lst.sort()

        for i in range(n):
            j=find(i+1,n,target-lst[i][0])
            if (j>0):
                return [lst[i][1],lst[j][1]]
                break