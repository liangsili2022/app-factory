# 国内外平台目录

目录版本：2026-11-05。这是首批主要渠道，不是全球全部商店。所有渠道目前提供规划与材料向导，未内置经过验收的商店上传连接器。可用宿主浏览器/API、账号权限和具体项目须分别验证。

| ID | 平台及市场 | 目标系统 | 注册/发布官方入口 | 本轮核实程度与注意事项 |
|---|---|---|---|---|
| apple | App Store，中国及海外所选地区 | iOS、iPadOS、macOS | [注册](https://developer.apple.com/programs/enroll/)；[团队权限](https://developer.apple.com/help/app-store-connect/manage-your-team/overview-of-accounts-and-roles/) | 注册正文已读；个人/组织身份、会员、协议与团队角色分别检查。一个账号管理可用地区，不需要每国重新注册；中国区资格另核。 |
| google-play | Google Play，海外可用市场 | Android | [注册](https://support.google.com/googleplay/android-developer/answer/6112435)；[新个人账号测试](https://support.google.com/googleplay/android-developer/answer/14151465) | 注册正文已读；个人/组织认证不同，新个人账号生产发布前有额外测试要求，按账号当日页面核验，不保证即时上线。 |
| huawei-harmony | 华为应用市场，鸿蒙发行 | HarmonyOS | [开发发行入口](https://developer.huawei.com/consumer/cn/appgallery/devstart/) | 本轮正文超时，细则待复核；原生鸿蒙独立工具链、签名及产物，不能上传 APK 冒充鸿蒙应用。 |
| huawei-android | Huawei AppGallery，Android及海外市场 | Android | [官方入口](https://developer.huawei.com/consumer/en/appgallery/) | 入口收录，目标国家、设备、账号和当前格式支持待核；不能与鸿蒙线路混用。 |
| xiaomi | 小米应用商店，中国 | Android | [开放平台](https://dev.mi.com/)；[备案说明](https://dev.mi.com/distribute/doc/details?pId=1739) | 页面依赖 JavaScript，详细要求待控制台复核；备案、主体及类目材料逐项检查。 |
| oppo | OPPO 软件商店，中国 | Android | [开放平台](https://open.oppomobile.com/)；[发布说明](https://open.oppomobile.com/new/developmentDoc/info?id=10035) | 页面依赖 JavaScript；账号资质、包格式与审核细则待控制台复核。 |
| vivo-cn | vivo 应用商店，中国 | Android | [国内开放平台](https://dev.vivo.com.cn/) | 入口可访问但正文不可读；详细注册及提交要求待复核。 |
| honor | 荣耀应用市场，中国及可选地区 | Android | [创建应用](https://developer.honor.com/cn/doc/guides/100882)；[发布 APK](https://developer.honor.com/cn/doc/guides/100884) | 官方检索摘要确认实名账号、应用创建和发布地区配置；执行前复核完整页面。 |
| tencent | 腾讯应用宝，中国 | Android | [开放平台](https://open.tencent.com/)；[应用管理](https://app.open.qq.com/) | 官方主页确认应用宝入口；账号类型、资质及类目细则待登录后核验，不把广告开户当作应用上架。 |
| samsung | Samsung Galaxy Store，可选国际市场 | Android | [准备与注册](https://developer.samsung.com/galaxy-store/prepare.html)；[API范围](https://developer.samsung.com/galaxy-store/galaxy-store-developer-api/get-started-with-the-gsd-api.html) | 官方指南入口已读；核 Seller Portal 与商业卖家资格。API不等于能自动首次创建应用，逐操作核权限。 |
| vivo-global | vivo 海外应用分发 | Android | [海外开发者平台](https://developer.vivo.com/home?lang=zh_cn) | 官方摘要确认海外入口与 APKS 指南；与国内平台分开核验账号和覆盖市场。 |

## 选择规则

- 先问目标用户所在国家/地区和设备，再选渠道；账号注册地、商店覆盖地区、用户所在地是不同概念。
- iOS 原生应用不能直接投 Android 商店；跨平台源码仍需分别构建、签名、测试。AAB、APK、APKS、鸿蒙发行包和 Apple 构建不可相互改后缀替代。
- Apple 国内外按地区建立发行子行；Android 各商店分别管理签名、SDK、支付与服务依赖，不能默认同一包全渠道通用。
- 费用、测试人数/天数、API级别、截图尺寸、资质及审核周期不设永久常量。行动前打开官方最新文档并在项目记录来源和日期；无法读取就列待核，不编数值。
- Windows、Web/PWA、小程序、独立网站和其他商店属于扩展路线，按用户需要单独研究；不把官网部署视为应用商店上架。Amazon等渠道须核当前设备范围，不能套用旧的通用Android分发清单。
