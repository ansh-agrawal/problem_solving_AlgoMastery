"""
Task 37: Course Schedule II

Given the total number of courses num_courses and a list of prerequisite pairs prerequisites, return the order in which you should take the courses to finish all. If it is not possible, return an empty list. Each prerequisite is a pair [a, b] meaning to take course a you must first take course b. Courses are 0-indexed.

Example:
    course_schedule_ii(num_courses=2, prerequisites=[[1,0]]) -> [0,1]
    course_schedule_ii(num_courses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]) -> [0,1,2,3] or [0,2,1,3]
    course_schedule_ii(num_courses=2, prerequisites=[[1,0],[0,1]]) -> []

Args:
    num_courses (int): Total number of courses (0-indexed)
    prerequisites (list[list[int]]): List of prerequisite pairs (0-indexed)

Returns:
    list[int]: Order to take courses, or empty list if impossible
"""

def course_schedule_ii(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Course Schedule II.

    Args:
        num_courses (int): Total number of courses (0-indexed)
        prerequisites (list[list[int]]): List of prerequisite pairs (0-indexed)

    Returns:
        list[int]: Order to take courses, or empty list if impossible
    """
    # TODO: implement
    pass
