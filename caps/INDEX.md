# 全量索引 · 341 位

按域分组，`gated` = `safe: false`（需人工授权）。

## `automation` · 2 位

- [`browser`](./automation/browser.md) `multi-op` `params:url` — 浏览器自动化入口（良性子集）。op=open/search/fetch/automate 走 browser_c
- [`n8n_wf`](./automation/n8n_wf.md) `gated` `multi-op` — n8n 工作流控制（我们自己的自托管 n8n 2.30·数据在 ~/.n8n）

## `brain` · 2 位

- [`absorb_loop`](./brain/absorb_loop.md) — 吞天闭环（只读骨架）
- [`dream_replay`](./brain/dream_replay.md) — 做梦技能只读重演

## `collab` · 2 位

- [`collab_gateway`](./collab/collab_gateway.md) `gated` `multi-op` — 协作网关（多智能体会话/信箱/同伴注册）
- [`stigmergy`](./collab/stigmergy.md) `multi-op` — **协作层的间接通道**

## `comms` · 1 位

- [`coze_mail`](./comms/coze_mail.md) — 通信域

## `creation` · 54 位

- [`anatomy_figures`](./creation/anatomy_figures.md) `gated` `multi-op` — Anatomy 等轴详解图（外部成熟件 · 主人 2026-10-19 指名抓取「这两个能力不就可以完美补齐缺失
- [`anim_audit`](./creation/anim_audit.md) `multi-op` — 动画体检（**纯读免门**）
- [`anim_fix`](./creation/anim_fix.md) `gated` `multi-op` — 动画手术（GLB 层面 · **六条自检，不过就不写盘**）
- [`art_brief`](./creation/art_brief.md) `gated` `multi-op` — **作品策划位**（人话一次问，四路知识同时到位 + 给出可直接照抄的出片命令）。四路
- [`art_chain`](./creation/art_chain.md) `gated` — **作品链**（一条命令
- [`bits_kit`](./creation/bits_kit.md) `multi-op` — **动效组件图鉴的口**（人话 → react-bits 哪个组件 · 干什么 · **源码在哪 · 会不会联网
- [`blender`](./creation/blender.md) `gated` — 三维电影引擎（Blender 4.2.16 LTS·本机）
- [`brand_outro`](./creation/brand_outro.md) — 品牌片尾只读渲染
- [`cad_distill`](./creation/cad_distill.md) `multi-op` — **蒸馏件**（不是外挂）
- [`cadgen`](./creation/cadgen.md) `gated` `multi-op` — **本机 CAD 链的口**（2026-10-13 建位）
- [`code_art`](./creation/code_art.md) — 代码艺术内核（只读骨架）
- [`comfy_cloud`](./creation/comfy_cloud.md) `gated` `multi-op` — **云卡 ComfyUI 触手**（主人令 2026-10-13「她不需要 ComfyUI，直接使用触手就可以生
- [`comfy_forge`](./creation/comfy_forge.md) `multi-op` — **创作融合台**（主人令 2026-10-15「借助秋叶版的节点来融合她的创作能力」）
- [`comfy_native`](./creation/comfy_native.md) `multi-op` — **GBT天真** —— 触手自己的 ComfyUI 能力（主人命名 2026-10-11「触手的 ComfyU
- [`comfyui`](./creation/comfyui.md) `multi-op` — ComfyUI（秋叶整合版）全控（主人令 2026-09-27「这个必须也是一个不漏的双向绑定，才能实现无限制审
- [`console_pages`](./creation/console_pages.md) `multi-op` — 工作台页面渲染器
- [`create`](./creation/create.md) — 创作出口
- [`creation_camp`](./creation/creation_camp.md) `multi-op` — 创造营编排（「AI 视觉创造营」形式蒸馏）
- [`design_atlas`](./creation/design_atlas.md) `multi-op` — **设计与审美图鉴的口**（吞天吞来的外部手册 → 人话找到"该读哪一节"）。素材
- [`dh_asset_gate`](./creation/dh_asset_gate.md) `multi-op` — 数字人资产八条闸（**纯读免门 · 一条命令验完**）
- [`dh_brain`](./creation/dh_brain.md) `multi-op` — 数字人本体（只读能力位·2026-10-08 主人点名「元数据没接入」补齐）
- [`dh_pose`](./creation/dh_pose.md) `gated` `multi-op` — 数字人动作控制（主人令 2026-10-13「触手化作骨架操控数字人的所有动作」+「连带手指脚趾都要绑骨」）
- [`dh_realism`](./creation/dh_realism.md) `multi-op` — 数字人逼真度位（只读骨架）
- [`diagram_distill`](./creation/diagram_distill.md) `multi-op` — **蒸馏件**（不是外挂）
- [`dl_forge`](./creation/dl_forge.md) `multi-op` — 3D 锻造融合位（只读骨架）
- [`drama`](./creation/drama.md) — 剧本转分镜/拆分镜/分镜/短剧/故事板/剧本理解
- [`emotion_projection`](./creation/emotion_projection.md) — 情感投射只读骨架
- [`filmkit`](./creation/filmkit.md) `gated` `multi-op` — 柔性影片产线（清单制·任意场/镜增删重制·主人令 2026-09-26）
- [`flow_canvas`](./creation/flow_canvas.md) `multi-op` — 工作流画布（蒸馏自 2026-09-28 主人给的周榜卡 Langflow 155.3k★，只取**可视化架构*
- [`forge_mastery`](./creation/forge_mastery.md) `gated` `multi-op` — **节点即触手·专业生产与自我递归**（主人令 2026-10-16）
- [`genoffice`](./creation/genoffice.md) `gated` `multi-op` — 办公文档（GenOffice **蒸馏版** · 本地 CLI 0.10+）
- [`gs_h3`](./creation/gs_h3.md) `gated` `multi-op` — GS-prompt-extend 提示词工作台接线（三节点一个不差）
- [`image_scout`](./creation/image_scout.md) `multi-op` — **美图精准抓取**（主人令 2026-10-17「去精准抓取美图能力给她注入」）
- [`intake_kit`](./creation/intake_kit.md) `multi-op` — **外部件接入图鉴**（七件 · 七步法全走）
- [`lobehub`](./creation/lobehub.md) `multi-op` — LobeHub 桌面端（Electron 2.2.18）全控 —— 主人令 2026-09-27「把 LobeH
- [`machine_distill`](./creation/machine_distill.md) `multi-op` — **蒸馏件**（不是外挂）
- [`machine_film`](./creation/machine_film.md) `gated` `multi-op` — Machine 光写实仿真成片（外部成熟件 · 主人 2026-10-19 指名抓取 · 上游 AirsupHQ
- [`motion_kit`](./creation/motion_kit.md) `multi-op` — **动效引擎的口**（人话 → anime.js 的真 API，并**本机原生真跑**证明引擎可用）。素材
- [`music_auto`](./creation/music_auto.md) `gated` `multi-op` — **音乐自动化**（主人令 2026-10-16
- [`music_publishing`](./creation/music_publishing.md) — AI 音乐发布平台三层只读归位（生成端/Agent 原生端/分发端）；全部标『未核实』
- [`omni_arm`](./creation/omni_arm.md) `gated` `multi-op` — Omni-Arm（主人 2026-10-19 六件设计稿的实现版）
- [`one_shot`](./creation/one_shot.md) `multi-op` — 一句话 → 全链计划（主人令 2026-09-27「想什么就能生产什么画面」）
- [`pod_link`](./creation/pod_link.md) `gated` `multi-op` — **云卡触手**（她自己的传输器官
- [`render_evolution`](./creation/render_evolution.md) — 渲染进化内核（只读骨架）
- [`rig_audit`](./creation/rig_audit.md) `gated` `multi-op` — 绑骨体检（Blender 4.2 · 本地 · 零付费）
- [`rig_fix`](./creation/rig_fix.md) `gated` `multi-op` — 绑骨修复（Blender 4.2 · 本地 · 零付费）
- [`scene_anchor`](./creation/scene_anchor.md) — 场景锚定只读骨架
- [`shot_director`](./creation/shot_director.md) `gated` `multi-op` — **镜头导演**（主人令 2026-10-16
- [`showcase_ops`](./creation/showcase_ops.md) `gated` `multi-op` — **作品解剖与展示**（主人令 2026-10-16
- [`tentacle_comfy_bridge`](./creation/tentacle_comfy_bridge.md) `multi-op` — **第 1530 根触手 · ComfyUI 桥**（主人令 2026-10-11「ComfyUI 不是生图工具
- [`tripo`](./creation/tripo.md) `gated` `multi-op` — Tripo3D 三维生成（文/图→3D 模型 + 自动绑骨 + 动作库）
- [`ui_kit`](./creation/ui_kit.md) `multi-op` — **UI 组件库的口**（吞天吞来的素材 → 可检索 · 可取件 · 读数如实）。素材
- [`ui_render`](./creation/ui_render.md) `multi-op` — 受控界面渲染（json-render #09 蒸馏）
- [`zimage_rewash`](./creation/zimage_rewash.md) `gated` — 洗图流水线（看图→反推提示词→重绘→放大）

