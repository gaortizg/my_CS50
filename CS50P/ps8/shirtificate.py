from fpdf import FPDF
import os

script_dir = os.path.dirname(__file__) # <-- absolute dir the script is in
rel_path = "./img/shirtificate.png"
abs_file_path = os.path.join(script_dir, rel_path)

# Create class for header
class PDF(FPDF):
    def header(self):
        # Set font
        self.set_font("helvetica", "B", 32)
        
        # Move cursor to right by changing only the x of the cell
        self.cell(80)

        # Print title in cell/box at x=30mm y=10mm away from cursor
        # Text centre aligned within box
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        
        # New line with gap of 150(mm)
        self.ln(100)


pdf = PDF()
pdf.add_page()

# Add shirt image at x=10mm (margin), y=107.1mm
# Allows bottom of image to align with bottom of page
# width = full page width
pdf.image(abs_file_path, 10, 107.1, pdf.epw)

# Prompt user for name
name = input ("Name: ")

# Changes text colour to white
pdf.set_text_color(255)

# Set font
pdf.set_font("helvetica", "B", 16)

# Move cursor to right by changing x of cell
pdf.cell(90)

# Print text in cell/box at 15mm x 10mm away from cursor
# Text centre aligned within box
pdf.cell(15, 10, f"{name} took CS50", align="C")

# Output pdf file
pdf.output(script_dir + "/pdf_with_image.pdf")