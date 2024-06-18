Barcodes are widely used in product packaging. When shopping, the cashier scans those barcodes of the products you purchase to directly read and input their price to the system.

ENCODER

Encoder creates an canvas of size 400 X 800.
I have defined a variable "step" where, Step = 9 pixels (space between bars).
Bar Height: The height of the bar be fixed from row 10 to row 350. 
Empty space between words be denoted by a shorter bar from row 150 to row 250.
Bar width: Empty space has a fixed width of 1 pixel. All other alphabets (ignored case) will have their corresponding bar width equals to the position of that alphabet+1. 
For example, character “A” or “a” must have a bar of width 2 pixels and character “S” or “s” must have a bar width of 20 pixels (position 19+1). See Fig.2. and Fig.3 for a visual explanation.
loop through the entered string character by character and encode (draw) the barcode according to the specifications above.
Result image is saved as image (output.png format).

DECODER

Read the output.png image.
Scan the image horizontally through the middle line (row 200) and follow the below algorithm to reconstruct the Barcode string (str):
Set the string Str = “”;
Scan the middle line at row 200 and calculate the width (w) of each bar.
IF w == 1 % is empty space -short bar-
Insert space into the string Str;
Else % is character
Match the character corresponding to that width, append the char to the
string Str.
End IF;