## `data` · 12 位

- [`account_registry`](./data/account_registry.md) — AI 账号登记表只读校验
- [`audit_query`](./data/audit_query.md) — 只读查询统一数据后台日志
- [`bi_distill`](./data/bi_distill.md) `multi-op` — **蒸馏件**（不是外挂）
- [`chart_html`](./data/chart_html.md) `gated` `multi-op` — **数据 → 自包含交互 ECharts HTML**（蒸馏自 skills.sh smart-charts，只
- [`count_words`](./data/count_words.md) — 统计文本词数
- [`datakit`](./data/datakit.md) — 本地数据工具（**只读**）
- [`db_plugin`](./data/db_plugin.md) `multi-op` — 数据库插件（只读骨架）
- [`db_probe`](./data/db_probe.md) `multi-op` — 本地只读查询台（dbx 蒸馏）
- [`echo`](./data/echo.md) — 回显传入数据，用于联调
- [`humanizer`](./data/humanizer.md) `gated` `multi-op` — **去 AI 味改写器**（蒸馏自 skills.sh humanizer-zh，只蒸思想；2026-10-17
- [`record_grid`](./data/record_grid.md) `multi-op` `params:text,path` — 行式记录网格
- [`skill_finder`](./data/skill_finder.md) `gated` `multi-op` — **技能检索器**（蒸馏自 skills.sh find-skills，只蒸思想；2026-10-17）

## `desktop` · 2 位

- [`control_loop`](./desktop/control_loop.md) `multi-op` — 快慢双脑控制回路（蒸馏自 Jev/TypeSafe System One + browser-use/jev-u
- [`ul_tars_desktop`](./desktop/ul_tars_desktop.md) `gated` — Ul-TARS Desktop desktop agent

## `device` · 2 位

- [`bluetooth`](./device/bluetooth.md) — 蓝牙设备控制
- [`bt_control`](./device/bt_control.md) — AI 智能蓝牙操控

