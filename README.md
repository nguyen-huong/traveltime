# Travel-time Maps by Speed

Take in data input (.csv), generate heatmaps based on speed condition with printed timestamps

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements

```bash
pip install requirements.txt
```

## Usage

```python
import timestamp

# returns heatmap with travel time statistics
get_timestamp('path/to/data.csv')

# returns heatmap
get_map('path/to/data.csv')

# save to build directory
map = get_map('path/to/data.csv')
save_map(map, name='map-name')
```
## Demo



https://user-images.githubusercontent.com/57471582/176513571-2eacc8c5-477a-4d7f-b4d2-92cc1e1549cd.mov



## Issues

Have a problem? Feedbacks? Create an issue [here](https://github.com/nguyen-huong/traveltime/issues)


