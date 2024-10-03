from behave import given, when, then
from selenium import webdriver
from pages.login_fp_page import LoginFBPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

@given('the user is on the facebook login page')
def step_given_on_login_page(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://www.facebook.com/")
    context.login_fp_page = LoginFBPage(context.driver)

@when('the user logs in facebook with valid credentials')
def step_when_user_logs_in_valid(context):
    context.login_fp_page.login("secret", "secret")

@then('the user should be redirected to the facebook dashboard page')
def step_then_dashboard_page(context):
    dashboard_page = DashboardPage(context.driver)
    assert dashboard_page.isTopDisplayed()



