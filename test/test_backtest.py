import QUANTAXIS as QA

class backtest(QA.QA_Backtest):

    def start(self):
        
        self.QA_backtest_init()
        #引入4个类  account,market,setting,bid

        self.settings()

        #数据库的查询示例
        #print(self.setting.client.quantaxis.stock_day.find_one({}))

        self.QA_backtest_start()

        self.get_data_from_market()

    def get_data_from_market(self):
        self.coll=self.setting.client.quantaxis.stock_day
        data=QA.QA_fetch_data('000001','2005-05-01','2006-05-04',self.coll)
        print(data)
    def get_data_from_ARP(self):
        pass
    def settings(self):
        # 设置数据库位置,用户名
        self.setting.QA_util_sql_mongo_ip='127.0.0.1'
        self.setting.QA_util_sql_mongo_port=27017
        self.setting.QA_setting_user_name='yutiansut'
        self.setting.QA_setting_user_password='yutiansut'
        # 初始化设置
        self.setting.QA_setting_init()
back=backtest()
back.start()