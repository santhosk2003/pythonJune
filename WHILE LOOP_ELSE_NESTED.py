
# i=0
# while i <20:
#     if i==5:
#         i=i+1
#         continue
#     print(i,end=" ")
#     i=i+1
# else:
#     print("no breaks")
# print("done")

# NESTED LOOP

# i=0
# while i<5:
#     j=0
#     while j<4:
#         print(i,j)
#         j=j+1
#     i=i+1

# i=0
# while i<3:
#     j=0
#     while j<2:
#         k=0
#         while k<1:
#             print(f"i={i},j={j},k={k}")
#             k=k+1
#         j=j+1
#     i=i+1
#
# i=0
# while i<4:
#     if i==1:
#         i=i+1
#         break
#     j=0
#     while j<3:
#         print(f"i={i}, j={j}")
#         j=j+1
#     i=i+1

#
# i=0
# while i<4:
#     j=0
#     while j<3:
#         print(f"i={i}, j={j}")
#         j=j+1
#     if i ==1:
#         break
#     i=i+1


i=0
while i<4:
    if i==1:
        i=i+1
        continue
    j=0
    while j<3:
        print(f"i={i}, j={j}")
        j=j+1
    i=i+1