# cis-core · 家族全家桶

**cis-core** 是 `cis-*` 合规工具家族的**统一安装入口(meta-package)**:一条命令装齐三件套。

```bash
pip install ohbs-core
```

安装后获得三个命令,覆盖合规全生命周期:

| 命令 | 工具 | 定位 | 仓库 |
|---|---|---|---|
| `cis-image` | **cis-image** | 镜像源头 · CIS 加固黄金镜像构建 | [github.com/susunola/cis-image](https://github.com/susunola/cis-image) |
| `cis-host` | **cis-host** | 主机运行时 · CIS 扫描/加固/漂移监控 | [github.com/susunola/cis-host](https://github.com/susunola/cis-host) |
| `cis-cloud` | **cis-cloud** | 云上配置 · 多云 CIS 合规(tencent/aws/azure/gcp/alibaba) | [github.com/susunola/cis-cloud](https://github.com/susunola/cis-cloud) |

```
镜像源头(合规左移) → 运行实例(持续治理) → 云上配置(多云合规)
```

## 这个包是什么

- **v0.2.0 起是元包(meta-package)**:`dependencies` 声明了 `ohbs-image` / `ohbs-host` / `ohbs-cloud`,pip 安装时会一并拉取三件套和它们的全部数据(Terraform stacks、Ansible roles 等),离线可用;
- 本包自身仍保留 `cis_core` 模块,作为未来**真正共享代码**的载体。

## 规划中的共享内容

当家族统一规则目录和报告格式时,以下内容将移入 `cis_core` 模块:

- **统一规则目录格式**:合并 cis-cloud 的 `catalog.json` 与 cis-image 的 `rules.json` 为单一 schema,三工具共用一份数据;
- **统一报告/导出规范**:HTML / JSON / SARIF / XCCDF 的公共约定;
- **家族品牌资产**:logo、命名规范、CI 模板。

## 独立声明

**Independent project** — cis-core is not affiliated with, sponsored by, or endorsed by the Center for Internet Security (CIS). CIS Benchmark content is copyright © Center for Internet Security, Inc. and used under their terms of use.

## License

MIT — see [LICENSE](LICENSE).
