#!/bin/bash
# ---------------------------------------------------------------------------
# 使用 DevEco Studio 打开 HarmonyOS 项目的正确方式
# ---------------------------------------------------------------------------
# 问题: 直接打开 harmony/ 目录 DevEco Studio 无法识别
# 原因: 缺少 hvigorw 包装器（由 DevEco Studio 在新建项目时自动生成）
# ---------------------------------------------------------------------------
# 解决方案:

echo "=== 鸿蒙项目设置指南 ==="
echo ""
echo "步骤1: 打开 DevEco Studio"
echo ""
echo "步骤2: File → New → Create Project"
echo "  选择: Empty Ability (Stage Model)"
echo "  Project Name: xyhy-hm"
echo "  Bundle name: com.xyhy.app"
echo "  Compile SDK: 11"
echo "  Compatible SDK: 11"
echo "  Save Location: 任意位置"
echo ""
echo "步骤3: 创建完成后关闭项目"
echo ""
echo "步骤4: 替换文件"
echo "  cp xyhy/xyhy-pad-cn-en.html xyhy-hm/entry/src/main/resources/base/rawfile/"
echo "  cp xyhy/xyhy-short1.mp4 xyhy-hm/entry/src/main/resources/base/rawfile/"
echo "  cp -r xyhy/extracted_images_v2 xyhy-hm/entry/src/main/resources/base/rawfile/"
echo ""
echo "步骤5: 修改 entry/src/main/ets/pages/Index.ets 添加 WebView"
echo ""
echo "  import web_webview from '@ohos.web.webview';"
echo "  @Entry @Component"
echo "  struct Index {"
echo "    controller: web_webview.WebviewController = new web_webview.WebviewController();"
echo "    build() {"
echo "      Column() {"
echo "        Web({ src: \$rawfile('xyhy-pad-cn-en.html'), controller: this.controller })"
echo "          .width('100%').height('100%')"
echo "          .javaScriptAccess(true)"
echo "          .domStorageAccess(true)"
echo "      }.width('100%').height('100%')"
echo "    }"
echo "  }"
echo ""
echo "步骤6: DevEco Studio 重新打开 xyhy-hm"
echo "  Build → Build HAP(s)"
echo ""

