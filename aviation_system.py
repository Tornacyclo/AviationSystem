class Plane:
  def __init__(self, name, fuel, destination):
    self.name = name
    self.fuel = fuel
    self.destination = destination

  def take_off(self):
    if self.fuel <= 0:
      return "Not enough fuel to take off"
    else:
      self.fuel -= 10
      return f"{self.name} is taking off"

  def land(self):
    if self.fuel <= 0:
      return "Not enough fuel to land"
    else:
      self.fuel = 0
      return f"{self.name} has landed at {self.destination}"

plane1 = Plane("Plane 1", 100, "New York")
plane2 = Plane("Plane 2", 50, "Paris")
plane3 = Plane("Plane 3", 0, "London")

print(plane1.take_off())
print(plane2.take_off())
print(plane3.take_off())
print(plane1.land())
print(plane2.land())
print(plane3.land())
