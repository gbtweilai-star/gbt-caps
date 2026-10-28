# `comfy_native`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`store` / `comfy_native` / `runs`） |
| 处理器 | `comfy_native` |

## 用途

**GBT天真** —— 触手自己的 ComfyUI 能力（主人命名 2026-10-11「触手的 ComfyUI 我们取名叫 GBT天真」）。常用说法（人这么问就命得中）：**放大 / 锐化 / 高清 / 4K / 图片放大 / 传统放大 / 洗图 / 出图放大**。（触发词前置是好习惯；但**截断已不再影响路由** —— 2026-10-13 根修：图鉴把被切掉的尾巴另存 `desc_tail` 并接回打分语料，本位原来「放大」写在 300 字外命不中的那个坑已从根上堵掉。）ComfyUI 能力的**原生版**（主人令 2026-10-11「按照 ComfyUI 的节点连接个契约，同样拥有契约和触手连接，他行我们也行」）：不装重壳、不依赖 8188 外挂，把 ComfyUI 的**架构**长成自己的触手小算子 —— ① workflow.json 当契约（图就是活合同，可复跑可留证）② 节点=能力位白名单（每节点一根触手）③ 执行=拓扑序跑一遍。节点：upscale_4k（Pillow LANCZOS + USM 传统放大 · 显存 0 · 内存<300MB，8G 机样张）／copy／sha／info；图契约 {"nodes":[{"id","node","inputs"}],"edges":[{"from","to","field":"out->image"}]}。铁律：**闸是唯一真源**（产物不过闸 ⇒ 不许落盘）· **不编**（缺依赖回 needs_dependency）· 证据只追加（store/comfy_native/runs.jsonl）· **白名单 fail-closed**（与 ComfyUI 的"任意 node"相反，这是故意的）。边界如实：重生成模型（文生图／神经超分）本机 AMD 无 CUDA + 7.39G 内存 ⇒ 跑不动，**未接**。【R-H996 · 2026-10-15 主人令「就是要 ComfyUI 节点和契约做我们自己的原生能力，不要 ComfyUI 的厚重外壳」的落地】：把秋叶版已抓下的 **962 把节点 schema** 归一化成我们自己的契约，并把**传统算法面**用纯 CPU 小算子长出来 —— 现 **18 个原生算子**，其中 **13 个与 ComfyUI 同名同契约**（ImageScale/ImageCrop/ImageInvert/ImageBlur/ImageCompositeMasked/MaskToImage/ImageToMask/ImageBatch/EmptyImage/LoadImage/SaveImage/AddTextPrefix/AddTextSuffix）=> 她的 workflow.json 可以直接用 **ComfyUI 的节点名**，而**不需要** ComfyUI 在位。新增只读 op：**contract**（契约面 + 原生覆盖率 + 未接原因分类）·**validate**（用我们自己的契约离线校验任意图：未知节点/缺必填/成环）。未接如实分类：重生成与模型面 332 · 控图检测面 290 · 传统算法面 201（可原生，按需再长）· 云端 API 126。op=status/nodes/graph/gate/contract/validate（读面免门）/ run（写面过 filesystem_write）/ 单节点名直跑

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("comfy_native")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show comfy_native          # 本页内容的终端版
gbt-caps show comfy_native --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("comfy_native", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `store`、`comfy_native`、`runs`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `comfy_native`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
