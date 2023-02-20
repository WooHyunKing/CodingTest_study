# n,k = list(map(int, input().split()))


# arr1 = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))

# arr1.sort()
# arr2.sort(reverse=True)

# for i in range(k):
#     if arr1[i] < arr2[i]:
#         arr1[i],arr2[i] = arr2[i], arr1[i]
#     else:
#         break

# print(sum(arr1))

n, k = map(int,input().split())

arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

for i in range(k):
    if arr_a[i] < arr_b[i]:
        arr_a[i],arr_b[i] = arr_b[i],arr_a[i]

print(sum(arr_a))
