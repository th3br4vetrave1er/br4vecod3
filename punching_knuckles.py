# ячейка 1
import pandas as pd
import seaborn as sns
from drawdata import draw_scatter
draw_scatter()


# ячейка 2
df = pd.read_clipboard(sep=',')
sns.scatterplot(data=df, x='x', y='y', hue='z')
