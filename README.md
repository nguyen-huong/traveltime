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

![Demo](https://user-images.githubusercontent.com/57471582/176513384-1d7ec1fd-21cf-4176-bc7d-49473e983a1d.mov)

## Issues

Have a problem? Feedbacks? Create an issue [here](https://github.com/nguyen-huong/traveltime/issues)


