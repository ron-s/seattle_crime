import requests
import json
import time

sea_incidents = []


def get_crime_info():
    """Contact the King county API to obtain a JSON list of objects containing restaurant health inspection info that will be saved to 3 separate JSON files. """
    #url to all king county restaurant health inspections since 2006

    offset = 0
    count = 0
    pk = 0

    while offset < 10000:
        url = "https://data.seattle.gov/resource/pu5n-trf4.json?$limit=10000&$offset=" + str(offset) + "&$where=event_clearance_date%20between%20%272016-01-01T12:01:00%27%20and%20%272016-06-01T12:00:00%27"

        #url = "https://data.kingcounty.gov/resource/gkhn-e8mn.json?&inspection_business_name=Subway&$where=inspection_date%20between%20%272015-01-01T12:00:00%27%20and%20%272016-03-22T14:00:00%27&$$app_token=ybQy5wLjPD5YeX6uCeahIgRdT"
        r = requests.get(url)

        data = r.json()
        #print(data)


        for val in data:
            try:
                #parse the JSON into a dict of keys called restaurant

                incident = {}
                incident["fields"] = {}
                incident["model"] = "seattle_crime_app.crimemodel"
                incident["pk"] = val["business_id"]
                incident["fields"]["cad_cdw_id"] = val["eventid"]
                incident["fields"]["event_clearance_description"] = val["description"]
                incident["fields"]["event_clearance_date"] = val["event_date"]
                incident["fields"]["event_clearance_group"] = val["group"]
                incident["fields"]["event_clearance_subgroup"] = val["subgroup"]
                incident["fields"]["general_offense_number"] = val["offense_num"]
                incident["fields"]["hundred_block_location"] = val["block_location"]
                incident["fields"]["zone_beat"] = val["zone_beat"]
                incident["fields"]["latitude"] = val["latitude"]
                incident["fields"]["longitude"] = val["longitude"]
                

                #add the results to the restaurant dict
                sea_incidents.append(incident)

                pk += 1


            except KeyError:
                pass

        offset += 500
        time.sleep(5)
        print(offset)



    #The restaurant file will contain the restaurant name and location.
    with open('seattle911.json', "w") as f:
        json.dump(sea_incidents, f, indent=2)




if __name__ == '__main__':
    get_crime_info()