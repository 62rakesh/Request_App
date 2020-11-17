from selenium import webdriver


class status:
    search_workflow = "(//INPUT[@id='mat-input-0'])"
    click_workflow = "(//TD[@class='ng-star-inserted'])[text()='RP-Regression_workflow']"
    create_new_status = "//DIV[@placement='left']"
    enter_status_name = "(//INPUT[@id='name'])[2]"
    assigntype = "(//SELECT[@id='assignedtype'])"
    fixedvalue = "(//SELECT[@id='fixedvalue'])"
    notification_assignee = "(//SPAN[@class='slider'])[1]"
    notification_originator = "(//SPAN[@class='slider'])[2]"
    Add_new_status = "(//BUTTON[@class='btn btn-primary btn-sm'])"


