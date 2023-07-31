# CS229-SuperMario-Project
CS229 Final Project

# Reinforcement Learning in Super Mario Bros: Impact of Learning Rates on PPO Algorithm

## Visualizations

![Project](mario.jpg)


## Abstract
Reinforcement learning algorithms, especially Proximal Policy Optimization (PPO), have gained popularity in artificial intelligence studies, particularly in complex environments like video games. This research explores the influence of different learning rates on the PPO algorithm's performance within the iconic video game, Super Mario Bros. A convolutional neural network (CNN) acts as the policy model, interpreting visual inputs from the game. The study identifies a learning rate of 3e-4 as optimal for the AI agent to navigate the game's first level effectively. The findings contribute valuable insights into optimizing learning parameters in reinforcement learning applications, specifically for PPO in gaming environments.

## Introduction
Reinforcement learning has a vast range of applications, with game playing being an intriguing challenge, especially in dynamic environments like Super Mario Bros. This project aims to refine the application of the PPO algorithm, known for its computational efficiency and ease of implementation. The focus lies on investigating the impact of varying learning rates on the PPO algorithm's performance within the Super Mario Bros environment. The research sheds light on effective tuning strategies for PPO in complex gaming environments, offering insights for real-world problems like autonomous vehicle navigation and financial trading strategies.

## Method
The study utilizes Proximal Policy Optimization (PPO), a policy gradient technique in reinforcement learning. PPO balances exploration and exploitation, ensuring the agent learns effectively without destabilizing the policy. The value function, defined as the game's objective, motivates the agent to maximize the reward function. Preprocessing techniques, including GrayScaleObservation, DummyVecEnv, and VecFrameStack, prepare the input data for efficient interaction with the RL algorithm. The Super Mario Bros environment is created using the gym_super_mario_bros library, allowing the agent to navigate and maximize game rewards.

## Experiments and Results
The experiments test four learning rates: 10^-5, 10^-4, 3 * 10^-4, and 10^-3. A learning rate of 3 * 10^-4 yielded the most consistent performance in the first level of Super Mario Bros. Higher learning rates (10^-3) resulted in unstable performance, while lower rates (10^-5) led to suboptimal learning. Learning rates of 10^-4 and 3 * 10^-4 showed more stable and effective learning over time, with the latter offering the most consistent performance overall.

## Conclusion
The study's findings highlight the significant impact of learning rates on the PPO algorithm's performance in Super Mario Bros. An optimal learning rate of 3e-4 was identified for the AI agent to navigate the game effectively. This research provides valuable insights into optimizing learning parameters in reinforcement learning applications, specifically in gaming environments. Future studies could explore different reinforcement learning algorithms and hyperparameters to gain a comprehensive understanding of effective tuning strategies in complex environments.
