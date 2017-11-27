#You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.
#Write a class TempTracker with these methods:

#insert()—records a new temperature
#get_max()—returns the highest temp we've seen so far
#get_min()—returns the lowest temp we've seen so far
#get_mean()—returns the mean ↴ of all temps we've seen so far
#get_mode()—returns a mode ↴ of all temps we've seen so far
#Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.

#get_mean() should return a float, but the rest of the getter methods can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..110.

#If there is more than one mode, return any of the modes.

class TempTracker:
    
    def __init__(self):
        
        #matrix where the ith element is the number of times i degrees has been recorded
        self.temperatures = [0]*111 # temps range from 0 to 110, that makes 110 + 1 possible temps
        
        # Init fields
        self.mean = 0
        self.mode = 0
        self.max = 0
        self.min = 111 # If no records exist min will be 110, is that a bug?
        self.num_of_records = 0 # Total number of recorded temperatures
        
    # All methods run in O(1), none of them iterathes through the list of temperatures
    def insert(self, temp):
        # Increase the number of times a temperature has been recorded
        self.temperatures[temp] = self.temperatures[temp] + 1
        # Update number of total records
        self.num_of_records = self.num_of_records + 1
    
        # Update mode if the new temperature is more common than previous mode
        if self.temperatures[temp] > self.temperatures[self.mode]: self.mode = temp
      
        # Update mins and max
        self.min = min(self.min, temp)
        self.max = max(self.max, temp)

        # Update mean using prev mean and number of records 
        self.mean =  (((self.num_of_records - 1) * self.mean) + temp)/self.num_of_records

    def getMin(self):
        return self.min
    
    def getMax(self):
        return self.max
    
    def getMode(self):
        return self.mode
    
    def getMean(self):
        return self.mean
    
    
temp = TempTracker()

temp.insert(35)
temp.insert(35)
temp.insert(35)
temp.insert(35)
temp.insert(67)
temp.insert(85)
temp.insert(85)
temp.insert(85)
temp.insert(85)
temp.insert(95)
temp.insert(73)
temp.insert(89)
temp.insert(82)
print(temp.getMin())
print(temp.getMax())
print(temp.getMean())
print(temp.getMode())
        
