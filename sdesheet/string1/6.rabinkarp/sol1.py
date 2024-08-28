def stringMatch(text: str, pattern: str) :
    # Write your code here.
     result=[]
     print(len(text)-len(pattern)+1)
     print("k")
     for i in range(len(text)-len(pattern)+1):
         print(i)
         flag=1

         for j in range(len(pattern)):
             if i+j==12:
                 print("yello")
             if text[i+j]!=pattern[j]:
                 flag=0

         if flag==1:

             result.append(i+1)

     return result

print(stringMatch("abracadabrabr","abr"))