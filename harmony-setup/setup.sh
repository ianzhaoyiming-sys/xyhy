#!/bin/bash
set -e
echo "=== 鸿蒙项目资源同步脚本 ==="
PROJ_DIR="$(dirname "$0")/.."
HARMONY_DIR="$PROJ_DIR/harmony"
RAWFILE="$HARMONY_DIR/entry/src/main/resources/base/rawfile"

# 复制最新HTML和视频
cp "$PROJ_DIR/xyhy-pad-cn-en.html" "$RAWFILE/"
cp "$PROJ_DIR/xyhy-short1.mp4" "$RAWFILE/"

echo "✅ 资源已同步到 $RAWFILE"
echo "请用 DevEco Studio 打开 harmony/ 目录构建"
