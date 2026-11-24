# 48 Bayesian network using pgmpy
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
m=DiscreteBayesianNetwork([("Cloudy","Rain"),("Cloudy","Sprinkler"),("Rain","Wet"),("Sprinkler","Wet")])
m.add_cpds(TabularCPD("Cloudy",2,[[.5],[.5]]),
 TabularCPD("Rain",2,[[.8,.2],[.2,.8]],evidence=["Cloudy"],evidence_card=[2]),
 TabularCPD("Sprinkler",2,[[.5,.9],[.5,.1]],evidence=["Cloudy"],evidence_card=[2]),
 TabularCPD("Wet",2,[[1,.1,.1,.01],[0,.9,.9,.99]],evidence=["Sprinkler","Rain"],evidence_card=[2,2]))
assert m.check_model();print(VariableElimination(m).query(["Rain"],evidence={"Wet":1}))