# 域 `finance`

**4 位能力** · 需授权 0 · 多操作 0 · 需入参 0

| 能力位 | 安全 | 形态 | 入参 | 一句话 |
|---|---|---|---|---|
| [`quant`](./quant.md) | safe | 单动作 | — | 量化/回测入口（外部业务模块 quant_tech，未挂载则如实报缺口） |
| [`quant_backtest`](./quant_backtest.md) | safe | 单动作 | — | 读取真实回测 API，返回类/函数/默认参数（外部业务模块 quant_te |
| [`quant_params`](./quant_params.md) | safe | 单动作 | — | 读取真实量化引擎的数值型策略参数（动量/ATR/止损；外部业务模块 quan |
| [`quant_strategy`](./quant_strategy.md) | safe | 单动作 | — | 读取真实量化引擎，返回策略信号/仓位模型（外部业务模块 quant_tech |

返回上级索引：[`caps/`](../README.md)
