from selenium import webdriver


class loginPage_Locator():
    # User Login process Xpath
    login_uname_xpath = "(//INPUT[@name='loginfmt'])"
    login_next_button_xpath = "(//INPUT[@id='idSIButton9'])"
    login_upwd_xpath = "(//INPUT[@name='passwd'])"
    login_signin_xpath = "(//INPUT[@id='idSIButton9'])"
    login_confirm_xpath = "(//INPUT[@id='idSIButton9'])"

    # User landed in the employee dashboard (Xpath)
    login_profile_xpath = "(//DIV[@class='img-box'])[1]"
    login_logout_xpath = "(//I[@class='icon-logout'])[1]"
    # Dashboard verify Xpath
    login_verify_dashboard = "(//H4[text()='Employee dashboard'])[1]"




