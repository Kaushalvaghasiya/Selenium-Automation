import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import ipaddress
import subprocess
import platform

start_ip = '192.168.1.10'
end_ip = '192.168.1.254'

start_ip_obj = ipaddress.IPv4Address(start_ip)
end_ip_obj = ipaddress.IPv4Address(end_ip)

def change_ip_address(interface_name, ip_address):
    system = platform.system()
    if system == "Windows":
        command = f"netsh interface ip set address name=\"{interface_name}\" source=static addr={ip_address}"
    elif system in ["Linux", "Darwin"]:
        command = f"sudo ifconfig {interface_name} {ip_address} netmask 255.255.255.0" 
    else:
        print("Unsupported operating system.")
        return
    try:
        subprocess.run(command, shell=True, check=True)
        print(interface_name + "'s IP is changed to " + str(ip_address))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")    

def link_allips(interface, url):
    for ip_int in range(int(start_ip_obj), int(end_ip_obj) + 1):

        ip_addr = ipaddress.IPv4Address(ip_int)

        change_ip_address(interface, ip_addr)
        driver = webdriver.Chrome()
        driver.get(url)
        try:
            button = driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')
            button.click()
        except Exception:
            pass
        time.sleep(2)
        driver.quit()
        print(str(ip_addr) + " complete viewing")

def allreels_allips(interface, channel):
    for ip_int in range(int(start_ip_obj), int(end_ip_obj) + 1):

        ip_addr = ipaddress.IPv4Address(ip_int)
        change_ip_address(interface, ip_addr)

        driver = webdriver.Chrome()
        url = 'https://www.youtube.com/@' + channel + '/shorts'
        driver.get(url)
        try:
            try:
                reject_button = driver.find_element(By.XPATH, "//span[text()='Reject all']")
                reject_button.click()
            except Exception:
                pass
            link_element = driver.find_element(By.CSS_SELECTOR, 'h3.style-scope.ytd-rich-grid-slim-media a.yt-simple-endpoint')
            link_element.click()
            while(1):
                time.sleep(1)
                active_element = driver.find_element(By.CSS_SELECTOR, 'ytd-reel-video-renderer[is-active]')
                old_id = active_element.get_attribute('id')
                actions = ActionChains(driver)
                actions.send_keys(Keys.DOWN)
                actions.perform()
                time.sleep(1)
                active_element = driver.find_element(By.CSS_SELECTOR, 'ytd-reel-video-renderer[is-active]')
                new_id = active_element.get_attribute('id')
                if old_id == new_id:
                    print(str(ip_addr) + " complete viewing")
                    driver.quit()
        except Exception as e:
            print(f"Error: {e}")
    print(channel + " complete viewing")

class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if option_string == "-C":
            setattr(namespace, "channel", values)
        elif option_string == "-U":
            setattr(namespace, "url", values)
        elif option_string == "-I":
            setattr(namespace, "interface", values)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-C", action=CustomAction, help="Channel")
    parser.add_argument("-U", action=CustomAction, help="Url")
    parser.add_argument("-I", action=CustomAction, required=True, help="Interface")

    args = parser.parse_args()

    channel = getattr(args, "channel", None)
    url = getattr(args, "url", None)
    interface = getattr(args, "interface", None)

    if channel is None:
        link_allips(interface=interface, url=url)
    else:
        allreels_allips(interface=interface, channel=channel)