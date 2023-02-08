#imports
import numpy as np
import math
import matplotlib.pyplot as plt

#####VARIABLES#######
urop_name = ["Robotic assistance of the sit-to-stand transfer","Large Corporations and their impact on US trade policy","Building a web app (e.g. Shiny R or other) to enable users to browse and interact with transcriptome data","Chemistry Information Extraction System","Product Performance Analysis of MIT Fiber Extrusion Device (FrED)","Comparing patterns of oscillatory neuronal activity across cortical layers between humans, monkeys, and mice","Software Development and Testing for an ISS-Based Education Outreach Program","Fusing nanoelectronics with biological systems","Zika Virus Differential Pathogenesis in Cerebral Organoids","Digital Humanities Lab: Ottoman Music Analysis","Autonomous Sea Turtle Robot","Machine learning modeling to optimize bioenergy production","Transmedia Publication Assistance","Engineering nanobodies as a tool to detect glycans","Artificial neuroscience","Quotable Content: Applying Text Reuse Detection to Humanities Scholarship on JSTOR","Building functional tissues using electrical stimulation"]
urop_scores = {}
# urop_scores = {"apples":1, "oranges":2}

####FUNCTIONS#####
def calc_urop_score(course2, course6, econ, multi, happiness):
  return 1*course2+1*course6+2*econ+2*multi+2*happiness

####MAIN######
# #make a list of urop names
stopper = ""
while(stopper != 'STOP'):
  stopper = input("Add your urop name or type 'STOP' to move onto ratings: ")
  if(stopper!='STOP'):
    urop_name.append(stopper)

# #assign scores to each urop
for urop in urop_name:
  print("You are now rating: ", urop)
  print()
  course2 = int(input("On a scale of 1 to 5 (1 being lowest), how much does this UROP deal with Course 2 content?"))
  course6 = int(input("On a scale of 1 to 5 (1 being lowest), how much does this UROP deal with Course 6 content?"))
  econ = int(input("On a scale of 1 to 5 (1 being lowest), how much does this UROP deal with Econ content?"))
  multi = int(input("On a scale of 1 to 5 (1 being lowest), how much does this UROP deal with multidisciplinary content?"))
  happiness = int(input("On a scale of 1 to 5 (1 being lowest), how much does this UROP contribute to your overall happiness?"))
  score = calc_urop_score(course2, course6, econ, multi, happiness)
  urop_scores.update({urop:score})

#graph the results
# print(urop_scores.keys())
x = np.array([key for key in urop_scores.keys()])
y = np.array([val for val in urop_scores.values()])

plt.bar(x,y)
plt.xticks(x, rotation=45)
plt.show()

# #return the top 10, top 5, and top 3 scores
# top_10 = []
# top_5 = []
# top_3 = []

# for urop in [key for key in urop_scores.keys()]:
#   if len(top_10) == 0:
#     top_10.append(urop)
#   elif urop_scores.get(urop) >