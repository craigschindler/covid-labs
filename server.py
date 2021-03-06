import re
from flask import Flask, render_template, request, redirect
app = Flask(__name__)



def find_lab(mystr, lab_pattern):
	search = re.findall(lab_pattern + '\s+([\d\.<>]+)\s+',mystr)
	dummyString = ""
	x = range(1,len(search)+1)
	try:
		if len(search) > 0:
			for n in x:
				dummyString = dummyString + str(search[-n])
				if not (n == len(search)):
					dummyString = dummyString + " -> "
			return dummyString
		else:
			return(dummyString)
	except:
		return dummyString

def pv(x,y):
	if not (x == ""):
		return "*{}*: {}<br>".format(x, y)
	else:
		return ""

def pv_from_list(mystr_list):
	ans = ""
	for x,y in mystr_list.items():
		if not (y == ""):
			ans = ans + pv(x,y)
	return ans

@app.route('/', methods=["GET", "POST"])
def coronalabs():
	if request.method == "POST":

		req = request.form
		mystr = req["labResults"]

		#COVID
		WBC = find_lab(mystr, "WBC Count")
		CRP = find_lab(mystr,"Reactive Protein")
		Procal = find_lab(mystr,"Procalcitonin")
		Ferritin = find_lab(mystr, "Ferritin.")
		Plts = find_lab(mystr, "Platelet Count")
		DDimer = find_lab(mystr, "Dimer")
		IL6 = find_lab(mystr, "Interleukin-6, Serum")
		LDH = find_lab(mystr, "LDH")
		Trop = find_lab(mystr, "Troponin I")
		BNP = find_lab(mystr, "B - Type Natriuretic Peptide")
		CPK = find_lab(mystr, "Creatine Kinase")
		Cr = find_lab(mystr, "Creatinine")
		AST = find_lab(mystr, "AST")
		ALT = find_lab(mystr, "ALT")
		covidDict = {"WBC":WBC, "CRP":CRP,"Procal":Procal,"Ferritin":Ferritin,"Plts":Plts, "DDimer":DDimer, "IL6":IL6, "LDH":LDH, "CPK":CPK, "CR":Cr, "AST":AST,"ALT":ALT, "Trop":Trop, "BNP":BNP}
		COVID = pv_from_list(covidDict)
		all_labs = [COVID]
		lab_printout = ""
		for lab in all_labs:
			if lab.strip(" ") != "":
				lab_printout = lab_printout + lab.strip(" ") + "<br>"

		# return lab_printout
		return render_template('/public/results.html',output=lab_printout)
	return render_template("public/input_report.html")