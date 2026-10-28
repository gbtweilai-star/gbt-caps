# GBT V8 · 原生能力验收报告

生成 2026-10-28T14:45:01　解释器 Python 3.14.0　耗时 111.4s　实跑 **341** 个能力位

方法：每个能力位**独立子进程**调用 `api.run_task(name, {})`，限时 90s，进程可被杀——因为「挂住不返回」正是这份报告要抓的东西，不该被它拖住整个验收。载荷一律是空字典 `{}`：先测**不喂输入时它说什么**，这是用户第一次点下去就会遇到的路径。

## 一、总判定

| 判定 | 数量 | 含义 |
|---|---:|---|
| `pass/ok` | 256 | 空载荷即可跑通，返回非空结果 |
| `pass/guardrail` | 32 | 被三道护栏拦下：点名缺哪个作用域 + 给出发放方式 |
| `defect/import` | 31 | 注册表声称已实现，但分发目标模块在树里不存在 |
| `pass/needs-input` | 14 | 输入校验拦下并说清缺哪个字段 |
| `pass/needs-state` | 5 | 前置状态未建（工作流/运行记录/排练计划），提示先做上一步 |
| `defect/timeout` | 2 | 限时内无任何返回 |
| `defect/exception` | 1 | Python 异常穿过 error_class=user_error 直接漏给调用方 |
| **合计** | **341** | 其中 **34** 个真缺陷 |

## 二、守卫双向验收（三道护栏 · 12 个作用域）

只看「没票会被拒」是不够的——那只证明门是关的。这里对每个作用域走四步：**无票必拒 → 手写一行账本 → 必须放行 → 一次性票用掉即失效（时段票可复用并记账）**。全程使用临时账本，**不碰真实 `store/auth_grants.jsonl`**。

| 作用域 | 模式 | 无票拒 | 点名作用域 | 给出发放方式 | 有票放行 | 用后行为 | 结论 |
|---|---|:--:|:--:|:--:|:--:|---|:--:|
| `audio_output` | window | ✅ | ✅ | ✅ | ✅ | 可复用+记账 | ✅ |
| `browser_control` | window | ✅ | ✅ | ✅ | ✅ | 可复用+记账 | ✅ |
| `data_export` | one_shot | ✅ | ✅ | ✅ | ✅ | 用掉即失效 | ✅ |
| `deploy_force` | one_shot | ✅ | ✅ | ✅ | ✅ | 用掉即失效 | ✅ |
| `deploy_publish` | one_shot | ✅ | ✅ | ✅ | ✅ | 用掉即失效 | ✅ |
| `desktop_control` | window | ✅ | ✅ | ✅ | ✅ | 可复用+记账 | ✅ |
| `device_control` | window | ✅ | ✅ | ✅ | ✅ | 可复用+记账 | ✅ |
| `external_llm` | window | ✅ | ✅ | ✅ | ✅ | 可复用+记账 | ✅ |
| `network_private` | window | ✅ | ✅ | ✅ | ✅ | 可复用+记账 | ✅ |
| `privacy_read` | window | ✅ | ✅ | ✅ | ✅ | 可复用+记账 | ✅ |
| `process_execute` | window | ✅ | ✅ | ✅ | ✅ | 可复用+记账 | ✅ |
| `remote_device` | one_shot | ✅ | ✅ | ✅ | ✅ | 用掉即失效 | ✅ |

> 结论：**全部通过**；`ai_can_grant = False` —— AI 调用路径上不存在任何发放入口，这条不是靠提示词约束的，是函数不存在。

## 三、真缺陷（34）

### defect/import（31）

注册表声称已实现，但分发目标模块在树里不存在

| 能力位 | 域 | 受闸 | 实测 |
|---|---|:--:|---|
| `book_skill` | `recon` | 是 | cannot import name 'book_skill' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `chart_html` | `data` | 是 | cannot import name 'chart_html' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `cli_ify` | `integration` | 是 | cannot import name 'cli_ify' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `cloud_llm` | `llm` |  | cannot import name 'cloud_llm_cap' from 'gbt_allinone.llm' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\llm\__init__.py) |
| `comfy_forge` | `creation` |  | cannot import name 'comfy_forge' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `db_plugin` | `data` |  | cannot import name 'db_plugin' from 'gbt_allinone.tools' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\tools\__init__.py) |
| `dh_realism` | `creation` |  | cannot import name 'dh_realism' from 'gbt_allinone.tools' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\tools\__init__.py) |
| `dl_forge` | `creation` |  | cannot import name 'dl_forge' from 'gbt_allinone.tools' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\tools\__init__.py) |
| `figure_gate` | `system` | 是 | cannot import name 'figure_gate' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `forge_mastery` | `creation` | 是 | cannot import name 'forge_mastery' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `humanizer` | `data` | 是 | cannot import name 'humanizer' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `image_scout` | `creation` |  | cannot import name 'image_scout' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `install_selfcheck` | `security` |  | cannot import name 'install_selfcheck' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `know_map` | `recon` | 是 | cannot import name 'know_map' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `music_auto` | `creation` | 是 | cannot import name 'music_auto' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `offense_ops` | `security` | 是 | cannot import name 'offense_ops' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `quant_plan` | `llm` | 是 | cannot import name 'quant_plan' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `scan_cap` | `system` | 是 | cannot import name 'scan_cap' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `self_intake` | `mind` | 是 | cannot import name 'self_intake' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `shot_director` | `creation` | 是 | cannot import name 'shot_director' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `showcase_ops` | `creation` | 是 | cannot import name 'showcase_ops' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `skill_finder` | `data` | 是 | cannot import name 'skill_finder' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `skill_forge` | `recon` | 是 | cannot import name 'skill_forge' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `spider_ops` | `recon` | 是 | cannot import name 'spider_ops' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `telegram_embed` | `integration` |  | cannot import name 'telegram_embed' from 'gbt_allinone.tools' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\tools\__init__.py) |
| `tentacle_learn` | `recon` | 是 | cannot import name 'tentacle_learn' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `theme_cap` | `system` | 是 | cannot import name 'theme_cap' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `topic_web` | `recon` | 是 | cannot import name 'topic_web' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `train_ground` | `llm` | 是 | cannot import name 'train_ground' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |
| `whatsapp_embed` | `integration` |  | cannot import name 'whatsapp_embed' from 'gbt_allinone.tools' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\tools\__init__.py) |
| `workflow_forge` | `engine` | 是 | cannot import name 'workflow_forge' from 'gbt_allinone' (C:\Users\ADMIN\WorkBuddy\Worktrees\GBT小土豆V8\main-bf436b33\gbt_allinone\__init__.py) |

