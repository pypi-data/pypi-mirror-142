'''
BasicMatrix: Matrix Algebra Package
Author: Christiaan van Eeden
Version: 0.1
'''

#import packages
import numpy as np 
import random as rdm

class BasicMatrix:
    '''
	The BasicMatrix class offers basic matrix arithmetic
	'''
    def __init__(self, row, col):
        '''
    	Attributes
    		rows (int): number of rows in matrix
    		cols (int): number of columns in matrix
    		method (str): filling method (randint/id)
    	'''
        self.row = row
        self.col = col
        self.mat = np.zeros([self.row, self.col])
        
    def get_matrix(self):
        '''
        Returns matrix from attribute
        '''
        return self.mat
    
    def set_matrix(self, X):
        '''
        Sets the instance matrix and dimensions to input matrix
        '''
        self.mat = X
        self.row = len(X)
        self.col = len(X[0])
        
    def shape(self):
        '''
        Returns dimensions (rows, columns) of instance matrix
        '''
        return np.shape(self.mat)
        
    
    def fill_matrix(self):
        '''
        Fills the matrix with random integers
        '''
        for m in range(self.row):
            for n in range(self.col):
                self.mat[m][n] = rdm.randint(0, 10)
                
    def dot(self, other):
        '''
        Multiplication of matrices after checking correct  dimension requirements
        
        Returns new shaped answer matrix or raises error for shape
        '''
        if self.col == other.row:
            new_mat = np.zeros([self.row, other.col])
            for m in range(self.row):
                for n in range(other.col):
                    for k in range(other.row):
                        new_mat[m][n] += self.mat[m][k] * other.mat[k][n]
            return new_mat            
        else:
            raise ValueError('Shapes cannot be multiplied: change A colummns to match B rows')
    
    def __add__(self, other):
        '''
        Overwrites '+'  method for adding matrices
        
        Returns answer matrix or raises error
        '''
        if (self.row == other.row) and (self.col == other.col):
            return self.mat + other.mat
        else:
            raise ValueError('Shapes cannot be added: require equal rows and columns for AB')
    
    def __sub__(self, other):
        '''
        Overwrites '-' method for subtracting matrices
        
        Returns answer matrix or raises error
        '''
        if (self.row == other.row) and (self.col == other.col):
            return self.mat - other.mat
        else:
            raise ValueError('Shapes cannot be subtracted: require equal rows and columns for AB')
        
            
        

                
# mat1 = BasicMatrix(2, 3)
# mat1.fill_matrix()
# print(mat1.get_matrix())
# mat2 = BasicMatrix(2, 2)
# mat2.fill_matrix()
# print(mat2.get_matrix())


# print(BasicMatrix.dot(mat1, mat2))

# print(np.dot(mat1.get_matrix(), mat2.get_matrix()))

# print(mat1 + mat2)
 	
# print(mat1 - mat2)


# bruh = np.ones([2, 2])

# mat1.set_matrix(bruh)

# print(mat1.get_matrix())

# print(mat1.shape())





