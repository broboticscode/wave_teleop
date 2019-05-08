# Wave Teleoperation

## Requirements

```
sudo apt install ros-kinetic-teleop-twist-joy ros-kinetic-joy
```

## Running

```
roslaunch launch/joy.launch
```

Then be sure to hold down the enable switch (Default 4 which is LB on XB1)

## Configuration

The joystick_param.yaml contains controller settings such as scaling and which joysticks control what ranges of motion.

* enable_button:  the index of the button to enable broadcasting of cmd_vel messages
* axis_linear: which joystick axis controls linear movement
* axis_angular: which joystick axis controls angular movement
