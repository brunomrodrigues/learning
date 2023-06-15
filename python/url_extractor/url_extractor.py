class UrlExtractor:
    def __init__(self, url):
        self.url = url.strip()
        self.sanitize_url()

    def sanitize_url(self):
        if not self.url:
            raise ValueError("URL is empty")
    
    def get_url_base(self):
        interrogation_index = self.url.find('?')
        url_base = self.url[:interrogation_index]
        return url_base

    def get_url_params(self):
        interrogation_index = self.url.find('?')
        url_parametros = self.url[interrogation_index + 1:]
        return url_parametros

    def get_value_param(self, search_param):
        param_index = self.get_url_params().find(search_param)
        value_index = param_index + len(search_param) + 1
        e_commercial_index = self.get_url_params().find('&', value_index)
        if e_commercial_index == -1:
            value = self.get_url_params()[value_index:]
        else:
            value = self.get_url_params()[value_index:e_commercial_index]
        return value


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url_extractor = UrlExtractor(url)
valor_quantidade = url_extractor.get_value_param("quantidade")
print(valor_quantidade)
