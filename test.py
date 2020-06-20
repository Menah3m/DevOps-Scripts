import psutil

a = psutil.virtual_memory()

print(a.percent/100)

