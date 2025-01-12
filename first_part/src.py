# Your code here

#-----------------------------------------------------------------------------------------------------------------------------------------#
#Task 1
def longest_sequence(keywords):

	seq_txt={}  ## STORING SEQUENCE OF DATA

	for i in range(0,len(keywords)): 

		word=keywords[i] 

		j=0  

		while len(word)>j: # STORE EACH CHARACTER ONE BY ONE TO A DICTIONARY AND THEIR OCCURANCES IN THE SEQ TEXT DICT

			char=word[:j+1] 

			if char in seq_txt: # CHECK IF THE CHARACTER IS ALREADY PRESENT OR NOT

				seq_txt[char] += 1  

			else:

				seq_txt[char] = 1 
			j+=1 


	result={} # STORE THE HIGHEST CHAR AND VALUE
	max_value = max(seq_txt.values()) 

	for key, value in seq_txt.items():
		if 1 < value <= max_value and len(key)>1:
			result[key]=value

	max_value = max(result.values()) # RESULT TO GET LONGEST SEQUENCE
	max_value_keys = [key for key, value in result.items() if value == max_value]
	longest_key = max(max_value_keys, key=len)

	return longest_key



#-------------------------------------------------------------------------------------------------------------------------------------#

# TASK 2


import re
import json

# Input string
input_text = "Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, Cuivre (3b405, 3b406) : 2,2 mg,Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603,3b605, 3b606) : 11 mg –Clinoptilolited’origine sédimentaire : 2 g. Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %."

def convert_dict(input_text):
	pattern = re.compile(r"(?P<name>[\w\u00e0-\u00fc \u2019\-(),]+)\s*:\s*(?P<value>[\d,.]+)\s*(?P<unit>mg|g|%|UI)")
	matches = pattern.finditer(input_text)

	result = {}
	for match in matches:
		name=match.group("name").strip().replace(", ", "").replace("- ", "")
		value=(match.group("value").replace(",", "."))+ match.group("unit")
		result[name]=value


	json_output = json.dumps(result, ensure_ascii=False)

	return json_output


#----------------------------------------------------------------------------------------------------------------------------------#

# TASK 3

def is_grandma_list(lst):

	def check_nested(sublist):
		if isinstance(sublist, list): # CHECK IT IS LIST OR NOT
			for i in range(len(sublist) - 1): # ITERATE THROUGH THE LIST OF ADJACEMENT PAIRS
				
				if isinstance(sublist[i], int) and isinstance(sublist[i + 1], int): # IF FIRST AND SECOND ELEMENT FROM THE ADJACEMENT PAIRS LIST ARE INTEGER

					# MULTIPLE IT TO GET FINAL PRODUCT AND FIND IT IN SUBLIST IF IS PRESENT THEN TRUE
					product = sublist[i] * sublist[i + 1]
					if product in sublist:
						return True

			## IF NO LIST FOUND THEN CONTINUE TO CHECK 

			return any(check_nested(item) for item in sublist)
		return False

	return check_nested(lst)


