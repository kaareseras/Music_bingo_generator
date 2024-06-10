import random
from PIL import ImageFont, ImageDraw, Image
import csv

main_title = "TilsynsBingo"
author = "Hanne""(C)2024 - Hanne Lmt"
secondary_text = "Bingoplader til tilsynsbesøg"
generate_count = 28
cell_size = 300
cell_offset = 0
rows= 2
colls = 5


# Generate a list of 40 real pop music pieces from 1995 to 1999, format it with Title - Artist - Year
pop_pieces = [
    "Smuk som et stjerneskud - Brødrene Olsen - 1990",
    "Mamma Mia - ABB - 1975",
    "Jalousi - Medina - 2009",
    "Girls Just Want to Have Fun - Cyndi Lauper - 1983",
    "I Will Survive - Gloria Gaynor - 1978",
    "Kongen Af Danmark - Malte Ebert - 1999",
    "Kom Tilbage Nu - Danseorkestret - 1985",
    "Jeg Vil La`Lyset brænde - Ray Dee Ohh - 1988",
    "Sig Du Ka´Li´Mig - Tøsedrengene - 1985",
    "Hold Me Now - Johnny Logan - 1987",
    "Only Teardrops - Emmelie de Forest - 2013",
    "I En Lille Båd Der Gynger - Bamses Venner - 1980",
    "I Want It That Way - Backstreet Boys - 1999",
    "Billie Jean - Michael Jackson - 1982",
    "Øde Ø - Rasmus Seebach - 2011",
    "Believe - Cher - 1998",
    "Kiss - Prince - 1986",
    "Vågner I natten - Dodo & the Dodos - 1987",
    "Stayin´Alive - Bee Gees - 1977",
    "De Første Kærester På Månen - TV-2 - 1986",
    "Hvor ska´vi sove i nat - Laban - 1982",
    "Bohemian Rhapsody - Queen - 1975",
    "Don´t Go Breaking My Heart - Elton John, Kiki Dee - 1976",
    "Oh, Pretty Woman - Roy Orbison - 1964",
    "Imagine - John Lennon - 1971",
    "Kender du det? - Søren Kragh-Jacobsen - 1985",
    "En som dig - Back To Back - 1989",
    "STOR MAND - Tobias Rahim, Andreas Odbjerg - 2020",
    "I will Always Love You - Whitney Houston - 1992",
    "Glor På Vinduer - Anne Linnet, Marquis De Sade - 1986"
]


list_of_pieces = []

class Piece:
    def __init__(self, number, title, artist, year):
        self.number = number
        self.title = title
        self.artist = artist
        self.year = year
        list_of_pieces.append(self)

    def __str__(self):
        return f"{self.number}. {self.title} - {self.artist} - {self.year}"

list_of_grids = []    
class bingo_grid:
    def __init__(self, number, pieces: list[Piece]):
        self.number = number
        self.pieces = pieces
        self.image = create_bingo_grid(number,pieces)
        list_of_grids.append(self)

    def __str__(self):
        return f"{self.number}. {self.pieces}"

def create_bingo_grid(number:int, pieces: list[Piece]):
    # Create a blank image with white background
    main_title_height = 80
    image_width = cell_size * colls
    main_title_width = image_width
    image_height = cell_size * rows
    image = Image.new("RGB", (image_width, main_title_height+image_height), "white")
    draw = ImageDraw.Draw(image)

    # Calculate the width and height of each cell in the grid
    cell_width = image_width / colls
    cell_height = image_height / rows

    # Draw the title
    draw.rectangle([(0,0), (main_title_width, main_title_height)], fill="black", width=10)
    main_title_font = ImageFont.truetype("arial.ttf", 60)
    main_title_position = (image_width/2, main_title_height/2)
    draw.text(main_title_position, main_title, font=main_title_font, fill="white", align="center", anchor="mm")

    # Draw the secondary text left of the main title
    secondary_text_font = ImageFont.truetype("arial.ttf", 25)
    secondary_text_x1, secondary_text_y1, secondary_text_x2, secondary_text_y2 = draw.textbbox((0,0), secondary_text, font=secondary_text_font, align="center")
    
    #print(secondary_text_x1, secondary_text_y1, secondary_text_x2, secondary_text_y2)

    secondary_text_y_padding = 50
    secondary_text_x = secondary_text_x2 + secondary_text_y_padding
    secondary_text_y = main_title_height / 2 
    secondary_text_position = (secondary_text_x, secondary_text_y)

    draw.text(secondary_text_position, secondary_text, font=secondary_text_font, fill="white", anchor="rm")

    # Draw the secondary text right of the main title
    secondary_text_x = image_width - secondary_text_x2 - secondary_text_y_padding
    secondary_text_position = (secondary_text_x, secondary_text_y)
    draw.text(secondary_text_position, secondary_text, font=secondary_text_font, fill="white", anchor="lm")


    # Draw the grid
    for row in range(rows):
        for col in range(colls):
            # Calculate the top left coordinates of the cell
            x1 = col * cell_width
            y1 = (row * cell_height) + main_title_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height

            # Draw a rectangle for the cell
            draw.rectangle([(x1+cell_offset, y1+cell_offset), (x2-cell_offset, y2-cell_offset)], outline="gray", width=5)

            # Write the selected piece in the cell
            piece = pieces[row * colls + col]
            title_font = ImageFont.truetype("arial.ttf", 22)
            artist_font = ImageFont.truetype("arial.ttf", 15)
            title_text = piece.title
            artist_text = piece.artist


            title_x1, title_y1, title_x2, title_y2  = draw.textbbox((0, 0),title_text, font=title_font, align="center")
            artist_x1, artist_y1, artist_x2, artist_y2  = draw.textbbox((0, 0),artist_text, font=artist_font, align="center")

            title_width = title_x2 - title_x1
            title_height = title_y2 - title_y1
            artist_width = artist_x2 - artist_x1
            artist_height = artist_y2 - artist_y1 

            title_height = 28
            artist_height = 19   
            
            title_position = (x1 + cell_width/2 - title_width/2, y1 + cell_height/2 - title_height/2 -10 )
            artist_position = (x1 + cell_width/2 - artist_width/2, y1 + cell_height/2 + artist_height/2  )

            draw.text(title_position, title_text, font=title_font, fill="black", align="center")
            draw.text(artist_position, artist_text, font=artist_font, fill="black", align="center")

    number_position = (image_width - 30, image_height -30 + main_title_height)
    draw.text(number_position, f"{number}", font=title_font, fill="black", align="bottom-right")

    number_position = (20, image_height -30 + main_title_height)
    draw.text(number_position, author, font=title_font, fill="black", align="bottom-left", )
    
    #image.show()
    return image

