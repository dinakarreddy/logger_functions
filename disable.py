import logging
import sys


def get_disabled(self):
    return self._disabled


def set_disabled(self, disabled):
    names = ["user_profile.tasks", "autosuggest.update_scripts.batch_update_developer_metrics",
             "bhi.rent_bhi.expected_leads_update", "autosuggest.tasks"]
    if self.name in names:
        for i in xrange(0, 100):
            try:
                frame = sys._getframe(i)
                print self.name, frame.f_code.co_filename, ':', frame.f_lineno
            except:
                break
        frame = sys._getframe(1)
        if disabled:
            print('{}:{} disabled the {} logger'.format(
                frame.f_code.co_filename, frame.f_lineno, self.name)), self
        else:
            print('{}:{} {} the {} logger'.format(
                frame.f_code.co_filename, frame.f_lineno, disabled, self.name)), self
    self._disabled = disabled

logging.Logger.disabled = property(get_disabled, set_disabled)

# logger.disabled = True or False, than functions are called
