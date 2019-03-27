from .tweets import get_tweets
from .checkcsv import data_in_dict
import csv
import paralleldots
import operator
def classify():
	list_of_complaints = get_tweets("railminindia")
	category = data_in_dict()
	paralleldots.set_api_key("qamrbbHa47QpyLFeMkwEQd7g5ae9RyelNaQZUyGwexg")
	classified_tweets = {}
	for text in list_of_complaints:
		response=paralleldots.custom_classifier(text,category)
		tag = response['taxonomy'][0]['tag']
		classified_tweets.update({tag:text})

	#print(classified_tweets)
	return classified_tweets

#classify()