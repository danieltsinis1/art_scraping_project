import pandas as pd
import urllib2
from bs4 import BeautifulSoup


entry = urllib2.urlopen("https://www.christies.com/lotfinder/paintings/suzanne-valadon-nu-assis-sur-un-canape-6127259-details.aspx?from=salesummery&intobjectid=6127259&sid=f9eb83bc-2273-4e0e-811f-9d981a621328").read()
soup = BeautifulSoup(entry)

def scrape_image(image_soup):
    lot_number = image_soup.find(id="main_center_0_lblLotNumber").string
    sold_amount = image_soup.find(id="main_center_0_lblPriceRealizedPrimary").string
    estimate_value = image_soup.find(id ="main_center_0_lblPriceEstimatedPrimary").string
    provenance = image_soup.find(id ="main_center_0_lblLotProvenance").string
    lot_description = image_soup.find(id ="main_center_0_lblLotDescription")

    print lot_number
    print sold_amount
    print estimate_value
    print provenance
    #     print lot_description