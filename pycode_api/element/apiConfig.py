#-*-coding:utf-8-*-
import random
brandName = []
class PageObject(object):
    class DpglLogin(object):
        """店铺管理录操作"""
        send_way = 'get'
        url = r'http://10.115.3.177:3860/bfsShop/list.do'
    class DpglgetFirstCategories(object):
        """获取一级分类信息"""
        send_way = 'post'
        url = r'http://10.115.3.177:3860/bfsShop/getFirstCategories.do'
    class DpglShopId(object):
        """点击编辑按钮，获取店铺信息"""
        send_way = 'get'
        url = r'http://10.115.3.177:3860/bfsShop/queryInfo.do'
        params = {'shopId':'SI_293'}
       # cookies = {'JSESSIONID': '47D463DE405572BCA335039DE6FDF1FE'}
    class DpglSearch_sqpp(object):
        """获取授权品牌"""
        send_way = 'get'
        url = r'http://10.115.3.177:3860/bfsShop/loadAllBrandInfo.do'
        params = {'brandName':'%25E5%25B0%258F%25E7%25B1%25B3'}
    class DpglgetShopByName_loginName(object):
        """验证旗舰店登录账号是否重复"""
        send_way = 'get'
        url = r'http://10.115.3.177:3860/bfsShop/getShopByName.do'
        params = {'loginName':'ghj1234544235234','shopId':''}
    class DpglgetShopByName_storeName(object):
        """验证旗舰店名称是否重复"""
        send_way = 'get'
        url = r'http://10.115.3.177:3860/bfsShop/getShopByName.do'
        params = {'storeName':'ghj1234544235234','shopId':''}
    class DpglUpload_img(object):
        """图片上传"""
        send_way = 'post'
        url = r'http://10.115.3.177:3860/bfsShop/upload.do'
        files = {"field1":('file.jpg',open(r'G:\pycode_api\data\w.jpg','rb'),'image/jpeg')}
    class DpglLoadAllBrandInfo(object):
        """搜索授权品牌"""
        send_way = 'get'
        url = r'http://10.115.3.177:3860/bfsShop/loadAllBrandInfo.do'
        params = {'brandName':'E5%B0%8F%E7%B1%B3'}
    class DpglgetCategorys(object):
        """获取二级分类"""
        send_way = 'post'
        url = r'http://10.115.3.177:3860/bfsShop/getCategorys.do'
        data = {'categoryId':'cat10000000'}
    class DpglsaveOrUpdate_save(object):
        """saveOrUpdate接口，保存店铺信息"""
        send_way = 'post'
        url = r'http://10.115.3.177:3860/bfsShop/saveOrUpdate.do'
        data = {'flag':'1','loginName':'ghj','loginPwd':'Ghj123456','storeName':'测试组_接口自动化',
        'brandLogo':r'//gfs10.atguat.net.cn/T1VCATBgWj1RCvBVdK.jpg','contacts':'郭宏杰','telephone':'15615611111',
        'mail':'491861@qq.com','state':'1','startDate':'2017-10-01','endDate':'2017-10-01',
        'brandTableRadio':'10007361_哆啦A梦','brandName':'哆啦A梦','brandId':'10007361','viceBrand':'',
        'categorys[0].firstCategoryId':'cat10000000','categorys[0].firstCategoryName':'手机、摄影、数码',
        'categorys[0].secondCategoryId':'cat10000012','categorys[0].secondCategoryName':'手机',
        'categorys[0].thirdCategoryId':'cat10000073','categorys[0].thirdCategoryName':'联通3G手机',
        'introduce':'接口自动化测试','remark':'接口自动化测试'	}
    class DpglsaveOrUpdate_fix(object):
        """saveOrUpdate接口，修改店铺信息"""
        send_way = 'post'
        url = r'http://10.115.3.177:3860/bfsShop/saveOrUpdate.do'
        data = {'id':'SI_364','flag':'1','loginName':'ghj1','loginPwd':'','storeName':'ghj1',
                'brandLogo':r'//gfs11.atguat.net.cn/T1gtWTBK_v1RCvBVdK.jpg',
                'contacts':'q','telephone':'18519118958','mail':'491861472@qq.com',
                'state':'1','startDate':'2017-10-01','endDate':'2017-10-01',
                'brandTableRadio':'10007234_小米（MI）',
                'brandName':'小米（MI）','brandId':'10007234',
                'viceBrand':'','categorys[0].firstCategoryId':'cat10000001',
                'categorys[0].firstCategoryName':'电脑、办公打印、文仪ss、礼品卡',
                'categorys[0].secondCategoryId':'cat10000015',
                'categorys[0].secondCategoryName':'笔记本',
                'categorys[0].thirdCategoryId':'cat10005442',
                'categorys[0].thirdCategoryName':'超极本',
                'introduce':'接口自动化测试','remark':'接口自动化测试'}
    class DpglDjUpdate(object):
        """冻结店铺"""
        send_way = 'post'
        url = r'http://10.115.3.177:3860/bfsShop/update.do'
        data = {'id':'SI_364','state':'0'}
    class DpglJhUpdate(object):
        """激活店铺"""
        send_way = 'post'
        url = r'http://10.115.3.177:3860/bfsShop/update.do'
        data = {'id': 'SI_364','state': '1'}
    #----------店铺审核-------------
    class DpshLogin(object):
        """店铺审核登录接口"""
        send_way = 'get'
        url = r'http://10.115.3.177:3860/bfsPage/list.do'
        params = {'shopId':'','storeName':'ghj','brandName':'','startDate':'','endDate':'','relateMobile':''}
    class DpshCheck(object):
        """店铺审核审核接口"""
        send_way = 'post'
        url = r'http://10.115.3.177:3860/bfsPage/check.do'
        data ={'id':'PI_2721','state':random.randint(1,2)}
if __name__ == "__main__":
    pass

