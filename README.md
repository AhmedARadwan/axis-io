# AxisIO Library

The AxisIO library provides a simple interface to control the IOs of Axis cameras. It allows you to turn on/off the IO ports, set pulse times, and retrieve port information.

## Installation

You can install the AxisIO library using pip:

```shell
pip install .
```

## Usage

```python
from axisio import AxisIO

# Create an instance of AxisIO
camera = AxisIO("CAMERA_IP", "USERNAME", "PASSWORD")

# Turn off port 1
camera.turn_off(1)

# Send a pulse to port 1 with a pulse time of 200ms
camera.send_pulse(1, 200)

# Turn on port 1
camera.turn_on(1)
```

## Documentation

The library provides the following methods:

- `turn_on(port_num)`: Turns on the specified port.
- `turn_off(port_num)`: Turns off the specified port.
- `send_pulse(port_num, pulse_time)`: Sends a pulse to the specified port with the given pulse time.
- `check_port_state()`: Checks the state of the ports and turns off any ports that have been on for longer than the specified delay.
- `get_port_state(port_num)`: Returns the state of the specified port (ON or OFF).
- `get_port_info(port_num)`: Retrieves information about the specified port.

## Contributing

Contributions to the AxisIO library are welcome! If you find a bug or have a suggestion for improvement, please open an issue. If you would like to contribute code, you can fork the repository, make your changes, and submit a pull request.

Please ensure that your code follows the project's coding conventions and includes appropriate tests.

## License

The AxisIO library is licensed under the MIT License.