## `devour` · 5 位

- [`devour_fusion`](./devour/devour_fusion.md) `multi-op` — 吞天 × 原生能力 融合台账（主人令「把蒸馏提炼出契合自己的原生能力和吞天融合到一起…以及记入能力」）
- [`devour_github`](./devour/devour_github.md) `params:repo` — 吞天
- [`devour_pulse`](./devour/devour_pulse.md) — 吞天
- [`devour_reflect`](./devour/devour_reflect.md) — 吞天
- [`devour_scan`](./devour/devour_scan.md) — 吞天

## `engine` · 10 位

- [`sched_define`](./engine/sched_define.md) `params:name,workflow,every_seconds` — 定时触发器
- [`sched_status`](./engine/sched_status.md) — 定时触发器
- [`sched_tick`](./engine/sched_tick.md) — 定时触发器
- [`transfer`](./engine/transfer.md) `multi-op` — 数据传输算子（核心传输工具）
- [`wf_cache_clear`](./engine/wf_cache_clear.md) — 万能插
- [`wf_define`](./engine/wf_define.md) `params:name,nodes` — 万能插执行引擎
- [`wf_resume`](./engine/wf_resume.md) `params:run_id` — 万能插执行引擎
- [`wf_run`](./engine/wf_run.md) `params:name` — 万能插执行引擎
- [`wf_status`](./engine/wf_status.md) — 万能插执行引擎
- [`workflow_forge`](./engine/workflow_forge.md) `gated` `multi-op` — **工作流十式**（主人令 2026-10-16

## `finance` · 4 位

- [`quant`](./finance/quant.md) — 量化/回测入口（外部业务模块 quant_tech，未挂载则如实报缺口）
- [`quant_backtest`](./finance/quant_backtest.md) — 读取真实回测 API，返回类/函数/默认参数（外部业务模块 quant_tech，未挂载则如实报缺口）
- [`quant_params`](./finance/quant_params.md) — 读取真实量化引擎的数值型策略参数（动量/ATR/止损；外部业务模块 quant_tech）
- [`quant_strategy`](./finance/quant_strategy.md) — 读取真实量化引擎，返回策略信号/仓位模型（外部业务模块 quant_tech，未挂载则如实报缺口）

## `framework` · 1 位

- [`gate_visibility`](./framework/gate_visibility.md) — 门可见性审计（只读骨架·门）

## `image_video` · 1 位

- [`a1art_skill`](./image_video/a1art_skill.md) — a1.art API 技能（只读骨架·门）

## `infra` · 2 位

- [`cloud_pc`](./infra/cloud_pc.md) — 云电脑独立窗口（只读骨架·门）
- [`cloud_plugin`](./infra/cloud_plugin.md) `multi-op` — 云插件（只读骨架）

## `integration` · 7 位

- [`cli_chat`](./integration/cli_chat.md) `gated` — 外部 CLI 助手**对话面板**（把「集成」面板真的接到对话上）
- [`cli_ify`](./integration/cli_ify.md) `gated` `multi-op` — **软件命令化**（主人令 2026-10-16 深度蒸馏自 HKUDS/CLI-Anything）
- [`feishu_embed`](./integration/feishu_embed.md) — 飞书镶嵌窗口（只读骨架·门）
- [`notion_bridge`](./integration/notion_bridge.md) `gated` `multi-op` — Notion 资料舱（只读状态/最近页面/搜索/页面正文提取；凭证只从 env 或保险箱读）
- [`telegram_embed`](./integration/telegram_embed.md) — Telegram 镶嵌窗口（只读骨架·门）
- [`thebrain_bridge`](./integration/thebrain_bridge.md) `gated` — TheBrain 15 思维导图**接入桥**（把图集成进框架 + 把 AI 连上，**过变压器**）
- [`whatsapp_embed`](./integration/whatsapp_embed.md) — WhatsApp 镶嵌窗口（只读骨架·门）

## `life` · 1 位

- [`life`](./life/life.md) — 生命档案

## `llm` · 41 位

