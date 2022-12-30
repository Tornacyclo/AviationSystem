# AviationSystem
A simple Python script for simulating an air traffic control system.

This code defines an Airport class with attributes for the name and capacity of the airport, as well as a list of planes currently at the airport. The Airport class also has methods for adding and removing planes from the airport. The Plane class has been written to include an attribute for the location of the plane, and the take_off and land methods have been modified to take an Airport object as an argument.

The code then creates three instances of the Airport class and three instances of the Plane class, and adds the planes to the airports using the add_plane method. It then prints the locations of the planes and simulates the planes taking off and landing at different airports. Finally, the code defines two functions for simulating delays and emergencies, which reduce the fuel levels of the planes at the specified airports.
