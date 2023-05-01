
import urllib.request
import json
import codecs

## Primary documentation: https://www.census.gov/data/developers/data-sets/acs-5year.html

##Place userID between quotes to run this module
userID = "b6d20e91a4d64fa3233ab299d2693382983b4276"

outFile = open("EdAttainment2020.txt","w")
reader = codecs.getreader('utf-8')

list_header = ["Year","Fips","Total","No Schooling completed","Nursery school","Kindergartern","1st grade","2nd grade","3rd grade","4th grade","5th grade","6th grade","7th grade","8th grade","9th grade","10th grade","11th grade","12 grade, no diploma","Regular high school diploma","GED or alternative credential","Some college, less than 1 year","Some college, 1 or more years, no degree","Associate's degree","Bachelor's degree","Master's degree","Professional school degree","Doctorate degree","County_State_Name"]
outFile.write('|'.join(list_header) + "\n")

target = "B15003_001E,B15003_002E,B15003_003E,B15003_004E,B15003_005E,B15003_006E,B15003_007E,B15003_008E,B15003_009E,B15003_010E,B15003_011E,B15003_012E,B15003_013E,B15003_014E,B15003_015E,B15003_016E,B15003_017E,B15003_018E,B15003_019E,B15003_020E,B15003_021E,B15003_022E,B15003_023E,B15003_024E,B15003_025E"
#Star entry provides for all states at county level for target

list_of_list = []

def processACS(target,year):
    url = "https://api.census.gov/data/" + year + "/acs/acs5?key=" + userID + "&get=" + target + ",NAME&for=county:*&in=State:18"
    json_obj = urllib.request.urlopen(url)
    data = json.load(reader(json_obj))
    numRecords = len(data)
    list_of_list
    for i in range(1,numRecords):
        list_out = []
        year_of_data = year
        list_out.append(year_of_data)
        county_fips_5 = data[i][26] + data[i][27]
        list_out.append(county_fips_5)
        B15003_001E_Val = data[i][0]
        list_out.append(B15003_001E_Val)
        B15003_002E_Val = data[i][1]
        list_out.append(B15003_002E_Val)
        B15003_003E_Val = data[i][2]
        list_out.append(B15003_003E_Val)
        B15003_004E_Val = data[i][3]
        list_out.append(B15003_004E_Val)
        B15003_005E_Val = data[i][4]
        list_out.append(B15003_005E_Val)
        B15003_006E_Val = data[i][5]
        list_out.append(B15003_006E_Val)
        B15003_007E_Val = data[i][6]
        list_out.append(B15003_007E_Val)
        B15003_008E_Val = data[i][7]
        list_out.append(B15003_008E_Val)
        B15003_009E_Val = data[i][8]
        list_out.append(B15003_009E_Val)
        B15003_010E_Val = data[i][9]
        list_out.append(B15003_010E_Val)
        B15003_011E_Val = data[i][10]
        list_out.append(B15003_011E_Val)
        B15003_012E_Val = data[i][11]
        list_out.append(B15003_012E_Val)
        B15003_013E_Val = data[i][12]
        list_out.append(B15003_013E_Val)
        B15003_014E_Val = data[i][13]
        list_out.append(B15003_014E_Val)
        B15003_015E_Val = data[i][14]
        list_out.append(B15003_015E_Val)
        B15003_016E_Val = data[i][15]
        list_out.append(B15003_016E_Val)
        B15003_017E_Val = data[i][16]
        list_out.append(B15003_017E_Val)
        B15003_018E_Val = data[i][17]
        list_out.append(B15003_018E_Val)
        B15003_019E_Val = data[i][18]
        list_out.append(B15003_019E_Val)
        B15003_020E_Val = data[i][19]
        list_out.append(B15003_020E_Val)
        B15003_021E_Val = data[i][20]
        list_out.append(B15003_021E_Val)
        B15003_022E_Val = data[i][21]
        list_out.append(B15003_022E_Val)
        B15003_023E_Val = data[i][22]
        list_out.append(B15003_023E_Val)
        B15003_024E_Val = data[i][23]
        list_out.append(B15003_024E_Val)
        B15003_025E_Val = data[i][24]
        list_out.append(B15003_025E_Val)
        state_county_name = data[i][25]
        list_out.append(state_county_name)
        list_of_list.append(list_out)
    for list in list_of_list:
        outFile.write('|'.join(list) + "\n")


processACS(target,"2020")

#For variable descriptions see: https://api.census.gov/data/2018/acs/acs5/variables.html

#For validation: https://data.census.gov/cedsci/table?q=Tippecanoe%20County,%20Indiana%20B21100&hidePreview=true&table=B21100&tid=ACSDT5Y2017.B21100&g=0500000US18157&vintage=2017&layer=county&cid=B21100_001E&lastDisplayedRow=8
outFile.close()
        
    








