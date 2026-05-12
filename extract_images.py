import os
import sys
from PIL import Image
import io

try:
    from docx import Document
except ImportError:
    print("Error: python-docx not installed. Run: pip install python-docx")
    sys.exit(1)

def is_grayscale_image(img):
    if img.mode == 'L':
        return True

    if img.mode == 'RGB':
        pixels = list(img.getdata())
        sample_size = min(10000, len(pixels))
        step = len(pixels) // sample_size if sample_size > 0 else 1

        color_pixel_count = 0
        for i in range(0, len(pixels), step):
            r, g, b = pixels[i]
            max_diff = max(abs(r - g), abs(r - b), abs(g - b))
            if max_diff > 15:
                color_pixel_count += 1

        color_ratio = color_pixel_count / sample_size if sample_size > 0 else 0
        return color_ratio < 0.1

    if img.mode == 'RGBA':
        img_rgb = img.convert('RGB')
        return is_grayscale_image(img_rgb)

    if img.mode == 'P':
        if 'transparency' in img.info:
            img_rgb = img.convert('RGB')
            return is_grayscale_image(img_rgb)
        img_rgb = img.convert('RGB')
        return is_grayscale_image(img_rgb)

    return False

def get_image_color_type(image_stream):
    try:
        image_stream.seek(0)
        img = Image.open(image_stream)
        img.load()

        if is_grayscale_image(img):
            return '黑白'
        else:
            return '彩色'
    except Exception as e:
        return f'未知({e})'

def extract_images_from_docx(docx_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = Document(docx_path)

    color_stats = {'黑白': 0, '彩色': 0, '未知': 0}
    saved_images = []

    image_count = 0

    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image_count += 1
            try:
                image_part = rel.target_part
                image_stream = io.BytesIO(image_part.blob)

                color_type = get_image_color_type(image_stream)
                color_stats[color_type] += 1

                ext = image_part.content_type.split('/')[-1]
                if ext == 'jpeg':
                    ext = 'jpg'

                filename = f"image_{image_count:03d}_{color_type}.{ext}"
                filepath = os.path.join(output_dir, filename)

                with open(filepath, 'wb') as f:
                    f.write(image_part.blob)

                saved_images.append({
                    'filename': filename,
                    'color_type': color_type,
                    'content_type': image_part.content_type
                })

            except Exception as e:
                print(f"Error processing image {image_count}: {e}")

    return color_stats, saved_images

if __name__ == "__main__":
    docx_file = "xyhy.docx"
    output_directory = "extracted_images"

    if not os.path.exists(docx_file):
        print(f"Error: {docx_file} not found")
        sys.exit(1)

    print(f"Processing: {docx_file}")
    print(f"Output directory: {output_directory}")
    print("-" * 50)

    stats, images = extract_images_from_docx(docx_file, output_directory)

    print(f"\n{'='*50}")
    print("提取结果统计")
    print(f"{'='*50}")
    print(f"总图片数量: {sum(stats.values())}")
    print(f"  - 黑白图片: {stats['黑白']}")
    print(f"  - 彩色图片: {stats['彩色']}")
    if stats['未知'] > 0:
        print(f"  - 未知: {stats['未知']}")
    print(f"\n图片已保存到: {output_directory}/")

    print(f"\n{'='*50}")
    print("图片详情列表")
    print(f"{'='*50}")
    for img in images:
        print(f"  {img['filename']} - {img['color_type']}")