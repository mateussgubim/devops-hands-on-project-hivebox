[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

## Project Architecture
![hivebox](https://devopsroadmap.io/assets/images/hivebox-architecture-a7fe504c22027e87b6f7b188cd57d2d8.png)

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---

## Current Progress

| Phase   | Progress   |
| ------- | ---------- |
| Phase 1 | ✅ Done    |
| Phase 2 | ✅ Done    |
| Phase 3 | ♾️ Pending |
| Phase 4 | ♾️ Pending |
| Phase 5 | ♾️ Pending |
| Phase 6 | ♾️ Pending |

## Phase 1
This phase has two objectives:
 - Create a GitHub account and fork the repository;
 - Create a GitHub [project board](https://github.com/users/mateussgubim/projects/1/views/1)
   
   My choice was a Kanban style template.

## Phase 2
In this phase a simple python script that prints the application version should be created and containerized.

To run and test it in your local machine:
```bash
# Building the image
docker build  -t hivebox:v0.0.1 . 

# Running the container:
docker run --rm hivebox:v0.0.1
```

## Phase 3
