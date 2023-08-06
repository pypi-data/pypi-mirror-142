FLA Basic Tools
======
## Description:
Set of tools to examine Legislative Maps that are commonly seen in result test cases in VRA suits

### Create Block Assignment File
##### Description:
Creates a csv Block Assigment file with 2 columns (GEOID,DISTRICT) when supplied with a GeoDataFrame with poltical geographies as the geometry column. Creats a shp file with block level feature when supplied witha DataFrame with a GEOID and DISTRICT Columns
```python
assign_baf(baf, state, disid, geoid=None)
```
- **baf** - GeoDataFrame with district geometries included or DataFrame with 15 Digit Census Block GEOID column
- **state** - the State for the Legdistric you are creating a Block Assigment file for.
- **geoid** - GEOID column **NEEDED** for DataFrame
- **disid** - District Name/Number Column

### Community Splits
##### Description:
Uses included 15 digit Census GEOID referne files to find splits in geogrpahy features not included in the standard Census GEOID
```python
community_split(distr, geoid, disid)
```
- **distr** - Block Assigment File 
- **geoid** - GEOID column 
- **disid** - District Name/Number Column

### Population Overlap PL94
##### Description:
Find overlap based on population between 2 maps to show shifts in communities between poltical districts
```python
Overlap_old_new(new_districts, geoid='GEOID', district='District', leg=None)
```
- **new_districts** - Block Assigment File to compare
- **geoid** - GEOID column 
- **disid** - District Name/Number Column
- **leg** - Column from PL94 districts ('CD116','SLDU18','SLDL18')

### Population Overlap 2 Maps
```python
Overlap_compare(old_districts, new_districts, data, geoid='GEOID', district='District')
```
- **new_districts** - Block Assigment File to compare old_districts
- **old_districts** - Block Assigment File to compare new_districts
- **data** - Data to append to the district Dataframes to create the population overlap analysis
- **geoid** - GEOID column 
- **disid** - District Name/Number Column