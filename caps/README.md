# 能力图集 · 341 位

**341 位能力 / 30 个域** · 需授权 79 · 多操作 171 · 需入参 29 · 触达外部 5

每位能力一份独立规格文件，可单独引用、单独查询、单独校验。全部文件由 `tools/build_atlas.py` 从 `src/gbt_caps/data/registry.json` 生成。

| 域 | 能力位 | 需授权 | 多操作 | 入口 |
|---|---|---|---|---|
| `creation` | 54 | 22 | 43 | [进入](./creation/README.md) |
| `system` | 51 | 5 | 29 | [进入](./system/README.md) |
| `llm` | 41 | 8 | 20 | [进入](./llm/README.md) |
| `security` | 29 | 9 | 9 | [进入](./security/README.md) |
| `mind` | 19 | 1 | 11 | [进入](./mind/README.md) |
| `pipeline` | 18 | 0 | 1 | [进入](./pipeline/README.md) |
| `tentacle` | 18 | 5 | 9 | [进入](./tentacle/README.md) |
| `recon` | 17 | 6 | 10 | [进入](./recon/README.md) |
| `video` | 14 | 9 | 6 | [进入](./video/README.md) |
| `data` | 12 | 3 | 7 | [进入](./data/README.md) |
| `engine` | 10 | 1 | 2 | [进入](./engine/README.md) |
| `tools` | 9 | 2 | 7 | [进入](./tools/README.md) |
| `integration` | 7 | 4 | 2 | [进入](./integration/README.md) |
| `devour` | 5 | 0 | 1 | [进入](./devour/README.md) |
| `vision` | 5 | 1 | 4 | [进入](./vision/README.md) |
| `finance` | 4 | 0 | 0 | [进入](./finance/README.md) |
| `longrun` | 4 | 0 | 0 | [进入](./longrun/README.md) |
| `voice` | 4 | 0 | 2 | [进入](./voice/README.md) |
| `automation` | 2 | 1 | 2 | [进入](./automation/README.md) |
| `brain` | 2 | 0 | 0 | [进入](./brain/README.md) |
| `collab` | 2 | 1 | 2 | [进入](./collab/README.md) |
| `desktop` | 2 | 1 | 1 | [进入](./desktop/README.md) |
| `device` | 2 | 0 | 0 | [进入](./device/README.md) |
| `infra` | 2 | 0 | 1 | [进入](./infra/README.md) |
| `project` | 2 | 0 | 1 | [进入](./project/README.md) |
| `social` | 2 | 0 | 1 | [进入](./social/README.md) |
| `comms` | 1 | 0 | 0 | [进入](./comms/README.md) |
| `framework` | 1 | 0 | 0 | [进入](./framework/README.md) |
| `image_video` | 1 | 0 | 0 | [进入](./image_video/README.md) |
| `life` | 1 | 0 | 0 | [进入](./life/README.md) |

## 怎么用

```bash
gbt-caps list                      # 341 位一览
gbt-caps domain vision             # 某个域的全部能力位
gbt-caps show vision_loop          # 单份规格
gbt-caps search 授权               # 全文检索
gbt-caps check                     # 契约自检
```

Python：

```python
from gbt_caps import all_caps, lookup, by_domain, search

len(all_caps())            # 341
lookup("vision_loop").safe  # True
by_domain("engine")        # 该域的全部规格
search("DAG")              # 命中的能力位
```

完整清单：[`INDEX.md`](./INDEX.md)
