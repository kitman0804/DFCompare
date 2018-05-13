import pandas as pd


class DFCompare(object):
    def __init__(self, base, debug=False):
        self._base = base
        self.debug = debug
    
    def __repr__(self):
        print_text = '<DF Comparer (Dim: {:} * {:}) at {:}>'.format(
            self._base.shape[0], self._base.shape[1], hex(id(self))
        )
        return print_text
    
    def compare_rows(self, data):
        rows = pd.Series(
            [self._base.shape[0], data.shape[0]], 
            index=['base', 'data']
        )
        return rows
    
    def find_common_cols(self, data):
        common_cols = list(
            set(self._base.columns.values) & 
            set(data.columns.values)
        )
        return common_cols
    
    def compare_cols(self, data):
        cols = pd.Series(
            [self._base.shape[1], data.shape[1], len(self.find_common_cols(data))], 
            index=['base', 'data', 'common']
        )
        return cols
    
    def compare_dtypes(self, data):
        dtypes = pd.merge(
                self._base.dtypes.reset_index(), 
                data.dtypes.reset_index(), 
                how='outer', on=['index']
            )
        dtypes.columns = pd.MultiIndex.from_tuples(
            [('Column', ''), ('dtype', 'base'), ('dtype', 'data')]
        )
        dtypes[('', 'match')] = (dtypes.dtype.base == dtypes.dtype.data)
        return dtypes
    
    def rows_not_in(self, data):
        # Find Common Columns
        common_cols = self.find_common_cols(data=data)
        if len(common_cols) < self._base.shape[1] or len(common_cols) < data.shape[1]:
            print("NOTE: Only common columns are checked.")
        # Select Common Columns
        data0 = self._base.copy()[common_cols]
        data1 = data[common_cols]
        # Sorting
        data0.sort_values(by=common_cols, inplace=True)
        data1.sort_values(by=common_cols, inplace=True)
        # Searching
        idx_row_not_found = []
        i1_start = 0
        for i0, row0 in data0.iterrows():
            if i1_start == data1.shape[0]:
                break
            for i1, row1 in data1.iloc[i1_start:].iterrows():
                if self.debug:
                    print(i0, i1)
                if row0.equals(row1):
                    i1_start = i1 + 1
                    break
                if i1 == (data1.shape[0] - 1):
                    idx_row_not_found.append(i0)
        # Output
        return self._base.loc[self._base.index.isin(data0.iloc[idx_row_not_found].index)]

