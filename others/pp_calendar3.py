import sys
input = lambda: sys.stdin.readline().rstrip()

class Calendar:
    def __init__(self, start_date: str, is_leap=False):
        self.dates = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        self.month_end_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if start_date not in self.dates:
            raise ValueError
        self.start_date = start_date
        if is_leap:
            self.month_end_date[1] = 29


    def _process(self, month) -> int:
        self.start_date_int = self.dates.index(self.start_date)
        month_start_date_int = sum(self.month_end_date[:month]) % 7

        return month_start_date_int
    
    def print_calendar(self, month: int):
        if not 1 <= month <= 12:
            raise ValueError
        
        for date in self.dates: print(f'{date} ', end='')
        print()
        
        index = self._process(month) - 1
        for _ in range(index): print('    ', end='')

        for i in range(1, self.month_end_date[month-1]+1):
            print(f'{i:4}', end='')
            index += 1
            if index % 7 == 0:
                print()
                index = 0


if __name__ == '__main__':
    c = Calendar('Thu', is_leap=True)
    c.print_calendar(1)
        
        
        
        

        