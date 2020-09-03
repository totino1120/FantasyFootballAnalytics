class Url():
    def __init__(self):
        self.real_link = "real_link"
        self.ip_addy = "ip_addy"
        self.ad_type = "ad_type"
        self.token = "token"
        self.date = "date"
        self.hour = "hour"

#Abstract Builder Class
class UrlBuilder(ABC):
    @abstractmethod
    def get_real_link(self,real_link):
        pass
    @abstractmethod
    def get_ip_addy(self,ip_addy):
        pass
    @abstractmethod
    def get_ad_type(self):
        pass
    @abstractmethod
    def get_date(self):
        pass
    @abstractmethod
    def generate_token(self):
        pass
    @abstractmethod
    def return_data(self):
        pass