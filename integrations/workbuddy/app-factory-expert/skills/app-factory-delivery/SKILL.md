---
name: app-factory-delivery
display_name: APP开发与全球发行
display_name_en: Software Development and Delivery
description: Build or improve software projects and deliver source, meaningful tests, explicit builds, and verified artifacts. Use for development, fixes, packaging, store selection, registration guidance, and multi-platform releases.
description_zh: 从需求到代码、测试和构建交付，记录实际执行证据及环境限制。
description_en: Deliver software through requirements, code, tests, explicit builds, and execution evidence.
version: 0.2.3
author: Huppy AI & Liang Sili
---

# 软件研发与交付

## 开始
确认用户的项目目录，先读项目规则和现有文件。检查当前宿主能力及目标所需工具；只检查与本项目相关的工具，不要求安装所有 AI CLI。没有 Shell 或 Python 时继续完成可做的代码/文档，明确执行与打包未验证。

本技能随包带有 App Factory MIT 核心，不需要 pip 安装或联网下载。以本 SKILL.md 所在目录解析 scripts/run_factory.py 的绝对路径，不依赖开发者本机目录。Python 3.9+ 可执行：

```sh
python3 "<skill-dir>/scripts/run_factory.py" init "<project-dir>"
python3 "<skill-dir>/scripts/run_factory.py" gate 1 --path "<project-dir>"
python3 "<skill-dir>/scripts/run_factory.py" gate 2 --path "<project-dir>" --test-cmd "python3 -m unittest discover -s tests"
python3 "<skill-dir>/scripts/run_factory.py" gate 3 --path "<project-dir>"
python3 "<skill-dir>/scripts/run_factory.py" gate 4 --path "<project-dir>" --build-cmd "python3 build.py" --artifact "dist/app.pyz"
```

上面测试与构建命令仅为 Python 项目示例；先检查项目脚本再执行，不将示例直接套用到其他技术栈。参数命令由原核心按空格切分，不支持 shell 运算符或含空格的内层参数；复杂命令写入项目内经过检查的脚本再调用，不拼接不可信输入。外层项目路径可含空格。

## 四阶段
1. 需求：补全 docs/PRD.md 的 Target User、Core Value、Out of Scope、Acceptance Criteria，标题后可写中文；docs/TASKS.md 使用勾选任务。CLI 仅检查结构，人工审查内容与可验收性，不把模板存在当作需求完成。
2. 实现：对行为变更使用有意义的失败/成功测试；低风险纯配置可做结构与运行校验。保留执行命令、退出码和摘要，不能用没有用例的成功命令替代测试。Gate 2 只验证命令退出码，不证明 TDD 历史或覆盖率。
3. 审查：读实际 diff，检查核心流程、错误处理及适用的安全风险，写 docs/REVIEW.md，明确范围、发现和未覆盖项。Gate 3 是有限规则扫描及部分 REVIEW 标记检查，不是全面安全审计；输出前脱敏，不复制密钥原值。
4. 构建：显式指定真实构建命令和预期产物。xcodebuild -showsdks、flutter analyze、cargo check、compileall 或 npm --if-present 均不能证明产物已生成。在构建前处理旧产物或记录其哈希/时间，确认这次产物来源；对产物做启动/安装/内容检查。iOS 真机签名、商店提交等按环境与授权分开验证。没有工具链时标为未验证，不伪造通过。

包装入口要求 Gate 4/check 有 --build-cmd 和 --artifact，并检查产物存在；文件存在仍不等于可运行。不要直接调用内置核心绕过这一检查。status 是历史记录，不能作为源码已变化后的最新证据。失败后重新执行有关检查。

## 交付
读取 [交付记录模板](references/delivery-template.md) 写 docs/DELIVERY.md。至少给出启动方法、测试/构建命令与退出码、产物路径和校验值、审查范围、剩余限制。新建项目先完成一个可演示核心流程再扩展。界面实际验证普通/大/小窗口布局。未获发布授权时止于本地候选，不将候选写成已上线。

## 全球发行入口
发行任务按需读取：
- [平台目录](references/platform-catalog.md)：国内外渠道、系统差异、官方入口与核实边界。
- [注册向导](references/registration-guide.md)：主体、本人操作、团队授权与缺项。
- [多平台流程](references/multi-platform-release.md)：材料、提审、回执、状态与维护。
- [发行记录模板](references/release-template.md)：据实写入 docs/RELEASE.md；已有文件先读取保留。

只写本地新文件的计划生成器（Python 3.9+，不联网、不上传）：
```sh
python3 "<skill-dir>/scripts/plan_release.py" --list
python3 "<skill-dir>/scripts/plan_release.py" --platform apple --platform google-play --system ios --system android --output "<project-dir>/docs/RELEASE.md"
```
系统参数表示计划提供的目标构建，不证明已有对应产物。工具拒绝系统不匹配、未知平台和覆盖文件。初始状态为待准备；不会检查真实账号或改变商店状态。生成后补充国家、主体、版本、证据和缺项。没有上传连接器时标为人工控制台操作待执行，不声称已接通。


### 首次生成必须完成的核对
完整发行准备请求先读 release-template.md、registration-guide.md 和 multi-platform-release.md；生成器已包含阶段清单与条件分支，不另起简化空模板。项目版本未知写待定，不能从专家包版本推断。根据用户事实填写账号状态、地区和账号功能，未知不猜。

多地区/无账号示例（按用户实际目标改，不机械套用）：
```sh
python3 "<skill-dir>/scripts/plan_release.py" --platform apple --platform google-play --platform xiaomi --system ios --system android --market apple=CN --market apple=US --market google-play=US --market xiaomi=CN --extension huawei-harmony --account-state unregistered --account-creation unknown --output "<project-dir>/docs/RELEASE.md"
```
`--market`逐平台声明目标国家，不证明可发行；未提供地区保持待定。`--extension`只列扩展，不替代兼容检查；系统不匹配不能放进`--platform`。`--account-creation no/yes/unknown`来自实际APP功能；默认unknown，离线不等于无账号。`--app-version`只用工程/用户已明确版本，默认待定。

生成后补齐用户给出的APP、主体、语言等信息，按项目调整每项适用性与责任人，保留证据和下一步。阅读 [首次交付自检](references/release-self-check.md) 并逐条完成；仅把本轮真实执行写成已验证。不要等用户指出错误才补清单。已有文件应保留副本/历史后定向修改，生成器拒绝覆盖不等于授权删除重建。


### 规划与构建检查分开
仅请求发行规划/注册清单时，读取本项目输入、内置发行资料并运行本地计划生成器即可；不主动运行doctor、扫描本机工具链、钥匙串、签名证书、账号登录态或其他项目。已有项目源码只有与清单有关且获授权时才读。用户明确没有账号就按用户声明记录，未知政策保留待核；不能用共享机器上曾安装的证书推翻项目身份信息。证书存在、工具已安装都不证明该项目主体拥有有效会员或发布权限。
实际进入构建、签名或账号操作阶段，再按目标与已有授权检查必要环境和当前账号状态；仅保存必要的脱敏结果，证书身份不进入可分享的规划材料。