### defect/timeout（2）

限时内无任何返回

| 能力位 | 域 | 受闸 | 实测 |
|---|---|:--:|---|
| `cross_scan` | `system` |  | cross_scan 在 90s 内无返回 |
| `page_scan` | `system` |  | page_scan 在 90s 内无返回 |

### defect/exception（1）

Python 异常穿过 error_class=user_error 直接漏给调用方

| 能力位 | 域 | 受闸 | 实测 |
|---|---|:--:|---|
| `selfscan` | `system` |  | scan() got an unexpected keyword argument 'full' |

## 四、三组读数

### 4.1 护栏拦下的是什么（32 次拦截）

| 作用域 | 拦截次数 | 能力位 |
|---|---:|---|
| `process_execute` | 12 | `codex_chat`, `codex_interrupt`, `codex_thread_new`, `codex_turn_send`, `comfy_cloud`, `mcp_call`, `mcp_connect`, `mirror_rehearse`, `mirror_release`, `omarchy_bridge`, `one_key_deploy`, `remote_confinement` |
| `external_llm` | 8 | `autopilot`, `codex_chat`, `codex_models`, `codex_turn_send`, `devour_pulse`, `llm_chat`, `sec_llm`, `think_loop` |
| `deploy_publish` | 6 | `mirror_ascend`, `mirror_release`, `mirror_rewind`, `one_key_deploy`, `pipeline_rollback`, `pipeline_submit` |
| `privacy_read` | 5 | `credential_steal`, `data_hijack`, `keylogger`, `screen_sniff`, `vision` |
| `data_export` | 3 | `devour_github`, `devour_pulse`, `omni_web` |
| `device_control` | 2 | `bluetooth`, `bt_control` |
| `audio_output` | 1 | `voice` |

这三道护栏不是「什么都拦」：341 个位里只有 32 个走到这道门，另外 309 个没走到——其中 34 个在更早的地方就失败了。拦得住的少，才说明拦得准。

### 4.2 最慢的 5 个（上限 90s，逼近上限的会被当成超时）

| 能力位 | 耗时 |
|---|---:|
| `sec_chain` | 48.2s |
| `sec_scan` | 48.0s |
| `file_hygiene` | 7.9s |
| `task_manager` | 7.8s |
| `cli_chat` | 7.5s |

> `sec_chain`、`sec_scan` 已经吃掉限时的一半以上。它们没超时，但如果调用方把超时设在 30s，就会变成假故障——这是**读数**，不是缺陷，写在这里免得下次误判。

### 4.3 返回最大的 5 个（一次调用灌给调用方/模型多少字节）

| 能力位 | 返回字节 |
|---|---:|
| `awesome_tools_index` | 103,532 |
| `caps_called_audit` | 81,244 |
| `tentacle_arm` | 25,473 |
| `code_audit` | 23,627 |
| `dh_brain` | 22,707 |

## 五、按设计拒绝（不算缺陷）

### pass/guardrail（32）— 被三道护栏拦下：点名缺哪个作用域 + 给出发放方式

| 能力位 | 域 | 实测返回 |
|---|---|---|
| `autopilot` | `llm` | 缺 external_llm |
| `bluetooth` | `device` | 缺 device_control |
| `bt_control` | `device` | 缺 device_control |
| `codex_chat` | `llm` | 缺 process_execute, external_llm |
| `codex_interrupt` | `llm` | 缺 process_execute |
| `codex_models` | `llm` | 缺 external_llm |
| `codex_thread_new` | `llm` | 缺 process_execute |
| `codex_turn_send` | `llm` | 缺 process_execute, external_llm |
| `comfy_cloud` | `creation` | 缺 process_execute |
| `credential_steal` | `security` | 缺 privacy_read |
| `data_hijack` | `security` | 缺 privacy_read |
| `devour_github` | `devour` | 缺 data_export |
| `devour_pulse` | `devour` | 缺 data_export, external_llm |
| `keylogger` | `security` | 缺 privacy_read |
| `llm_chat` | `llm` | 缺 external_llm |
| `mcp_call` | `tentacle` | 缺 process_execute |
| `mcp_connect` | `tentacle` | 缺 process_execute |
| `mirror_ascend` | `pipeline` | 缺 deploy_publish |
| `mirror_rehearse` | `pipeline` | 缺 process_execute |
| `mirror_release` | `pipeline` | 缺 deploy_publish, process_execute |
| `mirror_rewind` | `pipeline` | 缺 deploy_publish |
| `omarchy_bridge` | `tentacle` | 缺 process_execute |
| `omni_web` | `tentacle` | 缺 data_export |
| `one_key_deploy` | `pipeline` | 缺 deploy_publish, process_execute |
| `pipeline_rollback` | `pipeline` | 缺 deploy_publish |
| `pipeline_submit` | `pipeline` | 缺 deploy_publish |
| `remote_confinement` | `tentacle` | 缺 process_execute |
| `screen_sniff` | `security` | 缺 privacy_read |
| `sec_llm` | `security` | 缺 external_llm |
| `think_loop` | `llm` | 缺 external_llm |
| `vision` | `vision` | 缺 privacy_read |
| `voice` | `voice` | 缺 audio_output |

