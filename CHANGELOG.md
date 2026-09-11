# awesome-robotics 更新记录

## 2026-09-11

### 名称与结构

- 将项目标题统一为 `awesome-robotics`；本地目录原本已使用此名称。
- 增加总目录、按目标快速开始、贡献指南和来源说明，统一表格空白格式。
- 保留原有资源及原作者来源，将原始项目链接移至致谢，移除误导性的当前维护者与旧站点声明。
- 当前目录没有 `.git` 或远程配置，本轮只修改本地文件，未改名或发布任何 GitHub 仓库。

### 新增资源及官方来源

| 项目 | 核查来源 | 收录内容 |
| --- | --- | --- |
| InternVLA-A 系列 | [官方仓库](https://github.com/InternRobotics/InternVLA-A-series) | A1.5 主分支、A1 历史分支及非商业许可说明；不将所有计划发布项视为已发布。 |
| InternNav | [官方仓库](https://github.com/InternRobotics/InternNav) | 具身导航训练、评测与模型入口。 |
| MPlib | [官方仓库](https://github.com/haosulab/MPlib) | 机械臂运动规划库。 |
| PiPER ROS | [官方仓库](https://github.com/agilexrobotics/piper_ros) | 机械臂 ROS 工作空间。 |
| GCOPTER | [官方仓库](https://github.com/ZJU-FAST-Lab/GCOPTER) | 多旋翼轨迹优化。 |
| Point-LIO | [官方仓库](https://github.com/hku-mars/Point-LIO) | 高带宽激光惯性里程计。 |

### 修正与核查来源

| 条目 | 修正 | 官方来源 |
| --- | --- | --- |
| XR-1 | 删除缺乏支撑的“国标级”描述，改为模型方法介绍。 | [仓库](https://github.com/Open-X-Humanoid/XR-1) |
| EngineAI | 修正厂商混淆，介绍实际控制与部署用途。 | [仓库](https://github.com/engineai-robotics/engineai_humanoid) |
| Fourier N1 | 将组织首页替换为具体文档仓库，明确其不是 SDK 源码仓库。 | [仓库](https://github.com/FFTAI/fourier-grx-N1) |
| Booster Gym | 使用具体训练仓库，删除未经本轮确认的型号与比赛 Demo 描述。 | [仓库](https://github.com/BoosterRobotics/booster_gym) |
| OpenLoong | 使用具体动力学控制仓库，说明该入口覆盖的内容。 | [仓库](https://github.com/loongOpen/OpenLoong-Dyn-Control) |
| Genesis | 更新重定向后的仓库地址，删除脱离测试条件的速度倍数。 | [仓库](https://github.com/Genesis-Embodied-AI/genesis-world) |
| MaixPy / Sipeed | 区分 MaixCAM 的 Python 工具与 K210 的 MaixPy-v1，修正 Sipeed 中文名称。 | [仓库](https://github.com/sipeed/MaixPy) |
| MXNet | 更新仓库地址，标记 2023-11-17 归档状态。 | [仓库](https://github.com/apache/mxnet) |
| Kimi K2 | 删除没有来源支持的 GPT-5.5 对标，改为模型用途。 | [仓库](https://github.com/MoonshotAI/Kimi-K2) |
| MiniMax-M2 | 删除易过期的排名描述，改为编码与智能体用途。 | [仓库](https://github.com/MiniMax-AI/MiniMax-M2) |

### 核查范围

以上来源于本轮联网查看的官方仓库 README、仓库状态和重定向结果。核查日期为 2026-09-11，不代表项目发布日期，也不代表已运行其代码或复现其性能。

本轮未逐一验证所有历史外链、硬件资料和模型授权。其余条目保留历史内容，后续应继续核查，尤其是历史 HTTP 网站、机构首页、版本参数与论文获奖信息。
