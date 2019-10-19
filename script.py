from netCDF4 import Dataset

teste = Dataset('dataset.nc','r')

for i in teste.variables:
    print(i['lat'])
