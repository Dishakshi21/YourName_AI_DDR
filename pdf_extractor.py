import fitz
import os

def extract_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")

    text = ""
    images = []

    os.makedirs("images", exist_ok=True)

    for i, page in enumerate(doc):
        text += page.get_text("text")

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)

            img_bytes = base_image["image"]
            img_path = f"images/page{i+1}_{img_index}.png"

            with open(img_path, "wb") as f:
                f.write(img_bytes)

            images.append(img_path)

    return text, images