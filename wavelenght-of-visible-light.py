''' Question '''

# The wavelength of visible light ranges from 380 to 750 nanometers (nm).
# While the spectrum is continuous, it is often divided into 6 colors as shown below:

# |-----|---------|------------------------|
# | S/N | Color   |  Wavelength (nm)       |
# |-----|---------|------------------------|
# | 1.  | Violet  |  380 to less than 450  |
# |-----|---------|------------------------|
# | 2.  | Blue    |   450 to less than 495 |
# |-----|---------|------------------------|
# | 3.  | Green   |   495 to less than 570 |
# |-----|---------|------------------------|
# | 4.  | Yellow  |  570 to less than 590  |
# |-----|---------|------------------------|
# | 5.  | Orange  |   590 to less than 620 |
# |-----|---------|------------------------|
# | 6.  | Red     |   620 to 750           |
# |-----|---------|------------------------|

''' Algorithm '''

# Start
# Read the wavelength (in nanometers) from the user
# Check if the wavelength falls within the range for each color
#   If it falls within the range for a color, display the corresponding color
#   If it doesn't fall within any range, display "Not within the visible spectrum"
# Stop

''' Flowchart '''

# (Start) --> [Read wavelength from user] -->
# [Is wavelength within range for Violet?]
#    |
#    | Yes
#    |
#    v
#  [Display "Violet"]
#    |
#    |
#    v
#  [Is wavelength within range for Blue?]
#    |
#    | Yes
#    |
#    v
#  [Display "Blue"]
#    |
#    |
#    v
#  [Is wavelength within range for Green?]
#    |
#    | Yes
#    |
#    v
#  [Display "Green"]
#    |
#    |
#    v
#  [Is wavelength within range for Yellow?]
#    |
#    | Yes
#    |
#    v
#  [Display "Yellow"]
#    |
#    |
#    v
#  [Is wavelength within range for Orange?]
#    |
#    | Yes
#    |
#    v
#  [Display "Orange"]
#    |
#    |
#    v
#  [Is wavelength within range for Red?]
#    |
#    | Yes
#    |
#    v
#  [Display "Red"]
#    |
#    | No
#    v
#  [Display "Not within the visible spectrum"]
#    |
#    v
#  (Stop)


''' Source code '''

# Read the wavelength from the user
# wavelength = int(input("Enter the wavelength (in nanometers): "))

# # Check if the wavelength falls within the range for each color
# if 380 <= wavelength < 450:
#     print("Violet")
# elif 450 <= wavelength < 495:
#     print("Blue")
# elif 495 <= wavelength < 570:
#     print("Green")
# elif 570 <= wavelength < 590:
#     print("Yellow")
# elif 590 <= wavelength < 620:
#     print("Orange")
# elif 620 <= wavelength <= 750:
#     print("Red")
# else:
#     print("Not within the visible spectrum")


''' Another method '''

# Read the wavelength from the user
wavelength = int(input("Enter the wavelength (in nanometers): "))

# Dictionary mapping wavelength ranges to colors
color_ranges = {
    range(380, 450): "Violet",
    range(450, 495): "Blue",
    range(495, 570): "Green",
    range(570, 590): "Yellow",
    range(590, 620): "Orange",
    range(620, 750): "Red"
}

# Check if the wavelength falls within any range and display the corresponding color
for color_range, color in color_ranges.items():
    if wavelength in color_range:
        print(color)
        break
else:
    print("Not within the visible spectrum")
