from fbtapack.Browser.fbta_brwoser_constant import FBTABrowserConstant


class FBTABrowserDetectorCase:
    CASE_LOGIN_URL: dict = {
        'login/': FBTABrowserConstant.FBSCOPE_GLOBAL,
        'login.php?': FBTABrowserConstant.FBSCOPE_GLOBAL,
        'story.php?story_fbid=': FBTABrowserConstant.FBSCOPE_PRIVATE
    }

    CASE_LOGIN_TITLE: dict = {
        'เข้าสู่ระบบหรือสมัครใช้งาน': {
            'do': FBTABrowserConstant.STATUS_LOGIN_AGAIN,
            'step': [
                FBTABrowserConstant.DOING_TITLE_CHECK_ONLY
            ]
        },
        'เข้าสู่ระบบ facebook': {
            'do': FBTABrowserConstant.STATUS_LOGIN_AGAIN,
            'step': [
                FBTABrowserConstant.DOING_TITLE_CHECK_ONLY
            ]
        },
        'Facebook - เข้าสู่ระบบหรือสมัครใช้งาน': {
            'do': FBTABrowserConstant.STATUS_LOGIN_AGAIN,
            'step': [
                FBTABrowserConstant.DOING_TITLE_CHECK_ONLY
            ]
        },
        'Log in to Facebook': {
            'do': FBTABrowserConstant.STATUS_LOGIN_AGAIN,
            'step': [
                FBTABrowserConstant.DOING_TITLE_CHECK_ONLY
            ]
        },
        'การตรวจสอบสถานะความปลอดภัย': {
            'do': FBTABrowserConstant.STATUS_BROWSER_RESTART,
            'step': [
                FBTABrowserConstant.DOING_TITLE_CHECK_ONLY
            ]
        },
        'mobile_login_bar': {
            'do': FBTABrowserConstant.STATUS_LOGIN_AGAIN,
            'step': [
                FBTABrowserConstant.DOING_CONTENT_CHECK_ONLY
            ]
        },
        'เข้าร่วม Facebook หรือเข้าสู่ระบบเพื่อดำเนินการต่อ': {
            'do': FBTABrowserConstant.STATUS_LOGIN_AGAIN,
            'step': [
                FBTABrowserConstant.DOING_CONTENT_CHECK_ONLY
            ]
        },
        'Join Facebook or log in to continue.': {
            'do': FBTABrowserConstant.STATUS_LOGIN_AGAIN,
            'step': [
                FBTABrowserConstant.DOING_CONTENT_CHECK_ONLY
            ]
        },
        'Error Facebook': {
            'do': FBTABrowserConstant.STATUS_CONTENT_RELOAD_ONCE,
            'step': [
                FBTABrowserConstant.DEBUG_SHOW_SOURCE,
                FBTABrowserConstant.DOING_TITLE_CHECK_ONLY
            ]
        },
        'Content Not Found': {
            'do': FBTABrowserConstant.STATUS_CONTENT_RELOAD_ONCE,
            'step': [
                FBTABrowserConstant.DEBUG_SHOW_SOURCE,
                FBTABrowserConstant.DOING_TITLE_CHECK_ONLY
            ]
        }

    }
