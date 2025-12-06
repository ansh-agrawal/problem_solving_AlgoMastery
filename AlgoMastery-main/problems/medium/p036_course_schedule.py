"""
Task 36: Course Schedule

Given the total number of courses num_courses and a list of prerequisite pairs prerequisites, return True if it is possible to finish all courses. Each prerequisite is a pair [a, b] meaning to take course a you must first take course b. Courses are 0-indexed.

Example:
    course_schedule(num_courses=2, prerequisites=[[1,0]]) -> True
    course_schedule(num_courses=2, prerequisites=[[1,0],[0,1]]) -> False

Args:
    num_courses (int): Total number of courses (0-indexed)
    prerequisites (list[list[int]]): List of prerequisite pairs (0-indexed)

Returns:
    bool: True if possible to finish all courses, False otherwise
"""

def course_schedule(nc: int, pq: list[list[int]]) -> bool:

    adj=[[] for _ in range(nc)]
    vis=[0 for _ in range(nc)]
    indegree=[0 for _ in range(nc)]
    for i in range(len(pq)):
            adj[pq[i][1]].append(pq[i][0])
    for i in range(nc):
            for child in adj[i]:
                indegree[child]+=1
    q=[] 
    topo=[]
    for i in range(nc):
            if indegree[i]==0 and vis[i]==0:
                q.append(i)
                vis[i]=1
    while len(q)!=0:
            temp_node=q.pop()
            topo.append(temp_node)
            for child in adj[temp_node]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
                    vis[child]=1
    if len(topo) == nc:
            return True
    return False