# Wave Teleoperation

## Requirements

```
sudo apt install ros-kinetic-teleop-twist-joy ros-kinetic-joy
```



## Connecting

### PS4
1. Hold the PlayStation logo and Share buttons to put the controller into "pairing" mode (the Light Bar/LED should start to rapidly blink/flash), then pair the controller with the computer using the bluetooth settings (Show Applications → Settings → Bluetooth → Wireless Controller or bluetooth icon (at the top-right of the screen) → bluetooth icon (in sub-menu) → Bluetooth Settings → Wireless Controller).

2. Once the controller is "paired", you can turn it on by pressing (not holding!) the PlayStation logo button.

### XB1

1. Hold down the xbox button until it starts flashing
2. Follow the same pairing instructions as PS4

### Other BT Controllers

Virtually all other bluetooth controllers function the same way.

### Wired controllers

Most BT controllers can operate in wired mode, this requires no setup and should appear immediately in jstest.
## Additional Software

JSTest for configuring your joystick and finding out which axes and buttons correspond to which indexes.
```
sudo apt install jstest-gtk
```

to use simply run

```
jstest-gtk
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/2769347/57462375-1566fd80-72bc-11e9-83b4-c59702ffcee7.png" width="350" title="hover text">
  <img src="https://user-images.githubusercontent.com/2769347/57462391-1d26a200-72bc-11e9-901d-12e03dd87da9.png" width="350" alt="accessibility text">
</p>


## Running

From within a workspace after sourcing setup.bash
```
roslaunch launch/joy.launch

```
if you need to configure the publish topic change the launch file as shown 
```  
<node pkg="teleop_twist_joy" name="teleop_twist_joy" type="teleop_node">
  <rosparam command="load" file="$(find wave_joy_teleop)/joystick_param.yaml"/>
  <remap from="cmd_vel" to="operation_treadstone/cmd_vel" />
</node>
```
For standalone running you can simply use

```
rosparam load joystick_param.yaml
rosrun joy_teleop joy_teleop.py
```

Then be sure to hold down the enable switch (Default 4 which is LB on XB1)

## Configuration

The joystick_param.yaml contains controller settings such as scaling and which joysticks control what ranges of motion.

* enable_button:  the index of the button to enable broadcasting of cmd_vel messages
* axis_linear: which joystick axis controls linear movement
* axis_angular: which joystick axis controls angular movement

## Package Info

Package name wave_joy_teleop
