import os    
import time    
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   

Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
  
Game = Running    
Mark = 'X'    

print("These are the Numbering Of the game")
print("  1 |2 |3 |4 |5 |6 | 7")
print("_________________________")
print("  8 |9 |10|11|12|13|14")
print("_________________________")
print("  15|16|17|18|19|20|21")
print("_________________________")
print("  22|23|24|25|26|27|28")
print("_________________________")
print("  29|30|31|32|33|34|35")
print("_________________________")
print("  36|37|38|39|40|41|42")
print("_________________________")
print("  43|44|45|46|47|48|49")
print("_________________________")
   
 
def DrawBoard():    
    print(" %c | %c | %c | %c | %c | %c | %c " % (board[1],board[2],board[3],board[4],board[5],board[6],board[7]))    
    print("___|___|___|___|___|___|___")    
    print(" %c | %c | %c | %c | %c | %c | %c " % (board[8],board[9],board[10],board[11],board[12],board[13],board[14]))    
    print("___|___|___|___|___|___|___")    
    print(" %c | %c | %c | %c | %c | %c | %c " % (board[15],board[16],board[17],board[18],board[19],board[20],board[21])) 
    print("___|___|___|___|___|___|___") 
    print(" %c | %c | %c | %c | %c | %c | %c " % (board[22],board[23],board[24],board[25],board[26],board[27],board[28]))    
    print("___|___|___|___|___|___|___")    
    print(" %c | %c | %c | %c | %c | %c | %c " % (board[29],board[30],board[31],board[32],board[33],board[34],board[35]))    
    print("___|___|___|___|___|___|___")    
    print(" %c | %c | %c | %c | %c | %c | %c " % (board[36],board[37],board[38],board[39],board[40],board[41],board[42]))
    print("___|___|___|___|___|___|___")    
    print(" %c | %c | %c | %c | %c | %c | %c " % (board[43],board[44],board[45],board[46],board[47],board[48],board[49]))
    print("   |   |   |   |   |   |   ")    
   
  
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   
    
