# APP全球发行专家 0.2.2

WorkBuddy 单专家候选，内置软件研发与交付 Skill 及 App Factory MIT Python 核心。
保留开发、测试、构建交付能力，新增11条国内外发行路线、注册向导、多平台流程及本地计划生成器。全球是服务范围，不是全商店自动上传承诺。

## 使用
在 WorkBuddy 的“我的专家”创建/导入流程中使用同版本 ZIP 或其解压目录（仓库里的配置源目录需先运行打包脚本）。此包仅完成本地格式与执行验证，客户端实际导入及对话验收须单独进行，未上架。
可对专家说：为我的APP制定国内外发行计划，列出适合的平台、注册步骤和缺失材料。
需要本机执行时，授权所需项目目录；Python 3.9+ 用于随包 CLI，目标平台仍需对应工具链。
不依赖 Hermes/Codex/Claude 的额外安装，不预设 MCP、连接器或付费服务。

包内 skills/app-factory-delivery/scripts/run_factory.py 提供 init/gate/check/status/doctor。
Gate 4/check 必须显式提供 --build-cmd 和 --artifact；产物存在仍须实际运行验证。
核心自动扫描不是完整安全审计，历史状态不是当前代码的保证，云端 Xcode/签名能力未验证。

## 作者与许可
Huppy AI & Liang Sili；MIT，见 LICENSE。作者邮箱使用公开 GitHub noreply 地址，不作为客户支持邮箱。
核心来源 https://github.com/liangsili2022/app-factory ，版本及文件校验见 BUILD-MANIFEST.json。

## 格式依据
https://open.workbuddy.cn/docs/expert
https://open.workbuddy.cn/docs/skill
核对日期：2026-11-05。正式发布前核验客户端导入、宿主执行能力与运营资料。

## 版本迁移
0.2.0沿用插件app-factory-expert、Agent software-delivery和Skill app-factory-delivery标识，更新现有专家，不新建重复专家。0.1.0已有真实WorkBuddy CLI交付验收；0.2.0新增发行流程的实际客户端验收须另记。无内置已验证商店上传连接器，注册实名及付款由账号所有者完成，实际提审发布以授权和平台回执为准。

## 0.2.1 首次清单完整性
固化真实验收反馈：独立APP/专家版本、按平台地区拆行、条件式账号删除、中国区适用性核验、DevEco Studio正确名称、17项阶段准备任务、来源时效与执行证据、自检流程。生成器新增market/extension/account-state/account-creation/app-version参数，仍只写本地新文件，不联网、不上传。新包真实客户端验收单独记录。

0.2.2进一步限定纯规划的数据范围：不扫描本机证书、钥匙串、登录态或工具链，不以共享机器证书推断项目账号资格；实际构建阶段再核必要环境。
