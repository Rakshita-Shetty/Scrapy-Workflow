import scrapy
from ..items import MobiletutorialItem


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    pagenumber = 2
    start_urls = ['https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi%7CSamsung&dc&qid=1611369038&rnid=3837712031&ref=sr_nr_p_89_3/']

    def parse(self, response):
        items = MobiletutorialItem()
        
        mobile_name = response.css(".a-color-base.a-text-normal::text").extract()
        mobile_price = response.css(".a-price-whole::text").extract()
        mobile_rating = response.css("span.a-icon-alt::text").extract()
        mobile_deliverytype = response.css(".sg-col-12-of-16:nth-child(6) .a-icon-medium , .AdHolder+ .sg-col-12-of-16 .s-align-children-center span , .s-align-children-center .s-align-children-center+ .a-row span").css("::text").extract()


        mobile_deliverytype = [x.strip() for x in mobile_deliverytype]
        mobile_rating = [x.split(' ')[0] for x in mobile_rating]
        
        for mobiles in zip(mobile_name,mobile_price,mobile_rating,mobile_deliverytype):
             items['mobile_name'] = mobiles[0]
             items['mobile_price'] = mobiles[1]
             items['mobile_rating'] = mobiles[2]
             items['mobile_deliverytype'] = mobiles[3]
             yield items
            
        
        
        
        
        nextpage = 'https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi%7CSamsung&dc&page='+str(MobileSpider.pagenumber)+'/'
        
        if MobileSpider.pagenumber <= 37:
            MobileSpider.pagenumber+=1
            yield response.follow(nextpage, callback=self.parse)

