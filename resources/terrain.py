#!python


class Terrain:
    
    def __init__(self, width, heigth):
        self._bottom_row = 0
        self._left_col = 0
        self._width = width
        self._heigth = heigth
        self._top_row = heigth-1
        self._right_col = width-1
        
        self._corners = [
            self._bottom_row + self._left_col,
            self._bottom_row + self._right_col,
            self._top_row * self._heigth + self._left_col,
            self._top_row * self._heigth + self._right_col
        ]
        
        self._sides = []
    

    def get_width(self):
        return self._width
        
    def get_heigth(self):
        return self._heigth
    
    def get_max_zone(self):
         return self._width * self._heigth - 1
    
    def get_midfield_row(self):
        if self._top_row % 2 == 0:
            return self._top_row / 2
        else:
            return self._top_row / 2 + 1
            

    def in_sides(self, zone):
        if not self._sides:  # compute pitch sides if not already done
            for i in range(0, self._heigth * self._width, self._width):
                self._sides.append(i) #left
                self._sides.append(i + self._right_col) #right
        
        return zone in self._sides
    
    def distance(self, zone_a, zone_b):
        row_a = zone_a / self._width
        col_a = zone_a % self._heigth
        row_b = zone_b / self._width
        col_b = zone_b % self._heigth
        return abs(row_a - row_b) + abs(col_a - col_b)
    

    def get_support_area(self, zone):
        zones = []
        current_row = zone / self._width
        current_col = zone % self._heigth
        
        # all zones in the given row, minus the input zone
        zones += self.get_support_line(zone)
        
        # zones ahead and behind    
        if zone in self._corners:
            zones += self.get_support_ahead_behind_corner(zone)
        elif current_row == self._top_row:
            zones += self.get_support_behind(zone)
        elif current_row == self._bottom_row:
            zones += self.get_support_ahead(zone)
        else:
            zones += self.get_support_ahead(zone) + self.get_support_behind(zone)
        
        return sorted(zones)
        

    def get_support_line(self, zone):
        res = []
        current_row = zone / self._width
        current_col = zone % self._heigth
        
        # all zones in the given row, minus the input zone
        for i in range(0, self._width):
            if current_row * self._width + i != zone:
                res.append(current_row * self._width + i)
        
        return res
        

    def get_support_ahead_behind_corner(self, zone):
        if zone == self._corners[0]:
            return sorted([zone+self._width, zone+self._width+1, zone+2*self._width])
        elif zone == self._corners[1]:
            return sorted([zone+self._width, zone+self._width-1, zone+2*self._width])
        elif zone == self._corners[2]:
            return sorted([zone -2*self._width, zone-self._width, zone-self._width+1])
        elif zone == self._corners[3]:
            return sorted([zone -2*self._width, zone-self._width, zone-self._width-1])
        else:
            raise ValueError("Input zone " + str(zone) + " is not a corner")
        

    def get_support_ahead(self, zone):
        if zone in self._corners:
            raise ValueError("Input zone " + str(zone) + " is a corner")
        elif zone / self._heigth == self._top_row:
            raise ValueError("Input zone " + str(zone) + " is in the top row")
        elif zone % self._heigth == self._left_col:
            if zone / self._heigth < self._top_row - 1:
                return [zone+self._width, zone+self._width+1, zone+ 2*self._width]
            else:
                return [zone+self._width, zone+self._width+1]
        elif zone % self._heigth == self._right_col:
            if zone / self._heigth < self._top_row - 1:
                return [zone+self._width-1, zone+self._width, zone+ 2*self._width]
            else:
                return [zone+self._width-1, zone+self._width]                   
        else:
            return [zone+self._width-1, zone+self._width, zone+self._width+1]
        

    def get_support_behind(self, zone):
        if zone in self._corners:
            raise ValueError("Input zone " + str(zone) + " is a corner")
        elif zone / self._heigth == self._bottom_row:
            raise ValueError("Input zone " + str(zone) + " is in the bottom row")
        elif zone % self._heigth == self._left_col:
            if zone / self._heigth > self._bottom_row + 1:
                return [zone- 2*self._width, zone-self._width, zone-self._width+1]
            else:
                return [zone-self._width, zone-self._width+1]
        elif zone % self._heigth == self._right_col:
            if zone / self._heigth > self._bottom_row + 1:
                return [zone- 2*self._width, zone-self._width, zone-self._width+1]
            else:
                return [zone-self._width-1, zone-self._width]                       
        else:
            return [zone-self._width-1, zone-self._width, zone-self._width+1]
            
            
    def get_defence_zone(self, zone):
        return self._width * self._heigth - 1 - zone
        
if __name__ == "__main__":
    a = Terrain(5,5)
    print a.distance(1,22)  

        
