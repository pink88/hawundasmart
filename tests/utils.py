from pytest_homeassistant_custom_component.common import load_json_value_fixture
import json

def deserialize_get_devices_fixture(data):
    data = json.loads(data)
    devices = data.get("devices")
    if devices:
        data["devices"] = {int(k): v for k, v in devices.items()}

    for device_id, device in devices.items():
        device.setdefault("device_id", int(device_id))
        device.setdefault("hw_version", 4.0)

    return data