def create_bingo_grid_old(number: int):
    # Create a blank image with white background
    cell_size = 300
    cell_offset = 0
    image_width = cell_size * 5
    image_height = cell_size * 2
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Shuffle the list of pop pieces
    random.shuffle(pop_pieces)

    # Select 5 random elements from the list
    selected_pieces = random.sample(pop_pieces, 10)

    # Calculate the width and height of each cell in the grid
    cell_width = image_width // 5
    cell_height = image_height // 2

    # Draw the grid
    for row in range(2):
        for col in range(5):
            # Calculate the top left coordinates of the cell
            x1 = col * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height

            # Draw a rectangle for the cell
            draw.rectangle([(x1+cell_offset, y1+cell_offset), (x2-cell_offset, y2-cell_offset)], outline="black", width=5)

            # Write the selected piece in the cell
            piece = selected_pieces[row * 5 + col]
            title_font = ImageFont.truetype("arial.ttf", 22)
            artist_font = ImageFont.truetype("arial.ttf", 15)
            title_text = piece.split(" - ")[0]
            artist_text = piece.split(" - ")[1]


            title_x1, title_y1, title_x2, title_y2  = draw.textbbox((0, 0),title_text, font=title_font, align="center")
            artist_x1, artist_y1, artist_x2, artist_y2  = draw.textbbox((0, 0),artist_text, font=artist_font, align="center")

            title_width = title_x2 - title_x1
            title_height = title_y2 - title_y1
            artist_width = artist_x2 - artist_x1
            artist_height = artist_y2 - artist_y1 

            title_height = 28
            artist_height = 19   
            
            title_position = (x1 + cell_width/2 - title_width/2, y1 + cell_height/2 - title_height/2 -10 )
            artist_position = (x1 + cell_width/2 - artist_width/2, y1 + cell_height/2 + artist_height/2  )

            draw.text(title_position, title_text, font=title_font, fill="black", align="center")
            draw.text(artist_position, artist_text, font=artist_font, fill="black", align="center")

    # Save the image
    image.save(f"bingo_grid_{number}.png")
    #image.show()
    return selected_pieces

# Call the function to create the bingo grid
count = 0
for item in pop_pieces:
    print (item).__str__()
    title = item.split(" - ")[0]
    artist = item.split(" - ")[1]
    year = item.split(" - ")[2]
    Piece(count,title, artist, year)
    count += 1

#for item in list_of_pieces:
    #print(item.__str__())

for i in range(generate_count):
    # Shuffle the list of pop pieces
    random.shuffle(list_of_pieces)

    # Select 5 random elements from the list
    selected_pieces = random.sample(list_of_pieces, rows * colls)

    bingo_grid(i,selected_pieces)

for item in list_of_grids:
    # Save the image
    item.image.save(f"bingo/bingo_grid_{item.number}.png")

    # Create a CSV file to store the bingo plates
    with open('bingo_plates.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Bingo Plate Number', 'First 5 Numbers','','','','', 'Last 5 Numbers','','','',''])

        # Write each bingo plate as a row in the CSV file
        for plate in list_of_grids:
            plate_number = plate.number
            first_5_numbers = [piece.number for piece in plate.pieces[:5]]
            last_5_numbers = [piece.number for piece in plate.pieces[5:]]
            writer.writerow([
                plate_number, 
                first_5_numbers[0], 
                first_5_numbers[1],
                first_5_numbers[2],
                first_5_numbers[3],
                first_5_numbers[4],
                last_5_numbers[0],
                last_5_numbers[1],
                last_5_numbers[2],
                last_5_numbers[3],
                last_5_numbers[4]
            ]
           )