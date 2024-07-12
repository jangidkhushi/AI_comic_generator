# import json
# import os
# from generate_panel import generate_panels
# from stability_ai import text_to_image
# from add_text import add_text_to_panel
# from create_strip import create_strip

# # Define the number of panels (6 panels)
# NUM_PANELS = 6

# # Ensure the output directory exists
# output_dir = "static/output"
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # Function to generate comic based on given prompts
# def generate_comic(prompts, style):
#     panel_images = []

#     # Generate panels for each prompt
#     for i in range(NUM_PANELS):
#         panel_prompt = prompts[i]["description"] + ", cartoon box, " + style
#         print(f"Generating panel {i+1} with prompt: {panel_prompt}")

#         # Generate image based on panel description
#         panel_image = text_to_image(panel_prompt)

#         # Add text to panel image
#         panel_image_with_text = add_text_to_panel(prompts[i]["text"], panel_image)

#         # Append panel image with text to list
#         panel_images.append(panel_image_with_text)

#     # Create comic strip from panel images
#     comic_strip = create_strip(panel_images)

#     # Save comic strip image
#     comic_strip_path = os.path.join(output_dir, "comic_page.png")
#     comic_strip.save(comic_strip_path)

#     return comic_strip_path

# # Example usage:
# SCENARIO = """
# Characters: Peter is a tall guy with blond hair. Steven is a small guy with black hair.
# Peter and Steven walk together in New York when aliens attack the city. They are afraid and try to run for their lives. The army arrives and saves them.
# """

# if __name__ == "__main__":
#     print(f"Generate panels with style for this scenario: \n{SCENARIO}")

#     # User input for comic style
#     print("Choose a style for the comic:")
#     print("1. American Comic, Colored")
#     print("2. Manga, Black and White")
#     print("3. Cartoonish, Vibrant Colors")
#     style_choice = input("Enter the number corresponding to the style: ").strip()

#     # Mapping user input to styles
#     style_map = {
#         "1": "american comic, colored",
#         "2": "manga, black and white",
#         "3": "cartoonish, vibrant colors"
#     }

#     # Ensure valid input
#     STYLE = style_map.get(style_choice, "american comic, colored")

#     # Initialize list to store user prompts
#     prompts = []

#     # User input loop to gather 6 prompts
#     for i in range(NUM_PANELS):
#         prompt_text = input(f"Enter prompt {i+1}: ")
#         prompts.append({"description": prompt_text, "text": ""})  # You can optionally add image paths here if you have specific images

#     # Generate panel information based on user prompts
#     panels = generate_panels(SCENARIO)

#     # Write panel information to a file
#     with open('output/panels.json', 'w') as outfile:
#         json.dump(panels, outfile, indent=4)

#     # Generate comic strip based on panel information and selected style
#     comic_strip_path = generate_comic(prompts, STYLE)

#     print(f"Comic page generated successfully! Saved at: {comic_strip_path}")

import json
import os
from generate_panel import generate_panels
from stability_ai import text_to_image
from add_text import add_text_to_panel
from create_strip import create_strip
from PIL import Image

# Define the number of panels (6 panels)
NUM_PANELS = 6

# Ensure the output directory exists
output_dir = "static/output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to resize the image to half its size
def resize_image(image):
    new_width = image.width // 2
    new_height = image.height // 2
    return image.resize((new_width, new_height), Image.LANCZOS)

# Function to generate comic based on given prompts
def generate_comic(prompts, style):
    panel_images = []

    # Generate panels for each prompt
    for i in range(NUM_PANELS):
        panel_prompt = prompts[i]["description"] + ", cartoon box, " + style
        print(f"Generating panel {i+1} with prompt: {panel_prompt}")

        # Generate image based on panel description
        panel_image = text_to_image(panel_prompt)

        # Add text to panel image
        panel_image_with_text = add_text_to_panel(prompts[i]["text"], panel_image)

        # Append panel image with text to list
        panel_images.append(panel_image_with_text)

    # Create comic strip from panel images
    comic_strip = create_strip(panel_images)

    # Resize comic strip to half its original size
    resized_comic_strip = resize_image(comic_strip)

    # Save comic strip image
    comic_strip_path = os.path.join(output_dir, "comic_page.png")
    resized_comic_strip.save(comic_strip_path)

    return comic_strip_path

# Example usage:
SCENARIO = """
Characters: Peter is a tall guy with blond hair. Steven is a small guy with black hair.
Peter and Steven walk together in New York when aliens attack the city. They are afraid and try to run for their lives. The army arrives and saves them.
"""

if __name__ == "__main__":
    print(f"Generate panels with style for this scenario: \n{SCENARIO}")

    # User input for comic style
    print("Choose a style for the comic:")
    print("1. American Comic, Colored")
    print("2. Manga, Black and White")
    print("3. Cartoonish, Vibrant Colors")
    style_choice = input("Enter the number corresponding to the style: ").strip()

    # Mapping user input to styles
    style_map = {
        "1": "american comic, colored",
        "2": "manga, black and white",
        "3": "cartoonish, vibrant colors"
    }

    # Ensure valid input
    STYLE = style_map.get(style_choice, "american comic, colored")

    # Initialize list to store user prompts
    prompts = []

    # User input loop to gather 6 prompts
    for i in range(NUM_PANELS):
        prompt_text = input(f"Enter prompt {i+1}: ")
        prompts.append({"description": prompt_text, "text": ""})  # You can optionally add image paths here if you have specific images

    # Generate panel information based on user prompts
    panels = generate_panels(SCENARIO)

    # Write panel information to a file
    with open('output/panels.json', 'w') as outfile:
        json.dump(panels, outfile, indent=4)

    # Generate comic strip based on panel information and selected style
    comic_strip_path = generate_comic(prompts, STYLE)

    print(f"Comic page generated successfully! Saved at: {comic_strip_path}")
