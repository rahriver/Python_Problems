# Write a class, find a way to show different instance attributes, and then lastly find a way to compare salaries and print people with the same salary.

class Teacher:

    def __init__(self, first, last, phone, hour, salary):
        self.first = first
        self.last = last
        self.phone = str(phone)
        self.hour = int(hour)
        self.salary = int(salary)

    def __repr__(self):
        return f"Name: {self.first}\nLast Name: {self.last}\nPhone Number: {self.phone}\nPer Hour: {self.hour}$\nSalary: {self.salary}$"

    def Info(self):
        return f"{self.first} {self.last}: {self.salary}"

t1 = Teacher("Masoumeh", "ghobeh", "09126778954", 20, 150000)
t2 = Teacher("Arash", "Lotfi", "09126778954", 30, 130000)
t3 = Teacher("Javad", "rezaie", "09126778954", 14, 130000)
t4 = Teacher("Morteza", "samimi", "09126778954", 15, 144400)
t5 = Teacher("Ali", "hakimi", "09126778954", 10, 114040)

l = [t1, t2, t3, t4, t5]
s = []

for i in l:
    s.append(i.salary)

for i in l:
    if s.count(i.salary) > 1:
        print(f"{i.first} {i.last}: {i.salary}")
