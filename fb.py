import webbrowser

def report_facebook_id(fb_id):
    report_url = f'https://www.facebook.com/help/contact/307762347378917?u={fb_id}'
    webbrowser.open(report_url)

if __name__ == '__main__':
    fb_id = input('Enter the Facebook ID to report: ')
    report_facebook_id(fb_id)

