from withoutbg import WithoutBG

# ⚠️ INSTRUCTION: Change 'input.jpg' to the name of the image file you want to process
INPUT_IMAGE = 'input.jpg'

# ⚠️ INSTRUCTION: Set the name for the output image (PNG format is recommended for transparency)
OUTPUT_IMAGE = 'output_no_bg.png'

def process_image():
    """Removes the background from the specified image file."""
    try:
        print(f"Starting background removal for: {INPUT_IMAGE}")

        remover = WithoutBG.opensource()

        result = remover.remove_background(INPUT_IMAGE)

        result.save(OUTPUT_IMAGE)

        print(f"✅ Success! Result saved to: {OUTPUT_IMAGE}")

    except FileNotFoundError:
        print(f"❌ ERROR: Input file '{INPUT_IMAGE}' not found. Please check the file name and path.")
    except Exception as e:
        print(f"❌ AN ERROR OCCURRED: {e}")

if __name__ == "__main__":
    process_image()