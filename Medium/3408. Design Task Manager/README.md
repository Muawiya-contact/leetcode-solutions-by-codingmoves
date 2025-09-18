# Task Manager

This project implements **LeetCode 3408: Design Task Manager** in Python.  
The Task Manager allows users to add, edit, remove, and execute tasks with priorities.

---

## Problem Statement

We need to design a task management system that supports the following operations:

1. **Initialization**  
   - Start with a list of tasks, each defined as `[userId, taskId, priority]`.

2. **add(userId, taskId, priority)**  
   - Add a new task for a user with the given priority.  
   - Each taskId is guaranteed to be unique.

3. **edit(taskId, newPriority)**  
   - Update the priority of an existing task.

4. **rmv(taskId)**  
   - Remove a task from the system.

5. **execTop()**  
   - Execute the task with the highest priority.  
   - If multiple tasks share the same priority, choose the task with the larger taskId.  
   - Return the `userId` of the executed task.  
   - If no tasks are available, return `-1`.  
   - Executed tasks are removed from the system.

---

## Example

```python
# Input
["TaskManager","add","edit","execTop","rmv","add","execTop"]
[[[[1,101,8],[2,102,20],[3,103,5]]],[4,104,5],[102,9],[],[101],[50,101,8],[]]

# Output
[None, None, None, 2, None, None, 50]
