import pulp

# Divisions data
divisions = {
    'Thanthirimale': {'land': 2000, 'water': 3200},
    'Pulmude': {'land': 2300, 'water': 3400},
    'Rambewa': {'land': 600, 'water': 800},
    'Tirappane': {'land': 1100, 'water': 500},
    'Rajanganaya': {'land': 500, 'water': 600}
}

# Crop data
crops = {
    'BlackGram': {'water': 1.6, 'yield': 50, 'profit_per_unit': 2000},
    'Sesame': {'water': 2.9, 'yield': 1.5, 'profit_per_unit': 40000},
    'BigOnion': {'water': 3.5, 'yield': 2.2, 'profit_per_unit': 50000}
}

# Market constraints
market_limits = {
    'BlackGram': 110000,
    'Sesame': 1800,
    'BigOnion': 2200
}

# Minimum Sesame yield
min_sesame = 800

# Problem
prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Decision variables
x = pulp.LpVariable.dicts(
    "Acres", ((d, c) for d in divisions for c in crops), lowBound=0, cat='Continuous')

# Objective function
profit = []
for d in divisions:
    for c in crops:
        units = crops[c]['yield'] * x[(d, c)]
        profit_per_unit = crops[c]['profit_per_unit']
        profit.append(units * profit_per_unit)

prob += pulp.lpSum(profit)

# Land constraints
for d in divisions:
    prob += pulp.lpSum([x[(d, c)] for c in crops]) <= divisions[d]['land']

# Water constraints per division
for d in divisions:
    prob += pulp.lpSum([crops[c]['water'] * x[(d, c)]
                       for c in crops]) <= divisions[d]['water']

# Market constraints
prob += pulp.lpSum([crops['BlackGram']['yield'] * x[(d, 'BlackGram')]
                   for d in divisions]) <= market_limits['BlackGram']
prob += pulp.lpSum([crops['Sesame']['yield'] * x[(d, 'Sesame')]
                   for d in divisions]) <= market_limits['Sesame']
prob += pulp.lpSum([crops['BigOnion']['yield'] * x[(d, 'BigOnion')]
                   for d in divisions]) <= market_limits['BigOnion']

# Minimum sesame yield constraint
prob += pulp.lpSum([crops['Sesame']['yield'] * x[(d, 'Sesame')]
                   for d in divisions]) >= min_sesame

# Solve
prob.solve()

# Results
for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Maximum Profit = Rs", pulp.value(prob.objective))
