'''
Created on Mar 10, 2018

@author: gosha
'''
import unittest

import Main

class Test(unittest.TestCase):


    def testEmpty(self):
        self.assertEqual(Main.empty(), [[0] * 8] * 8)
        
    def testStart(self):
        self.assertEqual(Main.start(), [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]])

    def testJumps(self):
        board = Main.start()
        self.assertEqual(Main.check_for_jumps(board, 2, 1), [])
        self.assertEqual(Main.check_for_jumps(board, 0, 1), [])
        self.assertEqual(Main.check_for_jumps(board, 1, 2), [])
        board[3][2] = 2
        self.assertEqual(Main.check_for_jumps(board, 1, 2), [[[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]])
        board[4][3] = 2
        self.assertEqual(Main.check_for_jumps(board, 1, 2), [])
        board[4][3] = 0
        board[3][4] = 2
        self.assertEqual(Main.check_for_jumps(board, 3, 2), [[[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 2, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]], [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 1], [0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]])
        board = Main.start()
        board[4][3] = 1
        self.assertEqual(Main.check_for_jumps(board, 2, 5), [[[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]])
        
    def testMoves(self):
        board = Main.start()
        self.assertEqual(Main.check_for_moves(board, 1, 0), [])
        self.assertEqual(Main.check_for_moves(board, 7, 2), [[[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]])
            
    
if __name__ == "__main__":
    unittest.main()