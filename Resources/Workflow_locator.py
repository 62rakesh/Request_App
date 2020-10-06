from selenium import webdriver


class workflow_locator:
    # Create a new workflow locator
    dropdown_xpath = "(//DIV[@class='btn-group dropdown'])[1]"
    admin_menu_xpath = "(//A[@class='dropdown-item'])[3]"
    breadcrumb_xpath = "(//DIV[@class='left-menu-toggle'])[1]"
    workflow_menu_xpath = "(//A[@_ngcontent-ng-cli-universal-c5=''])[31]"
    workflow_submenu_xpath = "(//A[@href='/admin/workflows'])"
    new_btn_xpath = "(//DIV[text()=' New'])"
    workflow_name_xpath = "(//INPUT[@id='name'])[2]"
    workflow_description_xpath = "(//TEXTAREA[@id='description'])[2]"
    active_toggle_xpath = "(//SPAN[@class='slider'])"
    add_button_xpath = "(//BUTTON[@class='btn btn-primary btn-sm'])[text()='Add']"

    
