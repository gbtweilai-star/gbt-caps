# gbt-caps · 341 位能力的图集

**一个 AI 智能体框架的 341 位能力规格 —— 每位一份独立文件，可机器校验，零依赖。**

```bash
pip install gbt-caps
gbt-caps stats
```

```
caps     341
domains  30
gated    79  （safe: false —— 需要人签字）
multi-op 171  （描述里枚举了多个操作）
params   29
external 5
source   caps_registry.py  sha256 1c85007b73b9
```

---

## 这是什么

一个智能体框架长出了 **341 位能力**——`vision_loop`、`wf_define`、`osint_scan`、
`deploy_publish`、`room_space`、`tentacle`，还有 335 个——分布在 **30 个域**里。
它们原先声明在一个 235 KB 的 Python dict 里。那是**存**能力的好地方，是**讲**能力的烂地方。

这个仓库就是那个 dict 摊开后的样子：

- **341 份规格页**，在 `caps/<域>/<能力名>.md`
- **30 份域索引**，加一份全量 `INDEX.md`
- **一份快照**（`src/gbt_caps/data/registry.json`），任何工具都能读
- **查询用的 CLI 与 API**：`lookup`、`by_domain`、`search`、`stats`
- **一个契约校验器**，专门找注册表自相矛盾的地方

每份页面都写清：这一位干什么、怎么调、要什么入参、**不会做什么**、以及这个结论出自哪里。
页面上没有编造的内容——描述逐字引用，标记是注册表自己的，凡是推断出来的都标明是推断。

## 这不是什么

- **不是实现。** 能力由上游框架实现。本仓是**契约层**：能读、能 diff、能校验、能发布的那一层，
  不必把别人 600 个文件的应用一起搬过来。
