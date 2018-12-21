from testcase.interface.words_lists.all_cihui import AllCihuiInterface
from testcase.interface.grammer.all_gra_interface import AllGraInterface
from testcase.interface.writing.all_wrt_interface import AllWrtInterface
from testcase.interface.sysListening.all_listening_interface import AllListenInterface
from testcase.interface.reading.all_reading_interface import AllReadInterface


class AllInterface(AllCihuiInterface, AllGraInterface,AllWrtInterface,
                   AllListenInterface, AllReadInterface):
    pass