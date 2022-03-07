from driver import driver

driverObj = [driver("30086", "Doni",  "Male", "2030", "Grab", "Driver", "A-1865", "2025", "Car"),
driver("30062", "Michel", "Male", "2760", "Gojek", "CFO", "B-7775", "2025", "Car"),
driver("30072", "Mona", "Female", "2220", "Maxim", "Taxi Driver", "C-7271", "2025", "Car"), 
driver("32091", "David", "Male", "2860", "Shopee", "delivery driver", "D-9873", "2025", "Motorcycle"),
driver("30873", "Jeffry", "Male", "2882", "Uber", "Manager", "E-8218", "2025", "Motorcycle")]

#menampilkan keluaran data
print("-DRIVER DATA : 5")
for i in range(5):
    print("driver " , i+1)
    print(driverObj[i].printDriver())