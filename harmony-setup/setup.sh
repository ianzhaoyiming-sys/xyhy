#!/bin/bash
set -e
echo "=== 鸿蒙项目资源同步脚本 ==="
PROJ_DIR="$(dirname "$0")/.."
HARMONY_DIR="$PROJ_DIR/harmony"
RAWFILE="$HARMONY_DIR/entry/src/main/resources/base/rawfile"

cp "$PROJ_DIR/xyhy-pad-cn-en.html" "$RAWFILE/"
cp "$PROJ_DIR/xyhy-short1.mp4" "$RAWFILE/"
rm -rf "$RAWFILE/extracted_images_v2"
cp -r "$PROJ_DIR/extracted_images_v2" "$RAWFILE/"

echo "
已完成资源同步到 $RAWFILE

DevEco Studio 构建步骤:
1. 打开 harmony/build.gradle
2. Build -> Build HAP(s)
3. 输出: harmony/entry/build/default/outputs/default/entry-default-unsigned.hap
"
