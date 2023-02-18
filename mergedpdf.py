from PyPDF2 import PdfWriter

mergee = PdfWriter()
files = input("enter files name with quama with no space: ")
files = files.split(",")
print(files)

for pdf in files:
  mergee.append(pdf)

mergee.write("merged-4.pdf")
mergee.close()