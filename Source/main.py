import os
import math
import matplotlib.pyplot as plt
from collections import deque
import time

import matrixLib
import DFS_BFS
import Greedy_AStar
import Bonus_Search_1
import Bonus_Search_2
from ucs import *
    

def run(pr, pw):
    os.makedirs("./output" + pw +"dfs", exist_ok=True)
    os.makedirs("./output" + pw +"bfs", exist_ok=True) 
    os.makedirs("./output" + pw +"ucs", exist_ok=True) 
    os.makedirs("./output" + pw +"gbfs", exist_ok=True) 
    os.makedirs("./output" + pw +"astar", exist_ok=True) 
    
    
    matrix_1 = matrixLib.get_infor_from_matrix(pr)
    matrix = matrix_1[1]
    start = matrix_1[2]
    end = matrix_1[3]
    matrixLib.visualize_maze(matrix,matrix_1[0],start,end)

    #DFS
    path = DFS_BFS.dfs_search(matrix, start, end)
    pg = matrixLib.visualize_maze(matrix,matrix_1[0],start,end,path)
    pg.savefig("./output" + pw +"dfs/dfs.png")

    #BFS
    path = DFS_BFS.bfs_search(matrix, start, end)
    pg = matrixLib.visualize_maze(matrix,matrix_1[0],start,end,path)
    pg.savefig("./output"+ pw +"bfs/bfs.png")
    
    #UCS
    path = UCS(matrix, start, end).find()
    plt = matrixLib.visualize_maze(matrix,matrix_1[0],start,end, path)
    pg.savefig("./output"+ pw +"ucs/ucs.png")

    #GBFS
    [plt1, plt2, plt3] = Greedy_AStar.compareHeuristic_Greedy(matrix,matrix_1[0],start,end)
    plt1.savefig("./output"+ pw +"gbfs/gbfs_heuristic_1")
    plt2.savefig("./output"+ pw +"gbfs/gbfs_heuristic_2")
    plt3.savefig("./output"+ pw +"gbfs/gbfs_heuristic_3")

    #Astar
    [plt1, plt2, plt3] = Greedy_AStar.compareHeuristic_AStar(matrix,matrix_1[0],start,end)
    plt1.savefig("./output"+ pw +"astar/astar_heuristic_1")
    plt2.savefig("./output"+ pw +"astar/astar_heuristic_2")
    plt3.savefig("./output"+ pw +"astar/astar_heuristic_3")
    
def runBonus(pw, pr):
    os.makedirs("./output" + pw + "search1", exist_ok=True)
    os.makedirs("./output" + pw + "search2", exist_ok=True)
    
    matrix_bonus_1 = matrixLib.get_infor_from_matrix(pr)
    bonus_points = matrix_bonus_1[0]
    matrix = matrix_bonus_1[1]
    start = matrix_bonus_1[2]
    end = matrix_bonus_1[3]
    matrixLib.visualize_maze(matrix,bonus_points,start,end)

    #Bonus_Search_1
    cost = Bonus_Search_1.bonus_search_1(matrix, bonus_points,start, end)[0]
    path = Bonus_Search_1.bonus_search_1(matrix, bonus_points,start, end)[1]
    print(f'Cost: {cost}')
    plt = matrixLib.visualize_maze(matrix,bonus_points,start,end,path)
    plt.savefig("./output" + pw + "search1/search1.png")

    #Bonus_Search_2
    path = Bonus_Search_2.bonus_search_2(matrix,bonus_points,start,end)
    cost = Bonus_Search_2.cost_func(matrix,path,bonus_points)
    print(f'Cost: {cost}')
    plt = matrixLib.visualize_maze(matrix,bonus_points,start,end,path)
    plt.savefig("./output" + pw + "search2/search2.png")
        

pr = "./input/level_1/input1.txt"
pw = "/level_1/input1/"
run(pr, pw)

pr = "./input/level_1/input2.txt"
pw = "/level_1/input2/"
run(pr, pw)

pr = "./input/level_1/input3.txt"
pw = "/level_1/input3/"
run(pr, pw)

pr = "./input/level_1/input4.txt"
pw = "/level_1/input4/"
run(pr, pw)

pr = "./input/level_1/input5.txt"
pw = "/level_1/input5/"
run(pr, pw)


pr = "./input/level_2/input1.txt"
pw = "/level_2/input1/"
runBonus(pw,pr)

pr = "./input/level_2/input2.txt"
pw = "/level_2/input2/"
runBonus(pw,pr)

pr = "./input/level_2/input3.txt"
pw = "/level_2/input3/"
runBonus(pw,pr)


