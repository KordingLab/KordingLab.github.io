---
title: Robots
permalink: /robots/

---

<style>
.robot-thumbnail {
  max-width: 200px; /* Adjust the maximum width as per your requirement */
  height: auto;
}

.list-item-robot {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center the items horizontally */
  justify-content: center; /* Center the items vertically */
  text-align: center;
  margin-bottom: 4px;
  padding: 5px;
}

.row {
  display: flex;
  justify-content: center; /* Center the rows horizontally */
}

.robot-name {
  font-size: 20px; /* Adjust the font size as per your preference */
  margin-bottom: 10px; !important;/* Add spacing below the robot name */
}

.robot-caption-container {
  max-width: 200px;
  height: 70px; /* Adjust the height as needed */
  overflow: hidden;
}

.robot-caption {
  font-size: 13px;
  display: block;
  margin-top: -55px; /* Adjust the negative margin to show the caption */
  transition: margin-top 0.3s ease;
}

.list-item-robot:hover .robot-caption {
  margin-top: 0; /* Show the full caption on hover */
}
</style>

<div class="pos_header">
  <h3>Robots</h3>
</div>

<div class="content list robots">
  <div class="row">
    <div class="list-item-robot">
      <img class="robot-thumbnail" src="{{ site.baseurl }}/images/robots/bigarm.jpg">
      <span class="robot-name">Frank Emika Panda</span>
      <div class="robot-caption-container">
        <span class="robot-caption">2 7DoF robots arms that provide access to creative ranges of motion</span>
      </div>
    </div>

    <div class="list-item-robot">
      <img class="robot-thumbnail" src="{{ site.baseurl }}/images/robots/jetracer.jpg">
      <span class="robot-name">NVIDIA Jetracer</span>
      <div class="robot-caption-container">
        <span class="robot-caption">Programmable RC Car with a sensor suite and onboard computation by Nvidia Jetson</span>
      </div>
    </div>

    <div class="list-item-robot">
      <img class="robot-thumbnail" src="{{ site.baseurl }}/images/robots/minicopter.jpg">
      <span class="robot-name">ModalAI Voxal Drone</span>
      <div class="robot-caption-container">
        <span class="robot-caption">2x quadcopters, running Px4</span>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="list-item-robot">
      <img class="robot-thumbnail" src="{{ site.baseurl }}/images/robots/quadruped.jpg">
      <span class="robot-name">Unitree Go1 Edu</span>
      <div class="robot-caption-container">
        <span class="robot-caption">Quadrupedal robot with low-level torque control and a fancy sensor suite</span>
      </div>
    </div>

    <div class="list-item-robot">
      <img class="robot-thumbnail" src="{{ site.baseurl }}/images/robots/roomba.jpg">
      <span class="robot-name">iRobot Create3</span>
      <div class="robot-caption-container">
        <span class="robot-caption">Robot equipped with useful sensors and used for path planning testing</span>
      </div>
    </div>

    <div class="list-item-robot">
      <img class="robot-thumbnail" src="{{ site.baseurl }}/images/robots/turtlebot.jpg">
      <span class="robot-name">Turtlebot3 Burger</span>
      <div class="robot-caption-container">
        <span class="robot-caption">Robot running Raspberry Pi often used for algorithmic testing</span>
      </div>
    </div>
  </div>
</div>















