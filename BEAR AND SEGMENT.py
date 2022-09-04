



# for _ in range(int(input())):
#     s=input();
#     one=s.find('1');
#     last=s.rfind('1');
#     if(one==-1 and last==-1 or s.count('0',one,last)>0):
#         print("NO");
#     else:
#         print("YES");


n = [0,0,1,0,1,0,1,0]
s1 = sorted(n)
print(s1)
count = 0
count1 = 0
for i in range(len(n)):
    if s1[i] == 1:
        count1 += 1
        print(count1)
for i in range(len(n)):
    if n[i] == 1:
        for j in range(i, len(n)):
            if n[j] == 1:
                count += 1
                print(count)
            else:
                break
        break

if count == 0:
    print("NO")
elif count == count1:
    print("YES")
else:
    print("NOO")




