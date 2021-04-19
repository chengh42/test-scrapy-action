# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
import os
from datetime import datetime

# set up output data .csv file
data_filepath = os.path.join(os.path.dirname(__file__), "../../data/scrapped-%s.csv" % datetime.now().strftime("%Y-%m-%d-%H%M"))
if not (os.path.isfile(data_filepath)):
    with open(data_filepath, 'w') as fp:
        pass

class DemoPipeline:
    def __init__(self):
        self.file = open(data_filepath, 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
