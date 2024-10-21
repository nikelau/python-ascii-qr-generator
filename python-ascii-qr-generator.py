import qrcode
from PIL import Image

def create_ascii_qr(data, size=1):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, box_size=1, border=1)
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Resize the image
    img = img.resize((size * img.size[0], size * img.size[1]))
    
    # Convert to ASCII
    ascii_qr = ""
    for y in range(0, img.size[1], 2):
        for x in range(img.size[0]):
            # Get two vertical pixels at a time
            upper_pixel = img.getpixel((x, y))
            lower_pixel = img.getpixel((x, y+1)) if y+1 < img.size[1] else 255
            
            # Choose ASCII character based on the two pixels
            if upper_pixel == 0 and lower_pixel == 0:
                ascii_qr += "█"
            elif upper_pixel == 0 and lower_pixel == 255:
                ascii_qr += "▀"
            elif upper_pixel == 255 and lower_pixel == 0:
                ascii_qr += "▄"
            else:
                ascii_qr += " "
        ascii_qr += "\n"
    
    return ascii_qr

def main():
    print("Compact ASCII QR Code Generator")
    print("-------------------------------")
    
    while True:
        data = input("Enter the URL or text (or 'q' to quit): ")
        if data.lower() == 'q':
            break
        
        size = input("Enter the size (default is 1): ")
        size = int(size) if size.isdigit() else 1
        
        ascii_qr = create_ascii_qr(data, size)
        print("\nHere's your compact ASCII QR code:")
        print(ascii_qr)
        print(f"Data: {data}")

if __name__ == "__main__":
    main()