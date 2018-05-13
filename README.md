## DFCompare

*version 0.1*

- A package to compare two [pandas](https://pandas.pydata.org/) DataFrames.


---

### Prerequisites

System requirement:
- Python 3
  - [Anaconda (Recommened)](https://www.continuum.io/downloads)
  - [www.python.org](https://www.python.org/downloads/)

Required packages:
- [pandas](https://pandas.pydata.org/)


### Installation

**Method 1:**

1. Run the follow command.

```
pip install git+https://github.com/kitman0804/.git
```

**Method 2:**

1. Download the repository.

2. Run the following command in the downloaded directory.

```
python setup.py install
```


---

### Examples

```
from io import StringIO
import pandas as pd
from DFCompare import DFCompare

a = """Name,Value
Felix,123
Joyce,231213
Leo,1332
Perry,1999
Tat,
"""

b = """Name,Value
Felix,1234
Joyce,231213
Leo2,1332
Tat,
"""

df_a = pd.read_csv(StringIO(a), sep=',')
df_b = pd.read_csv(StringIO(b), sep=',')

compare_a = DFCompare(df_a)

# No. of rows
compare_a.compare_rows(df_b)
# Output:
# base    5
# data    4
# dtype: int64

# No. of columns
compare_a.compare_cols(df_b)
# Output:
# base      2
# data      2
# common    2
# dtype: int64

# Data types
compare_a.compare_dtypes(df_b)
# Output:
#   Column    dtype
#              base     data match
# 0   Name   object   object  True
# 1  Value  float64  float64  True

# Base data that is not in the data to be compared
compare_a.rows_not_in(df_b)
# Output:
#     Name   Value
# 0  Felix   123.0
# 2    Leo  1332.0
# 3  Perry  1999.0
```

