import pytest
import softest
from pages.homepage_pom import homepage
from ddt import ddt, data, file_data ,unpack




@pytest.mark.usefixtures("setup")
@ddt    #### use decorator at class level so that all methodscan use
class Test_addtobasket(softest.TestCase):

    @pytest.fixture(autouse=True)
    def objects_setup(self):
        self.homepage_1 = homepage(self.driver)

    @data(("adidas","1st"), ("under armour","2nd"), ("puma","3rd"))
    @unpack              ###Looks like the unpack decorator should be used when there are more than one arguments
    def test_4(self, item,number):
        self.homepage_1.open_search_box(item,number)


