import time

class Colors:
    class style:
        RESET         = '\033[0m'
        BOLD          = '\033[01m'
        DISABLE       = '\033[02m'
        UNDERLINE     = '\033[04m'
        REVERSE       = '\033[07m'
        STRIKETHROUGH = '\033[09m'
        INVISIBLE     = '\033[08m'
    class fg:
        BLACK         = '\033[30m'
        RED           = '\033[31m'
        GREEN         = '\033[32m'
        ORANGE        = '\033[33m'
        BLUE          = '\033[34m'
        PURPLE        = '\033[35m'
        CYAN          = '\033[36m'
        LIGHTGRAY     = '\033[37m'
        DARKGRAY      = '\033[90m'
        LIGHTRED      = '\033[91m'
        LIGHTGREEN    = '\033[92m'
        YELLOW        = '\033[93m'
        LIGHTBLUE     = '\033[94m'
        PINK          = '\033[95m'
        LIGHTCYAN     = '\033[96m'
    class bg:
        BLACK         = '\033[40m'
        RED           = '\033[41m'
        GREEN         = '\033[42m'
        ORANGE        = '\033[43m'
        BLUE          = '\033[44m'
        PURPLE        = '\033[45m'
        CYAN          = '\033[46m'
        LIGHTGRAY     = '\033[47m'


class log_level():
    CRITICAL = 1
    ERROR    = 2
    WARNING  = 4
    INFO     = 8
    DEBUG    = 16
    ALL      = 31

class Logger():
    def __init__(self, colorful: bool = True, log_level: int = log_level.ALL, 
                    label_size: int = 9, time_color: Colors = Colors.fg.CYAN):
        self._colorful = colorful
        self._label_size = label_size
        self._time_color = time_color
        self._log_level = log_level

    def _get_time(self):
        return '[' + time.strftime("%H:%M:%S", time.localtime()) + ']'

    def _get_label(self, label_name):
        length = self._label_size

        if len(label_name) >= length:
            prefix = '['
            postfix = ']'
            label_name = label_name[:length]
        else:
            prefix = '[' + ' ' * ((length + 1- len(label_name)) // 2)
            postfix = ' ' * ((length - len(label_name)) // 2) + ']'

        return prefix + label_name + postfix

    def set_level(self, log_level: int):
        self._log_level = log_level

    def custom(self, *data, label_name='', labelcolor: Colors = Colors.fg.CYAN):
        if self._colorful:
            time_color = self._time_color + Colors.style.BOLD
            label_color = labelcolor + Colors.style.BOLD
            reset = Colors.style.RESET
        else:
            time_color = label_color = reset = ''

        time = time_color + self._get_time() + reset

        label = label_color + self._get_label(label_name) + reset
        text = f'{" ".join([str(x) for x in data])}'

        print(f'{time} {label} {text}')
        
    def critical(self, *data):
        if self._log_level & (1 << 0):
            self.custom(*data, label_name='CRITICAL', labelcolor=Colors.bg.RED)

    def error(self, *data):
        if self._log_level & (1 << 1):
            self.custom(*data, label_name='ERROR', labelcolor=Colors.fg.RED)

    def warning(self, *data):
        if self._log_level & (1 << 2):
            self.custom(*data, label_name='WARNING', labelcolor=Colors.fg.ORANGE)

    def info(self, *data):
        if self._log_level & (1 << 3):
            self.custom(*data, label_name='INFO', labelcolor=Colors.fg.CYAN)

    def debug(self, *data):
        if self._log_level & (1 << 4):
            self.custom(*data, label_name='DEBUG', labelcolor=Colors.fg.PURPLE)

    def plus(self, *data):
        self.custom(*data, label_name='+', labelcolor=Colors.fg.GREEN)

    def minus(self, *data):
        self.custom(*data, label_name='-', labelcolor=Colors.fg.RED)
    
    def success(self, *data):
        self.custom(*data, label_name='SUCCESS', labelcolor=Colors.fg.GREEN)

    def failure(self, *data):
        self.custom(*data, label_name='FAILURE', labelcolor=Colors.fg.RED)

    def demo(self):
        self.critical('This is .critical()')
        self.error('This is .error()')
        self.warning('This is .warning()')
        self.info('This is .info()')
        self.debug('This is .debug()')
        print()
        self.plus('This is .plus()')
        self.minus('This is .minus()')
        print()
        self.success('This is .success()')
        self.failure('This is .failure()')
        print()
        self.custom('This is custom one, with labelcolor = Colors.fg.ORANGE', label_name='CUSTOM #1', labelcolor=Colors.fg.ORANGE)
        self.custom('This is custom one, with labelcolor = Colors.bg.PURPLE', label_name='CUSTOM #2', labelcolor=Colors.bg.PURPLE)
        self.custom('This is custom one, with labelcolor = Colors.fg.BLACK + Colors.bg.ORANGE', label_name='CUSTOM #3', labelcolor=Colors.fg.BLACK + Colors.bg.ORANGE)


if __name__ == '__main__':
    log = Logger()
    log.demo()