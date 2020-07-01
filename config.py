class Config(object):
    DEBUG = True


class DevConf(Config):
    DEBUG = True


class UserConf(Config):
    DEBUG = False
