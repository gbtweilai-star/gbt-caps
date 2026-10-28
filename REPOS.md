# The 341 repositories

Every capability bit in the registry has its own repository. One bit, one repo, one contract, one test suite — nothing bundled, nothing hidden.

Each repository is a zero-dependency Python package containing:/n/n- the contract, copied verbatim from the registry (`spec.py`), pinned by a drift test
- non-throwing validation (`check`) and a validate-then-execute `run()`
- a `Backend` protocol with a stub that reports `validated`, never `ok`
- a CLI (`info` / `spec` / `check` / `run`)
- a test suite that fails if the description drifts by a single character

**Total: 341 repositories across 30 domains.**

| # | capability | domain | repo | gated |
|---|---|---|---|---|
| 1 | `browser` | `automation` | [gbt-browser](https://github.com/gbtweilai-star/gbt-browser) |  |
| 2 | `n8n_wf` | `automation` | [gbt-n8n-wf](https://github.com/gbtweilai-star/gbt-n8n-wf) | yes |
| 3 | `absorb_loop` | `brain` | [gbt-absorb-loop](https://github.com/gbtweilai-star/gbt-absorb-loop) |  |
| 4 | `dream_replay` | `brain` | [gbt-dream-replay](https://github.com/gbtweilai-star/gbt-dream-replay) |  |
| 5 | `collab_gateway` | `collab` | [gbt-collab-gateway](https://github.com/gbtweilai-star/gbt-collab-gateway) | yes |
| 6 | `stigmergy` | `collab` | [gbt-stigmergy](https://github.com/gbtweilai-star/gbt-stigmergy) |  |
| 7 | `coze_mail` | `comms` | [gbt-coze-mail](https://github.com/gbtweilai-star/gbt-coze-mail) |  |
| 8 | `anatomy_figures` | `creation` | [gbt-anatomy-figures](https://github.com/gbtweilai-star/gbt-anatomy-figures) | yes |
| 9 | `anim_audit` | `creation` | [gbt-anim-audit](https://github.com/gbtweilai-star/gbt-anim-audit) |  |
| 10 | `anim_fix` | `creation` | [gbt-anim-fix](https://github.com/gbtweilai-star/gbt-anim-fix) | yes |
| 11 | `art_brief` | `creation` | [gbt-art-brief](https://github.com/gbtweilai-star/gbt-art-brief) | yes |
| 12 | `art_chain` | `creation` | [gbt-art-chain](https://github.com/gbtweilai-star/gbt-art-chain) | yes |
| 13 | `bits_kit` | `creation` | [gbt-bits-kit](https://github.com/gbtweilai-star/gbt-bits-kit) |  |
| 14 | `blender` | `creation` | [gbt-blender](https://github.com/gbtweilai-star/gbt-blender) | yes |
| 15 | `brand_outro` | `creation` | [gbt-brand-outro](https://github.com/gbtweilai-star/gbt-brand-outro) |  |
| 16 | `cad_distill` | `creation` | [gbt-cad-distill](https://github.com/gbtweilai-star/gbt-cad-distill) |  |
| 17 | `cadgen` | `creation` | [gbt-cadgen](https://github.com/gbtweilai-star/gbt-cadgen) | yes |
| 18 | `code_art` | `creation` | [gbt-code-art](https://github.com/gbtweilai-star/gbt-code-art) |  |
| 19 | `comfy_cloud` | `creation` | [gbt-comfy-cloud](https://github.com/gbtweilai-star/gbt-comfy-cloud) | yes |
| 20 | `comfy_forge` | `creation` | [gbt-comfy-forge](https://github.com/gbtweilai-star/gbt-comfy-forge) |  |
| 21 | `comfy_native` | `creation` | [gbt-comfy-native](https://github.com/gbtweilai-star/gbt-comfy-native) |  |
| 22 | `comfyui` | `creation` | [gbt-comfyui](https://github.com/gbtweilai-star/gbt-comfyui) |  |
| 23 | `console_pages` | `creation` | [gbt-console-pages](https://github.com/gbtweilai-star/gbt-console-pages) |  |
| 24 | `create` | `creation` | [gbt-create](https://github.com/gbtweilai-star/gbt-create) |  |
| 25 | `creation_camp` | `creation` | [gbt-creation-camp](https://github.com/gbtweilai-star/gbt-creation-camp) |  |
| 26 | `design_atlas` | `creation` | [gbt-design-atlas](https://github.com/gbtweilai-star/gbt-design-atlas) |  |
| 27 | `dh_asset_gate` | `creation` | [gbt-dh-asset-gate](https://github.com/gbtweilai-star/gbt-dh-asset-gate) |  |
| 28 | `dh_brain` | `creation` | [gbt-dh-brain](https://github.com/gbtweilai-star/gbt-dh-brain) |  |
| 29 | `dh_pose` | `creation` | [gbt-dh-pose](https://github.com/gbtweilai-star/gbt-dh-pose) | yes |
| 30 | `dh_realism` | `creation` | [gbt-dh-realism](https://github.com/gbtweilai-star/gbt-dh-realism) |  |
| 31 | `diagram_distill` | `creation` | [gbt-diagram-distill](https://github.com/gbtweilai-star/gbt-diagram-distill) |  |
| 32 | `dl_forge` | `creation` | [gbt-dl-forge](https://github.com/gbtweilai-star/gbt-dl-forge) |  |
| 33 | `drama` | `creation` | [gbt-drama](https://github.com/gbtweilai-star/gbt-drama) |  |
| 34 | `emotion_projection` | `creation` | [gbt-emotion-projection](https://github.com/gbtweilai-star/gbt-emotion-projection) |  |
| 35 | `filmkit` | `creation` | [gbt-filmkit](https://github.com/gbtweilai-star/gbt-filmkit) | yes |
| 36 | `flow_canvas` | `creation` | [gbt-flow-canvas](https://github.com/gbtweilai-star/gbt-flow-canvas) |  |
| 37 | `forge_mastery` | `creation` | [gbt-forge-mastery](https://github.com/gbtweilai-star/gbt-forge-mastery) | yes |
| 38 | `genoffice` | `creation` | [gbt-genoffice](https://github.com/gbtweilai-star/gbt-genoffice) | yes |
| 39 | `gs_h3` | `creation` | [gbt-gs-h3](https://github.com/gbtweilai-star/gbt-gs-h3) | yes |
| 40 | `image_scout` | `creation` | [gbt-image-scout](https://github.com/gbtweilai-star/gbt-image-scout) |  |
| 41 | `intake_kit` | `creation` | [gbt-intake-kit](https://github.com/gbtweilai-star/gbt-intake-kit) |  |
| 42 | `lobehub` | `creation` | [gbt-lobehub](https://github.com/gbtweilai-star/gbt-lobehub) |  |
| 43 | `machine_distill` | `creation` | [gbt-machine-distill](https://github.com/gbtweilai-star/gbt-machine-distill) |  |
| 44 | `machine_film` | `creation` | [gbt-machine-film](https://github.com/gbtweilai-star/gbt-machine-film) | yes |
| 45 | `motion_kit` | `creation` | [gbt-motion-kit](https://github.com/gbtweilai-star/gbt-motion-kit) |  |
| 46 | `music_auto` | `creation` | [gbt-music-auto](https://github.com/gbtweilai-star/gbt-music-auto) | yes |
| 47 | `music_publishing` | `creation` | [gbt-music-publishing](https://github.com/gbtweilai-star/gbt-music-publishing) |  |
| 48 | `omni_arm` | `creation` | [gbt-omni-arm](https://github.com/gbtweilai-star/gbt-omni-arm) | yes |
| 49 | `one_shot` | `creation` | [gbt-one-shot](https://github.com/gbtweilai-star/gbt-one-shot) |  |
| 50 | `pod_link` | `creation` | [gbt-pod-link](https://github.com/gbtweilai-star/gbt-pod-link) | yes |
| 51 | `render_evolution` | `creation` | [gbt-render-evolution](https://github.com/gbtweilai-star/gbt-render-evolution) |  |
| 52 | `rig_audit` | `creation` | [gbt-rig-audit](https://github.com/gbtweilai-star/gbt-rig-audit) | yes |
| 53 | `rig_fix` | `creation` | [gbt-rig-fix](https://github.com/gbtweilai-star/gbt-rig-fix) | yes |
| 54 | `scene_anchor` | `creation` | [gbt-scene-anchor](https://github.com/gbtweilai-star/gbt-scene-anchor) |  |
| 55 | `shot_director` | `creation` | [gbt-shot-director](https://github.com/gbtweilai-star/gbt-shot-director) | yes |
| 56 | `showcase_ops` | `creation` | [gbt-showcase-ops](https://github.com/gbtweilai-star/gbt-showcase-ops) | yes |
| 57 | `tentacle_comfy_bridge` | `creation` | [gbt-tentacle-comfy-bridge](https://github.com/gbtweilai-star/gbt-tentacle-comfy-bridge) |  |
| 58 | `tripo` | `creation` | [gbt-tripo](https://github.com/gbtweilai-star/gbt-tripo) | yes |
| 59 | `ui_kit` | `creation` | [gbt-ui-kit](https://github.com/gbtweilai-star/gbt-ui-kit) |  |
| 60 | `ui_render` | `creation` | [gbt-ui-render](https://github.com/gbtweilai-star/gbt-ui-render) |  |
| 61 | `zimage_rewash` | `creation` | [gbt-zimage-rewash](https://github.com/gbtweilai-star/gbt-zimage-rewash) | yes |
| 62 | `account_registry` | `data` | [gbt-account-registry](https://github.com/gbtweilai-star/gbt-account-registry) |  |
| 63 | `audit_query` | `data` | [gbt-audit-query](https://github.com/gbtweilai-star/gbt-audit-query) |  |
| 64 | `bi_distill` | `data` | [gbt-bi-distill](https://github.com/gbtweilai-star/gbt-bi-distill) |  |
| 65 | `chart_html` | `data` | [gbt-chart-html](https://github.com/gbtweilai-star/gbt-chart-html) | yes |
| 66 | `count_words` | `data` | [gbt-count-words](https://github.com/gbtweilai-star/gbt-count-words) |  |
| 67 | `datakit` | `data` | [gbt-datakit](https://github.com/gbtweilai-star/gbt-datakit) |  |
| 68 | `db_plugin` | `data` | [gbt-db-plugin](https://github.com/gbtweilai-star/gbt-db-plugin) |  |
| 69 | `db_probe` | `data` | [gbt-db-probe](https://github.com/gbtweilai-star/gbt-db-probe) |  |
| 70 | `echo` | `data` | [gbt-echo](https://github.com/gbtweilai-star/gbt-echo) |  |
| 71 | `humanizer` | `data` | [gbt-humanizer](https://github.com/gbtweilai-star/gbt-humanizer) | yes |
| 72 | `record_grid` | `data` | [gbt-record-grid](https://github.com/gbtweilai-star/gbt-record-grid) |  |
| 73 | `skill_finder` | `data` | [gbt-skill-finder](https://github.com/gbtweilai-star/gbt-skill-finder) | yes |
| 74 | `control_loop` | `desktop` | [gbt-control-loop](https://github.com/gbtweilai-star/gbt-control-loop) |  |
| 75 | `ul_tars_desktop` | `desktop` | [gbt-ul-tars-desktop](https://github.com/gbtweilai-star/gbt-ul-tars-desktop) | yes |
| 76 | `bluetooth` | `device` | [gbt-bluetooth](https://github.com/gbtweilai-star/gbt-bluetooth) |  |
| 77 | `bt_control` | `device` | [gbt-bt-control](https://github.com/gbtweilai-star/gbt-bt-control) |  |
| 78 | `devour_fusion` | `devour` | [gbt-devour-fusion](https://github.com/gbtweilai-star/gbt-devour-fusion) |  |
| 79 | `devour_github` | `devour` | [gbt-devour-github](https://github.com/gbtweilai-star/gbt-devour-github) |  |
| 80 | `devour_pulse` | `devour` | [gbt-devour-pulse](https://github.com/gbtweilai-star/gbt-devour-pulse) |  |
| 81 | `devour_reflect` | `devour` | [gbt-devour-reflect](https://github.com/gbtweilai-star/gbt-devour-reflect) |  |
| 82 | `devour_scan` | `devour` | [gbt-devour-scan](https://github.com/gbtweilai-star/gbt-devour-scan) |  |
| 83 | `sched_define` | `engine` | [gbt-sched-define](https://github.com/gbtweilai-star/gbt-sched-define) |  |
| 84 | `sched_status` | `engine` | [gbt-sched-status](https://github.com/gbtweilai-star/gbt-sched-status) |  |
| 85 | `sched_tick` | `engine` | [gbt-sched-tick](https://github.com/gbtweilai-star/gbt-sched-tick) |  |
| 86 | `transfer` | `engine` | [gbt-transfer](https://github.com/gbtweilai-star/gbt-transfer) |  |
| 87 | `wf_cache_clear` | `engine` | [gbt-wf-cache-clear](https://github.com/gbtweilai-star/gbt-wf-cache-clear) |  |
| 88 | `wf_define` | `engine` | [gbt-wf-define](https://github.com/gbtweilai-star/gbt-wf-define) |  |
| 89 | `wf_resume` | `engine` | [gbt-wf-resume](https://github.com/gbtweilai-star/gbt-wf-resume) |  |
| 90 | `wf_run` | `engine` | [gbt-wf-run](https://github.com/gbtweilai-star/gbt-wf-run) |  |
| 91 | `wf_status` | `engine` | [gbt-wf-status](https://github.com/gbtweilai-star/gbt-wf-status) |  |
| 92 | `workflow_forge` | `engine` | [gbt-workflow-forge](https://github.com/gbtweilai-star/gbt-workflow-forge) | yes |
| 93 | `quant` | `finance` | [gbt-quant](https://github.com/gbtweilai-star/gbt-quant) |  |
| 94 | `quant_backtest` | `finance` | [gbt-quant-backtest](https://github.com/gbtweilai-star/gbt-quant-backtest) |  |
| 95 | `quant_params` | `finance` | [gbt-quant-params](https://github.com/gbtweilai-star/gbt-quant-params) |  |
| 96 | `quant_strategy` | `finance` | [gbt-quant-strategy](https://github.com/gbtweilai-star/gbt-quant-strategy) |  |
| 97 | `gate_visibility` | `framework` | [gbt-gate-visibility](https://github.com/gbtweilai-star/gbt-gate-visibility) |  |
| 98 | `a1art_skill` | `image_video` | [gbt-a1art-skill](https://github.com/gbtweilai-star/gbt-a1art-skill) |  |
| 99 | `cloud_pc` | `infra` | [gbt-cloud-pc](https://github.com/gbtweilai-star/gbt-cloud-pc) |  |
| 100 | `cloud_plugin` | `infra` | [gbt-cloud-plugin](https://github.com/gbtweilai-star/gbt-cloud-plugin) |  |
| 101 | `cli_chat` | `integration` | [gbt-cli-chat](https://github.com/gbtweilai-star/gbt-cli-chat) | yes |
| 102 | `cli_ify` | `integration` | [gbt-cli-ify](https://github.com/gbtweilai-star/gbt-cli-ify) | yes |
| 103 | `feishu_embed` | `integration` | [gbt-feishu-embed](https://github.com/gbtweilai-star/gbt-feishu-embed) |  |
| 104 | `notion_bridge` | `integration` | [gbt-notion-bridge](https://github.com/gbtweilai-star/gbt-notion-bridge) | yes |
| 105 | `telegram_embed` | `integration` | [gbt-telegram-embed](https://github.com/gbtweilai-star/gbt-telegram-embed) |  |
| 106 | `thebrain_bridge` | `integration` | [gbt-thebrain-bridge](https://github.com/gbtweilai-star/gbt-thebrain-bridge) | yes |
| 107 | `whatsapp_embed` | `integration` | [gbt-whatsapp-embed](https://github.com/gbtweilai-star/gbt-whatsapp-embed) |  |
| 108 | `life` | `life` | [gbt-life](https://github.com/gbtweilai-star/gbt-life) |  |
| 109 | `automation_keys` | `llm` | [gbt-automation-keys](https://github.com/gbtweilai-star/gbt-automation-keys) |  |
| 110 | `autopilot` | `llm` | [gbt-autopilot](https://github.com/gbtweilai-star/gbt-autopilot) |  |
| 111 | `brain_execute` | `llm` | [gbt-brain-execute](https://github.com/gbtweilai-star/gbt-brain-execute) |  |
| 112 | `brain_health` | `llm` | [gbt-brain-health](https://github.com/gbtweilai-star/gbt-brain-health) |  |
| 113 | `brain_route` | `llm` | [gbt-brain-route](https://github.com/gbtweilai-star/gbt-brain-route) |  |
| 114 | `brain_unify` | `llm` | [gbt-brain-unify](https://github.com/gbtweilai-star/gbt-brain-unify) |  |
| 115 | `brain_verify` | `llm` | [gbt-brain-verify](https://github.com/gbtweilai-star/gbt-brain-verify) |  |
| 116 | `claude_code` | `llm` | [gbt-claude-code](https://github.com/gbtweilai-star/gbt-claude-code) | yes |
| 117 | `cloud_llm` | `llm` | [gbt-cloud-llm](https://github.com/gbtweilai-star/gbt-cloud-llm) |  |
| 118 | `codebuddy` | `llm` | [gbt-codebuddy](https://github.com/gbtweilai-star/gbt-codebuddy) | yes |
| 119 | `codex_chat` | `llm` | [gbt-codex-chat](https://github.com/gbtweilai-star/gbt-codex-chat) |  |
| 120 | `codex_interrupt` | `llm` | [gbt-codex-interrupt](https://github.com/gbtweilai-star/gbt-codex-interrupt) |  |
| 121 | `codex_models` | `llm` | [gbt-codex-models](https://github.com/gbtweilai-star/gbt-codex-models) |  |
| 122 | `codex_status` | `llm` | [gbt-codex-status](https://github.com/gbtweilai-star/gbt-codex-status) |  |
| 123 | `codex_thread_new` | `llm` | [gbt-codex-thread-new](https://github.com/gbtweilai-star/gbt-codex-thread-new) |  |
| 124 | `codex_tools` | `llm` | [gbt-codex-tools](https://github.com/gbtweilai-star/gbt-codex-tools) |  |
| 125 | `codex_turn_send` | `llm` | [gbt-codex-turn-send](https://github.com/gbtweilai-star/gbt-codex-turn-send) |  |
| 126 | `duty_board` | `llm` | [gbt-duty-board](https://github.com/gbtweilai-star/gbt-duty-board) |  |
| 127 | `energy_scheduler` | `llm` | [gbt-energy-scheduler](https://github.com/gbtweilai-star/gbt-energy-scheduler) |  |
| 128 | `fact_gate` | `llm` | [gbt-fact-gate](https://github.com/gbtweilai-star/gbt-fact-gate) |  |
| 129 | `freellmapi` | `llm` | [gbt-freellmapi](https://github.com/gbtweilai-star/gbt-freellmapi) |  |
| 130 | `genoffice_bridge` | `llm` | [gbt-genoffice-bridge](https://github.com/gbtweilai-star/gbt-genoffice-bridge) | yes |
| 131 | `key_gateway` | `llm` | [gbt-key-gateway](https://github.com/gbtweilai-star/gbt-key-gateway) | yes |
| 132 | `llm_chat` | `llm` | [gbt-llm-chat](https://github.com/gbtweilai-star/gbt-llm-chat) |  |
| 133 | `llm_status` | `llm` | [gbt-llm-status](https://github.com/gbtweilai-star/gbt-llm-status) |  |
| 134 | `llm_watch` | `llm` | [gbt-llm-watch](https://github.com/gbtweilai-star/gbt-llm-watch) |  |
| 135 | `model_key_pool` | `llm` | [gbt-model-key-pool](https://github.com/gbtweilai-star/gbt-model-key-pool) |  |
| 136 | `multimodal_port` | `llm` | [gbt-multimodal-port](https://github.com/gbtweilai-star/gbt-multimodal-port) | yes |
| 137 | `offload_distill` | `llm` | [gbt-offload-distill](https://github.com/gbtweilai-star/gbt-offload-distill) |  |
| 138 | `omni_plug` | `llm` | [gbt-omni-plug](https://github.com/gbtweilai-star/gbt-omni-plug) | yes |
| 139 | `policy_gate` | `llm` | [gbt-policy-gate](https://github.com/gbtweilai-star/gbt-policy-gate) |  |
| 140 | `prompt_bridge` | `llm` | [gbt-prompt-bridge](https://github.com/gbtweilai-star/gbt-prompt-bridge) |  |
| 141 | `quant_plan` | `llm` | [gbt-quant-plan](https://github.com/gbtweilai-star/gbt-quant-plan) | yes |
| 142 | `replan_loop` | `llm` | [gbt-replan-loop](https://github.com/gbtweilai-star/gbt-replan-loop) |  |
| 143 | `ring_context` | `llm` | [gbt-ring-context](https://github.com/gbtweilai-star/gbt-ring-context) |  |
| 144 | `task_graph` | `llm` | [gbt-task-graph](https://github.com/gbtweilai-star/gbt-task-graph) |  |
| 145 | `think_loop` | `llm` | [gbt-think-loop](https://github.com/gbtweilai-star/gbt-think-loop) |  |
| 146 | `train_ground` | `llm` | [gbt-train-ground](https://github.com/gbtweilai-star/gbt-train-ground) | yes |
| 147 | `train_recipe` | `llm` | [gbt-train-recipe](https://github.com/gbtweilai-star/gbt-train-recipe) |  |
| 148 | `transformer` | `llm` | [gbt-transformer](https://github.com/gbtweilai-star/gbt-transformer) |  |
| 149 | `warm_switch` | `llm` | [gbt-warm-switch](https://github.com/gbtweilai-star/gbt-warm-switch) |  |
| 150 | `lr_status` | `longrun` | [gbt-lr-status](https://github.com/gbtweilai-star/gbt-lr-status) |  |
| 151 | `lr_submit` | `longrun` | [gbt-lr-submit](https://github.com/gbtweilai-star/gbt-lr-submit) |  |
| 152 | `lr_tick` | `longrun` | [gbt-lr-tick](https://github.com/gbtweilai-star/gbt-lr-tick) |  |
| 153 | `tactics_advise` | `longrun` | [gbt-tactics-advise](https://github.com/gbtweilai-star/gbt-tactics-advise) |  |
| 154 | `agent_council` | `mind` | [gbt-agent-council](https://github.com/gbtweilai-star/gbt-agent-council) |  |
| 155 | `auto_switch` | `mind` | [gbt-auto-switch](https://github.com/gbtweilai-star/gbt-auto-switch) |  |
| 156 | `belief_forge` | `mind` | [gbt-belief-forge](https://github.com/gbtweilai-star/gbt-belief-forge) |  |
| 157 | `brain_council` | `mind` | [gbt-brain-council](https://github.com/gbtweilai-star/gbt-brain-council) |  |
| 158 | `brain_vault` | `mind` | [gbt-brain-vault](https://github.com/gbtweilai-star/gbt-brain-vault) |  |
| 159 | `command_chain` | `mind` | [gbt-command-chain](https://github.com/gbtweilai-star/gbt-command-chain) |  |
| 160 | `director_mood` | `mind` | [gbt-director-mood](https://github.com/gbtweilai-star/gbt-director-mood) |  |
| 161 | `doc_intake` | `mind` | [gbt-doc-intake](https://github.com/gbtweilai-star/gbt-doc-intake) |  |
| 162 | `local_brain` | `mind` | [gbt-local-brain](https://github.com/gbtweilai-star/gbt-local-brain) |  |
| 163 | `memory_bank` | `mind` | [gbt-memory-bank](https://github.com/gbtweilai-star/gbt-memory-bank) |  |
| 164 | `memory_manager` | `mind` | [gbt-memory-manager](https://github.com/gbtweilai-star/gbt-memory-manager) |  |
| 165 | `meta_cognition` | `mind` | [gbt-meta-cognition](https://github.com/gbtweilai-star/gbt-meta-cognition) |  |
| 166 | `mind` | `mind` | [gbt-mind](https://github.com/gbtweilai-star/gbt-mind) |  |
| 167 | `observer_anchor` | `mind` | [gbt-observer-anchor](https://github.com/gbtweilai-star/gbt-observer-anchor) |  |
| 168 | `obsidian_vault` | `mind` | [gbt-obsidian-vault](https://github.com/gbtweilai-star/gbt-obsidian-vault) |  |
| 169 | `persona_kernel` | `mind` | [gbt-persona-kernel](https://github.com/gbtweilai-star/gbt-persona-kernel) |  |
| 170 | `proactive_report` | `mind` | [gbt-proactive-report](https://github.com/gbtweilai-star/gbt-proactive-report) |  |
| 171 | `self_intake` | `mind` | [gbt-self-intake](https://github.com/gbtweilai-star/gbt-self-intake) | yes |
| 172 | `wiki_graph` | `mind` | [gbt-wiki-graph](https://github.com/gbtweilai-star/gbt-wiki-graph) |  |
| 173 | `deploy_queue` | `pipeline` | [gbt-deploy-queue](https://github.com/gbtweilai-star/gbt-deploy-queue) |  |
| 174 | `ghost_guard` | `pipeline` | [gbt-ghost-guard](https://github.com/gbtweilai-star/gbt-ghost-guard) |  |
| 175 | `mirror_ascend` | `pipeline` | [gbt-mirror-ascend](https://github.com/gbtweilai-star/gbt-mirror-ascend) |  |
| 176 | `mirror_parity` | `pipeline` | [gbt-mirror-parity](https://github.com/gbtweilai-star/gbt-mirror-parity) |  |
| 177 | `mirror_plan` | `pipeline` | [gbt-mirror-plan](https://github.com/gbtweilai-star/gbt-mirror-plan) |  |
| 178 | `mirror_rehearse` | `pipeline` | [gbt-mirror-rehearse](https://github.com/gbtweilai-star/gbt-mirror-rehearse) |  |
| 179 | `mirror_release` | `pipeline` | [gbt-mirror-release](https://github.com/gbtweilai-star/gbt-mirror-release) |  |
| 180 | `mirror_rewind` | `pipeline` | [gbt-mirror-rewind](https://github.com/gbtweilai-star/gbt-mirror-rewind) |  |
| 181 | `mirror_scan` | `pipeline` | [gbt-mirror-scan](https://github.com/gbtweilai-star/gbt-mirror-scan) |  |
| 182 | `mirror_shape` | `pipeline` | [gbt-mirror-shape](https://github.com/gbtweilai-star/gbt-mirror-shape) |  |
| 183 | `mirror_simulate` | `pipeline` | [gbt-mirror-simulate](https://github.com/gbtweilai-star/gbt-mirror-simulate) |  |
| 184 | `mirror_status` | `pipeline` | [gbt-mirror-status](https://github.com/gbtweilai-star/gbt-mirror-status) |  |
| 185 | `one_key_deploy` | `pipeline` | [gbt-one-key-deploy](https://github.com/gbtweilai-star/gbt-one-key-deploy) |  |
| 186 | `pipeline_rollback` | `pipeline` | [gbt-pipeline-rollback](https://github.com/gbtweilai-star/gbt-pipeline-rollback) |  |
| 187 | `pipeline_status` | `pipeline` | [gbt-pipeline-status](https://github.com/gbtweilai-star/gbt-pipeline-status) |  |
| 188 | `pipeline_submit` | `pipeline` | [gbt-pipeline-submit](https://github.com/gbtweilai-star/gbt-pipeline-submit) |  |
| 189 | `pipeline_versions` | `pipeline` | [gbt-pipeline-versions](https://github.com/gbtweilai-star/gbt-pipeline-versions) |  |
| 190 | `svc_inspect` | `pipeline` | [gbt-svc-inspect](https://github.com/gbtweilai-star/gbt-svc-inspect) |  |
| 191 | `platform_profile` | `project` | [gbt-platform-profile](https://github.com/gbtweilai-star/gbt-platform-profile) |  |
| 192 | `project_context` | `project` | [gbt-project-context](https://github.com/gbtweilai-star/gbt-project-context) |  |
| 193 | `book_skill` | `recon` | [gbt-book-skill](https://github.com/gbtweilai-star/gbt-book-skill) | yes |
| 194 | `case_mine` | `recon` | [gbt-case-mine](https://github.com/gbtweilai-star/gbt-case-mine) |  |
| 195 | `film_intel` | `recon` | [gbt-film-intel](https://github.com/gbtweilai-star/gbt-film-intel) |  |
| 196 | `know_map` | `recon` | [gbt-know-map](https://github.com/gbtweilai-star/gbt-know-map) | yes |
| 197 | `music_intel` | `recon` | [gbt-music-intel](https://github.com/gbtweilai-star/gbt-music-intel) |  |
| 198 | `osint_scan` | `recon` | [gbt-osint-scan](https://github.com/gbtweilai-star/gbt-osint-scan) |  |
| 199 | `rea_reverse` | `recon` | [gbt-rea-reverse](https://github.com/gbtweilai-star/gbt-rea-reverse) |  |
| 200 | `recon_distill` | `recon` | [gbt-recon-distill](https://github.com/gbtweilai-star/gbt-recon-distill) |  |
| 201 | `scrapling` | `recon` | [gbt-scrapling](https://github.com/gbtweilai-star/gbt-scrapling) |  |
| 202 | `skill_forge` | `recon` | [gbt-skill-forge](https://github.com/gbtweilai-star/gbt-skill-forge) | yes |
| 203 | `spider_ops` | `recon` | [gbt-spider-ops](https://github.com/gbtweilai-star/gbt-spider-ops) | yes |
| 204 | `tentacle_learn` | `recon` | [gbt-tentacle-learn](https://github.com/gbtweilai-star/gbt-tentacle-learn) | yes |
| 205 | `topic_watch` | `recon` | [gbt-topic-watch](https://github.com/gbtweilai-star/gbt-topic-watch) |  |
| 206 | `topic_web` | `recon` | [gbt-topic-web](https://github.com/gbtweilai-star/gbt-topic-web) | yes |
| 207 | `trend_watch` | `recon` | [gbt-trend-watch](https://github.com/gbtweilai-star/gbt-trend-watch) |  |
| 208 | `verification_watch` | `recon` | [gbt-verification-watch](https://github.com/gbtweilai-star/gbt-verification-watch) |  |
| 209 | `video_intel` | `recon` | [gbt-video-intel](https://github.com/gbtweilai-star/gbt-video-intel) |  |
| 210 | `asset_vault_freeze` | `security` | [gbt-asset-vault-freeze](https://github.com/gbtweilai-star/gbt-asset-vault-freeze) |  |
| 211 | `code_audit` | `security` | [gbt-code-audit](https://github.com/gbtweilai-star/gbt-code-audit) |  |
| 212 | `credential_steal` | `security` | [gbt-credential-steal](https://github.com/gbtweilai-star/gbt-credential-steal) | yes |
| 213 | `data_hijack` | `security` | [gbt-data-hijack](https://github.com/gbtweilai-star/gbt-data-hijack) | yes |
| 214 | `device_takeover` | `security` | [gbt-device-takeover](https://github.com/gbtweilai-star/gbt-device-takeover) | yes |
| 215 | `event_ledger` | `security` | [gbt-event-ledger](https://github.com/gbtweilai-star/gbt-event-ledger) |  |
| 216 | `hook_enforcer` | `security` | [gbt-hook-enforcer](https://github.com/gbtweilai-star/gbt-hook-enforcer) |  |
| 217 | `install_selfcheck` | `security` | [gbt-install-selfcheck](https://github.com/gbtweilai-star/gbt-install-selfcheck) |  |
| 218 | `keylogger` | `security` | [gbt-keylogger](https://github.com/gbtweilai-star/gbt-keylogger) | yes |
| 219 | `llm_redteam` | `security` | [gbt-llm-redteam](https://github.com/gbtweilai-star/gbt-llm-redteam) |  |
| 220 | `offense_ops` | `security` | [gbt-offense-ops](https://github.com/gbtweilai-star/gbt-offense-ops) | yes |
| 221 | `omission_detector` | `security` | [gbt-omission-detector](https://github.com/gbtweilai-star/gbt-omission-detector) |  |
| 222 | `onboarding_gate` | `security` | [gbt-onboarding-gate](https://github.com/gbtweilai-star/gbt-onboarding-gate) |  |
| 223 | `paywallbuster` | `security` | [gbt-paywallbuster](https://github.com/gbtweilai-star/gbt-paywallbuster) |  |
| 224 | `penetrating_cross_scan` | `security` | [gbt-penetrating-cross-scan](https://github.com/gbtweilai-star/gbt-penetrating-cross-scan) |  |
| 225 | `pentest` | `security` | [gbt-pentest](https://github.com/gbtweilai-star/gbt-pentest) | yes |
| 226 | `pentest_distill` | `security` | [gbt-pentest-distill](https://github.com/gbtweilai-star/gbt-pentest-distill) |  |
| 227 | `policy_delta` | `security` | [gbt-policy-delta](https://github.com/gbtweilai-star/gbt-policy-delta) |  |
| 228 | `redteam_recon` | `security` | [gbt-redteam-recon](https://github.com/gbtweilai-star/gbt-redteam-recon) | yes |
| 229 | `remote_domain` | `security` | [gbt-remote-domain](https://github.com/gbtweilai-star/gbt-remote-domain) | yes |
| 230 | `review_gate` | `security` | [gbt-review-gate](https://github.com/gbtweilai-star/gbt-review-gate) |  |
| 231 | `screen_sniff` | `security` | [gbt-screen-sniff](https://github.com/gbtweilai-star/gbt-screen-sniff) | yes |
| 232 | `sec_chain` | `security` | [gbt-sec-chain](https://github.com/gbtweilai-star/gbt-sec-chain) |  |
| 233 | `sec_defenses` | `security` | [gbt-sec-defenses](https://github.com/gbtweilai-star/gbt-sec-defenses) |  |
| 234 | `sec_llm` | `security` | [gbt-sec-llm](https://github.com/gbtweilai-star/gbt-sec-llm) |  |
| 235 | `sec_scan` | `security` | [gbt-sec-scan](https://github.com/gbtweilai-star/gbt-sec-scan) |  |
| 236 | `sec_surface` | `security` | [gbt-sec-surface](https://github.com/gbtweilai-star/gbt-sec-surface) |  |
| 237 | `sec_sweeper` | `security` | [gbt-sec-sweeper](https://github.com/gbtweilai-star/gbt-sec-sweeper) |  |
| 238 | `social_eng` | `security` | [gbt-social-eng](https://github.com/gbtweilai-star/gbt-social-eng) |  |
| 239 | `auto_publish` | `social` | [gbt-auto-publish](https://github.com/gbtweilai-star/gbt-auto-publish) |  |
| 240 | `eigenflux` | `social` | [gbt-eigenflux](https://github.com/gbtweilai-star/gbt-eigenflux) |  |
| 241 | `action_gate` | `system` | [gbt-action-gate](https://github.com/gbtweilai-star/gbt-action-gate) |  |
| 242 | `agent_console` | `system` | [gbt-agent-console](https://github.com/gbtweilai-star/gbt-agent-console) |  |
| 243 | `agent_control` | `system` | [gbt-agent-control](https://github.com/gbtweilai-star/gbt-agent-control) |  |
| 244 | `agent_rig` | `system` | [gbt-agent-rig](https://github.com/gbtweilai-star/gbt-agent-rig) |  |
| 245 | `alerts` | `system` | [gbt-alerts](https://github.com/gbtweilai-star/gbt-alerts) |  |
| 246 | `answer_shaper` | `system` | [gbt-answer-shaper](https://github.com/gbtweilai-star/gbt-answer-shaper) |  |
| 247 | `asset_index` | `system` | [gbt-asset-index](https://github.com/gbtweilai-star/gbt-asset-index) |  |
| 248 | `auth_gate_status` | `system` | [gbt-auth-gate-status](https://github.com/gbtweilai-star/gbt-auth-gate-status) |  |
| 249 | `cap_tags` | `system` | [gbt-cap-tags](https://github.com/gbtweilai-star/gbt-cap-tags) |  |
| 250 | `caps_called_audit` | `system` | [gbt-caps-called-audit](https://github.com/gbtweilai-star/gbt-caps-called-audit) |  |
| 251 | `console_hub` | `system` | [gbt-console-hub](https://github.com/gbtweilai-star/gbt-console-hub) |  |
| 252 | `context_vault` | `system` | [gbt-context-vault](https://github.com/gbtweilai-star/gbt-context-vault) |  |
| 253 | `coverage_auditor` | `system` | [gbt-coverage-auditor](https://github.com/gbtweilai-star/gbt-coverage-auditor) |  |
| 254 | `cross_scan` | `system` | [gbt-cross-scan](https://github.com/gbtweilai-star/gbt-cross-scan) |  |
| 255 | `delivery_gate` | `system` | [gbt-delivery-gate](https://github.com/gbtweilai-star/gbt-delivery-gate) | yes |
| 256 | `detail_habit` | `system` | [gbt-detail-habit](https://github.com/gbtweilai-star/gbt-detail-habit) |  |
| 257 | `energy_pool` | `system` | [gbt-energy-pool](https://github.com/gbtweilai-star/gbt-energy-pool) |  |
| 258 | `figure_gate` | `system` | [gbt-figure-gate](https://github.com/gbtweilai-star/gbt-figure-gate) | yes |
| 259 | `file_hygiene` | `system` | [gbt-file-hygiene](https://github.com/gbtweilai-star/gbt-file-hygiene) |  |
| 260 | `god_view` | `system` | [gbt-god-view](https://github.com/gbtweilai-star/gbt-god-view) |  |
| 261 | `gods_eye` | `system` | [gbt-gods-eye](https://github.com/gbtweilai-star/gbt-gods-eye) |  |
| 262 | `growth_hooks` | `system` | [gbt-growth-hooks](https://github.com/gbtweilai-star/gbt-growth-hooks) |  |
| 263 | `handoff` | `system` | [gbt-handoff](https://github.com/gbtweilai-star/gbt-handoff) |  |
| 264 | `health` | `system` | [gbt-health](https://github.com/gbtweilai-star/gbt-health) |  |
| 265 | `hook_registry` | `system` | [gbt-hook-registry](https://github.com/gbtweilai-star/gbt-hook-registry) |  |
| 266 | `impact_check` | `system` | [gbt-impact-check](https://github.com/gbtweilai-star/gbt-impact-check) |  |
| 267 | `inventory` | `system` | [gbt-inventory](https://github.com/gbtweilai-star/gbt-inventory) |  |
| 268 | `ledger_note` | `system` | [gbt-ledger-note](https://github.com/gbtweilai-star/gbt-ledger-note) |  |
| 269 | `orchestration_kernel` | `system` | [gbt-orchestration-kernel](https://github.com/gbtweilai-star/gbt-orchestration-kernel) |  |
| 270 | `page_scan` | `system` | [gbt-page-scan](https://github.com/gbtweilai-star/gbt-page-scan) |  |
| 271 | `project_drift` | `system` | [gbt-project-drift](https://github.com/gbtweilai-star/gbt-project-drift) |  |
| 272 | `room_space` | `system` | [gbt-room-space](https://github.com/gbtweilai-star/gbt-room-space) | yes |
| 273 | `root_fix` | `system` | [gbt-root-fix](https://github.com/gbtweilai-star/gbt-root-fix) |  |
| 274 | `scan_cap` | `system` | [gbt-scan-cap](https://github.com/gbtweilai-star/gbt-scan-cap) | yes |
| 275 | `selfscan` | `system` | [gbt-selfscan](https://github.com/gbtweilai-star/gbt-selfscan) |  |
| 276 | `shared_resources` | `system` | [gbt-shared-resources](https://github.com/gbtweilai-star/gbt-shared-resources) |  |
| 277 | `signature_guard` | `system` | [gbt-signature-guard](https://github.com/gbtweilai-star/gbt-signature-guard) |  |
| 278 | `skill_watch` | `system` | [gbt-skill-watch](https://github.com/gbtweilai-star/gbt-skill-watch) |  |
| 279 | `slim_profile` | `system` | [gbt-slim-profile](https://github.com/gbtweilai-star/gbt-slim-profile) |  |
| 280 | `spend_guard` | `system` | [gbt-spend-guard](https://github.com/gbtweilai-star/gbt-spend-guard) |  |
| 281 | `surface_bind` | `system` | [gbt-surface-bind](https://github.com/gbtweilai-star/gbt-surface-bind) |  |
| 282 | `task_manager` | `system` | [gbt-task-manager](https://github.com/gbtweilai-star/gbt-task-manager) |  |
| 283 | `tentacle_arm` | `system` | [gbt-tentacle-arm](https://github.com/gbtweilai-star/gbt-tentacle-arm) |  |
| 284 | `tentacle_bind` | `system` | [gbt-tentacle-bind](https://github.com/gbtweilai-star/gbt-tentacle-bind) |  |
| 285 | `tentacle_cognition` | `system` | [gbt-tentacle-cognition](https://github.com/gbtweilai-star/gbt-tentacle-cognition) |  |
| 286 | `theme_cap` | `system` | [gbt-theme-cap](https://github.com/gbtweilai-star/gbt-theme-cap) | yes |
| 287 | `trace_store` | `system` | [gbt-trace-store](https://github.com/gbtweilai-star/gbt-trace-store) |  |
| 288 | `truth_scan` | `system` | [gbt-truth-scan](https://github.com/gbtweilai-star/gbt-truth-scan) |  |
| 289 | `ux_doctrine` | `system` | [gbt-ux-doctrine](https://github.com/gbtweilai-star/gbt-ux-doctrine) |  |
| 290 | `wave_probe` | `system` | [gbt-wave-probe](https://github.com/gbtweilai-star/gbt-wave-probe) |  |
| 291 | `welcome` | `system` | [gbt-welcome](https://github.com/gbtweilai-star/gbt-welcome) |  |
| 292 | `agency_tentacles` | `tentacle` | [gbt-agency-tentacles](https://github.com/gbtweilai-star/gbt-agency-tentacles) |  |
| 293 | `desktop_commander` | `tentacle` | [gbt-desktop-commander](https://github.com/gbtweilai-star/gbt-desktop-commander) |  |
| 294 | `desktop_distill` | `tentacle` | [gbt-desktop-distill](https://github.com/gbtweilai-star/gbt-desktop-distill) |  |
| 295 | `express_direct` | `tentacle` | [gbt-express-direct](https://github.com/gbtweilai-star/gbt-express-direct) |  |
| 296 | `long_run_supervisor` | `tentacle` | [gbt-long-run-supervisor](https://github.com/gbtweilai-star/gbt-long-run-supervisor) |  |
| 297 | `mcp_call` | `tentacle` | [gbt-mcp-call](https://github.com/gbtweilai-star/gbt-mcp-call) |  |
| 298 | `mcp_connect` | `tentacle` | [gbt-mcp-connect](https://github.com/gbtweilai-star/gbt-mcp-connect) |  |
| 299 | `mcp_tools` | `tentacle` | [gbt-mcp-tools](https://github.com/gbtweilai-star/gbt-mcp-tools) |  |
| 300 | `omarchy_bridge` | `tentacle` | [gbt-omarchy-bridge](https://github.com/gbtweilai-star/gbt-omarchy-bridge) | yes |
| 301 | `omni_web` | `tentacle` | [gbt-omni-web](https://github.com/gbtweilai-star/gbt-omni-web) | yes |
| 302 | `remote_confinement` | `tentacle` | [gbt-remote-confinement](https://github.com/gbtweilai-star/gbt-remote-confinement) | yes |
| 303 | `tentacle` | `tentacle` | [gbt-tentacle](https://github.com/gbtweilai-star/gbt-tentacle) |  |
| 304 | `tentacle_equip` | `tentacle` | [gbt-tentacle-equip](https://github.com/gbtweilai-star/gbt-tentacle-equip) | yes |
| 305 | `tentacle_manifest` | `tentacle` | [gbt-tentacle-manifest](https://github.com/gbtweilai-star/gbt-tentacle-manifest) |  |
| 306 | `tentacle_pipeline` | `tentacle` | [gbt-tentacle-pipeline](https://github.com/gbtweilai-star/gbt-tentacle-pipeline) |  |
| 307 | `tentacle_scale` | `tentacle` | [gbt-tentacle-scale](https://github.com/gbtweilai-star/gbt-tentacle-scale) |  |
| 308 | `tentacle_status` | `tentacle` | [gbt-tentacle-status](https://github.com/gbtweilai-star/gbt-tentacle-status) |  |
| 309 | `tool_bay` | `tentacle` | [gbt-tool-bay](https://github.com/gbtweilai-star/gbt-tool-bay) | yes |
| 310 | `awesome_tools_index` | `tools` | [gbt-awesome-tools-index](https://github.com/gbtweilai-star/gbt-awesome-tools-index) |  |
| 311 | `capability_net` | `tools` | [gbt-capability-net](https://github.com/gbtweilai-star/gbt-capability-net) |  |
| 312 | `code_patch` | `tools` | [gbt-code-patch](https://github.com/gbtweilai-star/gbt-code-patch) | yes |
| 313 | `freebuff_term` | `tools` | [gbt-freebuff-term](https://github.com/gbtweilai-star/gbt-freebuff-term) |  |
| 314 | `git_read` | `tools` | [gbt-git-read](https://github.com/gbtweilai-star/gbt-git-read) |  |
| 315 | `git_write` | `tools` | [gbt-git-write](https://github.com/gbtweilai-star/gbt-git-write) | yes |
| 316 | `projection_card` | `tools` | [gbt-projection-card](https://github.com/gbtweilai-star/gbt-projection-card) |  |
| 317 | `pulse_direct` | `tools` | [gbt-pulse-direct](https://github.com/gbtweilai-star/gbt-pulse-direct) |  |
| 318 | `repo_publish` | `tools` | [gbt-repo-publish](https://github.com/gbtweilai-star/gbt-repo-publish) |  |
| 319 | `actioncam` | `video` | [gbt-actioncam](https://github.com/gbtweilai-star/gbt-actioncam) | yes |
| 320 | `audio_extract` | `video` | [gbt-audio-extract](https://github.com/gbtweilai-star/gbt-audio-extract) | yes |
| 321 | `audio_mix` | `video` | [gbt-audio-mix](https://github.com/gbtweilai-star/gbt-audio-mix) | yes |
| 322 | `digital_human` | `video` | [gbt-digital-human](https://github.com/gbtweilai-star/gbt-digital-human) |  |
| 323 | `edit_pipeline` | `video` | [gbt-edit-pipeline](https://github.com/gbtweilai-star/gbt-edit-pipeline) | yes |
| 324 | `h3_video_gen` | `video` | [gbt-h3-video-gen](https://github.com/gbtweilai-star/gbt-h3-video-gen) |  |
| 325 | `libtv_skill` | `video` | [gbt-libtv-skill](https://github.com/gbtweilai-star/gbt-libtv-skill) |  |
| 326 | `libtv_workflow` | `video` | [gbt-libtv-workflow](https://github.com/gbtweilai-star/gbt-libtv-workflow) |  |
| 327 | `look_grade` | `video` | [gbt-look-grade](https://github.com/gbtweilai-star/gbt-look-grade) | yes |
| 328 | `media_license` | `video` | [gbt-media-license](https://github.com/gbtweilai-star/gbt-media-license) | yes |
| 329 | `media_pipeline` | `video` | [gbt-media-pipeline](https://github.com/gbtweilai-star/gbt-media-pipeline) |  |
| 330 | `media_publish` | `video` | [gbt-media-publish](https://github.com/gbtweilai-star/gbt-media-publish) | yes |
| 331 | `media_run` | `video` | [gbt-media-run](https://github.com/gbtweilai-star/gbt-media-run) | yes |
| 332 | `media_stamp` | `video` | [gbt-media-stamp](https://github.com/gbtweilai-star/gbt-media-stamp) | yes |
| 333 | `vision` | `vision` | [gbt-vision](https://github.com/gbtweilai-star/gbt-vision) |  |
| 334 | `vision_grounding` | `vision` | [gbt-vision-grounding](https://github.com/gbtweilai-star/gbt-vision-grounding) |  |
| 335 | `vision_loop` | `vision` | [gbt-vision-loop](https://github.com/gbtweilai-star/gbt-vision-loop) | yes |
| 336 | `vision_print` | `vision` | [gbt-vision-print](https://github.com/gbtweilai-star/gbt-vision-print) |  |
| 337 | `vlx_flow` | `vision` | [gbt-vlx-flow](https://github.com/gbtweilai-star/gbt-vlx-flow) |  |
| 338 | `hf_voice` | `voice` | [gbt-hf-voice](https://github.com/gbtweilai-star/gbt-hf-voice) |  |
| 339 | `voice` | `voice` | [gbt-voice](https://github.com/gbtweilai-star/gbt-voice) |  |
| 340 | `voice_orchestra` | `voice` | [gbt-voice-orchestra](https://github.com/gbtweilai-star/gbt-voice-orchestra) |  |
| 341 | `voice_studio` | `voice` | [gbt-voice-studio](https://github.com/gbtweilai-star/gbt-voice-studio) |  |
