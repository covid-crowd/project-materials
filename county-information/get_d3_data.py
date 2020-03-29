import pandas as pandas

def check_status(fips_code):
	# counties with compliance info should be strict subset
	# of counties with intervention info
	counties_with_compliance_info = [] # Add FIPS codes here - none to start
	counties_with_intervention_info = ["06085"] # Add FIPS codes here - start with Santa Clara county

	if fips_code in counties_with_compliance_info:
		status = 2
	elif fips_code in counties_with_intervention_info:
		status = 1
	else: 
		status = 0
	return status

# read in a list of population estimates by-county
# released by the census bureau in March 2020
# and extract an up-to-date list of counties
# SOURCE: https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html#par_textimage_70769902
df = pandas.read_csv("co-est2019-alldata.csv", encoding="latin1")

d3_data = df[df.SUMLEV == 50]
d3_data = d3_data[["STNAME","CTYNAME"]]

# id is the FIPS code, which is used by both d3 and the UVA models
d3_data["id"] = df["STATE"].map("{0:02d}".format) + df["COUNTY"].map("{0:03d}".format)

d3_data["status"] = d3_data["id"].map(check_status)

d3_data.to_csv("county_data.csv",index=False)