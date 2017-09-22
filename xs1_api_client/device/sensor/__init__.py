from xs1_api_client.api_constants import Node
from xs1_api_client.device import XS1Device


class XS1Sensor(XS1Device):
    """
    Represents a XS1 Sensor
    """

    def __init__(self, state, api):
        super(XS1Sensor, self).__init__(state, api)

    def __str__(self):
        return "Sensor: " + super(XS1Sensor, self).__str__()

    def update(self) -> None:
        """
        Updates the state of this sensor
        """
        response = self._api_interface.get_state_sensor(self.id())
        new_value = self._get_node_value(response, Node.SENSOR)
        self.set_state(new_value)

    def set_value(self, value) -> None:
        """
        Sets a value for this sensor
        This should only be used for debugging purpose!
        :param value: new value to set
        """
        response = self._api_interface.set_sensor_value(self.id(), value)
        new_value = self._get_node_value(response, Node.SENSOR)
        self.set_state(new_value)
