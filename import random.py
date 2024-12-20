import random
import string
from PIL import Image, ImageDraw, ImageFont

def generate_captcha(text, width=200, height=60):
    # Create a new image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.truetype('arial.ttf', 36)
    
    # Draw the text on the image
    text_width, text_height = draw.textsize(text, font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), text, font=font, fill='black')
    
    # Add some noise
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill='black')
    
    return image

def random_text(length=5):
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# Generate a random text
captcha_text = random_text()

# Generate the CAPTCHA image
captcha_image = generate_captcha(captcha_text)

# Save the image
captcha_image.save('captcha.png')

# Display the image
captcha_image.show()
