from selenium import webdriver


class Group:
    request_group_xpath = "(//A[@_ngcontent-ng-cli-universal-c5=''])[40]"
    create_new_request_group_xpath = "(//DIV[text()=' New'])"
    enter_name_xpath = "(//INPUT[@id='name'])[2]"
    enter_description_xpath = "(//TEXTAREA[@id='Description'])"
    enable_toggle_xpath = "(//SPAN[@class='slider'])"
    add_request_group_xpath = "(//BUTTON[@class='btn btn-primary btn-sm'])[text()='Add']"
    search_group_xpath = "(//INPUT[@id='mat-input-0'])"
    find_group_name_xpath = "(//TD[@_ngcontent-ng-cli-universal-c12=''])[text()='RP-request group(Regression)']"
    create_new_request_type_xpath = "//A[@placement='left']"
    enter_request_type_name_xpath = "(//INPUT[@id='name'])[2]"
    enter_request_type_description_xpath = "(//INPUT[@id='description'])"
    select_workflow_name_xpath = "(//select[@id='statusGroupId'])"
    select_form_name_xpath = "(//select[@id='requestFormId'])"
    add_request_type_xpath = "(//BUTTON[@class='btn btn-outline-secondary btn-sm'])[text()='Add']"





