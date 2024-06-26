#!/usr/bin/env python
# coding: utf-8

# In[12]:


def relationship_status(from_member, to_member, social_graph):
    
    if from_member in social_graph and to_member in social_graph:
        
        from_following = social_graph[from_member]['following']
        to_following = social_graph[to_member]['following']
        
        if to_member in from_following and from_member in to_following:
            return 'friends'
            
        elif to_member in from_following:
            return 'follower'
            
        elif from_member in to_following:
            return 'followed by'
            
        else:
            return 'no relationship'
            
    else:
        return 'no relationship'

relationship_status("@bongolpoc", "@joaquin", "following")


# In[27]:


def tic_tac_toe(board):
    size = len(board)

    
    
    for row in board:
        if row[0] != '' and all(cell == row[0] for cell in row):
            return row[0]
    
    for col in range(size):
        first_cell = board[0][col]
        if first_cell != '' and all(board[row][col] == first_cell for row in range(size)):
            return first_cell
    
    first_diagonal = board[0][0]
    if first_diagonal != '' and all(board[i][i] == first_diagonal for i in range(size)):
        return first_diagonal
    
    last_diagonal = board[0][size - 1]
    if last_diagonal != '' and all(board[i][size - i - 1] == last_diagonal for i in range(size)):
        return last_diagonal
    
    return "NO WINNER"

board = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

tic_tac_toe(board)


# In[31]:


def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    total_time = 0
    
    while current_stop != second_stop:
        found_leg = False
        for leg in route_map:
            from_stop, to_stop = leg
            if from_stop == current_stop:
                total_time += route_map[leg]['travel_time_mins']
                current_stop = to_stop
                found_leg = True
                break
        
        if not found_leg:
            return "Route not found between stops"

    return total_time
    
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

eta("upd", "dlsu", legs)


# In[ ]:




