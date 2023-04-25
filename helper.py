import random
import urllib, requests
import json


def get_definition(definition_list):
	'''This function is used to extract the definition of the word 
	from the json file recieved from the dictionary api'''
	define = json.loads(definition_list)
	definition = define[0]['meanings'][0]['definitions'][0]['definition']
	return definition
	

def limitedword(words1):
	'''This function is used to load the word list and iterate through every word that has more than 3 characters.'''
	words = words1 + '.txt'
	with open(words) as word:
		count = 0
		my_words = []
		for line in word:
			line_list = line.split(',')
			for ele in line_list:
				ele_strip = ele.strip()
				ele_strip1 = ele_strip.strip('.')
				if len(ele_strip1) > 3:
					
					url = r'https://api.dictionaryapi.dev/api/v2/entries/en/' + ele_strip1
					
					try:
						res = requests.get(url=url)
					except:
						definition = 'No definition!'
					else:
						if res.status_code != 200:
							definition = 'No definition!'
						if res.status_code == 200:
							definition = get_definition(res.text)
					word_list = [ele_strip1, definition]
					my_words.append(word_list)
		random.shuffle(my_words)	
		return my_words
		
def from_stored_json(jsontxt):
	with open(jsontxt) as text:
		words_j1 = json.load(text)
	return words_j1
				
			

if __name__ == '__main__':
	"""The code below is used to get the .txt list of word
	convert it to json file and write it
	"""
	my_word = limitedword('computer')
	my_json = json.dumps(my_word)
	#my_word = from_stored_json('hang2.txt')
	#print(my_word)
	my_word2 =str(my_word)
	with open('hang.json', 'w') as w:
		w.write(my_json)
		print(my_word)
		
	
