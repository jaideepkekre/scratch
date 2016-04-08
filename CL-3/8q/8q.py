#!/usr/bin/python 

"""
author: Jaideep Kekre
"""
last_placed=list()
N = -1
r=7
glocol=7
def prin(board):
	print "       "
	for row in board :
		print row
def make_board(n):
       global N
       N=n
       board=list()
       for i in xrange(0,n):
       		
       		board.append([0]*n)
       		
       
       return board 


def check_row(board,col,row):
        for i in xrange(0,N):
                if board[row][i]==1 :
                	
                        return False
        return True       
                         
                                    
def check_column(board,col,row) :
        for i in xrange(0,N):
                if board[i][col]==1 :
                	
                        return False
        return True       
                
def check_diagonals(board,colpos,rowpos):
        row=rowpos
        col=colpos
           
        
        #upper diagonal 1 ( row : -1 , col : -1 ) 
        #print row
        #print col
        while row >=0 and col >=0 :
                if board[row][col]==1 :                	
                        return False
                row=row-1 
                col=col-1 
                        
        #lower diagonal 1 ( row : +1 , col : +1 )
        row=rowpos
        col=colpos 
        while row <N and col < N :
                if board[row][col]==1 :                	
                        return False
                row=row+1 
                col=col+1
                
                
         #upper diagonal 2 ( row : -1 , col : +1 ) 
        row=rowpos
        col=colpos 
        while row >=0 and col < N :
                if board[row][col]==1 :                	
                        return False
                row=row-1 
                col=col+1
         #lower diagonal 2 ( row : +1 , col : -1 ) 
        row=rowpos
        col=colpos 
        while row < N and col >=0 :
                if board[row][col]==1 :                	
                        return False
                row=row+1 
                col=col-1    
                
                
                
        return True  
                
                
def is_safe(board,col,row):
	if not check_diagonals(board,col,row) :
		print 
		return False 
        if not  check_row(board,col,row) :
        	return False 
        if not check_column(board,col,row):
        	return False
        return True 

def place(board,col,row=0):
	global glocol
	print col 
        if col>=8:
        	print "Done"
        	prin(board)
                return True
	                
        else:       	
        	
        	if col == glocol:        		
        		col = col+1 
                if col>=N:
        		print "Done"
        		prin(board)
                	return True       			
        		
        	for i in xrange(row,N) :
        		status = is_safe(board,col,i)       		
        		
        		if status :
        			
        			board[i][col]=1
        			last_placed.append([i,col])        			
        			print"Placed"
        			prin(board)
        			place(board,col+1)
        			return True 
        		 
        	#backtrack here
        	print"BackTracking"
        	pos=last_placed.pop()
        	r=pos[0]
        	c=pos[1]
        	board[r][c]=0
        	#print(board)       	
        	place(board,c,r+1)
        	return False 
        			
board=make_board(8)
prin(board )

board[r][glocol]=1 
prin(board)
place(board,0)


        		
        		
        		        	
		                	
                	
        
        
