n = int(input())

# print(n)

# area = [[0]*n for _ in range(n)]
area = []
visited = [[False]*n for _ in range(n)]

nx = [-1,1,0,0]
ny = [0,0,-1,1]

size = 0
size_list = []

for i in range(n):
	area.append(list(map(int,input().split())))
	# area[i] = list(map(int,input().split()))
	
def dfs(area,visited,x,y):
	global size
	
	if visited[x][y] or area[x][y] != 1:
		return False
	
	visited[x][y] = True
	size += 1
	
	for i in range(4):
		temp_x = x + nx[i]
		temp_y = y + ny[i]
		
		if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < n:
			if area[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
				dfs(area,visited,temp_x,temp_y)
	return True
				
for i in range(n):
	for j in range(n):
		if dfs(area,visited,i,j):
			size_list.append(size)
			size = 0
		
size_list.sort()
		
print(len(size_list))
for i in size_list:
	print(i, end=" ")
	

