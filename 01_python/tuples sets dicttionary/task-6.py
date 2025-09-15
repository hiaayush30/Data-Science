given = [(1,1),(2,2),(3,3),(4,4)]
query = (0,0)
min_distance=float("inf")
target_coordinate = [0,0,]
for i,j in given:
  distance = ((i-query[0])**2 + (j-query[1])**2)**0.5
  if distance < min_distance:
    min_distance = distance
    target_coordinate[0] = i
    target_coordinate[1] = j
print(f"Nearest to {query} is {tuple(target_coordinate)}")