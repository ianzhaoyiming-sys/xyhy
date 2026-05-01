#!/bin/bash
set -e

echo "=== XYHY APP Build ==="

if ! command -v java &> /dev/null; then
    echo "Java not found. Install JDK 17"
    exit 1
fi

if [ -z "$ANDROID_HOME" ]; then
    echo "ANDROID_HOME not set"
    exit 1
fi

npm install
npx cap sync android

cd android
chmod +x gradlew
./gradlew assembleRelease

APK_PATH="app/build/outputs/apk/release/app-release.apk"
if [ -f "$APK_PATH" ]; then
    cp "$APK_PATH" "../XYHY-app.apk"
    echo "Done: XYHY-app.apk"
fi