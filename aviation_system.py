import random


class Airport:
  def __init__(self, name, capacity):
    self.name = name
    self.capacity = capacity
    self.planes = []

  def add_plane(self, plane):
    if len(self.planes) < self.capacity:
      self.planes.append(plane)
      return f"{plane.name} has been added to {self.name}"
    else:
      return "Airport is full"

  def remove_plane(self, plane):
    if plane in self.planes:
      self.planes.remove(plane)
      return f"{plane.name} has been removed from {self.name}"
    else:
      return f"{plane.name} is not at this airport"

class Plane:
  def __init__(self, name, fuel, destination):
    self.name = name
    self.fuel = fuel
    self.destination = destination
    self.location = None

  def take_off(self, airport):
    if self.fuel <= 0:
      return "Not enough fuel to take off"
    elif self.location != airport:
      return "Plane is not at this airport"
    else:
      self.fuel -= 10
      self.location = None
      return f"{self.name} is taking off"

  def land(self, airport):
    if self.fuel <= 0:
      return "Not enough fuel to land"
    elif self.location == airport:
      return "Plane is already at this airport"
    else:
      self.fuel = 0
      self.location = airport
      return f"{self.name} has landed at {airport.name}"

new_york = Airport("New York", 5)
paris = Airport("Paris", 5)
london = Airport("London", 5)

plane1 = Plane("Plane 1", 100, "New York")
plane2 = Plane("Plane 2", 50, "Paris")
plane3 = Plane("Plane 3", 0, "London")

print(new_york.add_plane(plane1))
print(paris.add_plane(plane2))
print(london.add_plane(plane3))

print(plane1.location)
print(plane2.location)
print(plane3.location)

print(plane1.take_off(new_york))
print(plane2.take_off(paris))
print(plane3.take_off(london))

print(plane1.location)
print(plane2.location)
print(plane3.location)

print(plane1.land(paris))
print(plane2.land(new_york))
print(plane3.land(london))

print(new_york.planes)
print(paris.planes)
print(london.planes)

print(new_york.remove_plane(plane1))
print(paris.remove_plane(plane2))
print(london.remove_plane(plane3))

print(new_york.planes)
print(paris.planes)
print(london.planes)

# Simulating delays
def simulate_delay(airport, delay):
  for plane in airport.planes:
    plane.fuel -= delay

simulate_delay(new_york, 10)
simulate_delay(paris, 5)
simulate_delay(london, 15)

# Simulating emergencies
def simulate_emergency(airport):
  for plane in airport.planes:
    plane.fuel = 0

simulate_emergency(new_york)
simulate_emergency(paris)
simulate_emergency(london)
