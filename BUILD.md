# 上海欣耀环禹 APP 构建指南

## 当前进度

- ✅ 已创建Android项目结构 (android/)
- ✅ 已安装Capacitor依赖
- ✅ 已配置Web资源

## 环境问题

当前服务器**未安装Android SDK**，无法直接生成APK。

## 本地构建方案

### 方案1：本地Capacitor构建（推荐）

```bash
# 1. 安装 Node.js 18+
node --version

# 2. 安装 Android Studio
# 下载: https://developer.android.com/studio

# 3. 配置环境变量
export ANDROID_HOME=~/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools

# 4. 构建
cd xyhy
npx cap sync android
cd android && ./gradlew assembleRelease
```

### 方案2：使用GitHub Actions（免费云构建）

创建 `.github/workflows/build.yml`:
```yaml
name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm install
      - run: npx cap sync android
      - uses: submint/action-gradle@main
        with:
          args: assembleRelease
      - uses: actions/upload-artifact@v4
        with:
          name: apk
          path: android/app/build/outputs/apk/release/*.apk
```

### 方案3：在线构建服务

- **VoltBuilder** (https://volt.build) - 云端Capacitor构建
- **PhoneGap Build** (https://build.phonegap.com) - Cordova云构建
- **AppCenter** (https://appcenter.ms) - Microsoft免费移动CI

### 方案4：PWA（无需APK，直接使用）

```bash
# 使用Vite创建PWA
npm create vite@latest . -- --template vanilla
npm install vite-plugin-pwa

# 编辑 vite.config.js
import { VitePWA } from 'vite-plugin-pwa'
export default defineConfig({
  plugins: [VitePWA({
    registerType: 'autoUpdate',
    manifest: {
      name: '欣耀环禹',
      short_name: 'XYHY',
      theme_color: '#f97316',
      icons: [
        { src: 'icon-192.png', sizes: '192x192', type: 'image/png' },
        { src: 'icon-512.png', sizes: '512x512', type: 'image/png' }
      ]
    }
  })]
})

# 部署到任意静态托管（Vercel, Netlify, GitHub Pages）
```

## iOS构建（仅macOS）

```bash
# 需要 macOS + Xcode
npx cap add ios
open ios/App.xcworkspace
# 在Xcode中 Product → Archive
```

## 技术支持

微信: 18916695809