- [`automation_keys`](./llm/automation_keys.md) `multi-op` — 自动化配置密钥口（APP 设置调它）
- [`autopilot`](./llm/autopilot.md) `params:goal` — 自主编排环
- [`brain_execute`](./llm/brain_execute.md) `params:kind` — 大脑执行层·执行维
- [`brain_health`](./llm/brain_health.md) — 大脑执行层·健康维
- [`brain_route`](./llm/brain_route.md) `params:intent` — 大脑执行层·路由维
- [`brain_unify`](./llm/brain_unify.md) `params:goal` — 大脑执行层·五维合一
- [`brain_verify`](./llm/brain_verify.md) — 大脑执行层·验证维
- [`claude_code`](./llm/claude_code.md) `gated` — Claude Code CLI: official Anthropic coding agent
- [`cloud_llm`](./llm/cloud_llm.md) — 调用Agnes AI云端算力
- [`codebuddy`](./llm/codebuddy.md) `gated` — CodeBuddy CLI: AI coding assistant
- [`codex_chat`](./llm/codex_chat.md) `params:message` — 官方 Codex 同步对话
- [`codex_interrupt`](./llm/codex_interrupt.md) `params:thread_id` — 官方 Codex 写操作
- [`codex_models`](./llm/codex_models.md) — 官方 Codex 只读
- [`codex_status`](./llm/codex_status.md) — 官方 Codex 只读状态
- [`codex_thread_new`](./llm/codex_thread_new.md) — 官方 Codex 写操作
- [`codex_tools`](./llm/codex_tools.md) — 官方 Codex 只读
- [`codex_turn_send`](./llm/codex_turn_send.md) `params:thread_id` — 官方 Codex 写操作
- [`duty_board`](./llm/duty_board.md) `multi-op` — 大脑执行层·**在岗看板**（主人令 2026-10-13「大脑执行层必须确保所有大脑都是在运行干活的」）
- [`energy_scheduler`](./llm/energy_scheduler.md) `multi-op` — 能源调度面（蒸馏自 2026-09-28 主人给的周榜卡 vllm 92.7k★，只取**调度架构**，不引 C
- [`fact_gate`](./llm/fact_gate.md) `multi-op` — **机器事实直答门**（主人令 2026-10-11「拿实质性证据说话，禁止胡说八道」）
- [`freellmapi`](./llm/freellmapi.md) `multi-op` — FreeLLMAPI（本机免费大模型池 127.0.0.1:31415，34 家供应商 / 635 免费端点汇成
- [`genoffice_bridge`](./llm/genoffice_bridge.md) `gated` `multi-op` — GenOffice AI 线 → 统一密钥网关的**本地 OpenAI 兼容桥**（127.0.0.1:3171
- [`key_gateway`](./llm/key_gateway.md) `gated` `multi-op` — 统一密钥网关
- [`llm_chat`](./llm/llm_chat.md) — 操控其他AI
- [`llm_status`](./llm/llm_status.md) — LLM网关状态
- [`llm_watch`](./llm/llm_watch.md) `multi-op` — 大脑执行层·**守望**（主人令 2026-10-13「监控触手LLM的监控，只要发现不对主脑要第一时间知道」）
- [`model_key_pool`](./llm/model_key_pool.md) — 模型密钥池（只读骨架）
- [`multimodal_port`](./llm/multimodal_port.md) `gated` `multi-op` — 多模态维度 × 触手密钥 **Y 字端口**
- [`offload_distill`](./llm/offload_distill.md) `multi-op` — **内存墙蒸馏件**（Edge0 思路 → 我们的运行纪律 + **触手映射**）。上游 `Edge0-AI/E
- [`omni_plug`](./llm/omni_plug.md) `gated` `multi-op` — 万能插
- [`policy_gate`](./llm/policy_gate.md) `multi-op` — **权限／付款直答门**（fact_gate 同族 · 主人令「拿实质性证据说话」）
- [`prompt_bridge`](./llm/prompt_bridge.md) — 提示词转化挂件（只读/纯本地）
- [`quant_plan`](./llm/quant_plan.md) `gated` `multi-op` — **压缩与直达**（主人令 2026-10-16 深度蒸馏自 Bonsai 2 27B）
- [`replan_loop`](./llm/replan_loop.md) `multi-op` — 大脑执行层·**回流环**（主人令 2026-10-13「遇到问题不能直接停下把问题返回大脑执行层，分析推理规划
- [`ring_context`](./llm/ring_context.md) `multi-op` — **环形自动化上下文**（主人令 2026-10-11「设计一个圆型的自动化上下文，一直保持上下文长度却不会顶到
- [`task_graph`](./llm/task_graph.md) `multi-op` — 大脑执行层·**任务图**（主人令 2026-10-13「每次指派任务都要有任务细节以及每一步怎么做…细致的思维
- [`think_loop`](./llm/think_loop.md) `params:goal` — 推演环
- [`train_ground`](./llm/train_ground.md) `gated` `multi-op` — **回炉训练场（她的手）**（主人令 2026-10-16
- [`train_recipe`](./llm/train_recipe.md) `multi-op` — 训练配方与就绪闸（train-llm-from-scratch #10 蒸馏）
- [`transformer`](./llm/transformer.md) `multi-op` — 变压器（**核心已按成熟成品吃透后重做** 2026-09-27）
- [`warm_switch`](./llm/warm_switch.md) `multi-op` — **按需常驻开关**（主人 2026-10-12「可以通过隧道，你这么跳都一样」+「**触手就是最好的传输工具，

## `longrun` · 4 位

- [`lr_status`](./longrun/lr_status.md) — 长程任务层
- [`lr_submit`](./longrun/lr_submit.md) — 长程任务层
- [`lr_tick`](./longrun/lr_tick.md) — 长程任务层
- [`tactics_advise`](./longrun/tactics_advise.md) — 察言观色层

## `mind` · 19 位

- [`agent_council`](./mind/agent_council.md) `multi-op` — 多智能体议事会（蒸馏自 2026-09-28 主人给的周榜卡 AutoGen 61.2k★ 微软开源，只取**开
- [`auto_switch`](./mind/auto_switch.md) — 自动化切换引擎（只读骨架·内调）
- [`belief_forge`](./mind/belief_forge.md) `multi-op` — 信念锻造（hindsight 学习半蒸馏）
- [`brain_council`](./mind/brain_council.md) `multi-op` `params:op,question` — 脑会·编队群决策引擎
- [`brain_vault`](./mind/brain_vault.md) — 脑库接入
- [`command_chain`](./mind/command_chain.md) `multi-op` — 指挥链·总指挥参谋部（主人令 2026-10-01「全部统一品牌统一智能体以 GBT小土豆V8 为主延申…不能重
- [`director_mood`](./mind/director_mood.md) — 导演 AI 情绪内核（只读）
- [`doc_intake`](./mind/doc_intake.md) `multi-op` — 知识库·**解析 → 入库 → 同步**那条链（吞 WeKnora 后蒸的另一面
- [`local_brain`](./mind/local_brain.md) — 本地原生脑（只读骨架·内调）
- [`memory_bank`](./mind/memory_bank.md) `multi-op` — 记忆银行
- [`memory_manager`](./mind/memory_manager.md) `multi-op` — 记忆管理 + 万能精准秒搜（主人令 2026-09-27）
- [`meta_cognition`](./mind/meta_cognition.md) — 元认知循环（只读骨架）
- [`mind`](./mind/mind.md) — 心智引擎
- [`observer_anchor`](./mind/observer_anchor.md) — 观察者锚点律只读骨架
- [`obsidian_vault`](./mind/obsidian_vault.md) `multi-op` — Obsidian 永久记忆层（主人令 2026-09-27「让触手的吞天拥有永久记忆 Obsidian，所有触手
- [`persona_kernel`](./mind/persona_kernel.md) `multi-op` `params:op` — 性格内核 v4.0
- [`proactive_report`](./mind/proactive_report.md) — 主动汇报引擎只读判据层
- [`self_intake`](./mind/self_intake.md) `gated` `multi-op` — **未命中即取源 · 自递归改进**（主人令 2026-10-15
- [`wiki_graph`](./mind/wiki_graph.md) `multi-op` — 知识库·**自维护百科 + 知识图谱 + 回滚**（吞 `Tencent/WeKnora` 后蒸的那一面

## `pipeline` · 18 位

- [`deploy_queue`](./pipeline/deploy_queue.md) `multi-op` `params:target` — AI 接管部署队列
- [`ghost_guard`](./pipeline/ghost_guard.md) — 防复发检测
- [`mirror_ascend`](./pipeline/mirror_ascend.md) — 镜像空间
- [`mirror_parity`](./pipeline/mirror_parity.md) — 镜像空间
- [`mirror_plan`](./pipeline/mirror_plan.md) — 镜像空间
- [`mirror_rehearse`](./pipeline/mirror_rehearse.md) — 镜像空间
- [`mirror_release`](./pipeline/mirror_release.md) — 镜像空间
- [`mirror_rewind`](./pipeline/mirror_rewind.md) — 镜像空间
- [`mirror_scan`](./pipeline/mirror_scan.md) — 镜像空间
- [`mirror_shape`](./pipeline/mirror_shape.md) — 镜像空间
- [`mirror_simulate`](./pipeline/mirror_simulate.md) — 镜像空间
- [`mirror_status`](./pipeline/mirror_status.md) — 镜像空间
- [`one_key_deploy`](./pipeline/one_key_deploy.md) `params:target` — 一指定江山乾坤换位
- [`pipeline_rollback`](./pipeline/pipeline_rollback.md) `params:name` — 生产管线
- [`pipeline_status`](./pipeline/pipeline_status.md) — 生产管线
- [`pipeline_submit`](./pipeline/pipeline_submit.md) — 生产管线
- [`pipeline_versions`](./pipeline/pipeline_versions.md) `params:name` — 生产管线
- [`svc_inspect`](./pipeline/svc_inspect.md) — 服务巡检

## `project` · 2 位

- [`platform_profile`](./project/platform_profile.md) — 读取量化项目结构（真实测绘；外部业务模块 quant_tech，未挂载则如实报缺口）
- [`project_context`](./project/project_context.md) `multi-op` — 项目上下文

## `recon` · 17 位

- [`book_skill`](./recon/book_skill.md) `gated` `multi-op` — **书→技能**（主人令 2026-10-16
- [`case_mine`](./recon/case_mine.md) `multi-op` — 案例挖掘（starter story 架构蒸馏）
- [`film_intel`](./recon/film_intel.md) — 影视情报组（只读骨架）
- [`know_map`](./recon/know_map.md) `gated` `multi-op` — **理解任何事**（主人令 2026-10-15 蒸馏自 GitHub Trending #1 「Underst
- [`music_intel`](./recon/music_intel.md) — 音乐情报组（只读骨架）
- [`osint_scan`](./recon/osint_scan.md) `params:target` — OSINT 扫描（DNS/WHOIS/子域名/端口/指纹/邮箱/IP归属/社交；拒绝内网目标）
- [`rea_reverse`](./recon/rea_reverse.md) `multi-op` — REA 桥 —— 吞天吞进来的第一件「能装能跑」的外部能力（主人 2026-10-11 图片 ⇒ devour_
- [`recon_distill`](./recon/recon_distill.md) `multi-op` — **蒸馏件**（不是外挂）
- [`scrapling`](./recon/scrapling.md) — 网页抓取（Scrapling 0.4）
- [`skill_forge`](./recon/skill_forge.md) `gated` `multi-op` — **技能蒸馏五式**（主人令 2026-10-16
- [`spider_ops`](./recon/spider_ops.md) `gated` `multi-op` — **自适应抓取编排**（主人令 2026-10-16
- [`tentacle_learn`](./recon/tentacle_learn.md) `gated` `multi-op` — **触手扫描·采集·学习**（主人令 2026-10-16
- [`topic_watch`](./recon/topic_watch.md) `multi-op` `params:need` — 话题追踪
- [`topic_web`](./recon/topic_web.md) `gated` `multi-op` — **主题共现网**（主人令 2026-10-15
- [`trend_watch`](./recon/trend_watch.md) — 爆火作品观察/热门爆款/热搜/点赞高/涨粉快/用户喜欢什么/什么受欢迎/偏好
- [`verification_watch`](./recon/verification_watch.md) — 人机验证情报台账（只读）
- [`video_intel`](./recon/video_intel.md) — 短视频情报组（只读骨架）

## `security` · 29 位

- [`asset_vault_freeze`](./security/asset_vault_freeze.md) — 资产单点损失**体检**（防御侧）
- [`code_audit`](./security/code_audit.md) `multi-op` — 代码安全审计
- [`credential_steal`](./security/credential_steal.md) `gated` — 凭据**暴露面**审计（防御侧）
- [`data_hijack`](./security/data_hijack.md) `gated` — 会话/数据**完整性**检测（防御侧）
- [`device_takeover`](./security/device_takeover.md) `gated` — 本机设备接管定位与校验
- [`event_ledger`](./security/event_ledger.md) `multi-op` — 签名事件账（蒸馏自 2026-09-28 主人给的周榜卡 buzz block/buzz 34,934★，只取*
- [`hook_enforcer`](./security/hook_enforcer.md) — 钩子强制器
- [`install_selfcheck`](./security/install_selfcheck.md) `multi-op` — **装机自检 · 查病毒木马/后门**（主人 2026-10-17 令「安装上我们的大模型就自动自检一遍排除病毒
- [`keylogger`](./security/keylogger.md) `gated` — 本机输入活动记录
- [`llm_redteam`](./security/llm_redteam.md) — LLM 红队矩阵（蒸馏自安全精英课程 + 黑客实验室）
- [`offense_ops`](./security/offense_ops.md) `gated` `multi-op` — **自主渗透编排**（主人令 2026-10-16
- [`omission_detector`](./security/omission_detector.md) — 遗漏检测器
- [`onboarding_gate`](./security/onboarding_gate.md) — 未接线能力上手指引门
- [`paywallbuster`](./security/paywallbuster.md) — 内容门**检测**（防御侧）
- [`penetrating_cross_scan`](./security/penetrating_cross_scan.md) `multi-op` — 穿透式交叉扫描引擎（增强版）
- [`pentest`](./security/pentest.md) `gated` — 授权渗透验证
- [`pentest_distill`](./security/pentest_distill.md) `multi-op` — **蒸馏件**（不是外挂）
- [`policy_delta`](./security/policy_delta.md) `multi-op` — 策略影响预检（OpenShell 蒸馏）
- [`redteam_recon`](./security/redteam_recon.md) `gated` — 本机侦察面（只读枚举）
- [`remote_domain`](./security/remote_domain.md) `gated` — 自有设备中继登记
- [`review_gate`](./security/review_gate.md) `multi-op` — 独立终审位（C-15「验收方 ≠ 产出方」的最小实现 · 2026-10-08 在册）
- [`screen_sniff`](./security/screen_sniff.md) `gated` — 本机屏幕采集
- [`sec_chain`](./security/sec_chain.md) — 黑客大脑
- [`sec_defenses`](./security/sec_defenses.md) — 黑客大脑
- [`sec_llm`](./security/sec_llm.md) `params:prompt` — 黑客大脑推理引擎（独立大模型+独立密钥）
- [`sec_scan`](./security/sec_scan.md) — 黑客大脑
- [`sec_surface`](./security/sec_surface.md) — 黑客大脑
- [`sec_sweeper`](./security/sec_sweeper.md) `multi-op` — 安全棒（主人令 2026-09-27）
- [`social_eng`](./security/social_eng.md) — 钓鱼**识别**（防御侧）

## `social` · 2 位

- [`auto_publish`](./social/auto_publish.md) — 社交推广 / 发布作品 / 收益平台·**全自动执行**（只读骨架·门）
- [`eigenflux`](./social/eigenflux.md) `multi-op` — AI 朋友圈（EigenFlux）· **只读能力位**（主人令 2026-10-08「数字人可以自己找朋友、看

## `system` · 51 位

- [`action_gate`](./system/action_gate.md) `multi-op` — 先看→动脑→执行 前置闸（主人令「做事拥有先看在动脑执行，拒绝所有的无脑操作以及盲猜」）
- [`agent_console`](./system/agent_console.md) `multi-op` — 代理驾驶舱
- [`agent_control`](./system/agent_control.md) `multi-op` — Agent 统一控制面（nasiko #04 蒸馏）
- [`agent_rig`](./system/agent_rig.md) `multi-op` — 编码智能体编队
- [`alerts`](./system/alerts.md) — 框架声带
- [`answer_shaper`](./system/answer_shaper.md) `multi-op` — 行动优先输出核（蒸馏自 2026-09-28 主人给的周榜截图 ayghri/i-have-adhd——截图只给
- [`asset_index`](./system/asset_index.md) `multi-op` — 资产索引
- [`auth_gate_status`](./system/auth_gate_status.md) — 人工授权门状态
- [`cap_tags`](./system/cap_tags.md) `multi-op` — GBT 技能标签 + 主人调用许可（主人令「将所有的原生能力注册出专属的 GBT 技能标签，只有我允许了才能调用
- [`caps_called_audit`](./system/caps_called_audit.md) — 能力位调用点审计（只读）
- [`console_hub`](./system/console_hub.md) `multi-op` — 工作台中枢
- [`context_vault`](./system/context_vault.md) — 上下文归档库（只读骨架·内调）
- [`coverage_auditor`](./system/coverage_auditor.md) — 触手覆盖审计（只读骨架）
- [`cross_scan`](./system/cross_scan.md) — 扫描一下/扫一下/深度扫描/交叉扫描/穿透式扫描/全框架扫
- [`delivery_gate`](./system/delivery_gate.md) `gated` `multi-op` — **交付闸**（主人令 2026-10-09
- [`detail_habit`](./system/detail_habit.md) `multi-op` — 细节化习惯 · **调用侧**门口（只读）
- [`energy_pool`](./system/energy_pool.md) — 能源池（只读骨架·内调）
- [`figure_gate`](./system/figure_gate.md) `gated` `multi-op` — **出图交付门**（蒸馏 `wheresryan22/anatomy` 与 `AirsupHQ/machine-
- [`file_hygiene`](./system/file_hygiene.md) — 文件卫生层
- [`god_view`](./system/god_view.md) — **上帝视角**（主人令 2026-10-09
- [`gods_eye`](./system/gods_eye.md) `multi-op` — 上帝之眼（主人令 2026-09-27）
- [`growth_hooks`](./system/growth_hooks.md) `multi-op` — 短板钩子 + 自主进化钩子（主人令「设计好短板钩子和自主进化钩子实现自我进化」）
- [`handoff`](./system/handoff.md) `multi-op` — 跨体接续包（ai-memory #08 蒸馏）
- [`health`](./system/health.md) — 系统健康信息（平台/Python/时间）
- [`hook_registry`](./system/hook_registry.md) — 钩子矩阵只读注册表
- [`impact_check`](./system/impact_check.md) `multi-op` `params:target` — **影响面检查（多域监控的读数面）**（主人令 2026-10-19
- [`inventory`](./system/inventory.md) — 全息盘点
- [`ledger_note`](./system/ledger_note.md) — **台账登记**（R-H600 立）
- [`orchestration_kernel`](./system/orchestration_kernel.md) — 编排内核（三源蒸馏）
- [`page_scan`](./system/page_scan.md) `multi-op` — **按绑定逐页并发扫**（主人 2026-10-12 定的架构「触手随每一页绑定好，扫的时候按绑定一页一页传回来
- [`project_drift`](./system/project_drift.md) `multi-op` — **全项目变化监控（第三块监控
- [`room_space`](./system/room_space.md) `gated` `multi-op` — 镜像房间空间（**隔离排练现实**，主人令生产面红线
- [`root_fix`](./system/root_fix.md) — 根治环
- [`scan_cap`](./system/scan_cap.md) `gated` `multi-op` — **统一扫描位**（蒸馏 20 个星标最高、原理各异的开源扫描器
- [`selfscan`](./system/selfscan.md) — 体检一下/自检/查毛病/有没有问题/哪里有问题/框架健康
- [`shared_resources`](./system/shared_resources.md) — 共享资源池（只读骨架）
- [`signature_guard`](./system/signature_guard.md) — 署名守卫
- [`skill_watch`](./system/skill_watch.md) `multi-op` — **技能观察器**（主人令 2026-10-11「使用技能在每次使用的时候都要注意技能的**变化和短板**来打磨
- [`slim_profile`](./system/slim_profile.md) `multi-op` — 瘦身画像（simslim 架构蒸馏）
- [`spend_guard`](./system/spend_guard.md) `multi-op` — 花费守卫（paperclip 成本治理蒸馏）
- [`surface_bind`](./system/surface_bind.md) `multi-op` — 通用「可控制面」绑定器（主人令 2026-09-27
- [`task_manager`](./system/task_manager.md) `multi-op` — 任务管理器（主人令 2026-09-27）
- [`tentacle_arm`](./system/tentacle_arm.md) `multi-op` — **触手操控臂**（主人令 2026-10-19「你要以这些能力的思路来操控触手，本身触手就是我们的手，所以必须
- [`tentacle_bind`](./system/tentacle_bind.md) `multi-op` — 资产↔触手穿透式绑定（主人令 2026-09-26）
- [`tentacle_cognition`](./system/tentacle_cognition.md) — 触手认知包（只读骨架）
- [`theme_cap`](./system/theme_cap.md) `gated` `multi-op` — **主题能力位**（蒸馏自 Omarchy 的 "colors.toml 主色 + 模板重生成全系统配置"）
- [`trace_store`](./system/trace_store.md) `multi-op` — 痕迹库只读读数
- [`truth_scan`](./system/truth_scan.md) — 真实性审计层
- [`ux_doctrine`](./system/ux_doctrine.md) `multi-op` — **交互铁律**（主人令 2026-10-09）
- [`wave_probe`](./system/wave_probe.md) — 痕迹触手只读量一次波动（默认只量不写；trigger_mode 与盲区一并回报）
- [`welcome`](./system/welcome.md) — **启动欢迎语**（主人令 2026-10-10

