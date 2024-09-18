"""
Mesomachukwu Nwankwo
@03054767
"""
import re
class Boggle:
    def __init__(self, grid, dictionary):
        # Constructor that initializes the grid and dictionary
        self.grid = self.grid_to_lower(grid)  # Converts the grid to lowercase
        self.dictionary = self.dict_to_lower(dictionary)  # Converts the dictionary to lowercase
        self.all_cases_dictionary = self.build_all_cases_dictionary(self.dictionary)  # Prepares all possible word cases
        self.solutions = []  # Initializes the solutions list

    def grid_to_lower(self, grid):
        # Converts all letters in the grid to lowercase
        return [[char.lower() for char in row] for row in grid]

    def dict_to_lower(self, dictionary):
        # Converts all words in the dictionary to lowercase
        return [word.lower() for word in dictionary]

    def is_grid_valid(self, grid):
        # Validates the grid against allowed characters and tiles ("st", "qu")
        regex = r'(qu|st)|[a-prt-z]'  # Defines allowed letters and tiles
        for row in grid:  # Loops through each row in the grid
            for char in row:  # Loops through each character in the row
                if not re.match(regex, char.lower()):  # If character does not match regex, return False
                    return False
        return True  # If all characters are valid, return True

    def build_all_cases_dictionary(self, dictionary):
        # Builds a dictionary of all possible words and their prefixes
        all_cases_dictionary = {"": False}  # Starts with an empty string as False
        for word in dictionary:  # Loops through each word in the dictionary
            all_cases_dictionary[word] = True  # Marks the full word as True (valid)
            word_sub_string = ''  # Initializes an empty string for building prefixes
            for j in range(len(word) - 1):  # Loops through each letter in the word to create prefixes
                word_sub_string += word[j]  # Adds the letter to the substring
                if word_sub_string not in all_cases_dictionary:  # If the substring is not already in the dictionary
                    all_cases_dictionary[word_sub_string] = False  # Adds the substring as False (prefix)
        return all_cases_dictionary  # Returns the complete dictionary of words and prefixes

    def get_results(self, used_points, i, j, current_sub_word):
        # Recursively finds valid words in the grid
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]):  # Checks if the current point is out of bounds
            return  # Exits if out of bounds
        if current_sub_word not in self.all_cases_dictionary:  # Exits if the current word is not a valid prefix
            return
        if self.all_cases_dictionary[current_sub_word] and len(current_sub_word) >= 3:  # Checks if the word is valid and at least 3 letters long
            if current_sub_word not in self.solutions:  # If the word is not already in solutions
                self.solutions.append(current_sub_word)  # Adds the word to solutions

        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)]  # Defines all 8 directions (diagonal, horizontal, vertical)
        for direction in directions:  # Loops through each direction
            new_i, new_j = i + direction[0], j + direction[1]  # Calculates the new point in the grid
            new_point = f"{new_i},{new_j}"  # Formats the new point as a string for tracking
            if new_point not in used_points and 0 <= new_i < len(self.grid) and 0 <= new_j < len(self.grid[0]):  # Checks if the new point is valid and not already used
                current_used_points = used_points[:]  # Creates a copy of the used points list
                current_used_points.append(new_point)  # Adds the new point to the used points list
                self.get_results(current_used_points, new_i, new_j, current_sub_word + self.grid[new_i][new_j])  # Recursively continues the search

    def find_all_solutions(self):
        # Finds all possible words in the grid
        if not self.is_grid_valid(self.grid):  # Returns empty solutions if the grid is not valid
            return self.solutions

        N = len(self.grid)  # Gets the size of the grid (NxN)
        for row in self.grid:  # Loops through each row in the grid
            if len(row) != N or not row:  # If the grid is not NxN or a row is empty, returns empty solutions
                return self.solutions

        for i in range(len(self.grid)):  # Loops through each row in the grid
            for j in range(len(self.grid[0])):  # Loops through each column in the row
                self.get_results([f"{i},{j}"], i, j, self.grid[i][j])  # Starts the search from each point in the grid

        return self.solutions  # Returns the list of valid words found

    def getSolution(self):
        # Getter method for retrieving the solutions
        return self.find_all_solutions()  # Calls the method to find and return solutions

    def set_grid(self, grid):
        # Setter method to update the grid
        self.grid = self.grid_to_lower(grid)  # Converts the new grid to lowercase

    def set_dictionary(self, dictionary):
        # Setter method to update the dictionary
        self.dictionary = self.dict_to_lower(dictionary)  # Converts the new dictionary to lowercase
        self.all_cases_dictionary = self.build_all_cases_dictionary(self.dictionary)  # Rebuilds the dictionary of cases

def main():
    # Main function to demonstrate the class usage
    grid = [["A", "B", "C", "D"],  # Example grid
            ["E", "F", "G", "H"],
            ["I", "J", "K", "L"],
            ["A", "B", "C", "D"]]

    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]  # Example dictionary

    mygame = Boggle(grid, dictionary)  # Creates an instance of the Boggle class
    print(mygame.getSolution())  # Prints the found solutions

if __name__ == "__main__":
    # Calls the main function if this file is run as a script
    main()
