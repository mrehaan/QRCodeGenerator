"""
QR Code Generator
Author: Mohammed Rehaan
Course: MSCS-633-M20 - Advanced Artificial Intelligence
Assignment: Hands-On Assignment 2 - Construct AI QR Code Generator with Python

Description:
This program asks the user for a URL and generates a scannable QR code
image for that URL using the qrcode library. The generated image is
saved to disk and also displayed on screen.

Note:
The assignment was issued on behalf of Biox Systems, so the Biox Systems
website (https://www.bioxsystems.com) is used as the default URL. Pressing
Enter without typing anything will encode that address, or any other URL
can be typed in instead.
"""

import qrcode  # Third-party library used to build QR code matrices and images

# Default URL supplied by the assignment (Biox Systems website).
DEFAULT_URL = "https://www.bioxsystems.com"


def get_url_from_user():
    """
    Prompt the user for a URL and return it as a cleaned string.
    If the user just presses Enter, the Biox Systems URL is used instead,
    since that is the site named in the assignment instructions.
    """
    url = input(
        f"Enter the URL you want to convert into a QR code "
        f"[press Enter to use {DEFAULT_URL}]: "
    ).strip()

    if url == "":
        url = DEFAULT_URL
        print(f"No URL entered, defaulting to {DEFAULT_URL}")

    return url


def generate_qr_code(url, file_name="qr_code.png"):
    """
    Build a QR code image for the given URL and save it to file_name.

    Parameters:
        url (str): The web address to encode.
        file_name (str): The output image file name.
    """
    # Create a QRCode object with basic settings.
    # box_size controls how many pixels each "box" of the QR code takes up.
    # border controls the thickness of the white frame around the code.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add the URL data to the QR code object
    qr.add_data(url)
    qr.make(fit=True)

    # Convert the QR code data into an actual image (black on white)
    image = qr.make_image(fill_color="black", back_color="white")

    # Save the image to disk so it can be shared or screenshotted
    image.save(file_name)
    print(f"QR code successfully generated and saved as '{file_name}'")

    return image


def main():
    """Main program flow: get the URL, build the QR code, show it to the user."""
    print("=== QR Code Generator ===")
    url = get_url_from_user()
    image = generate_qr_code(url)

    # Open the saved image using the default image viewer on the system
    image.show()


if __name__ == "__main__":
    main()


