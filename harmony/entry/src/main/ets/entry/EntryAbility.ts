import UIAbility from '@ohos.app.ability.UIAbility';

export default class EntryAbility extends UIAbility {
  onCreate(want, launchParam) {
    console.log('EntryAbility onCreate');
  }

  onDestroy() {
    console.log('EntryAbility onDestroy');
  }

  onWindowStageCreate(windowStage) {
    console.log('EntryAbility onWindowStageCreate');
    windowStage.loadContent('pages/index/index');
  }

  onWindowStageDestroy() {
    console.log('EntryAbility onWindowStageDestroy');
  }

  onForeground() {
    console.log('EntryAbility onForeground');
  }

  onBackground() {
    console.log('EntryAbility onBackground');
  }
}