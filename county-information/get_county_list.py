import pandas as pandas

# read in a list of population estimates by-county
# released by the census bureau in March 2020
# and extract an up-to-date list of counties
# SOURCE: https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html#par_textimage_70769902
df = pandas.read_csv("co-est2019-alldata.csv", encoding="latin1")

# filter out entries for states
# states have summary level 50, counties have summary level 40
counties_df = df[df.SUMLEV == 50]
counties_df = counties_df[["STNAME","CTYNAME"]]
counties_df.to_csv("counties.csv",index=False)

# filter out entries for counties
states_df = df[df.SUMLEV == 40]
states_df = states_df[["STNAME"]]
states_df.to_csv("states.csv",index=False)
