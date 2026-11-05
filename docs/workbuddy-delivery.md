# WorkBuddy 专家候选交付

## 当前交付：0.2.2

2026-11-05：APP全球发行专家0.2.2已安装WorkBuddy，源码[4f89ac9](https://github.com/liangsili2022/app-factory/commit/4f89ac904b4c0d10d2eebc0f953ef829cecc0bca)已推送至week1-onboarding。以下旧版本状态为历史记录。

- 候选：dist/app-factory-expert-0.2.2.zip；SHA-256：01fd041a6681c06731c57343681993c872e9879f9bc911eb21c89cfb71bf2ac2。
- 安装：官方validate/register通过；稳定ID不变；25文件哈希一致，客户端v0.2.2。
- 验收：21包内检查、11核心测试、全新自然需求首次交付17项独立检查通过。
- 真实对话RELEASE.md SHA-256：d55c76c45fa1cbfd979d8523c0059e0fab8e981040a20396ed08728ae6e324c0。
- 0.2.1规划越界失败样本保留；0.2.2固化范围限制和首次自检，旧安装有本机备份。
- BUILD-MANIFEST的upstream_commit为打包时核心来源a801cce；集成文件随后提交4f89ac9。收尾不重打候选包。
- 验收限本地软件交付及发行准备；未注册、付款、签名构建手机APP、上传、提审或上架。动态平台要求执行前复核。

详细证据：本机Documents/Codex/2026-11-05/app-factory-workbuddy/acceptance/global-release-v022/ACCEPTANCE.md；最终收尾在该任务目录CLOSEOUT-0.2.2.md。私有Wiki接续记录见[PR #213](https://github.com/liangsili2022/wiki/pull/213)。

## 历史：0.1.0配置与打包

2026-11-05，Codex；版本 0.1.0。

用户确认：单专家内置执行 Skill；本轮范围为配置和打包。
配置：integrations/workbuddy/app-factory-expert。
构建：python3 scripts/package_workbuddy.py。
验证：python3 scripts/smoke_workbuddy.py（12 项通过）；python3 -m unittest discover -s tests -v（原核心 11 项通过）。
产物：dist/app-factory-expert-0.1.0.zip，另附 .sha256 及 workbuddy-validation.json。

包含双语市场配置、单专家提示词、执行 Skill、512×512 PNG 头像、交付记录模板、MIT 核心及许可证、逐文件 SHA-256 清单。
ZIP 解压后从含空格的独立项目目录完成四阶段检查，构建 Python zipapp 并在项目外启动得到预期输出；测试失败、构建失败、产物缺失、越界产物、缺少显式构建参数均返回非零。临时验证目录已清理。

未验证：WorkBuddy 客户端实际导入和对话、云端宿主工具链、iOS 签名/安装、付费市场发布；未创建或发布线上专家。
CLI 结构检查、有限密钥扫描和产物存在检查不证明完整质量，专家须另核需求内容、差异审查、产物新鲜度与实际运行。
作者邮箱为公开 GitHub noreply 标识，不作为服务联系邮箱。公开售卖前需完善商业资料。

原项目运行核心未修改；新增 WorkBuddy 适配目录与构建/验证脚本。本地源码尚未提交或推送。

## 真实客户端验收接续

2026-11-05：专家已导入并完成离线练琴CLI真实交付；首轮发现坏记录覆盖，回到同一专家会话修复。修复后18项目测试和Codex独立183检查通过，产物源码一致；完整证据位于Documents/Codex/2026-11-05/app-factory-workbuddy/acceptance/STATUS.md。专家回复停滞后由Codex补齐交付记录。仅本机CLI验收，未上架/收费/验证云端及iOS。

## 0.2.0 全球发行扩展（2026-11-05）

用户最终名称：APP全球发行专家。稳定插件/Agent/Skill ID不变。新增11条发行路线目录、注册向导、多平台发布流程、发行记录模板和仅生成本地计划的plan_release.py。各平台正文可读性与待核项逐条标记，不宣称所有政策已经完整核验。未接入自动上传，不进行真实账号注册、付款、提审或公开发布。

0.2.0验收：隔离解压17项检查、原核心11测试通过。WorkBuddy原专家已更新，界面显示新名称；安装目录24文件SHA-256与清单全部一致。新发行真实对话未提交：桌面接口noWindowsAvailable，重新连接和Raise后点击/粘贴仍无变化。不得将此轮写为真实发行对话通过。未进行商店上传/提审/发布。

## 无账号真实对话验收恢复
2026-11-05：同一0.2.0专家真实对话生成RELEASE.md，首轮发现7项细节问题，经原专家修订后独立14内容检查+5工具测试通过。四渠道/地区未注册/未构建/待准备；鸿蒙扩展、本人注册和材料清单齐备，首版保留。证据：Documents/Codex/2026-11-05/app-factory-workbuddy/acceptance/global-release-demo/ACCEPTANCE.md。未执行商店注册/付款/上传/提审/发布；反馈尚未固化新版专家包。

## 0.2.1 固化首次生成（2026-11-05）

已将真实验收反馈固化：模板内置17条分阶段清单；生成器独立APP/专家版本、逐平台国家、注册状态与账号功能条件、扩展路线；新增首次交付自检。CLI仍拒绝未知平台、不匹配系统、错误地区绑定和覆盖文件。候选dist/app-factory-expert-0.2.1.zip，21包内检查+11核心测试通过。使用WorkBuddy内置expert-manager validate/register更新同一专家，保留0.2.0备份，安装25文件哈希全部一致，界面v0.2.1。新对话首次清单验收进行中，不能提前宣称通过。

0.2.1首次对话额外发现：纯规划探测本机签名证书并推断项目账号，不能据此验收通过。已升级0.2.2固化规划/构建检查范围，21包检查通过，官方validate/register成功，25文件哈希一致，UI显示v0.2.2。新会话同自然需求复验中，保留0.2.1失败记录。

最终0.2.2首次对话通过：新会话仅自然需求，无缺陷提示、无人工反馈修订；专家自行补齐项目资料并完成正向/负向验证。独立17项内容检查通过，最终RELEASE.md SHA与客户端已完成回复一致。证据acceptance/global-release-v022/ACCEPTANCE.md；候选SHA 01fd041a6681c06731c57343681993c872e9879f9bc911eb21c89cfb71bf2ac2。此为单场景首次交付证据，不保证未来任何项目零错误；实际政策/商店发布仍待独立核验。