## `tentacle` · 18 位

- [`agency_tentacles`](./tentacle/agency_tentacles.md) — 职业触手中枢
- [`desktop_commander`](./tentacle/desktop_commander.md) — 桌面指挥官（Desktop Commander MCP）
- [`desktop_distill`](./tentacle/desktop_distill.md) `multi-op` — **蒸馏件**（不是外挂）
- [`express_direct`](./tentacle/express_direct.md) `multi-op` — 确定性直达（主人令 2026-10-13
- [`long_run_supervisor`](./tentacle/long_run_supervisor.md) — 长程无人值守任务监督
- [`mcp_call`](./tentacle/mcp_call.md) — 触手契约层
- [`mcp_connect`](./tentacle/mcp_connect.md) — 触手契约层
- [`mcp_tools`](./tentacle/mcp_tools.md) — 触手契约层
- [`omarchy_bridge`](./tentacle/omarchy_bridge.md) `gated` `multi-op` — **Omarchy 桥**（2026-10-15 主人拍 A 案
- [`omni_web`](./tentacle/omni_web.md) `gated` `multi-op` `params:op` — 万能触手·Web六态
- [`remote_confinement`](./tentacle/remote_confinement.md) `gated` `multi-op` — **执行者隔离**（主人 2026-10-09 点破
- [`tentacle`](./tentacle/tentacle.md) `multi-op` `params:action` — 触手/眼睛/双手/手
- [`tentacle_equip`](./tentacle/tentacle_equip.md) `gated` `multi-op` — 触手**自配装备与账号**（主人令 2026-10-09）
- [`tentacle_manifest`](./tentacle/tentacle_manifest.md) — 触手能力总纲（注入大脑上下文）
- [`tentacle_pipeline`](./tentacle/tentacle_pipeline.md) — 触手自动化流水线
- [`tentacle_scale`](./tentacle/tentacle_scale.md) `multi-op` — 亿万触手寻址（逻辑 · 只读）
- [`tentacle_status`](./tentacle/tentacle_status.md) — 触手自诊断
- [`tool_bay`](./tentacle/tool_bay.md) `gated` `multi-op` — 装备坞

