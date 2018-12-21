# node = find_lowest_cost(costs)
# while node in not none:
#     cost = costs[node]
#     neighbors = graph[node]
#     for n in neighbors.keys():
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:
#             conts[n] = new_cost
#             parents[n] = node
#             processed.append(node)
#             node =find_lowest_cost(costs)

a = set([1, 2,3])
b = set([3, 5,6])
print(type(a))
print(a & b)