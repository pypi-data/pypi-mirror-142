# terrainy
Contains tools to get user defined resolution DTM's covering available countries

Example:

`import terrainy`\
`from terrainy import  terrainy_shp, download, getMaps, wcs_connect, export `

Load the shapefile you'd like to get a terrain surface for

`df = gpd.read_file("/path/to/some_area_of_interest_polygon.shp")`

Make sure it is in WGS84 / EPSG:4326 if it isnt already\

`df = df.to_crs("EPSG:4326")`

To see where terrainy has available data for your shapefile\
`data = getMaps(df)`\
`print(data)`

With the example of a DTM of Norway at 1m resolution

`data_dict = download(df, "Norway DTM", 1)`

Export your file to your local drive

`export(data_dict, "/path/to/dtm_for_some_area.tif"))`

