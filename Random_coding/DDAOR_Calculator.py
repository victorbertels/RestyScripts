
def DD_time(time):
    time = int(input("how many minutes do you need: "))
    bike_speed = 24000
    hour = 60
    tot_time = bike_speed * time / hour

    return(tot_time)


print(f"Set your Radius to ",DD_time(10), " meters, if you want {{time}} prep time")



 