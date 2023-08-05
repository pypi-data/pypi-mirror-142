"""Test Main Module

.. todo::

    Add tests for I2C communication, as a way to test the main board without I/O
    board attached to it. The tests provided here assume physical relays are in 
    place, since it uses the Raspberry Pi GPIOs to assert the relay state. The 
    I2C bus of the Raspberry Pi can be used for this purpose.
"""


import asyncio
import logging
import sys

from teramesh_hardware_tester.tester import getch

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

logger = logging.getLogger('test')


test_calibration_temperature = None
test_calibration_humidity = None

#: Raspberry Pi common GPIO output
RELAY_COMMON_GPIO = 5
#: Raspberry Pi GPIO input
RELAY_GPIO_MAP = {
    1: 4,
    2: 17,
    3: 27,
    4: 22,
    5: 23,
    6: 24,
    7: 25,
}


async def setup(AT):
    global test_calibration_temperature
    global test_calibration_humidity
    try:
        from teramesh_hardware_tester.idrc_esp_tools.sht85 import single_shot
        test_calibration_temperature, test_calibration_humidity = single_shot()
    except Exception as e:
        logger.warning('SHT85 failed to read: %s', e)


async def test_comms(AT):
    """Test Communications
    
    This function internally uses the ``TESTCOMMS`` cat command.
    """

    await AT.TESTCOMMS.execute()
    await AT.TESTCOMMS.expect_ok_or_error()


async def test_shtc3(AT):
    """Test SHTC3
    
    This function internally uses the ``TESTSHTC3`` cat command.
    """

    global test_calibration_temperature
    global test_calibration_humidity
    await AT.TESTSHTC3.execute()
    result = await AT.TESTSHTC3.expect_reply()
    temperature, humidity = result.strip().split(',')
    logger.info('SHTC3 temperature %s', temperature)
    logger.info('SHTC3 humidity %s', humidity)
    # FIXME: TODO: RPi could be connected to a calibration source and compare these to some ground truth
    assert 10 < float(temperature) < 50, 'SHTC3 returned erroneous temperature'
    assert 0 < float(humidity) < 100, 'SHTC3 returned erroneous humidity'
    if test_calibration_temperature is not None:
        logger.info('SHTC3 temperature offset: %f', test_calibration_temperature - float(temperature))
    if test_calibration_humidity is not None:
        logger.info('SHTC3 humidity offset: %f', test_calibration_humidity - float(humidity))


async def test_buzzer(AT):
    """Test buzzer
    
    This function internally uses the ``TESTBUZZ`` cat command.
    """

    await AT.TESTBUZZ.execute()
    await AT.TESTBUZZ.expect_ok_or_error()
    logger.critical('Did the buzzer buzz (y/n)?')
    assert getch().lower() == 'y', 'Buzzer did not buzz'


async def test_led(AT):
    """Test LED display
    
    This function internally uses the ``TESTLED`` cat command.
    """

    await AT.TESTLED.execute()
    await AT.TESTLED.expect_ok_or_error()
    logger.critical('Did the LED screen do the thing (y/n)?')
    assert getch().lower() == 'y', 'LED did not do the thing'


async def test_pir(AT):
    """Test PIR
    
    This function internally uses the ``TESTPIR`` cat command.
    """

    logger.critical('Please WAVE AT PIR!')
    await AT.TESTPIR.execute()
    result = await AT.TESTPIR.expect_reply(timeout=10)
    assert int(result) == 1, 'PIR did not detect waving'


async def test_btn(AT):
    """Test button
    
    This function internally uses the ``TESTBTN`` cat command.
    """

    # TESTBTN handler waits for 5 seconds
    await AT.TESTBTN.execute()
    logger.critical('Please PRESS DEV KEY!')
    await AT.TESTBTN.expect_ok_or_error(timeout=15)


def relays_setup():
    if GPIO is None:
        assert False, 'RPi GPIO module is not installed!'
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_COMMON_GPIO, GPIO.OUT)
    GPIO.output(RELAY_COMMON_GPIO, GPIO.HIGH)
    for relay_pin in RELAY_GPIO_MAP.values():
        GPIO.setup(relay_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

async def _test_relay(AT, relay_no: int):
    """Generic Test Relay

    This function internally uses the ``TESTRELAY`` cat command.

    This function first turns off the relay, then turns it on, and finally 
    turns it off again. At every step it checks through the Raspberry Pi GPIOs 
    if the relay state is the expected one.

    ``RELAY_COMMON_GPIO`` is used to produce an output signal, and the 
    ``RELAY_GPIO_MAP`` inputs are connected to it through the relays. This way,
    the program can assert if the relay is on or off.

    :param AT:
    :param relay_no: Relay number, from 1 to 7
    """

    relays_setup()
    try:
        await AT.TESTRELAY0.execute()
        try:
            await AT.TESTRELAY0.expect_ok_or_error()
        except Exception:
            pass
        relay_pin = RELAY_GPIO_MAP[relay_no]
        await getattr(AT, f'TESTRELAY{relay_no}').execute()
        await getattr(AT, f'TESTRELAY{relay_no}').expect_ok_or_error()
        await asyncio.sleep(0.1)
        assert GPIO.input(relay_pin), f'Relay {relay_no} did not open'
        await AT.TESTRELAY0.execute()
        await AT.TESTRELAY0.expect_ok_or_error()
        await asyncio.sleep(0.1)
        assert not GPIO.input(relay_pin), f'Relay {relay_no} did not close'
    finally:
        await AT.TESTRELAY0.execute()
        GPIO.cleanup()

async def test_relay1(AT):
    await _test_relay(AT, 1)

async def test_relay2(AT):
    await _test_relay(AT, 2)

async def test_relay3(AT):
    await _test_relay(AT, 3)

async def test_relay4(AT):
    await _test_relay(AT, 4)

async def test_relay5(AT):
    await _test_relay(AT, 5)

async def test_relay6(AT):
    await _test_relay(AT, 6)

async def test_relay7(AT):
    await _test_relay(AT, 7)

async def test_relays_4_and_6(AT):
    relays_setup()
    try:
        await AT.TESTRELAY0.execute()
        try:
            await AT.TESTRELAY0.expect_ok_or_error()
        except Exception:
            pass
        # turn on relay 4
        await AT.TESTRELAY4.execute()
        await AT.TESTRELAY4.expect_ok_or_error()
        await asyncio.sleep(0.1)
        assert GPIO.input(RELAY_GPIO_MAP[4]), 'Relay 4 did not open'
        # turn on relay 6
        await AT.TESTRELAY6.execute()
        await AT.TESTRELAY6.expect_ok_or_error()
        await asyncio.sleep(0.1)
        assert GPIO.input(RELAY_GPIO_MAP[6]), 'Relay 6 did not open'
        # after that relay 4 should turn off
        await asyncio.sleep(0.1)
        assert not GPIO.input(RELAY_GPIO_MAP[4]), 'Relay 4 did not close'
    finally:
        await AT.TESTRELAY0.execute()
        GPIO.cleanup()
