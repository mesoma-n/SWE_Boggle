import re


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = self.grid_to_lower(grid)
        self.dictionary = self.dict_to_lower(dictionary)
        self.all_cases_dictionary = self.build_all_cases_dictionary(
            self.dictionary
        )
        self.solutions = []

    def grid_to_lower(self, grid):
        return [[char.lower() for char in row] for row in grid]

    def dict_to_lower(self, dictionary):
        return [word.lower() for word in dictionary]

    def is_grid_valid(self, grid):
        regex = r'(qu|st)|[a-prt-z]'
        for row in grid:
            for char in row:
                if not re.match(regex, char.lower()):
                    return False
        return True

    def build_all_cases_dictionary(self, dictionary):
        all_cases_dictionary = {"": False}
        for word in dictionary:
            all_cases_dictionary[word] = True
            word_sub_string = ''
            for j in range(len(word) - 1):
                word_sub_string += word[j]
                if word_sub_string not in all_cases_dictionary:
                    all_cases_dictionary[word_sub_string] = False
        return all_cases_dictionary

    def get_results(self, used_points, i, j, current_sub_word):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]):
            return

        current_tile = self.grid[i][j]
        if current_tile == "qu":
            current_sub_word += "qu"
        elif current_tile == "st":
            current_sub_word += "st"
        else:
            current_sub_word += current_tile

        if current_sub_word not in self.all_cases_dictionary:
            return
        if (self.all_cases_dictionary[current_sub_word] and
                len(current_sub_word) >= 3):
            if current_sub_word not in self.solutions:
                self.solutions.append(current_sub_word)

        directions = [
            (1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)
        ]
        for direction in directions:
            new_i, new_j = i + direction[0], j + direction[1]
            new_point = f"{new_i},{new_j}"
            if (
                new_point not in used_points and
                0 <= new_i < len(self.grid) and
                0 <= new_j < len(self.grid[0])
            ):
                current_used_points = used_points[:]
                current_used_points.append(new_point)
                self.get_results(
                    current_used_points, new_i, new_j, current_sub_word
                )

    def find_all_solutions(self):
        if not self.is_grid_valid(self.grid):
            return self.solutions

        N = len(self.grid)
        for row in self.grid:
            if len(row) != N or not row:
                return self.solutions

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.get_results([f"{i},{j}"], i, j, "")

        return self.solutions

    def getSolution(self):
        return self.find_all_solutions()

    def set_grid(self, grid):
        self.grid = self.grid_to_lower(grid)

    def set_dictionary(self, dictionary):
        self.dictionary = self.dict_to_lower(dictionary)
        self.all_cases_dictionary = self.build_all_cases_dictionary(
            self.dictionary
        )


def main():
    grid = [["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["I", "J", "K", "L"],
            ["A", "B", "C", "D"]]

    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
