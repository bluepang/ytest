from core.driver import AndroidDriver
from common.process_config_file import Config


class BaseCase(object):

    def setup_method(self, method):
        self.d = AndroidDriver.get_driver()
        self.app_name = Config().get_target_name()
        if not self.d.info.get('screenOn'):
            self.d.screen_on()
            self.d(scrollable=True).scroll.toBeginning()
        self.d.app_start(self.app_name)

    def teardown_method(self, method):
        self.d.app_stop(self.app_name)