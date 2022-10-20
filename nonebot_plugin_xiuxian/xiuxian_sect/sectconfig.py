import json
import os
from pathlib import Path

configkey = [
    "LEVLECOST", 
    "等级建设度", 
    "发放宗门资材", 
    "每日宗门任务次上限", 
    "宗门任务完成cd", 
    "宗门任务刷新cd", 
    "宗门任务",
    "宗门主功法参数"
    ]
CONFIG = {
    "LEVLECOST" : {
    #攻击修炼的灵石消耗
    '0':10000,
    '1':20000,
    '2':40000,
    '3':80000,
    '4':160000,
    '5':320000,
    '6':500000,
    '7':500000,
    '8':500000,
    '9':500000,
    '10':500000,
    '11':500000,
    '12':500000,
    '13':500000,
    '14':500000,
    '15':500000,
    '16':500000,
    '17':500000,
    '18':500000,
    '19':500000,
    '20':500000,
    '21':500000,
    '22':500000,
    '23':500000,
    '24':500000,
    '25':0,
    },
    "等级建设度":5000000,#决定宗门修炼上限等级的参数，500万贡献度每级
    "发放宗门资材":{
        "时间":"11-12",#定时任务发放宗门资材，每日11-12点根据 对应宗门贡献度的 * 倍率 发放资材
        "倍率":1,#倍率
    },
    "每日宗门任务次上限":3,
    "宗门任务完成cd":1800,#宗门任务每次完成间隔，单位秒
    "宗门任务刷新cd":300,#宗门任务刷新间隔，单位秒
    "宗门主功法参数":{
        "获取消耗的资材":3000000,#最终消耗会乘档位
        "获取消耗的灵石":300000,#最终消耗会乘档位
        "获取到功法的概率":100,
        "建设度":10000000,#建设度除以此参数，一共10档（10档目前无法配置,对应天地玄黄人上下）
    },
    "宗门任务":{
        #type=1：需要扣气血，type=2：需要扣灵石
        #cost：消耗，type=1时，气血百分比，type=2时，消耗灵石
        #give：给与玩家当前修为的百分比修为
        #sect：给与所在宗门 储备的灵石，同时会增加灵石 * 10 的建设度
        "巡逻周边":{
            "desc":"宗门附近有人在捣乱，请道友去周边震慑宵小吧",
            "type":1,
            "cost":0.1,
            "give":0.002,
            "sect":20000,
        },
        "寻找宝物":{
            "desc":"宗门现在需要宝物：捆仙锁，请道友去寻来交给宗门吧",
            "type":2,
            "cost":30000,
            "give":0.05,
            "sect":50000,
        },
      "外出探查": {
         "desc": "宗门东北方有烟雾弥漫，请道友前去查看情况",
         "type": 1,
         "cost": 0.1,
         "give": 0.002,
         "sect": 5000
      },
      "抓捕劣徒": {
         "desc": "有弟子坠于铜臭，借钱抛洒，债台高筑，请道友将其抓回惩戒",
         "type": 1,
         "cost": 0.3,
         "give": 0.006,
         "sect": 15000
      },
      "狩猎邪修": {
         "desc": "传言山外村庄有邪修抢夺灵石，请道友下山为民除害",
         "type": 1,
         "cost": 0.7,
         "give": 0.014,
         "sect": 35000
      },
      "查抄窝点": {
         "desc": "有少量弟子不在金银阁消费，私自架设小型窝点，请道友前去查抄",
         "type": 1,
         "cost": 0.5,
         "give": 0.01,
         "sect": 25000
      },
      "搜查物品": {
         "desc": "宗门有弟子私下收藏铁锅和锤子烧火做饭，请道友前往搜查",
         "type": 1,
         "cost": 0.1,
         "give": 0.002,
         "sect": 5000
      },
      "九转仙丹": {
         "desc": "山门将开，宗门急缺一批药草熬制九转丹，请道友下山购买",
         "type": 2,
         "cost": 5000,
         "give": 0.025,
         "sect": 25000
      },
      "劝离凡俗": {
         "desc": "有凡俗漂泊至山外，虽有仙缘，但无仙份，请道友筹措一笔盘缠，助其回乡，重入红尘",
         "type": 2,
         "cost": 1000,
         "give": 0.005,
         "sect": 5000
      },
      "仗义疏财": {
         "desc": "在宗门外见到师弟欠了别人灵石被追打催债，请道友帮助其还清赌债",
         "type": 2,
         "cost": 8000,
         "give": 0.04,
         "sect": 40000
      },
      "红尘寻宝": {
         "desc": "山下一月一度的市场又开张了，其中虽凡物较多，但是请道友慷慨解囊，为宗门购买一些蒙尘奇宝",
         "type": 2,
         "cost": 6000,
         "give": 0.003,
         "sect": 30000
      }
    }
}

def get_config():
    try:
        config = readf()
        for key in configkey:
            if key not in list(config.keys()):
                config[key] = CONFIG[key]
        savef(config)
    except:
        config = CONFIG
        savef(config)
    return config

CONFIGJSONPATH = Path(__file__).parent
FILEPATH = CONFIGJSONPATH / 'config.json'
def readf():
    with open(FILEPATH, "r", encoding="UTF-8") as f:
        data = f.read()
    return json.loads(data)


def savef(data):
    data = json.dumps(data, ensure_ascii=False, indent=3)
    savemode = "w" if os.path.exists(FILEPATH) else "x"
    with open(FILEPATH, mode=savemode, encoding="UTF-8") as f:
        f.write(data)
        f.close
    return True