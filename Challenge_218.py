class To_Do():
    def __init__(self,x):
        self.list = []
        for item in x:
            self.list.append(item)       
        
    def add_item(self, item):
        self.list.append(item)

    def view_list(self):
        for item in self.list:
            print item       

    def delete_item(self, item):
        if item in self.list:
            self.list.remove(item)
        

Samplelist = ["Shower", "Shave", "Sleep", "Die", "Drool"]
todo1 = To_Do(Samplelist)
todo1.view_list()
print "\n\n\n\n"

todo1.add_item("Take a shower.")
todo1.add_item("Go to work.")
todo1.view_list()
print "\n\n\n\n"

todo1.delete_item("Take a shower.")
todo1.delete_item("Shower")
todo1.delete_item("Shave")
todo1.delete_item("Sleep")
todo1.view_list()
print "------------------"
print "\n\n\n\n"

tomo = To_Do(["No","Maybe","Never"])
tomo.view_list()
todo1.view_list()