def function_makes_good_name(function_name, *args):
    name = function_name.__name__.title().replace('_', ' ')
    print(name, *args)


def open_browser(browser_name):
    function_makes_good_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    function_makes_good_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    function_makes_good_name(find_registration_button_on_login_page, page_url, button_text)


open_browser('Chrome')
go_to_companyname_homepage('https://github.com/')
find_registration_button_on_login_page('https://github.com/', 'Sign in')