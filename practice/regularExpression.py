
import re

text = '''
howdoyou 67 wode 9nad8l --kl- . yhANGlm 
95959-23-1234
800-123-090
fahui@hotmail.com  
Mr. Schafer
Mr fahui
Ms zhang
Mrs. T
'''

pattern = re.compile(r'M(r|s|rs)\.?\s[a-zA-Z]*', re.IGNORECASE)

matches = pattern.finditer(text)
for match in matches:
    print(match.group(1))