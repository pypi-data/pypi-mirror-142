import pytest
from unittest import mock

from cores_ft.get_info import get_lm_sensors_info, read_cpuinfo


@pytest.fixture
def cpuinfo():
    core0 = 'cpu MHz         : 2195.050'
    core1 = 'cpu MHz         : 2000.050'
    core2 = 'cpu MHz         :   95.050'

    return '\n'.join((core0, core1, core2))


@pytest.fixture
def sensors():
    core0 = 'Core 0:        +62.0°C  (high = +85.0°C, crit = +105.0°C)'
    core1 = 'Core 1:        +60.0°C  (high = +85.0°C, crit = +105.0°C)'

    return '\n'.join((core0, core1))


def test_read_cpuinfo(mocker, cpuinfo):

    mock_open = mock.mock_open(read_data=cpuinfo)

    mocker.patch('builtins.open', mock_open)

    freq = read_cpuinfo()

    assert len(freq) == 3
    assert freq == {'core_0': 2.19505, 'core_1': 2.00005, 'core_2': 0.09505}


def test_get_info_sensors(mocker, sensors):

    mock_open = mock.mock_open(read_data=sensors)

    mocker.patch('builtins.open', mock_open)

    temp = get_lm_sensors_info()

    assert len(temp) == 2
    assert temp == {'core_0': '+62.0°C', 'core_1': '+60.0°C'}
