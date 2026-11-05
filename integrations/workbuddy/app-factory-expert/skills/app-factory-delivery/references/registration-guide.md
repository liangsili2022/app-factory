# 开发者注册向导

## 先确定身份

只收集推进需要的信息：应用类型/系统、目标国家、个人或组织主体、已有开发者账号及状态。不要索取密码、验证码、完整证件或银行卡到聊天/代码库。已存在账号优先复用，不为每个 APP 重复注册；不同商店通常需要分别入驻，同一商店的国内外入口是否互通须核实。

## 逐平台引导

1. 从平台目录进入官方注册页，确认域名和当前规则，记录查阅日期。
2. 用户选择真实主体和注册地区。按页面列出需要准备的身份、组织、联系人等材料类别；不要虚构资质，不默认个人账号能发布所有类目。
3. 由账号所有者完成登录、邮箱/手机验证、实名和有约束力的协议；需要收费时先给出页面显示的金额、币种与续费方式，由本人处理。没有账号可先完成代码、测试和上架素材。
4. 核对控制台实际审核状态；提交资料不等于认证通过。记录“未注册/认证中/可用/受限/待核”，只保存状态及脱敏证据位置。
5. 按实际需要邀请团队角色。Apple核 Account Holder 和 App Store Connect角色；Google核 Play Console用户权限；其他商店核对应团队功能。不要求共享主账号密码，有 API 也需单独核验操作范围。
6. 建立 APP 记录，核包名/Bundle ID、主体、签名归属和旧版本关联；存在应用时优先更新，不擅自重建导致升级链断裂。

## 平台差异检查

本轮读内置目录与本轮实时核官网必须分开记录。无账号也要交付三阶段准备清单（见release-template.md），含具体负责人、证据和下一步。无APP版本不可借用专家版本。账号删除看是否支持账号创建，离线不足以判断；没有账号功能时不要求增加账号系统。Apple中国大陆区单列APP备案/主体/离线适用性核验，参考[应用信息](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information/)；不将中国区要求套用其他国家。

- Apple：依照[官方注册指南](https://developer.apple.com/programs/enroll/)核个人/组织要求和会员状态；[角色说明](https://developer.apple.com/help/account/access/roles/)用于核验谁可签协议及授权。会员开通不表示 APP 已获批准。
- Google Play：依照[官方注册指南](https://support.google.com/googleplay/android-developer/answer/6112435)核账号类型、费用、身份及设备验证；[个人账号测试要求](https://support.google.com/googleplay/android-developer/answer/14151465)按实际账号核验，不能以内部测试成功替代生产权限。
- 国内 Android：依照各商店当前要求核实名、主体、APP备案及特定类目材料；不将软件著作权、APP备案、ICP许可证视为同一个文件，也不宣称所有应用一律同一套资质。无法判定的业务要求写“待官方确认”。
- Samsung：按[Seller Portal准备指南](https://developer.samsung.com/galaxy-store/prepare.html)核卖家状态；普通三星账号与具备发布资格的卖家状态分开记录。
- 华为：按目标设备区分原生鸿蒙与 Android 分发；开发者账号可用不代表两条技术路线均已适配。

输出到 RELEASE.md：平台、所选主体类型、账号状态、本人下一步、专家可继续准备的工作、官方来源/日期。证件、密钥、支付信息不进入发行包。
