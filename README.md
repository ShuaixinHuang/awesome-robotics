<a id="top"></a>

<div align="center">

# 🤖 awesome-robotics

**探索机器人世界 · 从硬件到智能**

🤖 A curated collection of robotics and embodied AI resources, covering VLA models, humanoid robots, robotic arms, SLAM, simulation, and embedded systems.

机器人 / 具身智能 / 嵌入式系统 / 人工智能

以中文社区及华人团队项目为主的资源清单，连接代码、硬件、模型与学习资料。

**136 个资源条目** &nbsp; · &nbsp; **4 大方向** &nbsp; · &nbsp; **8 个机器人专题**

[🧭 浏览目录](#navigation) &nbsp; · &nbsp; [🚀 快速开始](#quick-start) &nbsp; · &nbsp; [📝 更新记录](CHANGELOG.md) &nbsp; · &nbsp; [🤝 参与贡献](CONTRIBUTING.md)

<sub>本轮内容更新：2026-09-11 · 保留经典项目，补充可核实的新资源 · 排序不代表排名</sub>

</div>

---

<a id="navigation"></a>

## 🧭 资源导航

| 方向 | 内容概览 | 条目数 |
| :--- | :--- | ---: |
| [🤖 机器人项目](#robots) | 具身智能、运动控制、机械臂、无人机、自动驾驶与仿真 | 80 |
| [🔌 嵌入式系统](#embedded) | 开发板、边缘视觉、智能硬件与 DIY 电子项目 | 13 |
| [⚙️ 架构与操作系统](#arch-os) | RISC-V、实时操作系统与机器人运行时 | 5 |
| [🧠 机器学习](#ml) | 视觉语言模型、推理引擎、视觉与语音工具 | 38 |

<a id="quick-start"></a>

## 🚀 按目标快速开始

| 目标 | 入口 | 适合查找 |
| --- | --- | --- |
| 学习机器人感知与定位 | [SLAM、感知与状态估计](#16-slam感知与状态估计) | 教材代码、视觉惯性定位、激光建图 |
| 训练机器人操作策略 | [具身智能与 VLA](#11-具身智能与vla大模型) | 模型、训练与推理入口 |
| 开发机械臂应用 | [机械臂、抓取与操作](#13-机械臂抓取与操作) | 驱动、运动规划、抓取与操作基准 |
| 研究运动控制 | [人形与足式机器人](#12-人形与足式机器人) | 强化学习、全身控制和硬件资料 |
| 构建仿真与采集流程 | [仿真、数据集与遥操作](#17-仿真数据集与遥操作) | 仿真器、数据采集与遥操作 |

[↑ 返回顶部](#top)

---

<a id="robots"></a>

## 🤖 1. 机器人项目 · Robotics

| 模型与机器人平台 | 感知、仿真与工具 |
| :--- | :--- |
| [🧩 具身智能与 VLA](#11-具身智能与vla大模型) | [🚗 自动驾驶](#15-自动驾驶) |
| [🦿 人形与足式机器人](#12-人形与足式机器人) | [📡 SLAM、感知与状态估计](#16-slam感知与状态估计) |
| [🦾 机械臂、抓取与操作](#13-机械臂抓取与操作) | [🌐 仿真、数据集与遥操作](#17-仿真数据集与遥操作) |
| [🚁 无人机与空中机器人](#14-无人机与空中机器人) | [🛠️ SDK、工具与创客资源](#18-sdk工具diy创客与资源) |

### 1.1 具身智能与VLA大模型

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **XR-1 VLA模型** | 北京人形机器人创新中心 | [GitHub](https://github.com/Open-X-Humanoid/XR-1) | 通过统一视觉与运动表示学习构建视觉-语言-动作模型，提供项目说明与模型使用入口。 |
| **DexVLA** | 多机构联合 | [GitHub](https://github.com/juruobenruo/DexVLA) | 基于Qwen2-VL的视觉-语言-动作模型，支持单臂、双臂和灵巧手等多种机器人形态的通用控制。 |
| **ManiFoundation** | 新加坡国立大学/清华大学 | [GitHub](https://github.com/NUS-LinS-Lab/ManiFM) | 通用机器人操作基础模型，通过接触合成实现对刚性、铰接和可变形物体的操作。 |
| **RoboticsDiffusionTransformer (RDT-1B)** | 清华大学 | [GitHub](https://github.com/thu-ml/RoboticsDiffusionTransformer) | 双臂机器人操控基础模型，采用扩散Transformer架构，在多种双臂操控任务上取得SOTA效果。 |
| **RoboBrain 2.5** | 智源研究院 (FlagOpen)/北京大学 | [GitHub](https://github.com/FlagOpen/RoboBrain2.5) | 新一代具身AI基础模型，支持精确3D空间推理、深度感知坐标预测和时序建模，CVPR 2025延续工作。 |
| **WholebodyVLA** | 上海AI实验室 (OpenDriveLab) | [GitHub](https://github.com/OpenDriveLab/WholebodyVLA) | ICLR 2026，面向人形机器人全身移动操作控制的统一潜空间VLA模型。 |
| **X-VLA** | 2toinf 等 | [GitHub](https://github.com/2toinf/X-VLA) | ICLR 2026，软提示Transformer跨形态VLA模型，AgiBot World挑战赛(IROS 2025)冠军。 |
| **WALL-OSS具身基础模型** | 自变量机器人 (X Square Robot) | [GitHub](https://github.com/X-Square-Robot/wall-x) | 自变量机器人开源的WALL系列具身基础模型训练与推理框架，含WALL-OSS等VLA模型，预训练即可直接上真机执行操作。 |
| **Galaxea G0 / GalaxeaVLA** | 星海图 (Galaxea AI) | [GitHub](https://github.com/OpenGalaxea/GalaxeaVLA) | 星海图开源的双系统VLA模型G0/G0.5系列与500+小时真实场景开放世界数据集，支持长程移动操作的预训练、微调与真机部署。 |
| **GraspVLA抓取基础模型** | 银河通用 & 北京大学 (PKU-EPIC) | [GitHub](https://github.com/PKU-EPIC/GraspVLA) | 基于十亿帧合成数据SynGrasp-1B预训练的抓取基础模型，纯仿真训练即可零样本迁移到真实世界开放词汇抓取。CoRL 2025。 |
| **InternVLA-M1** | 上海人工智能实验室 (InternRobotics) | [GitHub](https://github.com/InternRobotics/InternVLA-M1) | 空间引导的视觉-语言-动作框架，基于Qwen2.5-VL统一空间定位与动作头训练，面向通用机器人操作策略，MIT协议开源。 |
| **DexGraspVLA灵巧抓取** | 灵初智能 (PsiBot) & 北京大学 | [GitHub](https://github.com/Psi-Robot/DexGraspVLA) | 层级式灵巧抓取VLA框架，以VLM作高层规划器、扩散策略作低层控制器，杂乱场景灵巧手抓取成功率超90%。AAAI 2026 Oral。 |
| **MiMo-Embodied跨具身大模型** | 小米 (Xiaomi MiMo) | [GitHub](https://github.com/XiaomiMiMo/MiMo-Embodied) | 小米开源的首个跨具身基础模型，统一自动驾驶与具身智能两大领域，在29项具身与驾驶基准上取得领先性能。 |
| **RynnVLA-001** | 阿里巴巴达摩院 | [GitHub](https://github.com/alibaba-damo-academy/RynnVLA-001) | 基于视频生成模型预训练的VLA模型，利用人类第一视角视频演示提升机械臂操作能力，已开源训练代码与预训练权重。ICRA 2026。 |
| **InternVLA-A 系列** | 上海人工智能实验室（InternRobotics） | [GitHub](https://github.com/InternRobotics/InternVLA-A-series) | 统一视觉语言理解、未来预测与动作生成；当前主分支介绍 A1.5，A1 代码位于 InternVLA-A1 分支。仓库注明非商业许可，发布状态见 README。 |

### 1.2 人形与足式机器人

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **AgiBot X1开源人形机器人** | 智元机器人 (AgibotTech) | [推理](https://github.com/AgibotTech/agibot_x1_infer) \| [训练](https://github.com/AgibotTech/agibot_x1_train) \| [硬件](https://github.com/AgibotTech/agibot_x1_hardware) | 智元机器人X1完整开源人形机器人项目，包含推理模块、强化学习训练代码和全套硬件设计资料。 |
| **OpenLoong 青龙全身控制** | loongOpen | [GitHub](https://github.com/loongOpen/OpenLoong-Dyn-Control) | 人形机器人全身动力学控制软件，包含 MPC、WBC 与 MuJoCo 仿真示例。 |
| **Fourier N1 SDK 文档** | 傅利叶智能（FFTAI） | [文档仓库](https://github.com/FFTAI/fourier-grx-N1) | N1 SDK 安装、接口、运行模式与任务指南；此链接为文档仓库，SDK 与示例入口见其说明。 |
| **EngineAI Humanoid** | EngineAI（众擎机器人） | [GitHub](https://github.com/engineai-robotics/engineai_humanoid) | 双足机器人运动控制与强化学习策略真机部署框架，配合 engineai_legged_gym 使用。 |
| **Booster Gym** | 加速进化（Booster Robotics） | [GitHub](https://github.com/BoosterRobotics/booster_gym) | 面向人形机器人运动控制的强化学习训练框架，提供训练和部署说明。 |
| **Unitree Qmini开源双足机器人** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/Qmini) | 开源双足平台，提供全套BOM/装配指南、RoboTamer4Qmini控制框架与URDF模型。 |
| **萝博头 Roboto Origin** | 萝卜派对 (RoboParty) | [GitHub](https://github.com/Roboparty/roboto_origin) | 全栈开源的双足人形机器人，开放全部结构图纸、电子、训练与ROS2部署代码，零件可全部通过淘宝采购复刻。 |
| **OpenCat** | Petoi | [GitHub](https://github.com/PetoiCamp/OpenCat) | 开源四足机器人平台 |
| **小米CyberDog开源四足机器人** | 小米科技 | [GitHub](https://github.com/MiRoboticsLab/cyberdog_ros2) | 小米CyberDog四足机器人的开源软件和硬件资料。 |
| **unitree_rl_gym** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unitree_rl_gym) | 宇树科技四足/人形机器人强化学习训练框架，基于Isaac Gym。 |
| **unitree_rl_lab** | 宇树科技 (Unitree) | [IsaacLab](https://github.com/unitreerobotics/unitree_rl_lab) \| [MuJoCo](https://github.com/unitreerobotics/unitree_rl_mjlab) | 宇树科技机器人强化学习实现，分别基于Isaac Lab和MuJoCo。 |
| **Humanoid-Gym** | 多校联合 (RoboterAX等) | [GitHub](https://github.com/roboterax/humanoid-gym) | 基于Isaac Gym的人形机器人强化学习训练框架，支持零样本迁移至真实机器人。 |
| **Dreamwaq轮足机器人强化学习库** | yusongmin1 (哈尔滨工程大学) | [GitHub](https://github.com/yusongmin1/Dreamwaq) | 面向轮足机器人的强化学习框架，复现DreamWaQ系列的CVAE隐式地形估计算法并支持视觉-本体感知融合，基于Isaac Gym训练、MuJoCo Sim2Sim验证，已在山猫M20轮足机器人实机部署，另含Go2倒立/后腿站立任务。（原始方法见KAIST的[DreamWaQ](https://arxiv.org/abs/2301.10602)，ICRA 2023；其改进版[DreamWaQ++](https://dreamwaqpp.github.io/)发表于T-RO 2026，暂未开源。） |

### 1.3 机械臂、抓取与操作

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **ManiSkill** | haosulab (Hillbot) | [GitHub](https://github.com/haosulab/ManiSkill) | SAPIEN操控技能框架，GPU并行化机器人仿真器和基准测试平台。 |
| **AnyGrasp** | 上海AI实验室 | [GitHub](https://github.com/graspnet/anygrasp_sdk) | 高效通用的6自由度抓取位姿估计算法，支持任意物体的机器人抓取检测。 |
| **vlm_arm** | 同济子豪兄 (TommyZihao) | [GitHub](https://github.com/TommyZihao/vlm_arm) | 机械臂+大模型+多模态 |
| **AgileX Cobot Magic** | 松灵机器人 (AgileX) | [GitHub](https://github.com/agilexrobotics) | 基于Mobile ALOHA架构的开源双臂移动操作平台，含PiPER机械臂、AGV底盘和深度相机。 |
| **RoboTwin双臂操作基准** | 港大/上海AI Lab/松灵 (陈天行等) | [GitHub](https://github.com/RoboTwin-Platform/RoboTwin) | 面向双臂协作操作的可扩展数据生成器与基准平台，内置强域随机化与50+任务，支持多种主流策略基线评测。CVPR 2025 Highlight。 |
| **MPlib** | haosulab | [GitHub](https://github.com/haosulab/MPlib) | 轻量级机械臂运动规划库，支持运动规划与碰撞检测，可结合 SAPIEN 使用。 |
| **PiPER ROS** | 松灵机器人（AgileX Robotics） | [GitHub](https://github.com/agilexrobotics/piper_ros) | PiPER 机械臂 ROS 工作空间，提供机械臂控制、模型与相关示例。 |

### 1.4 无人机与空中机器人

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **Prometheus自主无人机系统** | 阿木实验室 (amov-lab) | [GitHub](https://github.com/amov-lab/Prometheus) | 面向自主无人机的开源软件系统，支持目标检测、SLAM导航、编队控制等。 |
| **EGO-Planner** | 浙江大学FAST实验室 | [GitHub](https://github.com/ZJU-FAST-Lab/ego-planner) | 高效的无人机梯度引导在线局部规划器。 |
| **XTDrone无人机仿真平台** | robin-shaun | [GitHub](https://github.com/robin-shaun/XTDrone) | 基于PX4、ROS和Gazebo的无人机仿真平台，支持集群仿真。 |
| **浙江大学FAST实验室无人机项目** | 浙江大学FAST实验室 | [GitHub](https://github.com/ZJU-FAST-Lab/Fast-Drone-250) | 250mm自主无人机的硬件和软件设计。 |
| **香港科技大学空中机器人项目** | 香港科技大学 | [GitHub](https://github.com/HKUST-Aerial-Robotics/FIESTA) | 空中机器人在线运动规划的快速增量欧几里得距离场。 |
| **大疆Tello无人机SDK** | 大疆创新 (DJI) | [GitHub](https://github.com/dji-sdk/Tello-Python) | 大疆Tello系列无人机的Python SDK，支持编程控制和图像处理。 |
| **GCOPTER** | 浙江大学 FAST 实验室 | [GitHub](https://github.com/ZJU-FAST-Lab/GCOPTER) | 多旋翼飞行器轨迹优化框架，用于生成满足动力学约束的轨迹。 |

### 1.5 自动驾驶

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **Apollo自动驾驶平台** | 百度 | [GitHub](https://github.com/ApolloAuto/apollo) | 百度Apollo开源自动驾驶平台，国内最大的自动驾驶开源生态系统。 |
| **UniAD** | OpenDriveLab (上海AI实验室) | [GitHub](https://github.com/OpenDriveLab/UniAD) | CVPR 2023最佳论文，面向规划的统一自动驾驶框架，整合感知、预测和规划。 |
| **BEVFormer** | 上海AI实验室/南京大学 | [GitHub](https://github.com/fundamentalvision/BEVFormer) | ECCV 2022，基于纯相机的BEV感知框架，用于3D目标检测和语义地图分割。 |
| **DiffusionDrive端到端自动驾驶** | 华中科技大学 & 地平线 (hustvl) | [GitHub](https://github.com/hustvl/DiffusionDrive) | 面向实时端到端自动驾驶的截断扩散策略模型，NAVSIM基准达88.1 PDMS且以45 FPS实时运行，CVPR 2025 Highlight。 |

### 1.6 SLAM、感知与状态估计

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **视觉SLAM十四讲** | 高翔 | [GitHub](https://github.com/gaoxiang12/slambook2) | SLAM领域经典中文教程及配套代码，视觉SLAM入门必读。 |
| **VINS-Mono** | 香港科技大学 | [GitHub](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) | 鲁棒通用的单目视觉惯性状态估计器，VIO/SLAM领域经典项目。 |
| **VINS-Fusion** | 香港科技大学 | [GitHub](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) | 基于优化的多传感器状态估计器，支持单/双目相机+IMU融合。 |
| **LIO-SAM** | TixiaoShan | [GitHub](https://github.com/TixiaoShan/LIO-SAM) | 紧耦合激光惯性里程计（通过平滑和建图），被广泛引用的LiDAR SLAM方案。 |
| **FAST_LIO** | 港大MARS实验室 | [GitHub](https://github.com/hku-mars/FAST_LIO) | 计算高效且鲁棒的LiDAR惯性里程计，港大MARS实验室代表作。 |
| **FAST-LIVO2** | 港大MARS实验室 | [GitHub](https://github.com/hku-mars/FAST-LIVO2) | 快速、直接的LiDAR-惯性-视觉里程计，多传感器紧耦合方案。 |
| **R3LIVE** | 港大MARS实验室 | [GitHub](https://github.com/hku-mars/r3live) | 鲁棒、实时的RGB彩色LiDAR-惯性-视觉紧耦合状态估计与建图。 |
| **小觅双目相机系列** | 小觅智能 (MYNTAI) | [GitHub](https://github.com/slightech/MYNT-EYE-S-SDK) | 小觅双目相机系列，提供完整的SLAM和视觉算法解决方案。 |
| **宇树科技4D LiDAR SLAM** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/point_lio_unilidar) | 基于Point-LIO算法适配宇树L1 4D LiDAR的SLAM方案，仅使用点云与内置IMU。 |
| **Point-LIO** | 香港大学 MARS 实验室 | [GitHub](https://github.com/hku-mars/Point-LIO) | 高带宽激光惯性里程计，面向快速运动下的状态估计与建图。 |
| **InternNav** | 上海人工智能实验室（InternRobotics） | [GitHub](https://github.com/InternRobotics/InternNav) | 具身导航工具箱，基于 PyTorch、Habitat 与 Isaac Sim，提供视觉语言导航模型、训练和评测入口。 |

### 1.7 仿真、数据集与遥操作

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **Genesis** | Genesis-Embodied-AI | [GitHub](https://github.com/Genesis-Embodied-AI/genesis-world) | 面向机器人与具身智能学习的物理仿真平台，提供 Python 接口和多种物理求解器。 |
| **AgiBot-World** | OpenDriveLab (上海AI实验室) | [GitHub](https://github.com/OpenDriveLab/AgiBot-World) | IROS 2025最佳论文候选，面向可扩展和智能具身系统的大规模操控平台。 |
| **EmbodiedGen生成式3D世界引擎** | 地平线机器人 (Horizon Robotics) | [GitHub](https://github.com/HorizonRobotics/EmbodiedGen) | 面向具身智能的生成式3D世界引擎，将文本、图像编译为物理合理、可直接仿真的3D资产与场景，支持Isaac/MuJoCo/SAPIEN/Genesis等。 |
| **宇树科技MuJoCo仿真** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unitree_mujoco) | 基于MuJoCo的宇树机器人仿真环境，集成unitree_sdk2，包含MJCF模型和地形生成工具。 |
| **宇树科技Isaac Lab仿真** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unitree_sim_isaaclab) | 基于Isaac Lab的宇树机器人仿真环境，支持数据采集、回放和模型验证。 |
| **Open-TeleVision** | 多校联合 | [GitHub](https://github.com/OpenTeleVision/TeleVision) | 基于VR头显的沉浸式机器人遥操作系统，操作者通过第一视角实时控制机器人双臂完成灵巧操作。 |
| **宇树科技XR遥操作** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/xr_teleoperate) | 基于XR设备（Apple Vision Pro/Quest等）的H1/G1人形机器人遥操作系统，支持多种灵巧手。 |
| **OpenWBT人形全身遥操作** | 银河通用 & 清华大学 | [GitHub](https://github.com/GalaxyGeneralRobotics/OpenWBT) | 基于Apple Vision Pro的宇树G1/H1人形机器人全身遥操作系统，支持行走、下蹲、弯腰、抓取的真机与仿真控制。 |

### 1.8 SDK、工具、DIY创客与资源

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **宇树科技机器人SDK2** | 宇树科技 (Unitree) | [C++](https://github.com/unitreerobotics/unitree_sdk2) \| [Python](https://github.com/unitreerobotics/unitree_sdk2_python) | 宇树科技新一代机器人SDK，基于CycloneDDS，支持Go2/B2/H1/G1等机器人的开发与控制。 |
| **宇树科技四足机器人** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unitree_ros) | 宇树科技四足机器人Go1/Go2的ROS驱动包。 |
| **宇树科技ROS2** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unitree_ros2) | 宇树科技Go2/B2机器人的ROS2开发包，接口与unitree_sdk2一致。 |
| **宇树科技机器人控制教程** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unitree_guide) | 宇树科技四足机器人控制的开源教程项目，适合入门学习与参考。 |
| **超迷你机械臂机器人项目** | 稚晖君 (peng-zhihui) | [GitHub](https://github.com/peng-zhihui/Dummy-Robot) | 视频介绍：[【自制】我造了一台 钢 铁 侠 的 机 械 臂 ！【硬核】](https://www.bilibili.com/video/BV12341117rG) |
| **MiniRover火星车** | 稚晖君 (peng-zhihui) | [GitHub](https://github.com/peng-zhihui/MiniRover-Hardware) | 自制火星车的开源资料。 |
| **X-Bot智能机械臂写字机器人** | 稚晖君 (peng-zhihui) | [GitHub](https://github.com/peng-zhihui/X-Bot) | 基于CoreXY结构的机械臂。 |
| **ONE-Robot独轮机器人** | 稚晖君 (peng-zhihui) | [GitHub](https://github.com/peng-zhihui/ONE-Robot) | 基于IMU和STM32的独轮自平衡机器人。 |
| **ElectronBot迷你桌面机器人** | 稚晖君 (peng-zhihui) | [项目主页](https://github.com/peng-zhihui/ElectronBot) | 非常小巧的桌面机器人。 |
| **解魔方机器人** | 动力老男孩 | [项目主页](http://www.diy-robots.com/?page_id=46) | 基于乐高的解魔方机器人。 |
| **XLeRobot低成本双臂家用机器人** | 王高天 (Rice University) | [GitHub](https://github.com/Vector-Wangel/XLeRobot) | 约660美元的开源双臂移动家用机器人，兼容LeRobot生态，含3D打印硬件、仿真环境与VR/键盘/手柄遥操作，数小时可组装。 |
| **基于树莓派的目标识别与追踪** | 云飞机器人实验室 | [GitHub](https://github.com/automaticdai/rpi-object-detection) | 基于树莓派 + Web Camera的视觉追踪项目。 |
| **RoboWiki (云飞机器人中文百科)** | 云飞机器人实验室 | [GitHub](https://github.com/yfrobotics/robowiki) | 机器人领域的维基百科（公共知识编辑）。 |
| **Awesome-Robotics-Foundation-Models** | robotics-survey | [GitHub](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) | 机器人基础模型研究论文和项目汇总，包括RT-1、RT-2、OpenVLA等。 |
| **awesome-3dcv-papers-daily** | 3D视觉工坊 | [GitHub](https://github.com/qxiaofan/awesome-3dcv-papers-daily) | 主要记录计算机视觉、VSLAM、点云、结构光、机械臂抓取、三维重建、深度学习、自动驾驶等前沿paper与文章。 |

[↑ 返回顶部](#top)

---

<a id="embedded"></a>

## 🔌 2. 嵌入式系统 · Embedded Systems

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **PocketLCD: 带充电宝功能的便携显示器** | 稚晖君 (peng-zhihui) | [GitHub](https://github.com/peng-zhihui/PocketLCD) | 介绍视频：[【自制】你的下一个显示器，可能是个充电宝？？](https://www.bilibili.com/video/BV17D4y1X7AT) |
| **L-ink电子墨水屏NFC智能卡片** | 稚晖君 (peng-zhihui) | [GitHub](https://github.com/peng-zhihui/L-ink_Card) | 为了解决个人使用IC卡时遇到的一些痛点设计的一个迷你NFC智能卡片，基于STM32L051和ST25DV。 |
| **低成本激光投射虚拟键盘的设计制作** | 陈世凯 (CSK) |  | - [低成本激光投射虚拟键盘的设计制作-上(原理和硬件)](http://www.csksoft.net/blog/post/lowcost.laserkbd_part1.html) <br />- [低成本激光投射虚拟键盘的设计制作-下(算法与实现)](http://www.csksoft.net/blog/post/lowcost.laserkbd_part2.html) |
| **自制低成本3D激光扫描测距仪** | 陈世凯 (CSK) | [Google Code](https://code.google.com/archive/p/rp-3d-scanner/) | - [自制低成本3D激光扫描测距仪(3D激光雷达)，第一部分](http://www.csksoft.net/blog/post/lowcost_3d_laser_ranger_1.html) <br />- [自制低成本3D激光扫描测距仪(3D激光雷达)，第二部分](http://www.csksoft.net/blog/post/lowcost_3d_laser_ranger_2.html) |
| **NixieClock辉光管时钟** | Blanboom | [GitHub](https://github.com/blanboom/NixieClock) | 支持蓝牙 4.0 的辉光管时钟。 |
| **3D8光立方** | 官微宏 (aGuegu) | [项目主页](http://aguegu.net/?page_id=99) | 8 x 8 LED光立方。 |
| **Gameduino 2/3** | ExCamera / 云飞机器人实验室 | [Gameduino 2 (KS)](https://www.kickstarter.com/projects/2084212109/gameduino-2-this-time-its-personal?ref=discovery&term=Gameduino) \| [Gameduino 3 (KS)](https://www.kickstarter.com/projects/2084212109/gameduino-3?ref=discovery&term=Gameduino) | Gameduino是基于Arduino的图形交互和游戏扩展版。它是目前Arduino平台上性能最好的图形协处理器。它由ExCamera在Kickstarter上成功众筹。云飞实验室参与了工具链开发、中文手册 [(点击这里下载)](http://excamera.com/files/gd2book_cn.pdf) 以及中文推广。 |
| **妖姬 – 增强现实电子植物** | 云飞机器人实验室 | [GitHub](https://github.com/automaticdai/arduino-yaoji) | 妖姬是云飞实验室在极客大赛中的48小时极限创作作品。妖姬是一款概念式的互动电子植物，采用了Arduino + Android的方案，融合了信息与物理的概念式作品。 |
| **YF Smart Home** | 云飞机器人实验室 | [GitHub](https://github.com/yfrobotics/yf-home-iot) | 云飞智能家居项目旨在探索新的智能家居系统解决方案。 |
| **树莓派温湿度气象站** | 云飞机器人实验室 | [GitHub](https://github.com/automaticdai/rpi-environmental-sensing) | 基于树莓派的开源温湿度气象站。 |
| **ESP32智能家居开发板** | 乐鑫科技 (Espressif) | [GitHub](https://github.com/espressif/esp-idf) | ESP32系列芯片的官方开发框架和示例项目。 |
| **LicheeRV开发板项目** | 矽速科技 (Sipeed) | [GitHub](https://github.com/sipeed/LicheeRV-Nano-Build) | LicheeRV-Nano的构建项目和开发工具。 |
| **MaixPy** | 矽速科技（Sipeed） | [GitHub](https://github.com/sipeed/MaixPy) | 面向 MaixCAM 系列的 Python 边缘视觉与 AI 开发工具；K210 的 MicroPython 版本属于 MaixPy-v1。 |

[↑ 返回顶部](#top)

---

<a id="arch-os"></a>

## ⚙️ 3. 处理器架构及操作系统 · Architecture & OS

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **香山（XiangShan）开源处理器** | 中科院计算所 | [GitHub](https://github.com/OpenXiangShan/XiangShan) | 香山是一款开源的高性能 RISC-V 处理器。 |
| **RT-Thread** | Bernard Xiong | [GitHub](https://github.com/RT-Thread/rt-thread) | RT-Thread诞生于2006年，是一款以开源、中立、社区化发展起来的物联网操作系统。 |
| **TencentOS Tiny** | 腾讯 | [GitHub](https://github.com/Tencent/TencentOS-tiny) | 腾讯物联网终端操作系统（TencentOS tiny）是腾讯面向物联网领域开发的实时操作系统，具有低功耗，低资源占用，模块化，安全可靠等特点，可有效提升物联网终端产品开发效率。TencentOS tiny 提供精简的 RTOS 内核，内核组件可裁剪可配置，可快速移植到多种主流 MCU 及模组芯片上。而且，基于RTOS内核提供了丰富的物联网组件，内部集成主流物联网协议栈（如 CoAP/MQTT/TLS/DTLS/LoRaWAN/NB-IoT 等），可助力物联网终端设备及业务快速接入腾讯云物联网平台。 |
| **AimRT** | AimRT | [GitHub](https://github.com/AimRT/AimRT) | AimRT 是一个面向现代机器人领域的运行时开发框架。 它基于 Modern C++ 开发，轻量且易于部署，在资源管控、异步编程、部署配置等方面具有更现代的设计。AimRT 致力于整合机器人端侧、边缘端、云端等各种部署场景的研发。 它服务于现代基于人工智能和云的机器人应用，提供完善的调试和性能分析工具链，以及良好的可观测性支持。AimRT 还提供了全面的插件开发接口，具有高度可扩展性。 它与 ROS2、HTTP、Grpc 等传统机器人生态系统或云服务生态系统兼容，并支持对现有系统的逐步升级。 |
| **OpenHarmony** | 华为/开放原子基金会 | [Gitee](https://gitee.com/openharmony) | 面向全场景智能终端的开源分布式操作系统，支持从嵌入式设备到手机等多种形态，已广泛应用于IoT和机器人产品。 |

[↑ 返回顶部](#top)

---

<a id="ml"></a>

## 🧠 4. 机器学习 · Machine Learning

| 项目名称 | 发起人/作者 | 项目地址 | 项目介绍 |
| :--- | :--- | :---: | :--- |
| **UnifoLM世界模型** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unifolm-world-model-action) | 宇树科技开源的世界模型-动作架构(UnifoLM-WMA)，支持跨多种机器人形态的通用学习。 |
| **UnifoLM VLA** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unifolm-vla) | 面向通用人形机器人操作的视觉-语言-动作大模型(UnifoLM-VLA)。 |
| **unitree_IL_lerobot** | 宇树科技 (Unitree) | [GitHub](https://github.com/unitreerobotics/unitree_IL_lerobot) | 基于LeRobot框架的模仿学习工具，用于G1双臂灵巧手数据的训练与测试。 |
| **DeepSeek** | DeepSeek-AI | [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) \| [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | DeepSeek 模型是近年来在自然语言处理（NLP）领域备受瞩目的开源大规模语言模型系列。其最新版本 DeepSeek-V3 采用了混合专家（Mixture-of-Experts，MoE）架构，拥有 6710 亿个参数，每个词元（token）激活 370 亿个参数。该模型在多项基准测试中表现出色，性能媲美 GPT-4 和 Claude 等领先的闭源模型。 |
| **PaddleOCR** | 百度 | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | 支持100+语言的OCR工具包，提供文字检测、识别、版面分析等全流程能力，是GitHub上最受欢迎的中国AI项目之一。 |
| **ncnn** | 腾讯 | [GitHub](https://github.com/Tencent/ncnn) | 高性能神经网络推理框架，针对移动端和嵌入式设备优化，广泛应用于机器人端侧AI推理。 |
| **MNN** | 阿里巴巴 | [GitHub](https://github.com/alibaba/MNN) | 轻量级深度学习推理引擎，支持多种硬件后端，适用于移动端和边缘设备部署。 |
| **MiniCPM-o** | 面壁智能 (OpenBMB) | [GitHub](https://github.com/OpenBMB/MiniCPM-o) | Gemini 2.5 Flash级别的多模态语言模型，支持视觉、语音和全双工多模态直播，可在手机端运行。 |
| **YOLOX** | 旷视科技 (Megvii) | [GitHub](https://github.com/Megvii-BaseDetection/YOLOX) | 旷视科技开源的高性能无锚点YOLO目标检测器。 |
| **InternVL** | 上海AI实验室 | [GitHub](https://github.com/OpenGVLab/InternVL) | 开源多模态视觉-语言模型，对标GPT-4o，支持图像理解和多模态推理。 |
| **Yi** | 零一万物 (01.AI) | [GitHub](https://github.com/01-ai/Yi) | 零一万物开源大语言模型系列，从头训练，支持中英双语。 |
| **CogVLM2** | 智谱AI | [GitHub](https://github.com/THUDM/CogVLM2) | GPT4V级别的开源多模态视觉语言模型。 |
| **Step1X-Edit** | 阶跃星辰 (StepFun) | [GitHub](https://github.com/stepfun-ai/Step1X-Edit) | SOTA开源图像编辑模型，性能对标GPT-4o和Gemini 2 Flash。 |
| **TVM** | 陈天奇 | [GitHub](https://github.com/apache/tvm) | *Apache TVM* 是一个用于CPU、GPU 和机器学习加速器的开源机器学习编译器框架，旨在让机器学习工程师能够在任何硬件后端上高效地优化和运行计算。 |
| **MXNet（已归档）** | Apache MXNet 社区 | [GitHub](https://github.com/apache/mxnet) | 历史深度学习框架；官方仓库于 2023-11-17 归档，保留供旧项目维护与学习参考。 |
| **Caffe2** | 贾扬清 (Yangqing Jia) | [GitHub](https://github.com/facebookarchive/caffe2) | 深度学习编程框架，支持C++/Python/Matlab。现已与Pytorch合并。 |
| **PaddlePaddle** | 百度 | [GitHub](https://github.com/PaddlePaddle/Paddle) | 飞桨（PaddlePaddle）以百度多年的深度学习技术研究和业务应用为基础，集深度学习核心训练和推理框架、基础模型库、端到端开发套件、丰富的工具组件于一体，是中国首个自主研发、功能丰富、开源开放的产业级深度学习平台。 |
| **DeepVision** | 稚晖君 (peng-zhihui) | [GitHub](https://github.com/peng-zhihui/DeepVision) | 本项目实现了移动端CV算法快速验证框架，旨在提供一套通用的CV算法验证框架。框架经过本人一年多的开发和维护，目前已经完成绝大部分API的开发，实现包括实时视频流模块、单帧图像处理模块、3D场景模块、云端推理模块等众多功能。 |
| **MMDetection** | 商汤科技 | [GitHub](https://github.com/open-mmlab/mmdetection) | 商汤的目标检测工具箱及基准测试 |
| **ChatGLM** | 智谱AI | [GitHub](https://github.com/THUDM/ChatGLM-6B) | 开源双语对话语言模型，支持中英文对话。 |
| **Qwen** | 阿里云 | [GitHub](https://github.com/QwenLM/Qwen) | 阿里云通义千问大语言模型系列。 |
| **Baichuan** | 百川智能 | [GitHub](https://github.com/baichuan-inc/Baichuan2) | 百川智能开源大语言模型。 |
| **InternLM** | 上海AI实验室 | [GitHub](https://github.com/InternLM/InternLM) | 上海AI实验室开源的大语言模型。 |
| **Qwen2-VL** | 阿里云 | [GitHub](https://github.com/QwenLM/Qwen2-VL) | 阿里云通义千问多模态视觉-语言模型，广泛应用于VLA模型开发。 |
| **Wan2.1** | 阿里巴巴 | [GitHub](https://github.com/Wan-Video/Wan2.1) | 阿里巴巴开源的高质量视频生成大模型，支持文生视频，性能对标商业顶级模型。 |
| **HunyuanVideo** | 腾讯 | [GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo) | 腾讯开源的高分辨率视频生成模型，支持文生视频和图生视频，视频质量业界领先。 |
| **ControlNet** | 张吕敏 (Lvmin Zhang) | [GitHub](https://github.com/lllyasviel/ControlNet) | 为扩散模型添加条件控制的神经网络结构，支持姿态、深度、边缘等多种控制信号，极具影响力。 |
| **AnimateDiff** | 郭宇威等 | [GitHub](https://github.com/guoyww/AnimateDiff) | 即插即用的视频动画模块，无需额外训练即可将现有图像扩散模型转化为视频生成器。 |
| **CogVideoX** | 智谱AI/清华大学 | [GitHub](https://github.com/THUDM/CogVideo) | 开源视频生成大模型，生成质量优秀，支持文生视频和图生视频。 |
| **Janus** | DeepSeek | [GitHub](https://github.com/deepseek-ai/Janus) | 统一多模态理解与生成的框架，通过解耦视觉编码解决理解与生成任务之间的冲突。 |
| **GroundingDINO** | IDEA Research | [GitHub](https://github.com/IDEA-Research/GroundingDINO) | 开放集目标检测框架，通过自然语言描述实现任意类别目标的定位，零样本检测能力强。 |
| **FunASR** | 阿里达摩院 | [GitHub](https://github.com/modelscope/FunASR) | 工业级端到端语音识别工具链，支持语音识别、标点恢复、说话人分离等任务。 |
| **ChatTTS** | 2noise | [GitHub](https://github.com/2noise/ChatTTS) | 专为对话设计的高质量中英文语音合成模型，支持细粒度韵律控制（停顿、笑声等）。 |
| **Kimi K2** | 月之暗面（Moonshot AI） | [GitHub](https://github.com/MoonshotAI/Kimi-K2) | 面向推理、编码和工具调用的 MoE 语言模型，含 Base 与 Instruct 模型入口。 |
| **MiniMax-M2** | MiniMax | [GitHub](https://github.com/MiniMax-AI/MiniMax-M2) | 面向编码和智能体工作流的语言模型，提供模型使用与部署说明。 |
| **GLM-4.6V** | 智谱AI (Z.ai) | [GitHub](https://github.com/zai-org/GLM-V) | 多模态视觉推理大模型，支持思维链推理与可扩展强化学习，含106B-A12B云端版与9B-Flash端侧版。 |
| **Hunyuan3D-2.1** | 腾讯混元 | [GitHub](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) | 首个生产级开源3D资产生成模型，支持图像到高保真3D+PBR材质，含完整训练代码与权重。 |
| **HunyuanWorld** | 腾讯混元 | [GitHub](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) | 首个开源、可仿真、沉浸式3D世界生成模型，从文本或图像生成可交互的3D场景。 |

[↑ 返回顶部](#top)

---

<details>
<summary><strong>📌 收录与使用说明</strong></summary>

收录不等于代码、权重、数据和硬件均采用同一开源许可。使用前请查看对应仓库的 LICENSE、模型卡和授权说明。历史条目尚未逐项重新核实，本轮核查范围见 [更新记录](CHANGELOG.md)。

</details>

<a id="credits"></a>

## 🤝 推荐与收录

如果你发现了适合本清单的机器人、具身智能、嵌入式系统或 AI 项目，欢迎通过 [Issue](https://github.com/ShuaixinHuang/awesome-robotics/issues) 推荐，或提交 Pull Request 将项目加入清单，一起完善这份资源合集。


<div align="center">

**发现好项目，一起完善这份清单。**

[参与贡献](CONTRIBUTING.md) · [更新记录](CHANGELOG.md) · [返回顶部 ↑](#top)

</div>
