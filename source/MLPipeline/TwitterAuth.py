
from .References import References

class TwitterAuth(References):
    """SET UP TWITTER AUTHENTICATION"""
    def __init__(self):
        self.bearer_token = self.BEARER_TOKEN

    def authenticateTwitterApp(self):
        return self.bearer_token
