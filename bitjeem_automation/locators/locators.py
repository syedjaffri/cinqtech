class Locators:

    # login page objects
    email_textbox_id = "email"
    password_textbox_id = "password"
    login_button_id = "login"
    twofactor_button_id = "2faButton"

    # home page objects
    login_button_xpath = "/html/body/app-root/div/app-header-guest/section[1]/nav/div/div/ul/li[2]/a"
    user_icon_xpath = "/html/body/app-root/div/app-header-guest/section[1]/nav/div/div/ul/li[5]/button"
    logout_button_xpath = "/html/body/app-root/div/app-header-guest/section[1]/nav/div/div/ul/li[5]/div/a[2]"
    register_button_xpath = "/html/body/app-root/div/app-header-guest/section[1]/nav/div/div/ul/li[3]/a"

    # Register page objects
    firstname_textbox_id = "fn"
    lastname_textbox_id = "ln"
    mobile_number_textbox_id = "phone"
    code_email_button_id = "code_email"
    verify_xpath = "/html/body/div[2]/div[3]/div[1]/div/div/span"
    mvc_textbox_id = "phone_num_code"
    evc_textbox_id = "vcode"
    password_text_id = "pass"
    cp_textbox_id = "cp"
    pp_checkbox_id = "form-check"
    reg_button_xpath = "/html/body/app-root/div/app-guest/section/app-register/section/div/div/div/form/button"
    # recaptcha_checkbox_xpath = "/html/body/div[2]/div[3]/div[1]/div/div/span/div[3]"