"""
Accepts a quiz in the format of

1. question
a. option 1
b. option 2
c. option 3*
d. option 4

or 

2. T/F: question
a. True
b. False

and creates valid xml representation of it for the 
quizmaker flash game. To be used with all 25 current
strands and any possible future strands
"""

prefix_string = """<?xml version="1.0" encoding="UTF-8"?>
<quzimaker all_levels="2">
     <info>
	<level>1</level>
	<num_questions>25</num_questions>"""

source_string =  = raw_input('--> ')

suffix_string = """
	</info>
</quzimaker>"""

def formatStr(cur_str):
	if cur_str == "" or len(cur_str) < 3:
		return cur_str
        
	return cur_str[3:].strip()

def isTF(cur_str):
	if len(cur_str) > 14:
		header = cur_str[0:14]
		if header == "True* or False" or header == "True or False*":
			return True
	else:
		return False

def createTF(cur_str):
	if cur_str[4] == "*":
		answer = "0"
	elif cur_str[13] == "*":
		answer = "1"
	else:
		return "error generating T/F for ", cur_str

	text = """\n\t<question>
		<text>True or False"""+cur_str[14:]+"""</text>
		<answer>"""+answer+"""</answer>
	   	<choice>TRUE</choice>
	   	<choice>FALSE</choice>
	</question>"""
	
	return text

def createMC(cur_pos, matches):
	start_pos = cur_pos
	question = formatStr(matches[cur_pos])
	answer = ""
	choices = ""
	
	for i in range(cur_pos+1, cur_pos + 5):
		if (i < len(matches)):
			cur_choice = formatStr(matches[i])
			if len(cur_choice) > 0:
				if cur_choice[-1] == "*":
					answer = str(i - 1  - start_pos)
					cur_choice = cur_choice[0:-1]
				choices += "<choice>"+cur_choice+"</choice>\n\t\t"
		else:
			break
			
	text = """\n\t<question>
		<text>"""+question+"""</text>
		<answer>"""+answer+"""</answer>
		"""+choices[0:-3]+"""
	</question>"""
	
	return text

matches = source_string.split("\n")
cur_pos = 0
result = prefix_string
while cur_pos < len(matches):
	cur_str = formatStr(matches[cur_pos])
	if isTF(cur_str) ==  True:
		#print createTF(cur_str)
		result += createTF(cur_str)
	else:
		try:
			result += createMC(cur_pos, matches)
			cur_pos += 4
		except:
			print "error"
			pass
	cur_pos += 1

result += suffix_string

print result