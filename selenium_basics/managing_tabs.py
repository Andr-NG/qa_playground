from utils.config_provider import ConfigProvider


driver = ConfigProvider.get_selenium_driver()

# going to google.com
driver.get("http://google.com")

# opening a new tab
driver.switch_to.new_window("window")

# getting a list of tabs
tabs = driver.window_handles

# getting the current tab id
current_tab = driver.current_window_handle

if current_tab == tabs[1]:
    print("Current tab id is at tabs[1]")
else:
    print("Current tab id is NOT at tabs[1]")
