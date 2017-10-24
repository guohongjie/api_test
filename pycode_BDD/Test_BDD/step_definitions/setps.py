#-*-coding:utf-8-*-
from lettuce import *  
from lettuce_webdriver.util import assert_false  
from lettuce_webdriver.util import AssertContextManager
from selenium.common.exceptions import WebDriverException
import time
import requests
from selenium.webdriver.common.action_chains import ActionChains
def input_frame(browser,tag,attribute, timeout=15):
    start = time.time()
    elems = []
    xpath = "//%s%s" % (tag, attribute)
    while time.time() - start < timeout:
        elems = browser.find_elements_by_xpath(str(xpath))
        if elems:
            return elems[0] if elems else False
        time.sleep(0.2)
    return elems[0] if elems else False
def drag_element(browser,Ftag,Fattribute,Ttag,Tattribute):
    dragger = input_frame(browser,Ftag,Fattribute)
    item = input_frame(browser,Ttag,Tattribute)
    action = ActionChains(browser)
    action.drag_and_drop(dragger, item).perform()
def click_alert(browser,bool,countout=10):
    start = time.time()
    count = 1
    while count<=countout:
        try:
            s = browser.switch_to_alert()
            if bool:
                s.accept()
                break
            else:
                s.dismiss(0)
                break
        except Exception as e:
            time.sleep(0.5)
            print 'Next step to obtain alert'
            count += 1
def move_element_to(browser,Ttag,Tattribute):
    e = input_frame(browser,Ttag,Tattribute)
    action = ActionChains(browser)
    action.move_to_element(e).perform()
