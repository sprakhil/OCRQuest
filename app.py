import os
import easyocr
import gradio as gr 
from PIL import Image

reader = easyocr.Reader(['en', 'hi'], gpu=False)

def convert_hindi_numerals_to_arabic(text):
    hindi_to_arabic = {
        '०': '0', '१': '1', '२': '2', '३': '3', '४': '4',
        '५': '5', '६': '6', '७': '7', '८': '8', '९': '9'
    }
    for hindi, arabic in hindi_to_arabic.items():
        text = text.replace(hindi, arabic)
    return text

def extract_text(image_path):
    img = Image.open(image_path)

    temp_jpg_path = "temp_image.jpg"
    img.convert("RGB").save(temp_jpg_path,"JPEG")

    result = reader.readtext(temp_jpg_path, detail=0) 
    extracted_text = " ".join(result)
    extracted_text = convert_hindi_numerals_to_arabic(extracted_text)

    os.remove(temp_jpg_path)

    return extracted_text

def search_text(image_path, keyword):
    extracted_text = extract_text(image_path)
    if keyword.lower() in extracted_text.lower():
        return f"Keyword '{keyword}' found in the extracted text.", extracted_text
    else:
        return f"Keyword '{keyword}' not found in the extracted text.", extracted_text

def create_interface():
    interface = gr.Interface(
        fn=search_text, 
        inputs=[
            gr.Image(type="filepath", label="Upload Image"),  # Changed to filepath
            gr.Textbox(lines=1, placeholder="Enter keyword to search", label="Keyword") 
        ],
        outputs=[
            gr.Textbox(label="Search Result"),  
            gr.Textbox(label="Extracted Text")  
        ],
        title="OCR and Keyword Search Application",
        description="Upload an image containing text in English or Hindi. Enter a keyword to search within the extracted text.",
    )
    
    return interface

if __name__ == "__main__":
    interface = create_interface()
    interface.launch(share=True)
