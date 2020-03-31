#2.7 Ball Table
def projectile(t,v0): # Function for projectile motion
    return v0*t-0.5*g*t**2 #This is the function for projectile motion, when variables plugged in output is the result of this

def change_in_time(n,v0): #Defining the parts of the list
    tlist=[]
    ylist=[]
    t=0
    dt=(2*v0/(g*n))
    while t <=2*v0/g: #While t is less than the given value
        y = projectile(t, v0)
        tlist.append(t)  # tlist.append(2*v0/g)
        ylist.append(y) # ylist.append(projectile_motion(2*v0/g,v0))
        t=t+dt
    return [tlist, ylist] #the outcome of following code is list of tlist and ylist

#We need vale for v0, we will assume that the v0 is 500m/s
v0=500
g = 9.8
n = 11 #We make n 11 because we want 10 elements

listty=change_in_time(n,v0)
print(listty[0]) #Listty left side
print(listty[1]) #Listty right side
