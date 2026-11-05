"""Create a local release plan without network access or overwriting files."""
import argparse
import json
from pathlib import Path


def safe_text(value):
    if any(c in value for c in '\n\r|'):
        raise argparse.ArgumentTypeError('Use a single line without table separators')
    return value


def catalog():
    source = Path(__file__).resolve().parents[1] / 'references/platform-catalog.md'
    rows = {}
    for line in source.read_text(encoding='utf-8').splitlines():
        if not line.startswith('| '):
            continue
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if cells[0] == 'ID':
            continue
        rows[cells[0]] = cells
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--platform', action='append', default=[])
    parser.add_argument('--system', action='append', default=[],
                        choices=['ios', 'ipados', 'macos', 'android', 'harmonyos'])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--market', action='append', default=[],
                        help='Repeat PLATFORM=COUNTRY, e.g. apple=CN and apple=US')
    parser.add_argument('--extension', action='append', default=[],
                        help='Catalog route to discuss separately, not a compatible build')
    parser.add_argument('--app-version', type=safe_text, default='待定')
    parser.add_argument('--account-state', choices=['unknown', 'unregistered'], default='unknown')
    parser.add_argument('--account-creation', choices=['unknown', 'yes', 'no'], default='unknown')
    args = parser.parse_args()
    rows = catalog()
    if args.list:
        for key, row in rows.items():
            print(f'{key}: {row[1]} ({row[2]})')
        return
    if not args.platform or not args.system or args.output is None:
        parser.error('--platform, --system and --output are required')
    selected = list(dict.fromkeys(args.platform))
    extensions = list(dict.fromkeys(args.extension))
    for key in extensions:
        if key not in rows or key in selected:
            parser.error('Extensions must be known routes outside the selected release platforms')
    markets = {key: [] for key in selected}
    for entry in args.market:
        key, sep, region = entry.partition('=')
        if not sep or key not in markets or len(region) != 2 or not region.isascii() or not region.isalpha():
            parser.error('--market requires selected-platform=two-letter-country')
        if region.upper() not in markets[key]:
            markets[key].append(region.upper())
    for key in selected:
        if key not in rows:
            parser.error(f'Unknown platform: {key}')
        supported = {s.strip().lower() for s in rows[key][2].split('、')}
        if not supported.intersection(args.system):
            parser.error(f'System mismatch for {key}: requires {rows[key][2]}')
    template = Path(__file__).resolve().parents[1] / 'references/release-template.md'
    body = template.read_text(encoding='utf-8')
    plugin = Path(__file__).resolve().parents[3]
    version = json.loads((plugin / '.codebuddy-plugin/plugin.json').read_text())['version']
    body = body.replace('{{APP_VERSION}}', args.app_version).replace('{{EXPERT_VERSION}}', version)
    account = '未注册（用户提供，尚未验证）' if args.account_state == 'unregistered' else '待核（未获账号证据）'
    deletion = {
        'unknown': '待核：当前未明确是否提供账号创建；离线不等于无账号。确认产品功能后判断，不为满足检查而新增账号系统。',
        'yes': '用户说明提供账号创建：核对应用内账号删除、关联数据及适用平台要求；尚未实现/验证。',
        'no': '用户说明无账号创建：账号删除功能不适用；仍核实SDK与数据收集、本地数据清理，不新增账号系统。',
    }[args.account_creation]
    body = body.replace('{{ACCOUNT_DELETION}}', deletion)
    lines = []
    for key in selected:
        row = rows[key]
        for region in markets[key] or ['待定地区']:
            gaps = '账号资格、签名构建、隐私网页、素材、评级及数据声明待准备/复核'
            if region == 'CN':
                gaps += '；中国大陆APP备案/类目资质适用性待官方核验（含离线和个人主体）'
            if key == 'google-play':
                gaps += '；新个人账号生产权限、测试及设备验证待核'
            lines.append(f'| {row[1]}（{key}） / {region} | {account} | 未构建 | {gaps} | 待准备 | 无 | 本人核注册资格；专家准备材料 |')
    body = body.replace('{{RELEASE_ROWS}}', '\n'.join(lines))
    extension_text = []
    for key in extensions:
        row = rows[key]
        supported = {s.strip().lower() for s in row[2].split('、')}
        reason = '系统不匹配' if not supported.intersection(args.system) else '尚未纳入本轮发行'
        extension_text.append(f'- {row[1]}（{key}）：{reason}，仅扩展适配待办；目标{row[2]}，无兼容成功/构建/发布证据。官方入口：{row[3]}。')
        if key == 'huawei-harmony':
            extension_text.append('- 原生鸿蒙需单独适配、签名和发行产物；APK不能冒充鸿蒙包。工具为 [DevEco Studio](https://developer.huawei.com/consumer/en/deveco-studio)。')
    body = body.replace('{{EXTENSIONS}}', '\n'.join(extension_text) or '未指定扩展路线；不得据此推断其他系统兼容。')
    registrations = []
    for key in selected:
        steps = {
            'apple': '本人Apple账号/双重认证 → 按真实个人或组织身份注册 → 核年费、验证和协议 → 本人完成必要步骤 → 回读会员状态；同一账号管理可用地区，不逐国重复注册。',
            'google-play': '本人Google账号 → 选择真实个人/组织类型 → 按控制台完成协议、注册费、身份及适用设备验证 → 核新个人账号测试和生产权限；费用、人数/天数不写死。',
        }.get(key, '本人进入官方开放平台 → 核主体/国家/类目资格 → 注册和实名 → 按实际要求核费用与协议 → 回读认证状态，缺项继续准备材料。')
        registrations.append(f'- **{rows[key][1]}**：{steps} 官方入口：{rows[key][3]}')
    body = body.replace('{{REGISTRATION_STEPS}}', '\n'.join(registrations))
    body += '\n## 所选渠道官方入口与核实边界\n\n'
    for key in selected:
        row = rows[key]
        body += f'- {row[1]}：{row[3]}。目录编制历史（不是本次实时核验）：{row[4]}\n'
    body += '\n本文件只证明计划已生成；账号、构建、上传、审核、上线均未由此工具验证。\n'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with args.output.open('x', encoding='utf-8') as output:
            output.write(body)
    except FileExistsError:
        parser.error(f'Refusing to overwrite existing file: {args.output}')
    print(args.output)


if __name__ == '__main__':
    main()
