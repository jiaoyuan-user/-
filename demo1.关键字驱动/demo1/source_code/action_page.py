import pywinauto
from pywinauto.keyboard import send_keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import logging
import time
import os
from demo1.run_code.common import CommonFuntion


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    datefmt='%a, %Y - %m - %d %H: %M: %S',
)
# keyword 关键字
# loc 定位方式
# element 定位元素
# value 传参
def sendkeys(file_path):
    pass


class KeyWords(object):

    def __init__(self):
        self.driver = None
        if self.driver is None:
            self.driver = webdriver.Chrome(executable_path=r'..\source_code\chromedriver.exe')

    def open_browser(self, value: str):
        browser = str(value).title()
        if  browser =='Chrome':
            self.driver = webdriver.Chrome(executable_path=r'..\source_code\chromedriver.exe')
            #chromedriver浏览器驱动路径
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = 'type error'
            logging.info( 'type error')
        return self.driver

    def open_url(self, value: str):
        """
        获取url地址
        使窗口最大化
        设置隐性等待30秒
        :param url:
        :return:
        """
        self.driver.get(value)
        logging.info("Open url: {}".format(value))
        self.driver.maximize_window()
        logging.info("Maximizes the current window")
        self.driver.implicitly_wait(30)

    def call(self,value):
        """
        调用common中的函数
        :param value: 调用的函数名称
        :return:
        """
        try:
            call_dri = CommonFuntion(self.driver)
            getattr(call_dri,value)()
            logging.info('Call funtion success daily:{}'.format(value))
        except:
            logging.info('Call funtion failed daily:{}'.format(value))

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.sleep(2)
        logging.info("Quit the browser!")
        self.driver.quit()

    def close(self):
        """
        关闭当前标签页
        :return:
        """
        self.sleep(2)
        logging.info("Closing and quit the browser.")
        self.driver.close()

    def sleep(self, value:float=1):
        """
        强制等待时间
        :param value:等待的时间（s）
        :return:
        """
        logging.info("Sleep for {} seconds".format(value))
        time.sleep(value)

    def is_displayed(self,element):
        """
        判断元素是否存在
        :param element: 元素对象（WebElement对象）
        :return:
        """
        value = element.is_displayed()
        return value

    def locate_element(self,element,name):
        """
        定位元素方法
        :param loc: 定位器
        :return:
        eg：demo.locate_element((By.XPATH,'//span[text()="登录"]')).click()
        """
        locator = (element,name)

        try:        # 注意:以下入参本身是元组，不需要加()
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element
        except NoSuchElementException:
            logging.error("Page not found the element: {}".format(locator))
        except Exception as e:
            logging.error("Locate Failed，Error:{}".format(e))
        return self.driver.find_element(locator)

    def send_value (self,element,name,value, clear=True):
        """
        输入值
        :param element 元素定位类型
        :param name 定位元素
        :param value 参数
        :param clear: 是否清除
        :return
        """
        loctor = self.locate_element(element,name)
        if clear:
            loctor.clear()
        try:
            self.sleep(0.5)
            loctor.send_keys(value)
            logging.info("Input data: {}".format(value))
        except Exception as e:
            logging.error("Faild to input: {}，Error: {}".format(value, e))

    def click(self,element,name):
        """
        点击元素
        :param element: 元素定位类型
        :param name: 定位信息
        :return:
        """
        ele = self.locate_element(element,name)
        try:
            ele.click()
            logging.info("The element \' {} \' was clicked.".format(ele.get_attribute(element)))
        except Exception as e:
            display = self.is_displayed(ele)
            if display is True:
                self.sleep(3)
                ele.click()
                logging.info('The element was clicked')
            else:
                self.save_image(time.time()+element)
                logging.error('Failed to click the element, Error: {}'.format(e))

    def save_image(self,save_name):
        """
        截图
        :return:
        """
        # date = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        if not os.path.exists("../screenshots"):    #如果没有screenshots这个文件夹，新建
            os.mkdir("../screenshots")
        screen_name = os.path.join("../screenshots", '{}.png'.format(save_name))

        try:
            time.sleep(1)
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("Had take screenshot and save to folder : common1/screenshots")
        except NameError as e:
            logging.error("Failed to take screenshot! Error: {}".format(e))

    def switch_frame(self, element,name):
        """
        切换 frame 框架
        :param loc: 定位方式
        :param element: 定位元素
        :return:
        """
        try:
            frame = self.locate_element(element,name)
            self.driver.switch_to.frame(frame)
            logging.info("Successful to switch to frame!")
        except Exception as e:
            logging.error("Failed to switch to frame: {}{}, Error: {}".format(element,name,e))

    def quit_frame(self):
        """
        退出当前frame
        :return:
        """
        self.driver.switch_to.default_content()
        logging.info("Successful to quit the current frame!")

    def get_attribute(self, element,name,value = '',):
        """
        获取元素属性
        :param element: 定位方式
        :param name: 定位元素
        :param attribute: 属性名称
        :return:
        """
        try:
            ele = self.locate_element(element,name)
            return ele.get_attribute(value)
        except Exception as e:
            logging.info("Failed to get attribute with %s" % e)
            self.save_image(time.time()+element)
            raise

    def get_title(self):
        """
        获取title
        :return:
        """
        title = self.driver.title
        logging.info('Current page title is:%s' % title)
        return title

    def get_text(self,element,name):
        """
        获取元素对象文本
        :param element: 定位方式
        :param name: 定位元素
        :return:
        """
        try:
            text = self.locate_element(element,name).text
            logging.info("Get the text: {}".format(text))
            return text
        except Exception as e:
            logging.error("Faild to Get the text: {} Error: {}".format(element, e))

    def forward(self):
        """
        浏览器前进
        :return:
        """
        self.driver.forward()
        logging.info("Click forward on current page.")

    def back(self):
        """
        浏览器后退
        :return:
        """
        self.driver.back()
        logging.info("Click back on current page.")

    def execute_js(self, value):
        """
        执行 script 语句
        :param value: JS 语句
        :return:
        """
        try:
            self.driver.execute_script(value)
            logging.info("Successful to execute JS statements: {}" % value)
        except Exception as e:
            logging.error("Faild to execute JS statements， Error: {}".format(e))

    def assert_title(self, value):
        """
        断言title是否匹配
        :param value:
        :return:
        """
        if value != self.driver.title:
            logging.error("Assert Failed: {} is equal driver.title".format(value))
            return 0
        else:
            logging.info("Assert Passed: {} is not equal driver.title".format(value))
            return 1

    def assert_in_page_source(self, value):
        """
        断言数据是否存在page_source资源中
        :param value: 参数
        :return:
        """
        if value not in self.driver.page_source:
            logging.error("Assert Failed: {} not in page_source".format(value))
            return 0
        else:
            logging.info("Assert Passed: {} in page_source".format(value))
            return 1

    def assert_ele_exist(self,element,name):
        """
        判断元素是否存在
        :param element: 定位方式
        :param name:定位元素
        :return:
        """
        locator = (element,name)
        try:
            ele = self.locate_element(element,name)
            logging.info('Assert passed:the element is exist:{}'.format(locator))
            return 1
        except:
            logging.info('Assert failed:not found the element:{}'.format(locator))
            return 0

    def assert_ele_notexist(self,element,name):
        """
        判断元素是否存在
        :param element: 定位方式
        :param name:定位元素
        :return:
        """
        locator = (element,name)
        try:
            ele = self.locate_element(element,name)
            logging.info('Assert failed:the element is exist:{}'.format(locator))
            return 0
        except:
            logging.info('Assert passed:not found the element:{}'.format(locator))
            return 1

    def import_file(self,value):
        """
        导入文件，value用路径+文件名，中间用#隔开
        :param value: 文件名称+路径
        :return:
        """
        file_path = value.split('#', 1)[0]
        file_name = value.split('#', 1)[1]
        try:
            app = pywinauto.Desktop()
            dlg = app['打开']
            dlg['Toolbar3'].click()
            send_keys(file_path)
            send_keys('{VK_RETURN}')
            dlg['文件名(&N):Edit'].type_keys(file_name)
            dlg['打开(&0)'].click()
            logging.info('Import file success daily:{}'.format(file_path+file_name))
        except:
            logging.info('Import file failed daily:{}'.format(file_path + file_name))

    def repeat(self,value):
        print('重复执行{}次！'.format(value))
#
if __name__ == '__main__':
    demo = KeyWords()     #实例化ActionaPage类对象
    # demo.open_browser('Chrome')       #指定浏览器
    demo.open_url('https://www.atstudy.com/')       #指定url
#     demo.click(('xpath','//span[text()="登录"]'))     #点击操作
#     demo.locate_element('xpath','//span[text()="登录"]').click()
#
#     demo.locate_element((By.XPATH,'//span[text()="登录"]'))       #元素定位
#     demo.save_image()       #截图
#     demo.driver.quit()
#     demo.save_image()
