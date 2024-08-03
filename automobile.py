from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
automobile = fetch_ucirepo(id=10) 
X = automobile.data.features 
y = automobile.data.targets 
  
# variable information 
print(automobile.variables)
