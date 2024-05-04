#bài 1
# n = int(input())
# for i in range(n):
#     print('*'*(i+1))

#bài 2
# n = float(input("Nhập số thực dương n: "))
# while not n > 0 :
#     n = float(input("Nhập lại: "))
# print("Kết quả: ","{:.1f}".format(n))

#bài 3
# def fac(n):
#     if n < 0 : 
#         print("Invalid")
#         return 0 
#     P = 1
#     for i in range(2,n+1) : P *= i 
#     print(P) 
# n = int(input())
# fac(n)


#bài 4
# n = str(input("Input number: "))
# print("Sum of digits of",n,"=",sum([int(i) for i in n]))


#bài 5
# print("Number with sum of digits = 9")
# d = 10
# s = 1000
# while d:
#     if sum([int(i) for i in str(s)]) == 9:
#         print(s,end=' ')
#         d-=1
#     s+=1