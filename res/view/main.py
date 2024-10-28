from ..base_class.custom_tk import CustomTk
from ..controllers.download_controller import DownloadController


class Window(CustomTk):
    def __init__(self, curr_dir: str):
        super().__init__()
        self.curr_dir = curr_dir

        download_controller = DownloadController(self, curr_dir)
        download_controller.pack(side="top", anchor="w")


        self.mainloop()

