"""Employee pay calculator."""
import re

"""ENTER YOUR SOLUTION HERE!"""

import re

class Employee:
    def __init__(self, name):
        self.name = name
        self.contract_type = None
        self.hourly_wage = None
        self.monthly_salary = None
        self.hours_worked = None
        self.bonus = None
        self.commission_per_contract = None
        self.num_contracts = None

    def set_monthly_salary(self, salary):
        self.contract_type = 'salary'
        self.monthly_salary = salary

    def set_hourly_contract(self, hourly_wage, hours_worked):
        self.contract_type = 'hourly'
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def set_bonus(self, bonus):
        self.bonus = bonus

    def set_commission(self, commission_per_contract, num_contracts):
        self.commission_per_contract = commission_per_contract
        self.num_contracts = num_contracts

    def get_pay(self):
        contract_pay = 0
        commission = 0
        if self.contract_type == 'salary':
            contract_pay = self.monthly_salary
        elif self.contract_type == 'hourly':
            contract_pay = self.hourly_wage * self.hours_worked

        if self.bonus:
            contract_pay += self.bonus

        if self.commission_per_contract and self.num_contracts:
            commission = self.commission_per_contract * self.num_contracts

        total_pay = contract_pay + commission
        return total_pay


    def __str__(self):
        explanation = f"{self.name} works on a"

        if self.contract_type == 'salary':
            explanation += f" monthly salary of {self.monthly_salary}"
            if self.commission_per_contract and self.num_contracts:
                explanation += f" and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract"
            if self.bonus:
                explanation += f" and receives a bonus commission of {self.bonus}"



        elif self.contract_type == 'hourly':
            explanation += f" contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
            if self.commission_per_contract and self.num_contracts:
                explanation += f" and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract"
            if self.bonus:
                explanation += f" and receives a bonus commission of {self.bonus}"

        explanation += "."



        explanation += f" Their total pay is {self.get_pay()}."

        return explanation



# Creating employee objects and setting their contracts, bonuses, and commissions
billie = Employee('Billie')
billie.set_monthly_salary(4000)

charlie = Employee('Charlie')
charlie.set_hourly_contract(25, 100)

renee = Employee('Renee')
renee.set_monthly_salary(3000)
renee.set_commission(200, 4)

jan = Employee('Jan')
jan.set_hourly_contract(25, 150)
jan.set_commission(220, 3)

robbie = Employee('Robbie')
robbie.set_monthly_salary(2000)
robbie.set_bonus(1500)

ariel = Employee('Ariel')
ariel.set_hourly_contract(30, 120)
ariel.set_bonus(600)



