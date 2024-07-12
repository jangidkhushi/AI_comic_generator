import re
import os
from transformers import pipeline

# Define the prompt template
template = """
You are a cartoon creator.

You will be given a short scenario, you must split it into 6 parts.
Each part will be a different cartoon panel.
For each cartoon panel, you will write a description of it with:
 - the characters in the panel, they must be described precisely each time
 - the background of the panel
The description should be only words or groups of words delimited by commas, no sentences.
Always use the characters' descriptions instead of their names in the cartoon panel description.
You cannot use the same description twice.
You will also write the text of the panel.
The text should not be more than 2 small sentences.
Each sentence should start with the character name.

Example input:
Characters: Adrien is a guy with blond hair wearing glasses. Vincent is a guy with black hair wearing a hat.
Adrien and Vincent want to start a new product, and they create it in one night before presenting it to the board.

Example output:

# Panel 1
description: 2 guys, a blond hair guy wearing glasses, a dark hair guy wearing a hat, sitting at the office, with computers
text:
Vincent: I think Generative AI is the future of the company.
Adrien: Let's create a new product with it.
# end

Short Scenario:
{scenario}

Split the scenario into 6 parts:
"""

def generate_panels(scenario):
    # Load a model from Hugging Face
    generator = pipeline('text-generation', model='gpt2')

    # Format the prompt with the scenario
    prompt = template.format(scenario=scenario)

    # Generate the text
    result = generator(prompt, max_length=1000, num_return_sequences=1, truncation=True)

    # Extract and print the generated text
    generated_text = result[0]['generated_text']
    print(generated_text)

    return extract_panel_info(generated_text)

def extract_panel_info(text):
    panel_info_list = []
    panel_blocks = text.split('# Panel')

    for block in panel_blocks:
        if block.strip() != '':
            panel_info = {}
            
            # Extracting panel number
            panel_number = re.search(r'\d+', block)
            if panel_number is not None:
                panel_info['number'] = panel_number.group()
            
            # Extracting panel description
            panel_description = re.search(r'description: (.+)', block)
            if panel_description is not None:
                panel_info['description'] = panel_description.group(1).strip()
            else:
                panel_info['description'] = "Description not found"

            # Extracting panel text
            panel_text = re.search(r'text:\n(.+?)\n# end', block, re.DOTALL)
            if panel_text is not None:
                panel_info['text'] = panel_text.group(1).strip()
            else:
                panel_info['text'] = "Text not found"
            
            panel_info_list.append(panel_info)
    return panel_info_list

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

# Example usage:
scenario = "John, a tall man with brown hair, and Emily, a short woman with red hair, find a mysterious map in their attic and decide to follow it to find a hidden treasure."
panel_info_list = generate_panels(scenario)

# Write the results to a file
with open('output/panels.json', 'w') as outfile:
    import json
    json.dump(panel_info_list, outfile, indent=4)

for panel in panel_info_list:
    print(f"Panel {panel['number']}:")
    print(f"Description: {panel['description']}")
    print(f"Text: {panel['text']}")
    print()
