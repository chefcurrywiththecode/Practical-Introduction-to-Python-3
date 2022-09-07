#Create a float object named weight with the value 0.2, and create a string object named animal with the value "newt". Then use these objects to print the following string using only string concatenation:
from sunau import AUDIO_FILE_ENCODING_MULAW_8


weight=0.2
animal="newt"

print(str(weight) + " kg is the weight of the " + animal)

print("{} kg is the weight of the {} ".format(weight, animal))

print(f"{weight} kg is the weight of the {animal}")