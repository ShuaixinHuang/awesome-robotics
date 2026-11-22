# 机器人实践路线

按目标选择最短路径。先用示例或已有数据跑通流程，再增加硬件和训练成本。

| 目标 | 起点 | 下一步 | 跑通的标志 |
| --- | --- | --- | --- |
| 零硬件理解仿真 | [MuJoCo 入门](https://mujoco.readthedocs.io/en/stable/overview.html) + [Menagerie 模型](https://github.com/google-deepmind/mujoco_menagerie) | 加载模型，查看关节、执行器与传感器，再修改控制输入 | 能解释模型状态与控制输入的对应关系 |
| 机械臂采集与模仿学习 | [LeRobot 官方文档](https://huggingface.co/docs/lerobot)；图形操作可从 [LeLab](https://github.com/huggingface/leLab) 开始 | 选受支持硬件 → 校准 → 遥操作 → 记录 episode → 检查回放 → 训练策略 | 数据的动作、图像和时间轴对应正确，再开始训练 |
| 已有数据研究 VLA | [OpenPI](https://github.com/Physical-Intelligence/openpi#readme) | 先运行官方推理示例，再检查数据格式、动作空间和模型配置，按官方示例微调 | 自有样本能通过数据转换与推理；评估与训练数据分离 |
| ROS 2 机械臂应用 | [MoveIt 2 教程](https://moveit.picknik.ai/main/index.html) | 先在示例机器人中规划，再接入自己的 URDF、关节限制和控制器 | 仿真中完成碰撞检查、规划与执行 |

## 选择前确认

- **数据与硬件：** 确认关节顺序、单位、频率、相机标定和动作空间。训练与部署配置应保持一致。
- **计算资源：** 浏览数据、仿真、训练和部署的资源需求不同；按对应项目的安装说明选择环境。
- **许可：** 项目代码、模型权重与数据集分别查看许可证或模型卡。
- **真机操作：** 先完成标定、关节限位、低速验证和急停检查，再运行策略。

## 维护本清单

从仓库根目录运行，无需第三方依赖或联网：

```bash
python scripts/check_catalog.py
```

检查资源总数、四大方向计数、四列表格连续性、重复名称与内部导航。外部仓库的可访问性和内容更新依据每期列出的官方来源人工核查。

[返回资源导航](../README.md#navigation)
