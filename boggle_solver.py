"""
Mesoma Nwankwo
@03054767
"""

class Boggle:
    def __init__(self, grid, dictionary):
        # Initialize the grid and dictionary
        self.grid = grid
        self.dictionary = dictionary
        self.rows = len(grid)
        self.cols = len(grid[0])

    def getSolution(self):
        """
        Returns a list of valid words found in the grid.
        """
        # For each word in the dictionary, check if it's in the grid
        return [word for word in self.dictionary if self._is_word_in_grid(word)]

    def _is_word_in_grid(self, word):
        """
        Helper function to check if a word exists in the grid using DFS.
        """
        visited = [[False] * self.cols for _ in range(self.rows)]

        def dfs(r, c, word_index):
            # If all characters of the word are found
            if word_index == len(word):
                return True

            # Check if we're out of bounds or visited this cell
            if not (0 <= r < self.rows and 0 <= c < self.cols) or visited[r][c]:
                return False

            # Check if the current grid cell matches the current word character
            if self.grid[r][c] != word[word_index]:
                return False

            # Mark this cell as visited
            visited[r][c] = True

            # Explore all 8 directions (diagonal, vertical, and horizontal)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if dfs(r + dr, c + dc, word_index + 1):
                    return True

            # Backtrack (unmark this cell)
            visited[r][c] = False
            return False

        # Start DFS from each grid cell
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False

def main():
    """
    Main function to run the Boggle solver.
    """
    # Define the grid and dictionary
    grid = [["T", "W", "Y", "R"], 
            ["E", "N", "P", "H"], 
            ["G", "Z", "Qu", "R"], 
            ["O", "N", "T", "A"]]

    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", 
                  "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]

    # Create an instance of the Boggle game
    mygame = Boggle(grid, dictionary)

    # Get the solution (list of valid words) and print it
    print(mygame.getSolution())

if __name__ == "__main__":
    main()