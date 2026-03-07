# Program 1: Hybrid Inheritance Example

class Company:
    def company_info(self):
        print("This is the company information")

class Manager(Company):
    def manager(self):
        print("Manager manages the team")

class Developer(Company):
    def developer(self):
        print("Developer writes code")

class TeamLead(Manager, Developer):
    def lead(self):
        print("TeamLead leads the project")

print("----- Hybrid Inheritance Example -----")
obj = TeamLead()
obj.company_info()
obj.manager()
obj.developer()
obj.lead()