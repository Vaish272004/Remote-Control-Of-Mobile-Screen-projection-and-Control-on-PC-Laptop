import subprocess


package_name = "pillow"
subprocess.run(["pip", "install", package_name])

package_name1 = "pyautogui"
subprocess.run(["pip", "install", package_name1])


import pyautogui
from PIL import Image


laptop_width = 1920
laptop_height = 1080


redmi_width = 1080
redmi_height = 2400


scaled_redmi_height = laptop_height
scaled_redmi_width = int(scaled_redmi_height * (redmi_width / redmi_height))


left = (laptop_width - scaled_redmi_width) // 2
top = (laptop_height - scaled_redmi_height) // 2


screenshot = pyautogui.screenshot(region=(left, top, scaled_redmi_width, scaled_redmi_height))


grayscale_image = screenshot.convert('L')


grayscale_image.save("redmi_note9_pro_grayscale.png")


grayscale_image.show()
















