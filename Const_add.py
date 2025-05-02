# class NumSum:
#     def __init__(self,num1,num2):
#         self.num1=num1;
#         self.num2=num2;
#         self.result=self.num1+self.num2;
#         print("Car is a created:",self.result);
# SUM1=NumSum(10,30)        
  
 # Creating class mathmetical operations
 
class Math:
     def __init__(self,num1,num2):
         self.num1=num1;
         self.num2=num2;
         self.result=self.num1-self.num2;
         self.result1=self.num1*self.num2;
         self.result2=self.num1/self.num2;
         self.result3=self.num1%self.num2;
         print("Calculate the subtraction:",self.result);
         print("Calculate the multiplication:",self.result1);
         print("Calculate the divide:",self.result2);
         print("Calculate the moduls:",self.result3);
# Create instance with all mathmetical operations         
num1=int(input("Enter the first number:"));
num2=int(input("Enter the first number:"));

#Creating instance

MATH1=Math(num1,num2)         