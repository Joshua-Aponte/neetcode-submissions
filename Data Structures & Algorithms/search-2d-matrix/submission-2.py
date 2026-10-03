class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = -1
        while(left <= right):
            mid = left + (right - left) // 2
            if(matrix[mid][0] <= target <= matrix[mid][-1]):
                row = mid
                break
            elif(matrix[mid][0] > target):
                right = mid - 1
            else:
                left = mid + 1
        
        print(row)
        low = 0
        high = len(matrix[0]) - 1
        while(low <= high):
            mid = low + (high - low) // 2
            if(matrix[row][mid] < target):
                low = mid + 1
            elif(matrix[row][mid] > target):
                high = mid - 1
            else:
                return True
        return False    