def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[3] == board[4] and board[1] != ' '):    
        Game = Win
    elif(board[2] == board[3] and board[3] == board[4] and board[4] == board[5] and board[2] != ' '):    
        Game = Win   
    elif(board[3] == board[4] and board[4] == board[5] and board[5] == board[6] and board[3] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[6] == board[7] and board[4] != ' '):    
        Game = Win  
        
    elif(board[8] == board[9] and board[9] == board[10] and board[10] == board[11] and board[8] != ' '):    
        Game = Win
    elif(board[9] == board[10] and board[10] == board[11] and board[11] == board[12] and board[9] != ' '):    
        Game = Win
    elif(board[10] == board[11] and board[11] == board[12] and board[12] == board[13] and board[10] != ' '):    
        Game = Win
    elif(board[11] == board[12] and board[12] == board[13] and board[13] == board[14] and board[11] != ' '):    
        Game = Win
        
    elif(board[15] == board[16] and board[16] == board[17] and board[17] == board[18] and board[15] != ' '):    
        Game = Win
    elif(board[16] == board[17] and board[17] == board[18] and board[18] == board[19] and board[16] != ' '):    
        Game = Win
    elif(board[17] == board[18] and board[18] == board[19] and board[19] == board[20] and board[17] != ' '):    
        Game = Win
    elif(board[18] == board[19] and board[19] == board[20] and board[20] == board[21] and board[18] != ' '):    
        Game = Win
        
    elif(board[22] == board[23] and board[23] == board[24] and board[24] == board[25] and board[22] != ' '):    
        Game = Win
    elif(board[23] == board[24] and board[24] == board[25] and board[25] == board[26] and board[23] != ' '):    
        Game = Win
    elif(board[24] == board[25] and board[25] == board[26] and board[26] == board[27] and board[24] != ' '):    
        Game = Win
    elif(board[25] == board[26] and board[26] == board[27] and board[27] == board[28] and board[25] != ' '):    
        Game = Win
        
    elif(board[29] == board[30] and board[30] == board[31] and board[31] == board[32] and board[29] != ' '):    
        Game = Win
    elif(board[30] == board[31] and board[31] == board[32] and board[32] == board[33] and board[30] != ' '):    
        Game = Win
    elif(board[31] == board[32] and board[32] == board[33] and board[33] == board[34] and board[31] != ' '):    
        Game = Win
    elif(board[32] == board[33] and board[33] == board[34] and board[34] == board[35] and board[32] != ' '):    
        Game = Win
        
    elif(board[36] == board[37] and board[37] == board[38] and board[38] == board[39] and board[36] != ' '):    
        Game = Win
    elif(board[37] == board[38] and board[38] == board[39] and board[39] == board[40] and board[37] != ' '):    
        Game = Win
    elif(board[38] == board[39] and board[39] == board[40] and board[40] == board[41] and board[38] != ' '):    
        Game = Win
    elif(board[39] == board[40] and board[40] == board[41] and board[41] == board[42] and board[39] != ' '):    
        Game = Win
        
    elif(board[43] == board[44] and board[44] == board[45] and board[45] == board[46] and board[43] != ' '):    
        Game = Win
    elif(board[44] == board[45] and board[45] == board[46] and board[46] == board[47] and board[45] != ' '):    
        Game = Win
    elif(board[45] == board[46] and board[46] == board[47] and board[47] == board[48] and board[45] != ' '):    
        Game = Win
    elif(board[46] == board[47] and board[47] == board[48] and board[48] == board[49] and board[46] != ' '):    
        Game = Win
        
     
        
    #Vertical Winning Condition    
    elif(board[1] == board[8] and board[8] == board[15] and board[15] == board[22] and board[1] != ' '):    
        Game = Win
    elif(board[8] == board[15] and board[15] == board[22] and board[22] == board[29] and board[8] != ' '):    
        Game = Win
    elif(board[15] == board[22] and board[22] == board[29] and board[29] == board[36] and board[15] != ' '):    
        Game = Win
    elif(board[22] == board[29] and board[29] == board[36] and board[36] == board[43] and board[22] != ' '):    
        Game = Win
    
    elif(board[2] == board[9] and board[9] == board[16] and board[16] == board[23] and board[2] != ' '):    
        Game = Win
    elif(board[9] == board[16] and board[16] == board[23] and board[23] == board[30] and board[9] != ' '):    
        Game = Win
    elif(board[16] == board[23] and board[23] == board[30] and board[30] == board[37] and board[16] != ' '):    
        Game = Win
    elif(board[23] == board[30] and board[30] == board[37] and board[37] == board[44] and board[23] != ' '):    
        Game = Win
        
    elif(board[3] == board[10] and board[10] == board[17] and board[17] == board[24] and board[3] != ' '):    
        Game = Win
    elif(board[10] == board[17] and board[17] == board[24] and board[24] == board[31] and board[10] != ' '):    
        Game = Win
    elif(board[17] == board[24] and board[24] == board[31] and board[31] == board[38] and board[17] != ' '):    
        Game = Win
    elif(board[24] == board[31] and board[31] == board[38] and board[38] == board[45] and board[24] != ' '):    
        Game = Win
        
    elif(board[4] == board[11] and board[11] == board[18] and board[18] == board[25] and board[4] != ' '):    
        Game = Win
    elif(board[11] == board[18] and board[18] == board[25] and board[25] == board[32] and board[11] != ' '):    
        Game = Win
    elif(board[18] == board[25] and board[25] == board[32] and board[32] == board[39] and board[18] != ' '):    
        Game = Win
    elif(board[25] == board[32] and board[32] == board[39] and board[39] == board[49] and board[25] != ' '):    
        Game = Win
        
    elif(board[5] == board[12] and board[12] == board[19] and board[19] == board[26] and board[5] != ' '):    
        Game = Win
    elif(board[12] == board[19] and board[19] == board[26] and board[26] == board[33] and board[12] != ' '):    
        Game = Win
    elif(board[19] == board[26] and board[26] == board[33] and board[33] == board[40] and board[19] != ' '):    
        Game = Win
    elif(board[26] == board[33] and board[33] == board[40] and board[40] == board[47] and board[26] != ' '):    
        Game = Win
        
    elif(board[6] == board[13] and board[13] == board[20] and board[20] == board[27] and board[6] != ' '):    
        Game = Win
    elif(board[13] == board[20] and board[20] == board[27] and board[27] == board[34] and board[13] != ' '):    
        Game = Win
    elif(board[20] == board[27] and board[27] == board[34] and board[34] == board[41] and board[20] != ' '):    
        Game = Win
    elif(board[27] == board[34] and board[34] == board[41] and board[41] == board[48] and board[27] != ' '):    
        Game = Win
        
    elif(board[7] == board[14] and board[14] == board[21] and board[21] == board[28] and board[7] != ' '):    
        Game = Win
    elif(board[14] == board[21] and board[21] == board[28] and board[28] == board[35] and board[14] != ' '):    
        Game = Win
    elif(board[21] == board[28] and board[28] == board[35] and board[35] == board[42] and board[21] != ' '):    
        Game = Win
    elif(board[28] == board[35] and board[35] == board[42] and board[42] == board[49] and board[28] != ' '):    
        Game = Win
    #Diagonal Winning Condition    
    elif(board[4] == board[10] and board[10] == board[16] and board[16] == board[22] and board[4] != ' '):    
        Game = Win
    elif(board[5] == board[11] and board[11] == board[17] and board[17] == board[23] and board[5] != ' '):    
        Game = Win
    elif(board[11] == board[17] and board[17] == board[23] and board[23] == board[29] and board[11] != ' '):    
        Game = Win
    elif(board[6] == board[12] and board[12] == board[18] and board[18] == board[24] and board[6] != ' '):    
        Game = Win
    elif(board[12] == board[18] and board[18] == board[24] and board[24] == board[30] and board[12] != ' '):    
        Game = Win
    elif(board[18] == board[24] and board[24] == board[30] and board[30] == board[36] and board[18] != ' '):    
        Game = Win
    elif(board[7] == board[13] and board[13] == board[19] and board[19] == board[25] and board[7] != ' '):    
        Game = Win
    elif(board[13] == board[19] and board[19] == board[25] and board[25] == board[31] and board[13] != ' '):    
        Game = Win
    elif(board[19] == board[25] and board[25] == board[31] and board[31] == board[37] and board[19] != ' '):    
        Game = Win
    elif(board[25] == board[31] and board[31] == board[37] and board[37] == board[43] and board[25] != ' '):    
        Game = Win
    elif(board[14] == board[20] and board[20] == board[26] and board[26] == board[32] and board[14] != ' '):    
        Game = Win
    elif(board[20] == board[26] and board[26] == board[32] and board[32] == board[38] and board[20] != ' '):    
        Game = Win
    elif(board[26] == board[32] and board[32] == board[38] and board[38] == board[44] and board[26] != ' '):    
        Game = Win
    elif(board[21] == board[27] and board[27] == board[33] and board[33] == board[39] and board[21] != ' '):    
        Game = Win
    elif(board[27] == board[33] and board[33] == board[39] and board[39] == board[45] and board[27] != ' '):    
        Game = Win
    elif(board[28] == board[34] and board[34] == board[40] and board[40] == board[46] and board[28] != ' '):    
        Game = Win
    
    elif(board[22] == board[30] and board[30] == board[38] and board[38] == board[46] and board[22] != ' '):    
        Game = Win
    elif(board[15] == board[23] and board[23] == board[31] and board[31] == board[39] and board[15] != ' '):    
        Game = Win
    elif(board[23] == board[31] and board[31] == board[39] and board[39] == board[47] and board[23] != ' '):    
        Game = Win
    elif(board[8] == board[16] and board[16] == board[24] and board[24] == board[32] and board[8] != ' '):    
        Game = Win
    elif(board[16] == board[24] and board[24] == board[32] and board[32] == board[40] and board[16] != ' '):    
        Game = Win
    elif(board[24] == board[32] and board[32] == board[40] and board[40] == board[48] and board[24] != ' '):    
        Game = Win
    elif(board[1] == board[9] and board[9] == board[17] and board[17] == board[25] and board[1] != ' '):    
        Game = Win
    elif(board[9] == board[17] and board[17] == board[25] and board[25] == board[33] and board[9] != ' '):    
        Game = Win
    elif(board[17] == board[25] and board[25] == board[33] and board[33] == board[41] and board[17] != ' '):    
        Game = Win
    elif(board[25] == board[33] and board[33] == board[41] and board[41] == board[49] and board[25] != ' '):    
        Game = Win
    elif(board[2] == board[10] and board[10] == board[18] and board[18] == board[26] and board[2] != ' '):    
        Game = Win
    elif(board[10] == board[18] and board[18] == board[26] and board[26] == board[34] and board[10] != ' '):    
        Game = Win
    elif(board[18] == board[26] and board[26] == board[34] and board[34] == board[24] and board[18] != ' '):    
        Game = Win
    elif(board[3] == board[11] and board[11] == board[19] and board[19] == board[27] and board[3] != ' '):    
        Game = Win
    elif(board[11] == board[19] and board[19] == board[27] and board[27] == board[35] and board[11] != ' '):    
        Game = Win
    elif(board[4] == board[12] and board[12] == board[20] and board[20] == board[28] and board[4] != ' '):    
        Game = Win
        
        
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' ' and board[10]!=' ' and board[11]!=' ' and board[12]!=' ' and board[13]!=' ' and board[14]!=' ' and board[15]!=' ' and board[16]!=' ' and board[17]!=' ' and board[18]!=' ' and board[19]!=' ' and board[20]!=' ' and board[21]!=' ' and board[22]!=' ' and board[23]!=' ' and board[24]!=' ' and board[25]!=' ' and board[26]!=' ' and board[27]!=' ' and board[28]!=' ' and board[29]!=' ' and board[30]!=' ' and board[31]!=' ' and board[32]!=' ' and board[33]!=' ' and board[34]!=' ' and board[35]!=' ' and board[36]!=' ' and board[37]!=' ' and board[38]!=' ' and board[39]!=' ' and board[40]!=' ' and board[41]!=' ' and board[42]!=' ' and board[43]!=' ' and board[44]!=' ' and board[45]!=' ' and board[46]!=' ' and board[47]!=' ' and board[48]!=' ' and board[49]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
print("Tic-Tac-Toe Game")    
print("Player 1 [X] --- Player 2 [O]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3)    
while(Game == Running):    
    os.system('cls')    
    DrawBoard()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-49] where you want to mark : "))    
    if choice > 49:
        print("You have enterd greater number mark again\nEnter from 1 to 49 only..")
    else:
        if(CheckPosition(choice)):    
            board[choice] = Mark    
            player+=1    
            CheckWin()
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won")