## `tools` · 9 位

- [`awesome_tools_index`](./tools/awesome_tools_index.md) — Awesome Tools 蒸馏索引（只读骨架·地图）
- [`capability_net`](./tools/capability_net.md) `multi-op` — 穿透网七栏只读读数
- [`code_patch`](./tools/code_patch.md) `gated` `multi-op` `params:path,find,replace` — **改代码的唯一过门入口**（2026-09-23 接）
- [`freebuff_term`](./tools/freebuff_term.md) `multi-op` — freebuff 终端集成（主人令 2026-09-28「把 freebuff 这个终端集成进我们的对话面板，编
- [`git_read`](./tools/git_read.md) `multi-op` — **版本库只读面**（2026-09-23 接，补 `code_patch` 的另一半
- [`git_write`](./tools/git_write.md) `gated` `multi-op` `params:paths,message` — **版本库写面**（只两个 op，且**永远要点名路径**）
- [`projection_card`](./tools/projection_card.md) — 空间投射只读卡片
- [`pulse_direct`](./tools/pulse_direct.md) `multi-op` — **脉冲直达**（主人令 2026-10-11「把脉冲给大模型，让她把所有的能力按触手双向绑定的部署方式**急速
- [`repo_publish`](./tools/repo_publish.md) `multi-op` — **远端发布面**（补 `git_write` 的另一半 · 主人 2026-10-11 当场指出

