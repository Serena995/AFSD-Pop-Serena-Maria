import string

my_text='Cifra de afaceri AUTO START EXPERT S.R.L.. a fost de 274,800.00 RON în anul 2023, cu un profit de -16,878.00 RON, după de activitate.'
jumatate=len(my_text)//2
jumatate1=my_text[:jumatate]
jumatate2=my_text[jumatate:]

jumatate1=jumatate1.upper()
jumatate1=jumatate1.strip()

jumatate2=jumatate2[::-1]
jumatate2=jumatate2.translate(str.maketrans('', '', string.punctuation))

rezultatul=jumatate1+jumatate2

print(rezultatul)