### pass/needs-input（14）— 输入校验拦下并说清缺哪个字段

| 能力位 | 域 | 实测返回 |
|---|---|---|
| `brain_execute` | `llm` | 缺少 kind 或 parallel |
| `brain_route` | `llm` | 需要 intent：任务意图描述 |
| `brain_unify` | `llm` | 需要 goal（意图）或 kind（指定能力） |
| `browser` | `automation` | 缺少 url |
| `code_patch` | `tools` | find 不能为空（空白替换只会误伤） |
| `git_write` | `tools` | git_write 不认 op=（只认 stage/add/commit） |
| `lr_submit` | `longrun` | 需要 description |
| `osint_scan` | `recon` | 缺少 target（要扫的域名或 IP）。例：{"target": "example.com"} |
| `pipeline_versions` | `pipeline` | 缺少 name：请给出产物名 |
| `record_grid` | `data` | 需要 text（内联文本）或 path（框架内相对路径） |
| `sched_define` | `engine` | 需要 name |
| `tentacle` | `tentacle` | 缺少 action：给触手能力名（tentacle_manifest）、给 intent 走自动路由、或 op=caps 看全部能力 |
| `topic_watch` | `recon` | 缺少 need：请给一句需求（如「帮我盯着 AI 行业动态」） |
| `wf_define` | `engine` | 需要 name 与非空 nodes 列表 |

### pass/needs-state（5）— 前置状态未建（工作流/运行记录/排练计划），提示先做上一步

| 能力位 | 域 | 实测返回 |
|---|---|---|
| `mirror_parity` | `pipeline` | 排练计划不存在: default |
| `mirror_plan` | `pipeline` | 排练计划不存在: default |
| `mirror_simulate` | `pipeline` | 排练计划不存在: default |
| `wf_resume` | `engine` | 运行记录不存在:  |
| `wf_run` | `engine` | 工作流不存在: （先 wf_define） |

## 六、全部能力位一览

