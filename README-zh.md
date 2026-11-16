# Biology Research Superpowers — Codex 本地插件

这是一个**可直接安装**的生物学研究插件，基于 leiverkus/research-superpowers 的研究生命周期、证据审计和 SOFT-GATE 思路而重新设计。

## 快速安装

1. 解压整个 ZIP 到固定目录。
2. 在终端注册目录（请替换成解压后的绝对路径）：

```bash
codex plugin marketplace add /absolute/path/biology-research-superpowers-marketplace
```

3. 启动 Codex，输入 `/plugins`，在 `biology-research-local` 来源下安装 `biology-research-superpowers`。**注册 marketplace 不等于安装插件。**
4. 打开一个研究项目并使用自然语言调用，例如：`使用 Biology Research Superpowers 审阅我蛋白家族演化模拟器的科学合同、功效、独立 Oracle 与联合事件验证`。

## 生物学功能

- 18 个原研究生命周期阶段（规划、检索、获取、证据摄取、分析、论文、同行评审、研究归档等），全部重写为生物学流程。
- 11 个新增专用 Skill（序列管理、比较基因组、系统发育、蛋白家族演化、模拟器、组学、结构功能、功能实验、HPC 可复现性、图表审计、数据提交）。
- 8 个可选 Codex Agent TOML，**不会自动注册**，可执行 `python3 scripts/install_agents.py --scope user --dry-run` 预览，再运行安装。
- 科学审计脚本：原始输入 hash、研究主张及数据来源、引用 Wiki、知识图谱、漂移检查、门槛跳过理由。
- 初始项目模板：`python3 scripts/scaffold_project.py --name my-project --destination ~/Research --study-type mixed --discipline Microbiology --taxon Geodermatophilaceae`。

## 保留原作者完整代码（可选）

如果希望**同时保留上游全部 18 个原 Skill 原文及模板、脚本**，可在联网 Mac 上，在本 ZIP 解压根目录运行：

```bash
bash prepare_full_upstream.sh
```

此命令会调用随包携带的前一轮上游转换器，克隆并检验固定的 v0.47.0 源码，然后在同级目录生成 `biology-with-full-upstream/`。

原作者流程原样存放为参考资料，**生物学专用 SKILL.md 仍是实际执行指令**，以免把考古/神学的方法学假设直接套用到生物学。若上游更新了版本或目录清单，转换器会拒绝自动覆盖并要求人工检查。

## 使用边界与验证

不捆绑需授权的科学数据库 MCP，不主动执行下载或 HPC 任务，不会声称自动完成湿实验。此压缩包通过本地结构和工具测试，但尚未在你的 Codex 版本中执行完整工作流。详见 `TEST_REPORT.md`。

**项目来源与版权：** 思路来自 Patrick Leiverkus，原仓库 https://github.com/leiverkus/research-superpowers，MIT；本包是独立生物学改写，并非原作者官方插件。