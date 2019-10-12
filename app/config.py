class Config:
    """
    Genral configuration parent class
    """
    NEWS_API_BASE_URL = "https://newsapi.org/v2/everything?q=news&apiKey=e58b87334b40467082f5b07a1192007b"
    

class ProdConfig(Config):
    """
    Production configuration child class
    """

class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = True        