class Login(object):
    """登录操作"""
    #定位输入框输入关键字
    @step('I fill username in field with tag "(.*)" and attribute "(.*)" and "(.*)"')
    def input_username(step,tag,attribute,text):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.clear()
            text_field.send_keys(text)
    @step('I fill password in field with tag "(.*)" and attribute "(.*)" and "(.*)"')
    def input_password(step,tag,attribute,text):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.clear()
            text_field.send_keys(text)
    @step('I fill auth in field with tag "(.*)" and attribute "(.*)" and "(.*)"')
    def input_auth(step,tag,attribute,text):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.clear()
            text_field.send_keys(text)
    @step('I click tag "(.*)" and attribute "(.*)" with Gome Login once way')
    def click_submit(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('I chose to use cookies "(.*)" for  login in "(.*)"')
    def click_submit_cookies(step,cookies,url):
        with AssertContextManager(step):
            c = world.browser.get_cookies()
            for m in c:
                m['value'] = cookies
            world.browser.delete_all_cookies()
            world.browser.add_cookie(m)
            world.browser.get(url)
    @step('I want to enlarge this browser window')
    def max_window(step):
        with AssertContextManager(step):
            world.browser.maximize_window()
    @step('I stand here for "(\d*)" seconds')
    def timeSleep(step, num):
        with AssertContextManager(step):
            time.sleep(int(num))
class HomePage(object):
    @step('I arrive in system page,The first I click HomePage button tag "(.*)" and attribute "(.*)"')
    def click_HomePage(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('I click tag "(.*)" and attribute "(.*)" with Create HomePage immediately button')
    def click_createHomePage_button(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('In the Page attribute windows,For PageType I want to chose tag "(.*)" and attribute "(.*)"')
    def chose_Pagetype(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('In the Page attribute windows,For PageName I want to fill tag "(.*)" and attribute "(.*)" and written "(.*)"')
    def pageName(step,tag,attribute,text):
        text_field = input_frame(world.browser, tag, attribute)
        text_field.send_keys(text)
    @step('In the Page attribute windows,For PageKeyWord I want to fill tag "(.*)" and attribute"(.*)" and written "(.*)"')
    def pageKeyWord(step, tag, attribute, text):
        text_field = input_frame(world.browser, tag, attribute)
        text_field.send_keys(text)
    @step('In the Page attribute windows,For PageDescription I want to fill tag "(.*)" and attribute "(.*)" and written "(.*)"')
    def pageDescription(step, tag, attribute, text):
        text_field = input_frame(world.browser, tag, attribute)
        text_field.send_keys(text)
    @step('In the Page attribute windows,Must input was over,So we have save this message,I will click tag "(.*)" and attribute "(.*)" to save this HomePage')
    def save_Page(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
class PC_Client_fitting(object):
    @step('I arrive in PC-Client-Fitting page,The first I click Public_Model button tag "(.*)" and attribute "(.*)"')
    def click_public_Model(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('I will drag Dianzhao_tool_bar tag "(.*)" and attribute "(.*)" to tag "(.*)" and attribute "(.*)"')
    def dz_drag_dzqy(step,Ttag,Tattribute,Ftag,Fattribute):
        with AssertContextManager(step):
            text_field = drag_element(world.browser,Ttag,Tattribute,Ftag,Fattribute)
    @step('I will drag HengDaohang_tool_bar tag "(.*)" and attribute "(.*)" to tag "(.*)" and attribute "(.*)"')
    def HDH_drag_DHqy(step,Ttag,Tattribute,Ftag,Fattribute):
        with AssertContextManager(step):
            text_field = drag_element(world.browser,Ttag,Tattribute,Ftag,Fattribute)
    @step('Public Model was fit over, so we are begin to ZH_Model,I click Public_Model button tag "(.*)" and attribute "(.*)"')
    def click_ZH_Model(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('I will drag DANTU_tool_bar tag "(.*)" and attribute "(.*)" to tag "(.*)" and attribute "(.*)"')
    def singleIMG_drag_ZhTemplate(step,Ttag,Tattribute,Ftag,Fattribute):
        with AssertContextManager(step):
            text_field = drag_element(world.browser,Ttag,Tattribute,Ftag,Fattribute)
    @step('This Template tag "(.*)" and attribute "(.*)" will be saved "(.*)')
    def save_template(step,tag,attribute,bool):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
            time.sleep(2)
            click_alert(world.browser,bool)
class UpLoadImgLibrary(object):
    @step('I want to go to click tag "(.*)" and attribute "(.*)" button')
    def click_PictureLibrary(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('I want to upload to local picture tag "(.*)" and attribute "(.*)",and send file "(.*)"')
    def upload_file(step,tag,attribute,file):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.send_keys(file)
    @step('I will be click one_click_upload button tag "(.*)" and attribute "(.*)" to uploading')
    def upload_img(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
            time.sleep(2)
    @step('If upload successful,I will click close button tag "(.*)" and attribute "(.*)" to over uploading')
    def close_upload(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
class ProductManage(object):
    @step('I will go to Product Manage with tag "(.*)" and attribute "(.*)"')
    def click_ProductManager(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('I am arriving Product Manage Page,The first,I will fill classify name tag "(.*)" and attribute "(.*)" to written "(.*)"')
    def fill_classifyName(step,tag,attribute,text):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.clear()
            text_field.send_keys(text)
    @step('I execute script "(.*)"')
    def add_classify(step,tag):
        with AssertContextManager(step):
            world.browser.execute_script(tag)
    @step('I am click add classify button tag "(.*)" and attribute "(.*)"')
    def click_add_classify(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('I will click Import Button tag "(.*)" and attribute "(.*)"')
    def click_Import_button(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    # @step('alert a Input window,I will click chose classify tag "(.*)" and attribute "(.*)"')
    # def click_chose_classify(step,tag,attribute):
    #     with AssertContextManager(step):
    #         text_field = input_frame(world.browser,tag,attribute)
    #         text_field.click()
    # @step('I will chose the newest classify tag "(.*)" and attribute "(.*)')
    # def click_newest_classify(step,tag,attribute):
    #     with AssertContextManager(step):
    #         text_field = input_frame(world.browser,tag,attribute)
    #         text_field.click()
    @step('Now I was build a first classify,So I will build a second classify tag "(.*)" and attribute "(.*)"')
    def move_add_classify(step,tag,attribute):
        with AssertContextManager(step):
            e = move_element_to(world.browser,tag,attribute)
    @step('I will click add "(.*)" and attribute "(.*)"')
    def click_add_second(step,tag,attribute):
        with AssertContextManager(step):
            e = input_frame(world.browser,tag,attribute)
            ActionChains(world.browser).click(e).perform()
    @step('I will fill in second classify tag "(.*)" and attribute "(.*)" and written "(.*)"')
    def second_name(step,tag,attribute,text):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.send_keys(text)
    @step('I click submit to save the second classify tag "(.*)" and attribute "(.*)"')
    def click_submitSecond(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('I will click Import Button tag "(.*)" and attribute "(.*)"')
    def click_submitImport(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            text_field.click()
    @step('alert a Input window,I will click chose classify tag "(.*)" and attribute "(.*)"')
    def display_oneC(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            ActionChains(world.browser).move_to_element(text_field).perform()
            ActionChains(world.browser).click(text_field).perform()
    @step('I will chose the newest classify tag "(.*)" and attribute "(.*)"')
    def chose_oneC(step, tag, attribute):
        with AssertContextManager(step):#这里写死调用方法，因为选择框容易受其他操作触发隐藏
            xpath = "//%s%s" % (tag, attribute)
            field = world.browser.find_elements_by_xpath(xpath)
            field[1].click()
    @step('In the ImportFrame I will click the second classify tag "(.*)" and attribute "(.*)"')
    def display_twoC(step,tag,attribute):
        with AssertContextManager(step):
            text_field = input_frame(world.browser,tag,attribute)
            ActionChains(world.browser).move_to_element(text_field).perform()
            ActionChains(world.browser).click(text_field).perform()
    @step('So I will be chose second classify tag "(.*)" and attribute "(.*)"')
    def chose_twoC(step, tag, attribute):
        with AssertContextManager(step):#这里写死调用方法，因为选择框容易受其他操作触发隐藏
            xpath = "//%s%s" % (tag, attribute)
            field = world.browser.find_elements_by_xpath(xpath)
            field[1].click()
    @step('In the end,I will be upload a tag "(.*)" and attribute "(.*)" Excel file ,this path is "(.*)"')
    def upload_excel_file(step, tag, attribute,file):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag,attribute)
            field.send_keys(file)
    @step('I click make sure Import Button to save this Import Product tag "(.*)" and attribute "(.*)"')
    def click_import_button(step, tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag,attribute)
            field.click()
    @step('If upload was succesful,This system was alert Import Successful "(.*)"')
    def import_alert(step,bool):
        with AssertContextManager(step):
            click_alert(world.browser,bool)
    @step('I click close Button to close this window tag "(.*)" and attribute "(.*)"')
    def close_import_button(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag,attribute)
            field.click()
class PageManage(object):
    @step('I will be go to Page Manage,I will click tag "(.*)" and attribute "(.*)"')
    def click_pageManage(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag,attribute)
            field.click()
    @step('I arrive in the Page Manage,The first I fill in page name tag "(.*)" and attribute "(.*)" and written "(.*)"')
    def search_page(step,tag, attribute,text):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag,attribute)
            field.send_keys(text)
    @step('I want to search this Page,I click button tag "(.*)" and attribute "(.*)"')
    def click_search_button(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag,attribute)
            field.click()
    @step('I will click fitting Button tag "(.*)" and attribute "(.*)"')
    def click_fitting(step,tag, attribute):
        with AssertContextManager(step):
            xpath = "//%s%s" % (tag, attribute)
            field = world.browser.find_elements_by_xpath(xpath)
            m = [h for h in field if h.text == u"装修"]
            cur_window = world.browser.current_window_handle
            m[0].click()
            time.sleep(2)
            handles = world.browser.window_handles
            for handle in handles:  # 切换窗口（切换）
                if handle != cur_window:
                    world.browser.switch_to_window(handle)
    @step('I want to replace dzqy picture,so I click button tag "(.*)" and attribute "(.*)"')
    def start_replace_dzqy(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag, attribute)
            count = 0
            while count<=30:
                try:
                    field.click()
                except WebDriverException as e:
                    time.sleep(1)
                    count += 1
    @step('In the forward step,system alert a Frame,I want to replace Picture tag "(.*)" and attribute "(.*)"')
    def second_repalce_change(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag, attribute)
            field.click()
    @step('If I click change place,system will be alert upload picture,I chose the first IMG "(.*)" and attribute "(.*)"')
    def choseFirstImg(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag, attribute)
            field.click()
    @step('The picture was chosed,I click OK to save tag "(.*)" and attribute "(.*)"')
    def click_ok_button(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag, attribute)
            field.click()
    @step('I am click OK too,because This Picture was enable tag "(.*)" and attribute "(.*)"')
    def sure_ok_button(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag, attribute)
            field.click()
    @step('I am click save this model to save tag "(.*)" and attribute "(.*)"')
    def pageSave_click(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag, attribute)
            field.click()
    @step('If saving is successful,system alert "(.*)",I was accept it')
    def alert_ok(step,bool):
        with AssertContextManager(step):
            click_alert(world.browser, bool)
    @step('all model was complate,I will be starting commit audit tag "(.*)" and attribute "(.*)"')
    def commit_auditPage(step,tag, attribute):
        with AssertContextManager(step):
            field = input_frame(world.browser,tag, attribute)
            field.click()
    @step('I am closing current window')
    def close_cur_window(step):
        with AssertContextManager(step):
            cur_handle = world.browser.current_window_handle
            all_handle = world.browser.window_handles
            for handle in all_handle:
                if handle != cur_handle:
                    world.browser.close()
                    world.browser.switch_to_window(handle)
                    world.browser.refresh()

class check_page(object):
    @step('I will goto url "(.*)" and This written "(.*)" tag "(.*)" and attribute "(.*)", return Check suceessful')
    def post_check(step,url,pagename,tag,attribute):
        with AssertContextManager(step):
            input_page_name = input_frame(world.browser,"input","[@id='title']")
            input_page_name.clear()
            input_page_name.send_keys(pagename)
            click_search = input_frame(world.browser,"div","[@id='pageCon-btn']/input[1]")
            click_search.click()
            field = input_frame(world.browser,tag, attribute)
            id = field.text
            #world.browser.execute_script("alert('%s')"%(id))
            # 1不通过、2通过
            cookies = world.browser.get_cookies()
            s = requests.post(url,data={'id':str(id),'state':2})
            #world.browser.execute_script("alert('%s')"%(s.content))
    @step('I will be click preview button,system will be alert new window tag "(.*)" and attribute "(.*)"')
    def click_previewWindow(step, tag, attribute):
        with AssertContextManager(step):
            world.browser.refresh()
            time.sleep(2)
            xpath = "//%s%s" % (tag, attribute)
            field = world.browser.find_elements_by_xpath(xpath)
            m = [h for h in field if h.text == u"预览"]
            m[0].click()

