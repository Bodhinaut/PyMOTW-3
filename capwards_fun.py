# string_capwords.py

import string

s = 'The quick brown fox jumped over the lazy dog.'

print(s)
print(string.capwords(s))

"""
The results are the same as those obtained by calling split(), 
capitalizing the words in the resulting list, and then calling join() 
to combine the results.
"""