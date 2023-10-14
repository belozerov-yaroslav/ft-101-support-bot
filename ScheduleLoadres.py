from openpyxl import load_workbook
from openpyxl.cell.cell import MergedCell
import abc


class ScheduleLoader:
    @abc.abstractmethod
    def load(self):
        """Возвращает список из двух списков (две подгруппы), в каждом списке
        7 списков (7 дней недели), в кажом из семи по списку на два элемента
        (чётная и нечётная пара)"""
        pass


class XlsxScheduleLoader(ScheduleLoader):
    MAX_PAIRS_IN_DAY = 6
    FIRST_GROUP_INDEX = "C3:C72"
    SECOND_GROUP_INDEX = "D3:D72"

    def __init__(self, file_path, sheet_name):
        self.workbook = load_workbook(filename=file_path)
        self.worksheet = self.workbook[sheet_name]

    def get_original_cell_from_merged(self, merged_cell, merged_ranges):
        return list(filter(lambda x: merged_cell.coordinate in x, merged_ranges))[0].start_cell

    def load_schedule_for_group(self, cells, merged_cells):
        result_list = [[[[] for _ in range(2)] for _ in range(self.MAX_PAIRS_IN_DAY)] for _ in range(7)]
        for index in range(0, len(cells)):
            cell = cells[index]
            if isinstance(cell, MergedCell):
                cell = self.get_original_cell_from_merged(cells[index], merged_cells)
            if cell.value is not None:
                day_num = index // (self.MAX_PAIRS_IN_DAY * 2)
                pair_num = ((index % (self.MAX_PAIRS_IN_DAY * 2)) // 2) % self.MAX_PAIRS_IN_DAY
                even_pair = index % 2
                result_list[day_num][pair_num][even_pair] = cell.value
        return result_list

    def load(self):
        f_group, s_group = [], []
        f_group += self.load_schedule_for_group(list(map(lambda x: x[0], self.worksheet[self.FIRST_GROUP_INDEX])),
                                                self.worksheet.merged_cells.ranges)
        s_group += self.load_schedule_for_group(list(map(lambda x: x[0], self.worksheet[self.SECOND_GROUP_INDEX])),
                                                self.worksheet.merged_cells.ranges)
        return [f_group, s_group]
