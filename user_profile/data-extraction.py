import requests
from bs4 import BeautifulSoup
import re
from bs4 import NavigableString
import csv

def trained_categories():
  url1 = 'https://indiarailinfo.com/trains/new/'
  url3 = '/0/0/0'
  
  # https://indiarailinfo.com/trains/new/0/0/0/0
  category  = { "NR": [ "Delhi", "Ambala", "Firozpur", "Lucknow NR", "Moradabad", "Farrukhabad"], 
          "NER": [ "Izzatnagar", "Lucknow NER", "Varanasi"], 
          "NFR":[ "Alipurduar", "Katihar", "Rangiya", "Lumding", "Tinsukia"],
          "ER":[ "Howrah", "Sealdah", "Asansol", "Malda"],
          "SER":[ "Adra", "Chakradharpur", "Kharagpur", "Ranchi"],
          "SCR":["Secunderabad", "Hyderabad", "Vijayawada","Guntakal", "Guntur", "Nanded"],
          "SR":["Chennai", "Tiruchirappalli", "Madurai", "Palakkad", "Salem", "Thiruvananthapuram"],
          "CR":[ "Mumbai", "Bhusawal", "Pune", "Solapur", "Nagpur"],
          "WR":["Mumbai WR", "Ratlam", "Ahmedabad", "Rajkot", "Bhavnagar", "Vadodara"],
          "SWR":["Hubballi", "Bengaluru", "Mysuru"],
          "NWR":["Jaipur","Ajmer", "Bikaner", "Jodhpur"],
          "WCR":["Jabalpur", "Bhopal", "Kota"],
          "NCR":["Allahabad", "Agra", "Jhansi"],
          "SECR":["Bilaspur", "Raipur", "Nagpur SEC"],
          "ECoR":["Khurda Road", "Sambalpur", "Waltair"],
          "ECR":["Danapur", "Dhanbad", "Mughalsarai", "Samastipur", "Sonpur"],
         }
  for i in range(1,17):
    url2 = str(i)
    url = url1+url2+url3
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for line in soup.select('div.topcapsule > div.listingcapsulehalf > div.srhres.newbg.inline.alt > div')[2::2]:
      l = [i.text for i in line.select('div')]
      if len(l)==0:
        continue
      pass
      category[l[3]].append(l[0])
      

trained_categories()