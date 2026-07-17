// Last updated: 7/17/2026, 3:08:49 PM
class Solution {
    public boolean isValidPosition(char[][] board, int row, int col , int num){
        for(int i=0;i<9;i++){
            //row
            if(board[row][i] == (char)(num + '0')) return false;
            //col
            if(board[i][col] == (char)(num + '0')) return false;
        }
        //grid
        int r = row-row%3;
        int c = col-col%3;

        for(int i = r;i < r+3; i++){
            for(int j = c; j < c+3 ;j++){
                if(board[i][j] == num+48) return false;
            }
        }
        return true;   
    }
    public boolean sudokuValid(char[][] board){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j] == '.'){
                    for(int num = 1;num<=9;num++){
                        if(isValidPosition(board , i , j , num)){
                            board[i][j] = (char)(num + '0');
                            if(sudokuValid(board)) return true;
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public void solveSudoku(char[][] board) {
        boolean check = sudokuValid(board);
    }
}