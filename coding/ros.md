---
title: ROS and Gazebo
---


ROS
---

- Noetic does not work with "/" in frame id
- What's the use of package.xml?


Gazebo
------

- `gazebo/gazebo.hh` includes a core set of basic gazebo functions. It doesn't
  include gazebo/physics/physics.hh, gazebo/rendering/rendering.hh, or
  gazebo/sensors/sensors.hh as those should be included on a case by case basis.
- All plugins must be in the gazebo namespace.
- Plugin types:
  - World
  - Model
  - Sensor
  - System
  - Visual
  - GUI


RL
--

- 1d action space: td3_1_61


Progress Report
---------------

- ROS basics
  - Pub Sub
  - Custom Msg and Srv
  - Record and Play with Bag
- Rviz
  - Markers
  - Interactive markers
  - Interactive marker server
  - Plugins
    - Display (add func to visualize unsupported messages)
    - How useful are rviz plugs
- Gazebo
  - Model editor
  - Plugin (6 types)
    - Model
    - World
    - System
    - How plugin of two types at once?
    - How know which type to use?
- Random
  - catkin_install_python
  - shit to catkin tools
  - boost pointer casting and ADL
  - debugging gz plugs w gdb
- Todo
  - Understand rqt graph
  - Gz plugs and where to get docs
  - Use case of rviz plugs
  - Actual workflow of dbg gz plug

- point cloud
- ground segmentation
- lidar pc ground subtraction
- edge detection from extract image

