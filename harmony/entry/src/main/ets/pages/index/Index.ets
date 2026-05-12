@Entry
@Component
struct Index {
  webController: WebViewController = new WebViewController()

  build() {
    Column() {
      Web({
        src: $rawfile('xyhy-pad-cn-en.html'),
        controller: this.webController
      })
        .domStorageAccess(true)
        .fileAccess(true)
        .onlineImageAccess(true)
        .width('100%')
        .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}