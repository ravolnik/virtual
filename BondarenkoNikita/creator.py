import csv
from PIL import Image


with open('colors.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        color_name, hex_value = row[0], row[1]
        
        image = Image.new('RGB', (50, 50), hex_value)
        image.save(f'colors/{color_name}.png')  
