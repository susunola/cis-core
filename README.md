# cis-core · 家族共享层

**cis-core** 是 `cis-*` 合规工具家族的共享基础层(shared foundation)。家族三件套:

| 工具 | 中文名 | 定位 | 仓库 |
|---|---|---|---|
| **cis-image** | 金汤·筑城 (Forge) | 镜像源头 · CIS 加固黄金镜像构建 | [github.com/susunola/cis-image](https://github.com/susunola/cis-image) |
| **cis-host** | 金汤·守城 (Keep) | 主机运行时 · CIS 扫描/加固/漂移监控 | [github.com/susunola/cis-host](https://github.com/susunola/cis-host) |
| **cis-cloud** | 金汤·巡城 (Watch) | 云上配置 · 多云 CIS 合规 | [github.com/susunola/cis-cloud](https://github.com/susunola/cis-cloud) |

口号:**固若金汤 · CIS compliance, automated**。

## 这个包现在是什么

当前是**最小占位包**(v0.1.0):提前注册 PyPI 名字 `cis-core`,作为家族共享层的地基。三个工具当前各自独立(技术栈不同:Python/Packer、Python/Ansible、Ruby/Terraform),暂不依赖本包。

## 规划中的共享内容

当家族统一规则目录和报告格式时,以下内容将移入本包:

- **统一规则目录格式**:合并 cis-cloud 的 `catalog.json` 与 cis-image 的 `rules.json` 为单一 schema,三工具共用一份数据;
- **统一报告/导出规范**:HTML / JSON / SARIF / XCCDF 的公共约定;
- **家族品牌资产**:logo、命名规范、CI 模板。

## 独立声明

**Independent project** — cis-core is not affiliated with, sponsored by, or endorsed by the Center for Internet Security (CIS). CIS Benchmark content is copyright © Center for Internet Security, Inc. and used under their terms of use.

## License

MIT — see [LICENSE](LICENSE).
