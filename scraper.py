from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "http://www.ashfield.gov.uk/media/1969/polling-stations.xlsx"
districts_url = "http://www.ashfield.gov.uk/media/1966/polling-districts.zip"
council_id = 'E07000170'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts')
districts_scraper.scrape()
