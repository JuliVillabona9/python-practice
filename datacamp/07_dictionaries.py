# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')
# Use ind_ger to print out capital of Germany

print(capitals[ind_ger])

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Para agregar un nuevo obj al diccionario
europe['Nuevo valor'] = 'asi agrego otro obj'


print(europe)
print(europe.keys())
print('Nuevo valor' in europe)

#para actualizar un obj se pone tal cual que si estuviera agregando, los obj son unicos

europe['Nuevo valor'] = 'asi actualizo un obj'

print(europe)
print(europe.keys())
print('Nuevo valor' in europe)

#para borrar un obj

del(europe['Nuevo valor'])
print(europe)
print(europe.keys())
print('Nuevo valor' in europe) #el resultado es True o False indicando si a key esta en el diccionario


# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data

data = {'capital': 'rome', 'population' :59.83}

# Add data to europe under key 'italy'

europe['italy'] = data

# Print europe
print(europe)
