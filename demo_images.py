"""SSD1351 demo (images)."""
from time import sleep
from ssd1351 import Display
from machine import Pin, SPI


def test():
    """Test code."""
    spi = SPI(0, baudrate=14500000, sck=Pin(2), mosi=Pin(3))
    display = Display(spi, dc=Pin(6), cs=Pin(5), rst=Pin(4))

    display.draw_image('images/RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.draw_image('images/MicroPythonW128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.draw_image('images/Tabby128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.draw_image('images/Tortie128x128.raw', 0, 0, 128, 128)
    sleep(9)

    display.cleanup()


test()
