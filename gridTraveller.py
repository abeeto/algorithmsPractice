class grid:
    waes = {}
    @classmethod
    def possible(self, x, y):
        key = f"{x},{y}"
        if key in self.waes:
            return self.waes[key]
        elif x == 0 or y == 0:
            return 0
        elif x == 1 and y == 1:
            return 1
    
        self.waes[key] = self.possible(x-1, y) + self.possible(x, y-1)
        return self.waes[key]

print(grid.possible(3,3))
