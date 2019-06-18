import wx_django.settings


def proxy():
    if wx_django.settings.USE_PROXY:
        # add your proxy here
        return {}
    else:
        return {}