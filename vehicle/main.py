from ship import ship
from airplane import airplane

airplaneObj = [airplane("Boeing 747", "Jet fuel", "250", "10 year", "A380", "40 meters"),
            airplane("Cessna Skyhawk", "Jet fuel", "300", "12 year", "B-355", "50 meters"),
            airplane("Piper Cherokee", "Avgas", "50", "5 year", "373", "30 meters"),
            airplane("Pilatus PC-12", "Avgas", "600", "20 year", "757", "65 meters"),
            airplane("Mooney M-20", "Avgas", "50", "3 year", "3000-F", "45 meters")]


shipObj = [ship("Titanic", "charcoal", "1200", "100 year", "THT-0813", "British"),
        ship("Ambulu", "wood", "300", "14 year", "AC-7663", "Germany"),
        ship("Blue Bird", "natural gas", "500", "5 year", "KE-8728", "USA"),
        ship("Tjakra", "petroleum", "1000", "4 year", "JG-7932", "Soviet union"),
        ship("Gajah Mada", "LPG", "250", "1 year", "KH-7253", "Indonesia")]

# menampilkan keluaran data
print("-AIR PLANE DATA : 5")
print()
for i in range (5):
    print("Air Plane " , i+1)
    print(airplaneObj[i].printAirplane())

print("-SHIP DATA : 5")
print()
for i in range(5):
    print("Ship " , i+1)
    print(shipObj[i].printShip())



