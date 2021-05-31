from fastapi import FastAPI, File, Form
from PIL import Image
import pytesseract
import io

app = FastAPI(title='Inference for Optical Character Recognition',
              description='<b>API for extracting english or german text from an image<br><br><br>Contact the developer:<br><font color="#808080">Kay Wünsche: <a href="mailto:">kay.wuensche@gmx.de</a>')

custom_config = r'-c tessedit_char_whitelist=' \
                r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' \
                r'üäöÜÖÄ.!?:""$€@ß/{[|]}\%&=+*->< --psm 6'

@app.post('/optical_character_recognition', tags=['Optical Character Recognition'])
async def optical_character_recognition(
    image_file: bytes = File(..., description="Image for text extraction:"),
    language: str = Form(..., description="Language for text extraction, 'eng' or 'deu':")
):
    """This endpoint takes an image and returns extracted text."""
    result = {}
    if language not in ['eng', 'deu']:
        language = 'eng+ger'
    with Image.open(io.BytesIO(image_file)).convert("RGB") as image_file:
        extracted_text = pytesseract.image_to_string(image_file, lang=language, config=custom_config).split("\n")
        result['extracted text'] = [x.strip() for x in extracted_text if len(x.strip()) > 0]
    return result
