import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    area_threshold = 3000000
    pop_threshold = 25000000
    mask = (world['area'] >= area_threshold) | (world['population'] >= pop_threshold)
    return world.loc[mask, ['name','population','area']]
    