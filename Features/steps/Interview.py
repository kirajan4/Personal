from behave import *
from selenium import webdriver
import time

"""
Steps or Step definition for the 'Interview.feature' file.
Author - KamatchiRajan
Date - 31Mar20
"""

driver = webdriver.Chrome()

"""The below code snipped is opening the Google web page"""

@given("I opened browser page")
def i_opened_browser_page(context):
    driver.get('https://www.google.com')

"""Verify the Google search page"""

@then("I validate present in Search page")
def i_validate_present_in_search_page(context):
    driver.find_element_by_name('q')

"""Input the wurl.com string into search box"""

@when("I enter the wurl.com in Search box")
def i_enter_the_wurl_in_search_box(context):
    driver.find_element_by_name('q').send_keys('wurl.com')
    driver.implicitly_wait(5)

"""Click the I'm feeling lucky button"""

@step("click on the I’m feeling lucky button")
def click_on_the_im_feeling_lucky_button(context):
    driver.find_element_by_class_name('RNmpXc').click()
    
"""Validate the WURL Home page"""

@then("I validate the wurl is present")
def i_validate_the_wurl_is_present(context):
    driver.find_element_by_class_name('logo')