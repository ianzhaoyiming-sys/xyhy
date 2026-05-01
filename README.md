# XYHY - 上海欣耀环禹汽车维修设备APP

## 文件结构
```
xyhy/
├── android/           # Android原生项目
├── ios/               # iOS原生项目
├── dist/              # Web资源
├── capacitor.config.json
└── package.json
```

## 本地构建

### Android (需要本地环境)
```bash
npm install
npx cap sync android
cd android && ./gradlew assembleRelease
```

### iOS (仅macOS)
```bash
npx cap add ios
open ios/App.xcworkspace
```

## 在线构建（无需本地环境）

| 服务 | 免费额度 | 地址 |
|------|---------|------|
| VoltBuilder | 30天 | volt.build |
| PhoneGap Build | 私有 | build.phonegap.com |
| AppCenter | 无限 | appcenter.ms |

## Web托管（PWA）

```bash
npm create vite@latest . -- --template vanilla
```
部署到 Vercel / Netlify / GitHub Pages