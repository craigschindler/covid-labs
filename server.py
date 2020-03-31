import re
from flask import Flask, render_template, request, redirect
app = Flask(__name__)



def find_lab(mystr, lab_pattern):
	search = re.findall(lab_pattern + '\s+([\d\.<>]+)\s+',mystr)
	try:
		return search[1] + " -> " + search[0]
	except:
		try:
			return search[0]
		except:
			return ""

def pv(x,y):
	if not (x == ""):
		return "*{}*: {}\n".format(x, y)
	else:
		return ""

def pv_from_list(mystr_list):
	ans = ""
	for x,y in mystr_list.items():
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
		Ferritin = find_lab(mystr, "Ferritin")
		Plts = find_lab(mystr, "Platelet Count")
		DDimer = find_lab(mystr, "Dimer")
		IL6 = find_lab(mystr, "Interleukin-6, Serum")
		LDH = find_lab(mystr, "LDH")
		covidDict = {"WBC":WBC, "CRP":CRP,"Procal":Procal,"Ferritin":Ferritin,"Plts":Plts, "DDimer":DDimer, "IL6":IL6, "LDH":LDH}
		COVID = pv_from_list(covidDict)
		all_labs = [COVID]
		lab_printout = ""

		for lab in all_labs:
			if lab.strip(" ") != "":
				lab_printout = lab_printout + lab.strip(" ") + "\n"

		return lab_printout
		#return redirect(request.url)
	return render_template("public/sign_up.html")