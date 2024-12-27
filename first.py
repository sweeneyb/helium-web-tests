from helium import *

#start_chrome('https://github.com/sweeneyb?tab=repositories', headless=True)
start_chrome('https://github.com/sweeneyb?tab=repositories')
write('briansweeney.dev')
press(ENTER)
get_driver().save_screenshot(r'screenshot.png')