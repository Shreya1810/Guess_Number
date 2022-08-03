text = """
Sometimes I get this feeling
That the sun is shining
And the birds are singing
All because of you
And Im living my whole life because of you
And everything I tried is because of you, its true
Cos all I see is you, oh yeah
"""
#print(text.split())

word_count = {}

for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)

  
