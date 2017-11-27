'''
Problem:
 An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image. 
'''

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.fill(image,sr,sc,image[sr][sc],newColor,[[0 for x in range(len(image[0]))] for y in range(len(image))])
        return(image)
    
    def fill(self, image,y,x,color,newColor,checked):
            image[y][x] = newColor
            
            if y > 0 and checked[y-1][x] == 0 and image[y-1][x] == color:
                checked[y-1][x] = 1
                self.fill(image,y-1,x,color,newColor,checked)
                
            if y < len(image)-1 and checked[y+1][x] == 0 and image[y+1][x] == color:
                checked[y+1][x] = 1
                self.fill(image,y+1,x,color,newColor,checked)
                
            if x > 0 and checked[y][x-1] == 0 and image[y][x-1] == color:
                checked[y][x-1] = 1
                self.fill(image,y,x-1,color,newColor,checked)
                
            if x < len(image[0])-1 and checked[y][x+1] == 0 and image[y][x+1] == color:
                checked[y][x+1] = 1
                self.fill(image,y,x+1,color,newColor,checked)