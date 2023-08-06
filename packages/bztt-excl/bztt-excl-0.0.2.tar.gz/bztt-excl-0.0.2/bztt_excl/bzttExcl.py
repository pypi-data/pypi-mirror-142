import json
from typing import Counter
import xlwings as xw
import shutil
from tqdm import tqdm
import datetime
from interval import Interval

class BzttExcl:  #工单处理
    log_lv = 3
    
    app=""
    wb = {}
    # def __init__(self, system_info, oltInfo, soft_ware_info):
    def  __init__(self,system_info={}):
        log_lv_data = {
            "ALL": 0,
            "TRACE": 1,
            "DEBUG": 2,
            "INFO": 3,
            "WARN": 4,
            "ERROR": 5,
            "FATAL": 6,
            "OFF": 7,
        }
        log_level = system_info.get("log_level","INFO")
        self.log_lv = log_lv_data[log_level]
        print_data = [
            {"text": "类构造成功", "color": "33"}
        ]
        self.print_log(print_data, "INFO")

        #self.app=xw.App(visible=True,add_book=False)
    def __del__(self):

        print ("")

        '''
        #time.sleep(1)
        for wdInfo in self.wb:
            print("关闭并保存:",wdInfo)
            self.wb[wdInfo].save()
            #time.sleep(2)
            self.wb[wdInfo].close()
        self.app.quit()
        '''
    # 显示信息
    def print_log(self, log_lv_info, log_lv_num):
        log_lv_data = {
            "ALL": 0,
            "TRACE": 1,
            "DEBUG": 2,
            "INFO": 3,
            "WARN": 4,
            "ERROR": 5,
            "FATAL": 6,
            "OFF": 7,
        }
        log_lv = log_lv_data[log_lv_num.upper()]
       
        if log_lv >= self.log_lv:
            print("\033[1;%sm%s\033[0m" % ("34", log_lv_num.upper()), end=" - ")
            for info in log_lv_info:
                info.setdefault("end", "\n")
                print("\033[1;%sm%s\033[0m" % (info["color"], info["text"]), end=info["end"])
    # excel 判断表格内容（ifs）
    def ifsData(self,jsonData):
        screen = "=IFS("
        for conditionInfo in jsonData["condition"]:
            if conditionInfo["type"] == "exist":
                #print("exist",conditionInfo)
                screenInfo = "OR(COUNTIF('[%s]%s'!%s,{" % (conditionInfo["sourceFile"],conditionInfo["sourceShell"],conditionInfo["Range"])
                for info in conditionInfo["sourceData"]:
                    screenInfo = screenInfo + "\"" + info + "\","
                screen = screen +screenInfo[:-1] + "})),\"" + conditionInfo["targetData"] + "\","
            if conditionInfo["type"] == "countifs":
                #print("countifs",conditionInfo)
                #COUNTIFS([20211102_待装池.xls]待调度工单!$E:$E,Q29),"待装池12"
                screenInfo = "COUNTIFS('[%s]%s'!%s:%s,%s),\"%s\"," % (conditionInfo["sourceFile"],conditionInfo["sourceShell"],conditionInfo["Range"],conditionInfo["Range"],conditionInfo["sourceData"],conditionInfo["targetData"])
                screen = screen + screenInfo
            if conditionInfo["type"] == "end":
                screenInfo = "1,\"%s\","%(conditionInfo["targetData"])
                screen = screen + screenInfo
        screen = screen[:-1] + ")" 
        # print("screen_debug",screen)

        sht = self.wb[jsonData["sourceTitle"]].sheets(jsonData["sourceShell"])
        info = sht.used_range
        nrows = info.last_cell.row
        ncolumns = info.last_cell.column
        # print("nrows",nrows,"ncolumns",ncolumns)

        # print("正在计算请稍后...")
        sht.range(jsonData["startRangeCol"] + jsonData["startRangeRow"]).value = screen
        rangeEndStr = jsonData["startRangeCol"] + str(nrows)
        sourceRange = sht.range(jsonData["startRangeCol"] + jsonData["startRangeRow"]).api
        fillRange = sht.range(jsonData["startRangeCol"] + jsonData["startRangeRow"] + ':' + rangeEndStr).api
        
        print_data = [
            {"text": "计算公式：" + screen, "color": "34"},

        ]
        self.print_log(print_data, "DEBUG")

        print_data = [
            {"text": "判断函数（ifs）", "color": "33"},
            {"text": "操作表格： [%s]%s!%s%s:%s" % (jsonData["sourceTitle"],jsonData["sourceShell"],jsonData["startRangeCol"],jsonData["startRangeRow"],rangeEndStr ), "color": "34"},
            {"text": "正在计算中，请稍后...", "color": "33"}

        ]
        self.print_log(print_data, "INFO")
        sourceRange.AutoFill(fillRange, 0)

    # 新建Shell
    def addShell(self,jsonData):
        # print("新建Shell",jsonData)
        print_data = [
            {"text": "新建Shell,请稍后...", "color": "33"},
            {"text": "[%s]%s,{%s}" % (jsonData["sourceTitle"],jsonData["after"],jsonData["targetShell"]), "color": "33"}

        ]
        self.print_log(print_data, "INFO")
        sht =  self.wb[jsonData["sourceTitle"]].sheets.add(jsonData["targetShell"], after=jsonData["after"])
    
    # 筛选数据，计算数量，列
    def countyCountyNum(self,jsonData):
        #print("jsonData",jsonData)
        print_data = [
            {"text": "正在筛选数据，计算数量，请稍后...", "color": "33"}

        ]
        self.print_log(print_data, "INFO")

        #生成专用  =SUM(COUNTIFS(
        screen = "=SUM(COUNTIFS("
        for conditionInfo in jsonData["condition"]:
            if conditionInfo["type"] == "exist":
                screenInfo = "'[%s]%s'!$%s1:$%s65536,{" % (jsonData["sourceFile"],jsonData["sourceShell"],conditionInfo["Range"],conditionInfo["Range"])
                for info in conditionInfo["data"]:
                    screenInfo = screenInfo + "\"" + info + "\","
                screen = screen +screenInfo[:-1] + "}," 
            elif conditionInfo["type"] == "timeRange":
               
                # print("conditionInfo",conditionInfo["data"])
                #if conditionInfo["data"]["start"]["disable"] == "false": #处理开始

                for timeInfo in conditionInfo["data"]:
                    screenInfo = "'[%s]%s'!$%s1:$%s65536," % (jsonData["sourceFile"],jsonData["sourceShell"],conditionInfo["Range"],conditionInfo["Range"])

                    if "Reformat" in timeInfo:
                        Reformat = timeInfo["Reformat"]
                    else:
                        Reformat = '%Y-%m-%d %H:%M:%S'

                    startTimeStr = timeInfo["data"]
                    SourceTimeStr = datetime.datetime.strptime(str(startTimeStr),timeInfo["dataFormat"])  + datetime.timedelta(days = int(timeInfo["num"]))
                    startTimeStr = SourceTimeStr.strftime( timeInfo["type"] + Reformat )   #'>%Y-%m-%d %H:%M:%S'
                    screenInfo = screenInfo + "\"" + startTimeStr + "\","
                    #print("screenInfo",screenInfo)
                    screen = screen +screenInfo[:-1] + "," 
                #循环赋值
        #print("screen",screen)
 
        data = {}
        log_data_tmp = ""
        #生成
        for info in jsonData["county"]:
            #print("countyCountyNum",info)
            screenInfoFor = ""
            for value in info["value"]:
                #print("value",value)
                screenInfo = r"'[%s]%s'!$%s1:$%s65536,{" % (jsonData["sourceFile"],jsonData["sourceShell"],value["Range"],value["Range"])
                screenInfo = screenInfo + "\"" + value["Regular"] + "\","
                screenInfoFor = screenInfoFor + screenInfo[:-1] + "},"
                #print("screenInfo",screenInfo)
                
            data[info["title"]] = screen + screenInfoFor[:-1] + "))" 
            log_data_tmp = log_data_tmp + info["title"] + " : " + screen + screenInfoFor[:-1] + "))" + "\n\n"
        
        print_data = [
            {"text": "筛选表格", "color": "33","end":"："},
            {"text": "[%s]%s" % (jsonData["targetTitle"],jsonData["targetShell"]), "color": "34","end":"\n"},

            {"text": "写入起始位置", "color": "33","end":"\n"},
            {"text": "[%s]%s!%s%s" % (jsonData["targetTitle"],jsonData["targetShell"],jsonData["targetRange"]["startLetter"],jsonData["targetRange"]["startNum"]), "color": "34"},

        ]
        self.print_log(print_data, "INFO")

        print_data = [
            {"text": "筛选条件", "color": "33","end":"\n"},
            {"text": log_data_tmp, "color": "34"},
        ]
        self.print_log(print_data, "DEBUG")

        i = int(jsonData["targetRange"]["startNum"])
        sht = self.wb[jsonData["targetTitle"]].sheets(jsonData["targetShell"])
        
        for info in data:
            rang = jsonData["targetRange"]["startLetter"]+ str(i)
            sht.range(rang).formula = data[info]#单元格赋值
            i = i +1

        return

    def RemoveDuplicates(self,jsonData):

        print_str_copy = "[%s]%s!%s:%s,{%s}" % (jsonData["sourceTitle"],jsonData["sourceShell"],jsonData["sourceRange"]["start"],jsonData["sourceRange"]["end"],jsonData["RemoveNum"])
        print_data = [
            {"text": "删除重复项", "color": "33"},
            {"text": print_str_copy, "color": "33"},

        ]
        self.print_log(print_data, "INFO")

        shtSource = self.wb[jsonData["sourceTitle"]].sheets(jsonData["sourceShell"])

        shtSource.range(jsonData["sourceRange"]["start"],jsonData["sourceRange"]["end"]).api.RemoveDuplicates(int(jsonData["RemoveNum"]))

    # 复制数据
    def copyData(self,copyJson):
        print_str_copy = "[%s]%s!%s" % (copyJson["sourceTitle"],copyJson["sourceShell"],copyJson["sourceRange"]["start"] + ":" + copyJson["sourceRange"]["end"])
        
        print_str_paste = "[%s]%s!{ " % (copyJson["targetTitle"],copyJson["targetShell"])
        for info in copyJson["targetRange"]:
            print_str_paste = print_str_paste + info["start"] + ", "
        print_str_paste = print_str_paste[:-1] + "}"

        print_data = [
            {"text": "复制数据", "color": "33"},
            {"text": print_str_copy, "color": "33","end":" --> "},
            {"text": print_str_paste, "color": "33"}
        ]
        self.print_log(print_data, "INFO")

        shtSource = self.wb[copyJson["sourceTitle"]].sheets(copyJson["sourceShell"])
        shtTarget = self.wb[copyJson["targetTitle"]].sheets(copyJson["targetShell"])
        rangSource = copyJson["sourceRange"]["start"] + ":" + copyJson["sourceRange"]["end"]
        shtSource.range(rangSource).copy(destination=None)

        for pasteInfo in copyJson["targetRange"]:
            rangTarget = pasteInfo["start"]
            shtTarget.range(rangTarget).paste(paste="values_and_number_formats")


        '''
        copyDataTmp = shtSource.range(rangSource).value
        print("copyDataTmp",copyDataTmp)
        print("rangTarget",rangTarget)
        #sht.range('A1').options(transpose=True).value=[1,2,3]
        shtTarget.range(rangTarget).options(transpose=True).value = copyDataTmp
        '''

    def ExcelColumn(self,n:int)->str:
        num = [chr(i) for i in range(65,91)]
        ret,(n,m) = '',divmod(n-1,26)
        if n: ret += self.ExcelColumn(n)
        ret += num[m]
        return ret
    def Col2Int(self,s:str)->int:
        ret=0
        ret += (ord(s[0])-64)*26**(len(s)-1)
        s = s[1:]
        if s: ret += self.Col2Int(s)
        return ret

    def advancedFilter(self,advancedFilterJson):#高级筛选
        print("advancedFilterJson",advancedFilterJson)
        
        #print("sourceTitle",advancedFilterJson["sourceTitle"])
        #print("sourceShell",advancedFilterJson["sourceShell"])

        #print("sourceTitle",advancedFilterJson["targetTitle"])
        #print("sourceShell",advancedFilterJson["targetShell"])

        #数据
        shtSource = self.wb[advancedFilterJson["sourceTitle"]].sheets(advancedFilterJson["sourceShell"])
        shtTarget = self.wb[advancedFilterJson["targetTitle"]].sheets(advancedFilterJson["targetShell"])
        condition = advancedFilterJson["condition"]
        iNum = 0
        #获取row
        info = shtSource.used_range
        nrows = info.last_cell.row
        ncolumns = info.last_cell.column
		#获取表头
        range_value_list = [shtSource.range((1,1),(1,ncolumns)).value]

        range_value_list_source = shtSource.range(1,1).expand().value
        for infoData in tqdm(range_value_list_source): #tqdm
            str_value_row = ""
            for infoAll in condition:  #符合所有条件  有一个条件不符,则停止
                for info in infoAll:
                    if info["type"] == "end":
                        str_value_row = infoData
                        break
                    numId = self.Col2Int(info["Range"]) - 1
                    select_value_sheet = infoData[numId]
                    if info["type"] == "disExist":#存在 
                        if select_value_sheet in info["data"]:
                            str_value_row = ""
                            break
                    elif info["type"] == "exist":#不存在,剔除
                        
                        if select_value_sheet not in info["data"]:
                            break
                    elif info["type"] == "end":
                        str_value_row = infoData
                #数据赋值
                if str_value_row == "":
                    continue
                else:
                    range_value_list.append(str_value_row)
                    break

        shtTarget.range(advancedFilterJson["targetRange"]).value = range_value_list
        self.wb[advancedFilterJson["targetTitle"]].save()

    # 格式化数据（初始）
    def formatJson(self,formatJson):
        print_data = [
            {"text": "开始格式化数据", "color": "33"}
        ]
        self.print_log(print_data, "INFO")

        formatJsonStr =json.dumps(formatJson,ensure_ascii=False)   #转换字符串
        
        for i in range(0,len(formatJson["formatVariable"])):
            formatJsonStr =json.dumps(formatJson,ensure_ascii=False)   #转换字符串
            fucInfoJson = formatJson["formatVariable"]
            info = fucInfoJson[i]

            print_data = [
                {"text": "格式化类型：", "color": "34","end":" "},
                {"text": info["type"] , "color": "33"},

                {"text": "格式化数据：", "color": "33","end":" "},
                {"text": info, "color": "34"},
            ]
            self.print_log(print_data, "DEBUG")

            if info["type"] == "input":
                inputIntStr = input(info["title"])
                #inputIntStr = "20211102"
                formatJsonStr = formatJsonStr.replace(info["name"],inputIntStr)

                #字符串转换
            elif info["type"] == "json":
                #print("json:",info["value"])
                valueStr = json.dumps(info["value"],ensure_ascii=False) 
                formatJsonStr = formatJsonStr.replace( "\"" + info["name"] + "\"",valueStr)
                #print("formatJsonStr:",formatJsonStr)
            elif info["type"] == "time":
                startTimeStr = str(info["value"])
                SourceTimeStr = datetime.datetime.strptime(startTimeStr,info["valueFormat"])  + datetime.timedelta(days = int(info["num"]))
                startTimeStr = SourceTimeStr.strftime( info["format"] )   #'>%Y-%m-%d %H:%M:%S'
                formatJsonStr = formatJsonStr.replace( "\"" + info["name"] + "\"",startTimeStr)

            elif info["type"] == "date2Rang":
                #print("date2Rang:",info["value"])
                #str转time
                SourceTimeStr = datetime.datetime.strptime(str(info["value"]["dateStr"]),info["value"]["dateFormat"])
                year = SourceTimeStr.year
                month = SourceTimeStr.month
                day = SourceTimeStr.day
                #print("SourceTimeStr",SourceTimeStr,year,month,day)
                for RangeFormatInfo in info["value"]["RangeFormat"]:
                    #print("RangeFormatInfo",RangeFormatInfo)
                    chengeStr = 0
                    #输出B1
                    if RangeFormatInfo["type"] == "day":
                        chengeStr = int(day)
                    elif RangeFormatInfo["type"] == "month":
                        chengeStr = int(month)
                    elif RangeFormatInfo["type"] == "year":
                        chengeStr = int(year)

                    zoom_2_5 = Interval(RangeFormatInfo["Range"][0], RangeFormatInfo["Range"][1])
                    
                    #在区间内
                    if chengeStr in zoom_2_5:
                        if RangeFormatInfo["direction"] == "column":
                            #字母转转数字 columnInitial
                            columnInitial = self.Col2Int(RangeFormatInfo["columnInitial"])
                            columnTial = columnInitial + chengeStr
                            columnStr = self.ExcelColumn(columnTial - RangeFormatInfo["Range"][0])
                            chengeAll = columnStr +  RangeFormatInfo["rowInitial"]
                            #print("chengeAll",chengeAll)
                            formatJsonStr = formatJsonStr.replace(info["name"],chengeAll)
                            break












            #重置
            formatJson = json.loads(formatJsonStr)



        data = json.loads(formatJsonStr)
        return data
            


    def advancedFilter_1(self,advancedFilterJson):
        print("advancedFilterJson",advancedFilterJson)


        #数据
        shtSource = self.wb[advancedFilterJson["sourceTitle"]].sheets(advancedFilterJson["sourceShell"])
        shtTarget = self.wb[advancedFilterJson["targetTitle"]].sheets(advancedFilterJson["targetShell"])
        condition = advancedFilterJson["condition"]
        iNum = 0
        #获取row
        info = shtSource.used_range
        nrows = info.last_cell.row
        ncolumns = info.last_cell.column
		#获取表头
        range_value_list = [shtSource.range((1,1),(1,ncolumns)).value]
        #获取currn
        for i in tqdm(range(2,nrows + 1)):
            #print("数据",i,sht.range("A" + str(i)).value)
            #判断数据
            #str_sheet1 = "A"+str(i)+":"+"E"+str(i)
            str_value_row = ""
            for infoAll in condition:  #符合所有条件  有一个条件不符,则停止
                #print("condition:",condition)
                #print("info:",info)
                for info in infoAll:
                    if info["type"] == "disExist":#存在 
                        #print("执行",iNum)
                        select_sheet_value = info["Range"]+str(i)
                        select_value_sheet = shtSource.range(select_sheet_value).value
                        if select_value_sheet in info["data"]:
                            str_value_row = ""
                            break
                            
                    elif info["type"] == "exist":#不存在,剔除
                        select_sheet_value = info["Range"]+str(i)
                        select_value_sheet = shtSource.range(select_sheet_value).value
                        if select_value_sheet not in info["data"]:
                            break
                    elif info["type"] == "end":
                        str_value_row = shtSource.range((int(i),1),(int(i),ncolumns)).value
                    if str_value_row != "":
                        break     
                #数据赋值
                if str_value_row == "":
                    continue
                else:
                    range_value_list.append(str_value_row)
                    break


        #print("data:")

        shtTarget.range(advancedFilterJson["targetRange"]).value = range_value_list

    def openfile(self,iniFile):        
        print_data = [
            {"text": "正在复制文件，请稍后...", "color": "33"}
        ]
        self.print_log(print_data, "INFO")

        #检测文件是否存在

        #复制文件,并重命名
        for fileInfo in iniFile["info"]:
            print_data = [
                {"text": fileInfo["sourcePath"] + fileInfo["name"] + "." + fileInfo["suffix"], "color": "33","end":" --> "},
                {"text": fileInfo["targetPath"] + fileInfo["name"] + "_" + fileInfo["title"] + "." + fileInfo["suffix"], "color": "33"},
            ]
            self.print_log(print_data, "INFO")

            shutil.copyfile(fileInfo["sourcePath"] + fileInfo["name"] + "." + fileInfo["suffix"], fileInfo["targetPath"] + fileInfo["name"] + "_" + fileInfo["title"] + "." + fileInfo["suffix"])
        print_data = [
            {"text": "文件复制完毕", "color": "33"}
        ]
        self.print_log(print_data, "INFO")

        print_data = [
                {"text": "正在打开文件,请稍后...", "color": "33"},
        ]
        self.print_log(print_data, "INFO")

        self.app = xw.App(visible=True,add_book=False)
        self.app.display_alerts=False
        
        #打开文件
        for fileInfo in iniFile["info"]:
            print_data = [
                {"text": fileInfo["title"], "color": "33","end":" - "},
                {"text": fileInfo["targetPath"] + fileInfo["name"] + "_" + fileInfo["title"] + "." + fileInfo["suffix"], "color": "33"},

            ]
            self.print_log(print_data, "INFO")

            #self.wb[fileInfo["title"]] =  xw.Book(fileInfo["path"] + fileInfo["name"] + "_" + fileInfo["title"] + "." + fileInfo["suffix"]) #创建一个新的Excel文件
            self.wb[fileInfo["title"]] =  self.app.books.open(fileInfo["targetPath"] + fileInfo["name"] + "_" + fileInfo["title"] + "." + fileInfo["suffix"]) #创建一个新的Excel文件
        print_data = [
            {"text": "文件打开完毕", "color": "33"}
        ]
        self.print_log(print_data, "INFO")
        #校验 文件
        

   

