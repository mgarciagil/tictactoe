    def select_cell(self):
        # empieza por el centro
        for row in range (0, 3):
            for column in range (0, 3):
                if self.cell_contains(self.counter, row, column):
                    if row == 0:
                        if column == 0:
                            if is_cell_empty(row +1, column):
                                return Move(self.counter, row +1, column)
                            elif is_cell_empty(row, column +1):
                                return Move(self.counter, row, column +1)
                        elif column == 1:
                            if is_cell_empty(row +1, column):
                                return Move(self.counter, row +1, column)
                            elif is_cell_empty(row, column +1):
                                return Move(self.counter, row, column +1)
                            elif is_cell_empty(row, column -1):
                                return Move(self.counter, row, column -1)
                        elif column == 2:
                            if is_cell_empty(row +1, column):
                                return Move(self.counter, row +1, column)
                            elif is_cell_empty(row, column +1):
                                return Move(self.counter, row, column +1)
                    elif row == 1:
                        if column == 0:
                            if is_cell_empty(row +1, column):
                                return Move(self.counter, row +1, column)
                            elif is_cell_empty(row -1, column):
                                return Move(self.counter, row -1, column)
                            elif is_cell_empty(row, column +1):
                                return Move(self.counter, row, column +1)
                        elif column == 1:
                            if is_cell_empty(row +1, column):
                                return Move(self.counter, row +1, column)
                            elif is_cell_empty(row -1, column):
                                return Move(self.counter, row -1, column
                            elif is_cell_empty(row, column +1):
                                return Move(self.counter, row, column +1)
                            elif is_cell_empty(row, column -1):
                                return Move(self.counter, row, column -1)
                        elif column == 2:
                            if is_cell_empty(row +1, column):
                                return Move(self.counter, row +1, column)
                            elif is_cell_empty(row -1, column):
                                return Move(self.counter, row -1, column)
                            elif is_cell_empty(row, column -1):
                                return Move(self.counter, row, column -1)
                    elif row == 2:
                        if column == 0:
                            if is_cell_empty(row -1, column):
                                return Move(self.counter, row -1, column)
                            elif is_cell_empty(row, column +1):
                                return Move(self.counter, row, column +1)
                        elif column == 1:
                            if is_cell_empty(row -1, column):
                                return Move(self.counter, row -1, column)
                            elif is_cell_empty(row, column +1):
                                return Move(self.counter, row, column +1)
                            elif is_cell_empty(row, column -1):
                                return Move(self.counter, row, column -1)
                        elif column == 2:
                            elif is_cell_empty(row -1, column):
                                return Move(self.counter, row -1, column)
                            elif is_cell_empty(row, column -1):
                                return Move(self.counter, row, column -1)
                else:
                    return self.random_select_cell()