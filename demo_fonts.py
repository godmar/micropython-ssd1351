"""SSD1351 demo (fonts)."""
from time import sleep
from ssd1351 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont


def test():
    """Test code."""
    spi = SPI(0, baudrate=14500000, sck=Pin(2), mosi=Pin(3))
    display = Display(spi, dc=Pin(6), cs=Pin(5), rst=Pin(4))

    print("Loading fonts, please wait.")
    arcadepix = XglcdFont('fonts/ArcadePix9x11.c', 9, 11)
    bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
    broadway = XglcdFont('fonts/Broadway17x15.c', 17, 15)
    espresso_dolce = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)
    fixed_font = XglcdFont('fonts/FixedFont5x8.c', 5, 8)
    neato = XglcdFont('fonts/Neato5x7.c', 5, 7, letter_count=223)
    robotron = XglcdFont('fonts/Robotron7x11.c', 7, 11)
    unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
    wendy = XglcdFont('fonts/Wendy7x8.c', 7, 8)
    print("Fonts loaded.")

    display.draw_text(0, 0, 'Arcade Pix 9x11', arcadepix, color565(255, 0, 0))
    display.draw_text(0, 12, 'Bally 7x9', bally, color565(0, 255, 0))
    display.draw_text(0, 23, 'Broadway', broadway, color565(0, 0, 255))
    display.draw_text(0, 36, 'Espresso', espresso_dolce,
                      color565(0, 255, 255))
    display.draw_text(0, 64, 'Fixed Font 5x8', fixed_font,
                      color565(255, 0, 255))
    display.draw_text(0, 76, 'Neato 5x7', neato, color565(255, 255, 0))
    display.draw_text(0, 85, 'Robotron 7x11', robotron,
                      color565(255, 255, 255))
    display.draw_text(0, 96, 'Unispace', unispace, color565(255, 128, 0))
    display.draw_text(0, 120, 'Wendy 7x8', wendy, color565(255, 0, 128))

    sleep(9)
    display.clear()

    display.draw_text(0, 0, 'Arcade Pix 9x11', arcadepix,
                      color565(255, 0, 0),
                      landscape=True)
    display.draw_text(12, 0, 'Bally 7x9', bally, color565(0, 255, 0),
                      landscape=True)
    display.draw_text(23, 0, 'Broadway', broadway, color565(0, 0, 255),
                      landscape=True)
    display.draw_text(36, 0, 'Espresso', espresso_dolce,
                      color565(0, 255, 255), landscape=True)
    display.draw_text(64, 0, 'Fixed Font 5x8', fixed_font,
                      color565(255, 0, 255), landscape=True)
    display.draw_text(76, 0, 'Neato 5x7', neato, color565(255, 255, 0),
                      landscape=True)
    display.draw_text(85, 0, 'Robotron 7x11', robotron,
                      color565(255, 255, 255),
                      landscape=True)
    display.draw_text(96, 0, 'Unispace', unispace, color565(255, 128, 0),
                      landscape=True)
    display.draw_text(120, 0, 'Wendy 7x8', wendy, color565(255, 0, 128),
                      landscape=True)

    sleep(9)
    display.clear()

    display.draw_text(0, 0, 'Arcade Pix 9x11', arcadepix, color565(255, 0, 0),
                      background=color565(0, 255, 255))
    display.draw_text(0, 12, 'Bally 7x9', bally, color565(0, 255, 0),
                      background=color565(0, 0, 128))
    display.draw_text(0, 23, 'Broadway', broadway, color565(0, 0, 255),
                      background=color565(255, 255, 0))
    display.draw_text(0, 36, 'Espresso', espresso_dolce,
                      color565(0, 255, 255), background=color565(255, 0, 0))
    display.draw_text(0, 64, 'Fixed Font 5x8', fixed_font,
                      color565(255, 0, 255), background=color565(0, 128, 0))
    display.draw_text(0, 76, 'Neato 5x7', neato, color565(255, 255, 0),
                      background=color565(0, 0, 255))
    display.draw_text(0, 85, 'Robotron 7x11', robotron,
                      color565(255, 255, 255),
                      background=color565(128, 128, 128))
    display.draw_text(0, 96, 'Unispace', unispace, color565(255, 128, 0),
                      background=color565(0, 128, 255))
    display.draw_text(0, 120, 'Wendy 7x8', wendy, color565(255, 0, 128),
                      background=color565(255, 255, 255))

    sleep(9)
    display.cleanup()


test()