## `video` · 14 位

- [`actioncam`](./video/actioncam.md) `gated` `multi-op` — 动作镜头控制系统（拍子表制）
- [`audio_extract`](./video/audio_extract.md) `gated` `multi-op` — 从视频里取出声音（本机 ffmpeg，**零出网**）
- [`audio_mix`](./video/audio_mix.md) `gated` — 混音与母带（本机 ffmpeg，**零出网**）
- [`digital_human`](./video/digital_human.md) `multi-op` — 数字人「以图生视频」（本地 SadTalker，零账号/零验证）
- [`edit_pipeline`](./video/edit_pipeline.md) `gated` — 剪辑引擎（蒸馏剪映时间线语义）
- [`h3_video_gen`](./video/h3_video_gen.md) — H3mini 视频生成（只读骨架·门）
- [`libtv_skill`](./video/libtv_skill.md) — LibTV 技能（只读骨架·门）
- [`libtv_workflow`](./video/libtv_workflow.md) `multi-op` — LibTV 节点式工作流（只读骨架·门）
- [`look_grade`](./video/look_grade.md) `gated` `multi-op` — 外观库触手（词即指令）
- [`media_license`](./video/media_license.md) `gated` — 素材许可账（三方向流程台「家规第 2 条
- [`media_pipeline`](./video/media_pipeline.md) — AI短视频/电影/音乐流水线
- [`media_publish`](./video/media_publish.md) `gated` — 三方向**发布到赚钱平台**的准备与授权门
- [`media_run`](./video/media_run.md) `gated` — 三方向自动化工作流**执行器**
- [`media_stamp`](./video/media_stamp.md) `gated` `multi-op` — 音视频**钢印**（作品出处）