| # | 能力位 | 域 | 受闸 | 判定 | 耗时 ms |
|---:|---|---|:--:|---|---:|
| 1 | `browser` | `automation` |  | pass/needs-input | 1269.8 |
| 2 | `n8n_wf` | `automation` | 是 | pass/ok | 4908.0 |
| 3 | `absorb_loop` | `brain` |  | pass/ok | 735.8 |
| 4 | `dream_replay` | `brain` |  | pass/ok | 621.7 |
| 5 | `collab_gateway` | `collab` | 是 | pass/ok | 663.5 |
| 6 | `stigmergy` | `collab` |  | pass/ok | 1003.2 |
| 7 | `coze_mail` | `comms` |  | pass/ok | 600.9 |
| 8 | `anatomy_figures` | `creation` | 是 | pass/ok | 785.7 |
| 9 | `anim_audit` | `creation` |  | pass/ok | 819.0 |
| 10 | `anim_fix` | `creation` | 是 | pass/ok | 778.5 |
| 11 | `art_brief` | `creation` | 是 | pass/ok | 901.1 |
| 12 | `art_chain` | `creation` | 是 | pass/ok | 806.9 |
| 13 | `bits_kit` | `creation` |  | pass/ok | 677.7 |
| 14 | `blender` | `creation` | 是 | pass/ok | 909.0 |
| 15 | `brand_outro` | `creation` |  | pass/ok | 727.9 |
| 16 | `cad_distill` | `creation` |  | pass/ok | 660.8 |
| 17 | `cadgen` | `creation` | 是 | pass/ok | 791.7 |
| 18 | `code_art` | `creation` |  | pass/ok | 600.3 |
| 19 | `comfy_cloud` | `creation` | 是 | pass/guardrail | 616.2 |
| 20 | `comfy_forge` | `creation` |  | defect/import | 618.0 |
| 21 | `comfy_native` | `creation` |  | pass/ok | 7023.6 |
| 22 | `comfyui` | `creation` |  | pass/ok | 2839.9 |
| 23 | `console_pages` | `creation` |  | pass/ok | 5480.9 |
| 24 | `create` | `creation` |  | pass/ok | 631.6 |
| 25 | `creation_camp` | `creation` |  | pass/ok | 624.4 |
| 26 | `design_atlas` | `creation` |  | pass/ok | 1221.1 |
| 27 | `dh_asset_gate` | `creation` |  | pass/ok | 1021.0 |
| 28 | `dh_brain` | `creation` |  | pass/ok | 1246.1 |
| 29 | `dh_pose` | `creation` | 是 | pass/ok | 1218.8 |
| 30 | `dh_realism` | `creation` |  | defect/import | 997.8 |
| 31 | `diagram_distill` | `creation` |  | pass/ok | 988.5 |
| 32 | `dl_forge` | `creation` |  | defect/import | 679.5 |
| 33 | `drama` | `creation` |  | pass/ok | 660.1 |
| 34 | `emotion_projection` | `creation` |  | pass/ok | 707.6 |
| 35 | `filmkit` | `creation` | 是 | pass/ok | 714.9 |
| 36 | `flow_canvas` | `creation` |  | pass/ok | 712.4 |
| 37 | `forge_mastery` | `creation` | 是 | defect/import | 699.4 |
| 38 | `genoffice` | `creation` | 是 | pass/ok | 626.1 |
| 39 | `gs_h3` | `creation` | 是 | pass/ok | 646.3 |
| 40 | `image_scout` | `creation` |  | defect/import | 536.0 |
| 41 | `intake_kit` | `creation` |  | pass/ok | 632.4 |
| 42 | `lobehub` | `creation` |  | pass/ok | 2783.3 |
| 43 | `machine_distill` | `creation` |  | pass/ok | 593.8 |
| 44 | `machine_film` | `creation` | 是 | pass/ok | 661.3 |
| 45 | `motion_kit` | `creation` |  | pass/ok | 679.3 |
| 46 | `music_auto` | `creation` | 是 | defect/import | 629.1 |
| 47 | `music_publishing` | `creation` |  | pass/ok | 614.7 |
| 48 | `omni_arm` | `creation` | 是 | pass/ok | 594.0 |
| 49 | `one_shot` | `creation` |  | pass/ok | 605.4 |
| 50 | `pod_link` | `creation` | 是 | pass/ok | 725.7 |
| 51 | `render_evolution` | `creation` |  | pass/ok | 751.0 |
| 52 | `rig_audit` | `creation` | 是 | pass/ok | 778.0 |
| 53 | `rig_fix` | `creation` | 是 | pass/ok | 834.6 |
| 54 | `scene_anchor` | `creation` |  | pass/ok | 811.8 |
| 55 | `shot_director` | `creation` | 是 | defect/import | 733.3 |
| 56 | `showcase_ops` | `creation` | 是 | defect/import | 758.4 |
| 57 | `tentacle_comfy_bridge` | `creation` |  | pass/ok | 4837.3 |
| 58 | `tripo` | `creation` | 是 | pass/ok | 5247.1 |
| 59 | `ui_kit` | `creation` |  | pass/ok | 524.3 |
| 60 | `ui_render` | `creation` |  | pass/ok | 500.2 |
| 61 | `zimage_rewash` | `creation` | 是 | pass/ok | 413.1 |
| 62 | `account_registry` | `data` |  | pass/ok | 696.1 |
| 63 | `audit_query` | `data` |  | pass/ok | 774.6 |
| 64 | `bi_distill` | `data` |  | pass/ok | 643.6 |
| 65 | `chart_html` | `data` | 是 | defect/import | 645.4 |
| 66 | `count_words` | `data` |  | pass/ok | 593.8 |
| 67 | `datakit` | `data` |  | pass/ok | 669.2 |
| 68 | `db_plugin` | `data` |  | defect/import | 668.3 |
| 69 | `db_probe` | `data` |  | pass/ok | 863.8 |
| 70 | `echo` | `data` |  | pass/ok | 683.7 |
| 71 | `humanizer` | `data` | 是 | defect/import | 567.4 |
| 72 | `record_grid` | `data` |  | pass/needs-input | 759.1 |
| 73 | `skill_finder` | `data` | 是 | defect/import | 814.1 |
| 74 | `control_loop` | `desktop` |  | pass/ok | 599.2 |
| 75 | `ul_tars_desktop` | `desktop` | 是 | pass/ok | 584.2 |
| 76 | `bluetooth` | `device` |  | pass/guardrail | 629.2 |
| 77 | `bt_control` | `device` |  | pass/guardrail | 664.9 |
| 78 | `devour_fusion` | `devour` |  | pass/ok | 986.3 |
| 79 | `devour_github` | `devour` |  | pass/guardrail | 720.1 |
| 80 | `devour_pulse` | `devour` |  | pass/guardrail | 653.1 |
| 81 | `devour_reflect` | `devour` |  | pass/ok | 791.0 |
| 82 | `devour_scan` | `devour` |  | pass/ok | 768.6 |
| 83 | `sched_define` | `engine` |  | pass/needs-input | 733.3 |
| 84 | `sched_status` | `engine` |  | pass/ok | 858.3 |
| 85 | `sched_tick` | `engine` |  | pass/ok | 885.5 |
| 86 | `transfer` | `engine` |  | pass/ok | 531.8 |
| 87 | `wf_cache_clear` | `engine` |  | pass/ok | 486.6 |
| 88 | `wf_define` | `engine` |  | pass/needs-input | 525.5 |
| 89 | `wf_resume` | `engine` |  | pass/needs-state | 531.0 |
| 90 | `wf_run` | `engine` |  | pass/needs-state | 607.3 |
| 91 | `wf_status` | `engine` |  | pass/ok | 527.1 |
| 92 | `workflow_forge` | `engine` | 是 | defect/import | 419.9 |
| 93 | `quant` | `finance` |  | pass/ok | 772.4 |
| 94 | `quant_backtest` | `finance` |  | pass/ok | 813.3 |
| 95 | `quant_params` | `finance` |  | pass/ok | 668.4 |
| 96 | `quant_strategy` | `finance` |  | pass/ok | 764.7 |
| 97 | `gate_visibility` | `framework` |  | pass/ok | 733.0 |
| 98 | `a1art_skill` | `image_video` |  | pass/ok | 748.4 |
| 99 | `cloud_pc` | `infra` |  | pass/ok | 678.8 |
| 100 | `cloud_plugin` | `infra` |  | pass/ok | 634.6 |
| 101 | `cli_chat` | `integration` | 是 | pass/ok | 7528.2 |
| 102 | `cli_ify` | `integration` | 是 | defect/import | 643.8 |
| 103 | `feishu_embed` | `integration` |  | pass/ok | 745.4 |
| 104 | `notion_bridge` | `integration` | 是 | pass/ok | 640.1 |
| 105 | `telegram_embed` | `integration` |  | defect/import | 747.9 |
| 106 | `thebrain_bridge` | `integration` | 是 | pass/ok | 3171.9 |
| 107 | `whatsapp_embed` | `integration` |  | defect/import | 488.0 |
| 108 | `life` | `life` |  | pass/ok | 696.9 |
| 109 | `automation_keys` | `llm` |  | pass/ok | 713.7 |
| 110 | `autopilot` | `llm` |  | pass/guardrail | 713.4 |
| 111 | `brain_execute` | `llm` |  | pass/needs-input | 700.5 |
| 112 | `brain_health` | `llm` |  | pass/ok | 1502.5 |
| 113 | `brain_route` | `llm` |  | pass/needs-input | 738.9 |
| 114 | `brain_unify` | `llm` |  | pass/needs-input | 679.2 |
| 115 | `brain_verify` | `llm` |  | pass/ok | 939.1 |
| 116 | `claude_code` | `llm` | 是 | pass/ok | 654.5 |
| 117 | `cloud_llm` | `llm` |  | defect/import | 605.1 |
| 118 | `codebuddy` | `llm` | 是 | pass/ok | 658.3 |
| 119 | `codex_chat` | `llm` |  | pass/guardrail | 649.0 |
| 120 | `codex_interrupt` | `llm` |  | pass/guardrail | 680.5 |
| 121 | `codex_models` | `llm` |  | pass/guardrail | 644.3 |
| 122 | `codex_status` | `llm` |  | pass/ok | 715.4 |
| 123 | `codex_thread_new` | `llm` |  | pass/guardrail | 655.7 |
| 124 | `codex_tools` | `llm` |  | pass/ok | 673.3 |
| 125 | `codex_turn_send` | `llm` |  | pass/guardrail | 638.1 |
| 126 | `duty_board` | `llm` |  | pass/ok | 787.8 |
| 127 | `energy_scheduler` | `llm` |  | pass/ok | 746.2 |
| 128 | `fact_gate` | `llm` |  | pass/ok | 703.1 |
| 129 | `freellmapi` | `llm` |  | pass/ok | 2743.7 |
| 130 | `genoffice_bridge` | `llm` | 是 | pass/ok | 792.1 |
| 131 | `key_gateway` | `llm` | 是 | pass/ok | 657.6 |
| 132 | `llm_chat` | `llm` |  | pass/guardrail | 609.2 |
| 133 | `llm_status` | `llm` |  | pass/ok | 704.4 |
| 134 | `llm_watch` | `llm` |  | pass/ok | 646.5 |
| 135 | `model_key_pool` | `llm` |  | pass/ok | 613.1 |
| 136 | `multimodal_port` | `llm` | 是 | pass/ok | 657.3 |
| 137 | `offload_distill` | `llm` |  | pass/ok | 825.9 |
| 138 | `omni_plug` | `llm` | 是 | pass/ok | 608.3 |
| 139 | `policy_gate` | `llm` |  | pass/ok | 718.3 |
| 140 | `prompt_bridge` | `llm` |  | pass/ok | 703.3 |
| 141 | `quant_plan` | `llm` | 是 | defect/import | 717.1 |
| 142 | `replan_loop` | `llm` |  | pass/ok | 838.0 |
| 143 | `ring_context` | `llm` |  | pass/ok | 947.2 |
| 144 | `task_graph` | `llm` |  | pass/ok | 799.5 |
| 145 | `think_loop` | `llm` |  | pass/guardrail | 599.2 |
| 146 | `train_ground` | `llm` | 是 | defect/import | 559.7 |
| 147 | `train_recipe` | `llm` |  | pass/ok | 4431.2 |
| 148 | `transformer` | `llm` |  | pass/ok | 478.1 |
| 149 | `warm_switch` | `llm` |  | pass/ok | 1056.0 |
| 150 | `lr_status` | `longrun` |  | pass/ok | 576.1 |
| 151 | `lr_submit` | `longrun` |  | pass/needs-input | 594.5 |
| 152 | `lr_tick` | `longrun` |  | pass/ok | 625.3 |
| 153 | `tactics_advise` | `longrun` |  | pass/ok | 939.4 |
| 154 | `agent_council` | `mind` |  | pass/ok | 729.0 |
| 155 | `auto_switch` | `mind` |  | pass/ok | 704.9 |
| 156 | `belief_forge` | `mind` |  | pass/ok | 656.3 |
| 157 | `brain_council` | `mind` |  | pass/ok | 706.4 |
| 158 | `brain_vault` | `mind` |  | pass/ok | 818.1 |
| 159 | `command_chain` | `mind` |  | pass/ok | 600.1 |
| 160 | `director_mood` | `mind` |  | pass/ok | 677.1 |
| 161 | `doc_intake` | `mind` |  | pass/ok | 667.9 |
| 162 | `local_brain` | `mind` |  | pass/ok | 651.1 |
| 163 | `memory_bank` | `mind` |  | pass/ok | 584.1 |
| 164 | `memory_manager` | `mind` |  | pass/ok | 1008.1 |
| 165 | `meta_cognition` | `mind` |  | pass/ok | 574.5 |
| 166 | `mind` | `mind` |  | pass/ok | 692.6 |
| 167 | `observer_anchor` | `mind` |  | pass/ok | 620.2 |
| 168 | `obsidian_vault` | `mind` |  | pass/ok | 663.5 |
| 169 | `persona_kernel` | `mind` |  | pass/ok | 602.0 |
| 170 | `proactive_report` | `mind` |  | pass/ok | 781.3 |
| 171 | `self_intake` | `mind` | 是 | defect/import | 691.5 |
| 172 | `wiki_graph` | `mind` |  | pass/ok | 488.1 |
| 173 | `deploy_queue` | `pipeline` |  | pass/ok | 883.9 |
| 174 | `ghost_guard` | `pipeline` |  | pass/ok | 2352.3 |
| 175 | `mirror_ascend` | `pipeline` |  | pass/guardrail | 564.9 |
| 176 | `mirror_parity` | `pipeline` |  | pass/needs-state | 654.3 |
| 177 | `mirror_plan` | `pipeline` |  | pass/needs-state | 617.4 |
| 178 | `mirror_rehearse` | `pipeline` |  | pass/guardrail | 557.9 |
| 179 | `mirror_release` | `pipeline` |  | pass/guardrail | 546.3 |
| 180 | `mirror_rewind` | `pipeline` |  | pass/guardrail | 590.1 |
| 181 | `mirror_scan` | `pipeline` |  | pass/ok | 653.4 |
| 182 | `mirror_shape` | `pipeline` |  | pass/ok | 596.9 |
| 183 | `mirror_simulate` | `pipeline` |  | pass/needs-state | 770.1 |
| 184 | `mirror_status` | `pipeline` |  | pass/ok | 666.7 |
| 185 | `one_key_deploy` | `pipeline` |  | pass/guardrail | 604.1 |
| 186 | `pipeline_rollback` | `pipeline` |  | pass/guardrail | 667.4 |
| 187 | `pipeline_status` | `pipeline` |  | pass/ok | 710.2 |
| 188 | `pipeline_submit` | `pipeline` |  | pass/guardrail | 621.0 |
| 189 | `pipeline_versions` | `pipeline` |  | pass/needs-input | 747.7 |
| 190 | `svc_inspect` | `pipeline` |  | pass/ok | 1753.7 |
| 191 | `platform_profile` | `project` |  | pass/ok | 744.6 |
| 192 | `project_context` | `project` |  | pass/ok | 837.6 |
| 193 | `book_skill` | `recon` | 是 | defect/import | 634.8 |
| 194 | `case_mine` | `recon` |  | pass/ok | 674.1 |
| 195 | `film_intel` | `recon` |  | pass/ok | 653.5 |
| 196 | `know_map` | `recon` | 是 | defect/import | 640.2 |
| 197 | `music_intel` | `recon` |  | pass/ok | 606.1 |
| 198 | `osint_scan` | `recon` |  | pass/needs-input | 585.7 |
| 199 | `rea_reverse` | `recon` |  | pass/ok | 732.5 |
| 200 | `recon_distill` | `recon` |  | pass/ok | 713.7 |
| 201 | `scrapling` | `recon` |  | pass/ok | 876.5 |
| 202 | `skill_forge` | `recon` | 是 | defect/import | 773.7 |
| 203 | `spider_ops` | `recon` | 是 | defect/import | 795.0 |
| 204 | `tentacle_learn` | `recon` | 是 | defect/import | 693.7 |
| 205 | `topic_watch` | `recon` |  | pass/needs-input | 560.7 |
| 206 | `topic_web` | `recon` | 是 | defect/import | 561.3 |
| 207 | `trend_watch` | `recon` |  | pass/ok | 826.1 |
| 208 | `verification_watch` | `recon` |  | pass/ok | 509.0 |
| 209 | `video_intel` | `recon` |  | pass/ok | 502.0 |
| 210 | `asset_vault_freeze` | `security` |  | pass/ok | 3595.8 |
| 211 | `code_audit` | `security` |  | pass/ok | 658.1 |
| 212 | `credential_steal` | `security` | 是 | pass/guardrail | 601.8 |
| 213 | `data_hijack` | `security` | 是 | pass/guardrail | 617.7 |
| 214 | `device_takeover` | `security` | 是 | pass/ok | 3542.6 |
| 215 | `event_ledger` | `security` |  | pass/ok | 686.7 |
| 216 | `hook_enforcer` | `security` |  | pass/ok | 543.5 |
| 217 | `install_selfcheck` | `security` |  | defect/import | 584.5 |
| 218 | `keylogger` | `security` | 是 | pass/guardrail | 603.0 |
| 219 | `llm_redteam` | `security` |  | pass/ok | 638.4 |
| 220 | `offense_ops` | `security` | 是 | defect/import | 631.3 |
| 221 | `omission_detector` | `security` |  | pass/ok | 671.9 |
| 222 | `onboarding_gate` | `security` |  | pass/ok | 645.8 |
| 223 | `paywallbuster` | `security` |  | pass/ok | 649.0 |
| 224 | `penetrating_cross_scan` | `security` |  | pass/ok | 627.3 |
| 225 | `pentest` | `security` | 是 | pass/ok | 647.7 |
| 226 | `pentest_distill` | `security` |  | pass/ok | 605.9 |
| 227 | `policy_delta` | `security` |  | pass/ok | 734.7 |
| 228 | `redteam_recon` | `security` | 是 | pass/ok | 869.6 |
| 229 | `remote_domain` | `security` | 是 | pass/ok | 765.5 |
| 230 | `review_gate` | `security` |  | pass/ok | 706.4 |
| 231 | `screen_sniff` | `security` | 是 | pass/guardrail | 864.5 |
| 232 | `sec_chain` | `security` |  | pass/ok | 48200.0 |
| 233 | `sec_defenses` | `security` |  | pass/ok | 7338.8 |
| 234 | `sec_llm` | `security` |  | pass/guardrail | 789.7 |
| 235 | `sec_scan` | `security` |  | pass/ok | 48016.9 |
| 236 | `sec_surface` | `security` |  | pass/ok | 4173.2 |
| 237 | `sec_sweeper` | `security` |  | pass/ok | 744.6 |
| 238 | `social_eng` | `security` |  | pass/ok | 1290.1 |
| 239 | `auto_publish` | `social` |  | pass/ok | 679.7 |
| 240 | `eigenflux` | `social` |  | pass/ok | 777.8 |
| 241 | `action_gate` | `system` |  | pass/ok | 792.3 |
| 242 | `agent_console` | `system` |  | pass/ok | 705.7 |
| 243 | `agent_control` | `system` |  | pass/ok | 760.3 |
| 244 | `agent_rig` | `system` |  | pass/ok | 627.4 |
| 245 | `alerts` | `system` |  | pass/ok | 774.0 |
| 246 | `answer_shaper` | `system` |  | pass/ok | 721.2 |
| 247 | `asset_index` | `system` |  | pass/ok | 905.4 |
| 248 | `auth_gate_status` | `system` |  | pass/ok | 676.8 |
| 249 | `cap_tags` | `system` |  | pass/ok | 747.5 |
| 250 | `caps_called_audit` | `system` |  | pass/ok | 3345.0 |
| 251 | `console_hub` | `system` |  | pass/ok | 595.4 |
| 252 | `context_vault` | `system` |  | pass/ok | 638.9 |
| 253 | `coverage_auditor` | `system` |  | pass/ok | 585.9 |
| 254 | `cross_scan` | `system` |  | defect/timeout | 90000 |
| 255 | `delivery_gate` | `system` | 是 | pass/ok | 1338.1 |
| 256 | `detail_habit` | `system` |  | pass/ok | 708.8 |
| 257 | `energy_pool` | `system` |  | pass/ok | 728.2 |
| 258 | `figure_gate` | `system` | 是 | defect/import | 645.6 |
| 259 | `file_hygiene` | `system` |  | pass/ok | 7941.5 |
| 260 | `god_view` | `system` |  | pass/ok | 915.6 |
| 261 | `gods_eye` | `system` |  | pass/ok | 2098.5 |
| 262 | `growth_hooks` | `system` |  | pass/ok | 2420.9 |
| 263 | `handoff` | `system` |  | pass/ok | 547.8 |
| 264 | `health` | `system` |  | pass/ok | 624.1 |
| 265 | `hook_registry` | `system` |  | pass/ok | 521.8 |
| 266 | `impact_check` | `system` |  | pass/ok | 602.9 |
| 267 | `inventory` | `system` |  | pass/ok | 642.5 |
| 268 | `ledger_note` | `system` |  | pass/ok | 640.7 |
| 269 | `orchestration_kernel` | `system` |  | pass/ok | 970.3 |
| 270 | `page_scan` | `system` |  | defect/timeout | 90000 |
| 271 | `project_drift` | `system` |  | pass/ok | 787.0 |
| 272 | `room_space` | `system` | 是 | pass/ok | 897.8 |
| 273 | `root_fix` | `system` |  | pass/ok | 783.2 |
| 274 | `scan_cap` | `system` | 是 | defect/import | 861.2 |
| 275 | `selfscan` | `system` |  | defect/exception | 734.8 |
| 276 | `shared_resources` | `system` |  | pass/ok | 759.9 |
| 277 | `signature_guard` | `system` |  | pass/ok | 895.5 |
| 278 | `skill_watch` | `system` |  | pass/ok | 884.1 |
| 279 | `slim_profile` | `system` |  | pass/ok | 911.9 |
| 280 | `spend_guard` | `system` |  | pass/ok | 1379.5 |
| 281 | `surface_bind` | `system` |  | pass/ok | 963.3 |
| 282 | `task_manager` | `system` |  | pass/ok | 7750.4 |
| 283 | `tentacle_arm` | `system` |  | pass/ok | 876.5 |
| 284 | `tentacle_bind` | `system` |  | pass/ok | 1413.0 |
| 285 | `tentacle_cognition` | `system` |  | pass/ok | 815.3 |
| 286 | `theme_cap` | `system` | 是 | defect/import | 601.1 |
| 287 | `trace_store` | `system` |  | pass/ok | 575.1 |
| 288 | `truth_scan` | `system` |  | pass/ok | 507.3 |
| 289 | `ux_doctrine` | `system` |  | pass/ok | 518.1 |
| 290 | `wave_probe` | `system` |  | pass/ok | 550.0 |
| 291 | `welcome` | `system` |  | pass/ok | 479.2 |
| 292 | `agency_tentacles` | `tentacle` |  | pass/ok | 708.3 |
| 293 | `desktop_commander` | `tentacle` |  | pass/ok | 1171.8 |
| 294 | `desktop_distill` | `tentacle` |  | pass/ok | 1038.3 |
| 295 | `express_direct` | `tentacle` |  | pass/ok | 719.1 |
| 296 | `long_run_supervisor` | `tentacle` |  | pass/ok | 584.7 |
| 297 | `mcp_call` | `tentacle` |  | pass/guardrail | 541.7 |
| 298 | `mcp_connect` | `tentacle` |  | pass/guardrail | 532.5 |
| 299 | `mcp_tools` | `tentacle` |  | pass/ok | 566.6 |
| 300 | `omarchy_bridge` | `tentacle` | 是 | pass/guardrail | 601.6 |
| 301 | `omni_web` | `tentacle` | 是 | pass/guardrail | 601.2 |
| 302 | `remote_confinement` | `tentacle` | 是 | pass/guardrail | 706.1 |
| 303 | `tentacle` | `tentacle` |  | pass/needs-input | 954.3 |
| 304 | `tentacle_equip` | `tentacle` | 是 | pass/ok | 1099.3 |
| 305 | `tentacle_manifest` | `tentacle` |  | pass/ok | 947.2 |
| 306 | `tentacle_pipeline` | `tentacle` |  | pass/ok | 622.7 |
| 307 | `tentacle_scale` | `tentacle` |  | pass/ok | 662.4 |
| 308 | `tentacle_status` | `tentacle` |  | pass/ok | 1086.3 |
| 309 | `tool_bay` | `tentacle` | 是 | pass/ok | 2385.8 |
| 310 | `awesome_tools_index` | `tools` |  | pass/ok | 760.6 |
| 311 | `capability_net` | `tools` |  | pass/ok | 683.4 |
| 312 | `code_patch` | `tools` | 是 | pass/needs-input | 613.4 |
| 313 | `freebuff_term` | `tools` |  | pass/ok | 710.2 |
| 314 | `git_read` | `tools` |  | pass/ok | 843.9 |
| 315 | `git_write` | `tools` | 是 | pass/needs-input | 674.8 |
| 316 | `projection_card` | `tools` |  | pass/ok | 748.3 |
| 317 | `pulse_direct` | `tools` |  | pass/ok | 825.8 |
| 318 | `repo_publish` | `tools` |  | pass/ok | 1085.4 |
| 319 | `actioncam` | `video` | 是 | pass/ok | 698.3 |
| 320 | `audio_extract` | `video` | 是 | pass/ok | 762.7 |
| 321 | `audio_mix` | `video` | 是 | pass/ok | 739.6 |
| 322 | `digital_human` | `video` |  | pass/ok | 578.4 |
| 323 | `edit_pipeline` | `video` | 是 | pass/ok | 854.1 |
| 324 | `h3_video_gen` | `video` |  | pass/ok | 600.1 |
| 325 | `libtv_skill` | `video` |  | pass/ok | 653.3 |
| 326 | `libtv_workflow` | `video` |  | pass/ok | 636.8 |
| 327 | `look_grade` | `video` | 是 | pass/ok | 602.2 |
| 328 | `media_license` | `video` | 是 | pass/ok | 589.4 |
| 329 | `media_pipeline` | `video` |  | pass/ok | 564.1 |
| 330 | `media_publish` | `video` | 是 | pass/ok | 597.1 |
| 331 | `media_run` | `video` | 是 | pass/ok | 674.7 |
| 332 | `media_stamp` | `video` | 是 | pass/ok | 641.5 |
| 333 | `vision` | `vision` |  | pass/guardrail | 492.1 |
| 334 | `vision_grounding` | `vision` |  | pass/ok | 509.1 |
| 335 | `vision_loop` | `vision` | 是 | pass/ok | 507.9 |
| 336 | `vision_print` | `vision` |  | pass/ok | 591.5 |
| 337 | `vlx_flow` | `vision` |  | pass/ok | 515.0 |
| 338 | `hf_voice` | `voice` |  | pass/ok | 530.9 |
| 339 | `voice` | `voice` |  | pass/guardrail | 481.5 |
| 340 | `voice_orchestra` | `voice` |  | pass/ok | 1139.8 |
| 341 | `voice_studio` | `voice` |  | pass/ok | 2537.7 |

## 七、这份报告不声称什么

1. **不声称 341 个能力都有用。** 空载荷跑通只证明「入口活着、返回非空」，不证明它在真实任务上做得对。功能正确性要靠各自仓库的测试与真实任务回溯。
2. **不声称受闸能力没被验证。** 它们被拦下了，而拦截本身在第二节做了双向验收：同一道门有票能放、没票必拒。但这不等于它们的功能被执行过——要执行就必须真的授权并产生真实后果，那不该由一次验收代劳。
3. **不声称超时的两个能力是死代码。** `cross_scan` / `page_scan` 在 300s 内也不返回，可能是等外部网络、也可能是死循环；本报告只如实记「限时内无返回」，不猜原因。
4. **不声称逐位可重复到永远。** 连跑两次逐位对比，341 位**零差异**；但更早的一次有 3 位结论不同（都属 `mirror_*` / `wf_*` 这类依赖前置状态与落盘的位）。所以对这类位，本报告只声称「当次读数」，不声称是常量。
5. 复现命令：`py -3.14 accept_v2.py --jobs 10 --timeout 90 --out acceptance_v2`。数字会随机器与网络浮动，结构不会。

