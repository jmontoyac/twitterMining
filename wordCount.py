import operator
import json
from collections import Counter
import tokenizer
from nltk.corpus import stopwords
from nltk import bigrams
import string


fname = 'data/stream_memo_anaya.json'
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation

with open(fname, 'r') as f:
	count_all = Counter()
	for line in f:
		tweet = json.loads(line)
		# Crear lista con todos los terminos
		terms_all = [term for term in tokenizer.preprocess(tweet['text'])]
		terms_stop = [term for term in tokenizer.preprocess(tweet['text']) if term not in stop]

		#	 Count terms only once, equivalent to Document Frequency
		terms_single = set(terms_all)
		# Count hashtags only
		terms_hash = [term for term in tokenizer.preprocess(tweet['text']) 
        if term.startswith('#')]

		terms_only = [term for term in tokenizer.preprocess(tweet['text']) 
        if term not in stop and not term.startswith(('#', '@'))] 

        # Bigrams no esta funcionando
        #terms bigram = bigrams(terms_stop)


		# Actualizar el contador
		count_all.update(terms_hash)
	# Imprimir las 5 palabras mas frecuentes
	print(count_all.most_common(5))