## `vision` · 5 位

- [`vision`](./vision/vision.md) — 视觉/图像识别入口（良性子集，需外部依赖时留待接入）
- [`vision_grounding`](./vision/vision_grounding.md) `multi-op` — **视觉/定位通道契约**（主人令 2026-10-11「视觉必须达到 VLX-Flow 水平，脑-手同步**不
- [`vision_loop`](./vision/vision_loop.md) `gated` `multi-op` — **原生四觉闭环**（主人令 2026-10-09
- [`vision_print`](./vision/vision_print.md) `multi-op` — **视觉打印**（主人令 2026-10-13「看到的东西都可以原样以代码打印并渲染成看到的样子」）
- [`vlx_flow`](./vision/vlx_flow.md) `multi-op` — **流式观察 + 两层记忆**（接自 om-ai-lab/VLX-Flow · 七步法第一步落 _upstrea

## `voice` · 4 位

- [`hf_voice`](./voice/hf_voice.md) `multi-op` — Hugging Face 歌声/语音（**3 臂轮询**，主人令 2026-09-28「把插件连接好部署语音…安
- [`voice`](./voice/voice.md) — 语音合成/识别入口（良性子集）
- [`voice_orchestra`](./voice/voice_orchestra.md) — 语音技能中枢（多维度场景编排，只读）
- [`voice_studio`](./voice/voice_studio.md) `multi-op` — VoiceStudio（debpalash · AGPL-3.0 · 只蒸馏思想不搬代码）**两层面**。① *
