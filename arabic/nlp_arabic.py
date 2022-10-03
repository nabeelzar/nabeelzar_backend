from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer

from camel_tools.tokenizers.word import simple_word_tokenize

from camel_tools.utils.normalize import normalize_alef_maksura_ar
from camel_tools.utils.normalize import normalize_alef_ar
from camel_tools.utils.normalize import normalize_teh_marbuta_ar
from camel_tools.utils.normalize import normalize_unicode

from camel_tools.utils.dediac import dediac_ar

from camel_tools.disambig.mle import MLEDisambiguator

from .helper import normalize_word_keep, normalize_word


def ortho_normalize(text):
	text = dediac_ar(text)
	text = normalize_alef_maksura_ar(text)
	text = normalize_alef_ar(text)
	text = normalize_teh_marbuta_ar(text)
	text  = normalize_unicode(text)

	return text


def analyze_sentence(sentence=None):
	if not sentence:
		sentence = 'هدا الكتاب هو هدية إلكم لأنكم علّمتوني'
	db = MorphologyDB.builtin_db()
	print(MorphologyDB.list_builtin_dbs())

	analyzer = Analyzer(db)

	words = simple_word_tokenize(sentence)
	
	for word in words:
		analyses = analyzer.analyze(word)

		if not analyses: 
			found_word = normalize_word_keep(word)
			print(f'could not find {found_word}')

		for analysis in analyses:
			if 'gloss' in analysis and 'diac' in analysis:
				found_word = normalize_word_keep(analysis['diac'])
				print(f"{found_word}: {analysis['gloss']}")
			else:
				found_word = nomalize_word_keep(word)
				print(f'could not find {found_word}')
		print()

	return words


def determine_pos(sentence):
	mle = MLEDisambiguator.pretrained()

	sentence = simple_word_tokenize(sentence)
	
	disambig = mle.disambiguate(sentence)

	diacritized = [d.analyses[0].analysis['diac'] for d in disambig]
	#diacritized = [normalize_word_keep(d) for d in diacritized]

	definitions = [d.analyses[0].analysis['gloss'] for d in disambig]

	pos_tags = [d.analyses[0].analysis['pos'] for d in disambig]
	lemmas = [d.analyses[0].analysis['lex'] for d in disambig]
	#lemmas = [normalize_word_keep(l) for l in lemmas]

	res = list(zip(diacritized, pos_tags, lemmas, definitions))

	full_sentence = ""
	for word in diacritized:
		if word in '.?!؟':
			full_sentence += f'{word}'
		else:
			full_sentence += f'{word} '

	full_sentence = full_sentence.strip()	
	return {'sentence_breakdown':res, 'complete_sentence':full_sentence}


def main():
	#sentence = 'انا ذهبت الي المدرسة'
	#analyze_sentence(sentence)

	sentence = '‏ولا خلاف في قبول مرسل الصحابي. لأن الصحابه كلهم عدول. وأما مرسل غير اصحابي'
	determine_pos(sentence)
	
	
if __name__ == '__main__':
	main()