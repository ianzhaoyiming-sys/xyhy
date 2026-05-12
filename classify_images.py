import json
import os
import shutil

def classify_images(manifest_path, images_dir):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    categories = {
        '外观图': [],
        '零部件图': [],
        '尺寸图': [],
        '专利图': [],
        '厂区环境': [],
        '公司介绍': []
    }

    parts_keywords = ['零配件', '配件', '零件', '组件', 'detail', 'component', 'part', 'exploded', 'explosion', '零配件展示']
    size_keywords = ['尺寸', '参数', '规格', 'mm', 'spec', 'feature', '外形尺寸', '安装尺寸', 'structure', 'dimension', '外形图', 'diagram', 'drawing']

    for m in manifest:
        filename = m['file']
        color_type = m.get('color_type', '')
        section = m.get('section', '')
        combined_text = (section + m.get('para_text', '') + m.get('prev_text', '') + m.get('next_text', '')).lower()

        img_num = int(filename.split('_')[1])

        if img_num <= 55:
            categories['公司介绍'].append(filename)
        elif img_num <= 71:
            categories['专利图'].append(filename)
        elif img_num <= 101:
            categories['厂区环境'].append(filename)
        else:
            is_parts = any(kw in combined_text for kw in parts_keywords)
            is_size = any(kw in combined_text for kw in size_keywords)

            if is_parts:
                categories['零部件图'].append(filename)
            elif is_size or color_type == '黑白':
                categories['尺寸图'].append(filename)
            else:
                categories['外观图'].append(filename)

    return categories

if __name__ == '__main__':
    manifest_path = 'extracted_images_v2/image_manifest.json'
    images_dir = 'extracted_images_v2'

    categories = classify_images(manifest_path, images_dir)

    print("=" * 50)
    print("图片分类结果")
    print("=" * 50)
    for cat, files in categories.items():
        print(f"\n{cat}: {len(files)} 张")

    output_base = 'classified_images'
    if os.path.exists(output_base):
        shutil.rmtree(output_base)

    for cat, files in categories.items():
        cat_dir = os.path.join(output_base, cat)
        os.makedirs(cat_dir, exist_ok=True)

        for filename in files:
            src = os.path.join(images_dir, filename)
            if os.path.exists(src):
                dst = os.path.join(cat_dir, filename)
                shutil.copy2(src, dst)

    print(f"\n图片已保存到 {output_base}/ 目录下的子目录")
    for cat in categories.keys():
        print(f"  - {output_base}/{cat}/")