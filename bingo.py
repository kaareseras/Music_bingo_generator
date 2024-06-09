import random
from PIL import ImageFont, ImageDraw, Image
import csv

# Generate a list of 40 real pop music pieces from 1995 to 1999, format it with Title - Artist - Year

pop_pieces = [
    "Barbie Girl - Aqua - 1997",
    "Wannabe - Spice Girls - 1996",
    "Be My Lover - La Bouche - 1995",
    "Baby One More Time - Britney Spears - 1999",
    "Mambo nr. 5 - Lou Bega - 1999",
    "Ice Ice Baby - Vanilla Ice - 1990",
    "Macarena - Los Del Rio - 1993",
    "Give It up - Cut ´N´Move - 1993",
    "Let Me Entertain You - Robbie Williams - 1997",
    "Believe - Cher - 1998",
    "I Want It that Way - Backstreet Boys - 1999",
    "When You´re Gone - Bryan Adams, Melanie C - 1998",
    "Spændt Op Til Lir - Den Gale Pose - 1998",
    "Saturday Night - Whigfield - 1995",
    "I Want You Back - NSYNC - 1997",
    "Dub-I-Dub - Me & My - 1995",
    "MMMBop - Hanson - 1997",
    "Could I Have This Kiss Forever - Enrique Iglesias, Whitney Houston - 1999",
    "Cotton Eye Joe - Rednex - 1994",
    "Livin´la Vida Loca - Ricky Martin - 1999",
    "All That She Wants - Ace of Base - 1992",
    "Genie In a Bottle - Christina Aguilera - 1999",
    "I´d Do Anything For Love - Meat Loaf - 1993",
    "Wonderwall - Oasis - 1995",
    "Don´t Speak - No Doubt - 1995",
    "How Deep Is Your Love - Take That - 1996",
    "En som dig - Back to Back - 1991",
    "I´m Too Sexy - Right Said Fred - 1991",
    "Losing My Religion - R.E.M - 1991",
    "Romeo - Blå øjne - 1995"
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
    cell_size = 300
    cell_offset = 0
    image_width = cell_size * 5
    image_height = cell_size * 2
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    

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
            draw.rectangle([(x1+cell_offset, y1+cell_offset), (x2-cell_offset, y2-cell_offset)], outline="gray", width=5)

            # Write the selected piece in the cell
            piece = pieces[row * 5 + col]
            title_font = ImageFont.truetype("arial.ttf", 22)
            artist_font = ImageFont.truetype("arial.ttf", 15)
            copyright_font = ImageFont.truetype("arial.ttf", 10)
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

    number_position = (image_width - 30, image_height -30)
    draw.text(number_position, f"{number}", font=title_font, fill="black", align="bottom-right")

    number_position = (20, image_height -30)
    draw.text(number_position, "(C)2024 - LawGirls Lmt", font=title_font, fill="black", align="bottom-left", )

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
            draw.text(artist_position, artist_text, font=copyright_font, fill="black", align="center")



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

for item in list_of_pieces:
    print(item.__str__())

for i in range(28):
    # Shuffle the list of pop pieces
    random.shuffle(list_of_pieces)

    # Select 5 random elements from the list
    selected_pieces = random.sample(list_of_pieces, 10)

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