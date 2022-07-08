# Travel-time Maps by Speed

Take in data input (.csv), generate heatmaps based on speed condition with printed timestamps

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements

```bash
pip install -r /path/to/requirements.txt
```

## As Library

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




https://user-images.githubusercontent.com/57471582/176595709-a78326a6-de2c-412f-809e-7e7e5a83c923.mov



<img width="1264" alt="demo" src="https://user-images.githubusercontent.com/57471582/176595645-f18a2bd1-1c49-4351-b8ff-4288aac4a9ec.png">



## Issues

Have a problem? Feedbacks? Create an issue [here](https://github.com/nguyen-huong/traveltime/issues)


