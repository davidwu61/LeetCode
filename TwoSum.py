from calendar import different_locale
import time

def TwoSum(nums,target): 

    index1 = -1

    for index0,value in enumerate(nums):

        difference = target - value

        try:
            index1 = nums.index(difference)
        except:
            pass

        if index0 != index1 :
            return [index0,index1]
    

start = time.perf_counter_ns()

TwoSum([1,5,7,9,8],15)

end = time.perf_counter_ns()

print(end-start)
