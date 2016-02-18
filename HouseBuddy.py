### Chris Dower 2016
### House Buddy
 
import random

class House(object):
    """docstring for House"""
    def __init__(self, bros, chores):
        super(House, self).__init__()
        self.brothers = bros
        self.tasks = chores
        self.assignments = []
        self.setRitual()
        self.assign()
        self.numTasks()

    def setRitual(self):
        i=0
        while i < len(self.brothers):
            if len(self.brothers[i]) > 3:
                self.brothers[i][3] = i
            else:
                self.brothers[i].append(i)
            i+=1

    def printAssignments(self):
        self.assignments = sorted(self.assignments, key=lambda assigned_task: assigned_task[0][3])
        for assignment in self.assignments:
            print assignment[0][0] +": " + assignment[1] + " " + assignment[2]

    def numTasks(self):
        sum = 0
        for task in self.tasks:
            sum += len(task[1])
        print sum

    ### Assembles assignments from list of tasks and brothers
    ### [brother, task[0], task[1][x]]
    def assign(self):
        for task in self.tasks:
            for subTask in task[1]:
                bIndex = int(random.random() * len(self.brothers))
                self.assignments.append([self.brothers[bIndex], task[0], subTask])
                self.brothers.pop(bIndex)
        self.printAssignments()



if __name__ == '__main__':
    execfile("./brother_list.py")
    execfile("./task_list.py")
    WorkParty = House(brother_list, task_list)