- **不是 341 个可 import 的函数。** 没有 `import gbt_caps; vision_loop()`。
  原因见[「为什么不一个能力一个仓库」](#为什么不一个能力一个仓库)。
- **不是自动生成的垃圾。** 生成器 300 行，你能读完；页面与数据不一致测试就红；
  `--check` 证明整棵树可逐字节复现。

---

## 30 秒

```bash
$ gbt-caps show vision_loop
vision_loop
  domain     vision
  handler    vision_loop
  safe       false   ← needs a human
  external   false
  params     —
  shape      multi-op
  ops        look / hear / speak / think / act / verify / loop / status
```

```bash
$ gbt-caps list --gated
actioncam                    video           [gated; multi-op]
anatomy_figures              creation        [gated; multi-op]
anim_fix                     creation        [gated; multi-op]
...
79 capability bit(s)

$ gbt-caps domain engine      # # engine · 10 bits
$ gbt-caps search 授权 --limit 5
$ gbt-caps check
```

```python
from gbt_caps import lookup, by_domain, search, gated_caps, stats

lookup("vision_loop").gated            # True —— 注册表没把它标成 safe
lookup("vision_lop")                   # UnknownCap: did you mean vision_loop?
[c.name for c in by_domain("engine")]  # 10 位
len(gated_caps())                      # 79
stats()["per_domain"]["creation"]      # {'caps': 54, 'gated': 22, 'multi_op': 43}
```

---

## 目录结构

```
caps/
  README.md                 # 30 个域、计数、入口
  INDEX.md                  # 341 位全量，按域分组
  vision/
    README.md               # 这个域：5 位，哪些要授权
    vision_loop.md          # 一位能力，六个小节
src/gbt_caps/
  spec.py                   # 加载、查询、检索、校验
  cli.py                    # gbt-caps
  data/registry.json        # 一切由它生成
tools/
  export_registry.py        # caps_registry.py → registry.json（走 AST，绝不 import）
  build_atlas.py            # registry.json → caps/**（确定性生成）
```

每份规格页都是同样六个小节，所以你可以逐位对比，也可以一次 grep 全 341 份：

| 小节 | 回答什么 |
|---|---|
| **用途** | 这一位干什么 —— 注册表原话，逐字引用 |
| **使用方式** | 怎么查规格，怎么真正调用 |
| **参数** | 必填入参，或明确说明不需要入参 |
| **返回** | 契约：`ok` + `gbt_stamp`；其余字段由实现决定 |
| **边界与注意** | `safe: false`？`external`？多操作却没 `op`？失败即拒绝的规则 |
| **出处** | 源文件、域、handler、快照 schema、源文件 sha256 |

---

## 校验器才是重点

发布 341 份页面很容易。**让它们一直是真话**才是难的。所以本仓有两条保证：

**1. 整棵树可复现。** `build_atlas.py --check` 在内存里重新生成每一页并逐字节比对。
手改过任何一页，检查就失败。

```bash
$ python tools/build_atlas.py --check
atlas up to date · 373 files
```

**2. 数据自洽。** `gbt-caps check` 对快照跑 11 项契约检查——命名是否 snake_case、
描述是否为空、域索引是否构成划分、计数是否与总数一致、`requires_params` 是否真配了 `params`。

```bash
$ gbt-caps check
warn  shared_handler            handler 'dh_rig' serves 5 names: ['anim_audit', ...]
warn  multi_op_without_selector voice_studio reads as multi-op but declares no op/action parameter
...
ok · 341 caps · 0 error(s) · 168 warning(s)
```

**那 168 条 warning 才是有意思的部分。** 它们是源注册表里「文字描述」与「入参契约」互相矛盾的地方：
描述里列了八个操作，却没登记 `op` 参数；或者一个 handler 悄悄服务了五个名字。
图集把它们找出来了，我们选择**发布出来**，而不是替上游抹平。每一条都能点开对应页面自己核。

---

## 域一览

完整表格见 [`caps/README.md`](caps/README.md) 与 [`caps/INDEX.md`](caps/INDEX.md)。

| 域 | 能力位 | 需授权 | 多操作 |
|---|---:|---:|---:|
| `creation` | 54 | 22 | 43 |
| `system` | 51 | 5 | 29 |
| `llm` | 41 | 8 | 20 |
| `security` | 29 | 9 | 9 |
| `mind` | 19 | 1 | 11 |
| `pipeline` | 18 | 0 | 1 |
| `tentacle` | 18 | 5 | 9 |
| `recon` | 17 | 6 | 10 |
| `video` | 14 | 9 | 6 |
| `data` | 12 | 3 | 7 |
| `engine` | 10 | 1 | 2 |
| `tools` | 9 | 2 | 7 |
| `integration` | 7 | 4 | 2 |
| 其余 17 个域 | 各 1–5 | — | — |

---

## 给自己的注册表也用

两个工具都是通用的——只要你的 `caps_registry.py` 是这种形状：

```python
BENIGN_CAPS = {
    "my_cap": {"domain": "mine", "desc": "它做什么", "handler": "my_cap", "safe": True},
}
PARAM_REQUIRED = {"my_cap": {"params": ["target"], "hint": "要打的目标"}}
```

```bash
python tools/export_registry.py path/to/caps_registry.py -o src/gbt_caps/data/registry.json
python tools/build_atlas.py
python tools/build_atlas.py --check
gbt-caps check
```

导出器**只解析、不导入**——导入一个框架包会触发它的模块级副作用，文档工具没有理由去执行它。
它只求值「数据表里可能出现的东西」，遇到别的就**拒绝**，而不是猜：

```python
literal("'上限 %d 轮' % 3")   # '上限 3 轮'      ← 支持 %-格式化
literal("dict(a=1)")          # LiteralError    ← 拒绝函数调用
```

---

## 为什么不一个能力一个仓库

341 个只放一个文件的仓库不是开源，是目录列表。三个具体理由：

1. **可发现性。** GitHub 索引的是**仓库和 topic**，不是仓库里的目录。341 个近乎空壳的仓
   在搜索里排不上任何词，还会触发反垃圾判定；一个仓、341 份有内容的页面，能吃到全部长尾。
2. **可审阅性。** 契约变更应该是一份人能读完的 diff。拆到 341 个仓，就变成 341 个 PR，没人会审。
3. **真实性维护。** 这里的价值是 `--check`：页面**不可能**与数据漂移。这个保证需要一棵树、一个生成器。

这个平台上真正跑出来的策展型仓库——技能库、规格仓、集成目录——都是这个形状：
**许多可单独寻址的产物，一个索引，一份契约，一次 CI。**

---

## 安装与开发

```bash
pip install gbt-caps
python -m gbt_caps stats

git clone https://github.com/gbtweilai-star/gbt-caps
cd gbt-caps && pip install -e ".[dev]"
make test      # 57 项测试，不联网
make check     # 图集可复现 + 契约干净
```

Python 3.9 – 3.13 · Linux / macOS / Windows · 运行时零依赖。

## 相关

- [`consent-gate`](https://github.com/gbtweilai-star/consent-gate) —— 管住那 79 位
  `safe: false` 的授权门：智能体只能申请，只有人能发放。
- [`GBTxiaotudouV8-Commander`](https://github.com/gbtweilai-star/GBTxiaotudouV8-Commander) ——
  这些能力所属的框架。

## 许可证

MIT。规格文本转载自上游注册表，同为 MIT。

---

**English: [README.md](README.md)**
