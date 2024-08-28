#Better to delay the job to the end days.
#Perform the maximum profit job.

#Sort According to the profit(des)
#Last day to perform a job. Cant perform beyond that.So n days.7 size array for 6 , put -1 Empty now.
#We can have a count of profit and simple cunt.
#Max Profit Deadline is 2.S on 2,Add the profit and cnt is 1.
#6 is done for 3rd so on 5. 



#GFG SOLN

class Job:
    # Job class which stores profit and deadline.
    def __init__(self, id=0, profit=0, deadline=0):
        self.id = id
        self.profit = profit
        self.deadline = deadline

class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # 1) Sort the jobs by profit in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # 2) Find the maximum deadline
        maxdeadline = max(job.deadline for job in Jobs)
        
        # 3) Initialize the hash array, cnt, and maxprofit
        hash = [-1] * (maxdeadline + 1)
        cnt = 0
        maxprofit = 0
        
        # 4) Schedule the jobs
        for job in Jobs:
            for j in range(job.deadline, 0, -1): #O cus the size of the array is like that.
                if hash[j] == -1:
                    cnt += 1
                    hash[j] = job.id
                    maxprofit += job.profit
                    break
        
        return cnt, maxprofit
    

#BELOW IS IF THE OBJECTS ARENT CREATED.
# class Job:
#     # Job class which stores profit and deadline.
#     def __init__(self, id=0, profit=0, deadline=0):
#         self.id = id
#         self.profit = profit
#         self.deadline = deadline

# class Solution:
#     # Function to find the maximum profit and the number of jobs done.
#     def JobScheduling(self, Jobs, n):
#         # 1) Create Job objects and sort them by profit in descending order
#         arr = [Job(Jobs[i][0], Jobs[i][1], Jobs[i][2]) for i in range(n)]
#         arr.sort(key=lambda x: x.profit, reverse=True)
        
#         # 2) Find the maximum deadline
#         maxdeadline = max(arr[i].deadline for i in range(n))
        
#         # 3) Initialize the hash array, cnt, and maxprofit
#         hash = [-1] * (maxdeadline + 1)
#         cnt = 0
#         maxprofit = 0
        
#         # 4) Schedule the jobs
#         for i in range(n):
#             for j in range(arr[i].deadline, 0, -1):
#                 if hash[j] == -1:
#                     cnt += 1
#                     hash[j] = arr[i].id
#                     maxprofit += arr[i].profit
#                     break
        
#         return cnt, maxprofit