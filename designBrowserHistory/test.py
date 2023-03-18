from .solution import BrowserHistory


def test():
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    assert browserHistory.back(1) == "facebook.com"
    assert browserHistory.back(1) == "google.com"
    assert browserHistory.forward(1) == "facebook.com"
    browserHistory.visit("linkedin.com")
    assert browserHistory.forward(2) == "linkedin.com"
    assert browserHistory.back(2) == "google.com"
    assert browserHistory.back(7) == "leetcode.com"
