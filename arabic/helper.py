from arabic_reshaper import ArabicReshaper as ar
from bidi.algorithm import get_display

def normalize_word(word):
	word = reshaper.reshape(word)
	return get_display(word)

def normalize_word_keep(word):
	word = reshaper_keep.reshape(word)
	return get_display(word)

configuration = {
	'delete_harakat': False,
	'support_ligatures': True,
	'shift_harakat_position': True,
}

reshaper_keep = ar(configuration=configuration)
reshaper = ar()
print('this is called')