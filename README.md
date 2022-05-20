# bfs_dfs_Astar

## Overview 
This is a programming assignment in which you will apply AI search techniques to lead an
exploration team to explore an underground cave system such as the one shown in Figure 1.
Conceptually speaking, each cave system is like a sophisticated 3D maze, as shown in Figure 2,
which consists of a grid of points (not cells) with (x, y, z) locations in which your agent may use
one of the 18 elementary actions (see their definitions below), named X+, X-, Y+, Y-, Z+, Z-;
X+Y+, X-Y+, X+Y-, X-Y-, X+Z+, X+Z-, X-Z+, X-Z-, Y+Z+, Y+Z-, Y-Z+, Y-Z-; to move to one of the 18
neighboring grid point locations. At each grid point, your agent is given a list of actions that are
available for the current point your agent is at. Your agent can select and execute one of these
available actions to move inside the 3D maze. For example, in Figure 2, there is a “path” from
(0,0,0) to (10,0,0) and to travel this path starting from (0,0,0), your agent would make ten
actions: X+, X+, X+, X+, X+, X+, X+, X+, X+, X+, and visit the following list of grid points: (0,0,0),
(1,0,0), (2,0,0), (3,0,0), (4,0,0), (5,0,0), (6,0,0), (7,0,0), (8,0,0), (9,0,0), (10,0,0). At each grid
point, your agent is given a list of available actions to select and execute. For example, in Figure
2, at the grid point (60,45,30) there are two actions for your agent: Z+ for going up, and Y- for
going backwards. At the grid point (60,103,97), the available actions are X+ and Y-. At
(60,45,97), the three available actions are Y+, Z-, and X-Y+. If a grid point has no actions
available, then that means such a point has nowhere to go.

The 18 actions are defined as follows. They are roughly divided as “straight-move” and
“diagonal-move” actions. As shown in Figure 3, the six straight-move actions are X+, X-, Y+, Y-, Z+,
Z-, and they allow your agent to move in a straight-line to the next grid point. The diagonal-move
actions are further defined on xy, xz, and yz planes, respectively. For example, the actions X+Y+,
X+Y-, X-Y+, and X-Y-, are those moves diagonally on the xy plane. Similarly, the actions X+Z+, X+Z-,
X-Z+, and X-Z-, are those moves diagonally on the xz plane. Finally, the actions Y+Z+, Y+Z-, Y-Z+,
and Y-Z-, are those moves diagonally on the yz plane. Notice that not all actions may be available
for a given grid location, and not all grid locations may have actions. 

## Task

 Given as inputs: (1) a list of grid points with their available
actions, (2) an entrance grid location, e.g., (0,0,0) in Figure 2, and (3) an exit grid location, e.g.,
(100,103,97) , your program must search in the maze configuration and find the optimal shortest
path from the entrance to the exit, using a list of actions that are available along the way.
Conceptually, the specification of a grid location and its associated actions is given as a grid
location with a list of actions. 
