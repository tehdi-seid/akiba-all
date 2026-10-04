print("=============== Travel Planner =====================")


destination=input("Enter the destination: ")
distance=float(input("Enter the distance in Km: "))
average_speed=float(input("Enter the average spedd in Km/h: "))

time=distance/average_speed

print("Destination:",destination)
print("Distance:",distance,"Km")
print("Average Speed:",average_speed,"Km/ha")

print("Estimated Travel Time:",round(time,3),"hour or",round(60*time,3),"minutes")
