# suppose you have data on the number of medals won by a country in the 2020 Tokyo Olympics. You want to visualize this data using a waffle
# chart to show the proportional representation of each country's medal count.
#  Data={'USA': 113, 'China': 88, 'Japan': 58, 'Great Britain': 65, 'ROC': 71, 'Australia': 46, 'Netherlands': 36, 'France': 33, 'Germany': 37, 'Italy': 40}

import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
# Create a DataFrame from the given data
data = pd.DataFrame.from_dict({'USA': 113, 'China': 88, 'Japan': 58,
                               'Great Britain': 65, 'ROC': 71,
                               'Australia': 46, 'Netherlands': 36,
                               'France': 33, 'Germany': 37, 'Italy': 40},
                              orient='index', columns=['medal_count'])
# Set up waffle chart parameters
fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    values=data['medal_count'],
    labels=list(data.index),
    colors=['#3F7FBF', '#DB3236', '#F5A623', '#1EB849', '#AA66CC',
            '#FFD100', '#00A3E0', '#E54028', '#00A651', '#6CABDD'],
    legend={'loc': 'upper left', 'bbox_to_anchor': (1.1, 1)}
)
# Add title
plt.title('2020 Tokyo Olympics Medal Count')
# Show the chart
plt.show()
