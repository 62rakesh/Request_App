from selenium import webdriver


class role:
    authorization_xpath = "(//A[@_ngcontent-ng-cli-universal-c5=''])[12]"
    roles_xpath = "(//A[@_ngcontent-ng-cli-universal-c5=''])[13]"
    search_role_xpath = "(//INPUT[@id='mat-input-5'])"
    three_dot_menu_xpath = "(//I[@_ngcontent-ng-cli-universal-c12=''])[10]"
    assign_manager_role_xpath = "(//BUTTON[@class='dropdown-item ng-star-inserted'])[text()=' Assign request groups " \
                                "to manager'][2] "
    assign_request_group_xpath = "(//A[@class='btn btn-link'])[text()=' New'][1]"
    select_request_group_xpath = "(//SELECT[@id='requestgroupId'])"
    add_request_group_xpath = "(//BUTTON[@class='btn btn-primary btn-sm'])"


