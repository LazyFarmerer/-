from time import time, sleep

from proglog import TqdmProgressBarLogger, ProgressBarLogger

from ..base_class.observer import Subscriber, EventType


class CustomProgressLogger(ProgressBarLogger, Subscriber):
    "역시 스택오버플로우선생님들 + 수정"
    def __init__(self):
        ProgressBarLogger.__init__(self)
        Subscriber.__init__(self)
        self.last_message: str

        self.value: float
        "현재 값"
        self.end_value: float
        "최종 값 value가 다 차면 100%가 되는건데 이 값은 퍼센트가 아니라서 나중에 따로 value / end_value 해야함"
        self.pass_time: float
        "지금까지 걸린 시간"
        self.start_time: float
        "시작 시간"
        self.standard_time: float
        "일정시간마다 업데이트 하기 위한 놈"

        self.reset_data()

    def reset_data(self):
        "새롭게 사용하기 위한 데이터 리셋"
        self.last_message = ''
        self.value: float = 0
        self.end_value: float = 100
        self.pass_time: float = 0
        self.start_time: float = time()
        self.standard_time: float = self.start_time


    def callback(self, **changes):
        # Every time the logger message is updated, this function is called with
        # the `changes` dictionary of the form `parameter: new value`.
        for (parameter, value) in changes.items():
            # print ('Parameter %s is now %s' % (parameter, value))
            self.last_message = value

    def bars_callback(self, bar, attr, value, old_value=None):
        # Every time the logger progress is updated, this function is called        
        if 'Writing video' in self.last_message:
            if self.time_check():
                # print(f"\r{pass_time:3.2f}초 {percentage:3.2f}%", end="")
                self.progress_view(value, self.bars[bar]['total'])

    def on_progress(self, stream, chunk, bytes_remaining):
        if self.time_check():
            filesize = stream.filesize
            bytes_received = filesize - bytes_remaining
            # print(f"{bytes_received / filesize * 100:3.2f}%")
            self.progress_view(bytes_received, filesize)

    def progress_view(self, value: float, end_value: float, bar_length=20):
        self.pass_time = time() - self.start_time
        self.value = value
        self.end_value = end_value

        percent = value / end_value
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        print(f"\r{self.pass_time:3.2f}초: [{arrow + spaces}] {percent * 100:3.2f}%", end="")
        self.notify(EventType.PROGRESS_VIEWER)

    def time_check(self) -> bool:
        difference_time = time() - self.standard_time
        if 0.5 <= difference_time:
            self.standard_time = time()
            return True
        return False



    # def bars_callback(self, bar, attr, value, old_value=None):
    #     # Every time the logger progress is updated, this function is called        
    #     if 'Writing video' in self.last_message:
    #         percentage = (value / self.bars[bar]['total']) * 100
    #         if percentage > 0 and percentage < 100:
    #             if int(percentage) != self.previous_percentage:
    #                 self.previous_percentage = int(percentage)
    #                 print(self.previous_percentage)