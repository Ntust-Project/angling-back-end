# coding: utf-8
# 後台處理
import time
while(True):
#   if int(time.strftime("%M"))*60+int(time.strftime("%S")) >= 585 or int(time.strftime("%M"))*60+int(time.strftime("%S")) <= 1385:
    if True:
        try:
            #資料抓取區
            import pandas
            import requests
            import sys
            reload(sys)
            sys.setdefaultencoding('utf-8')
            #參數區
            payload = {
                '__VIEWSTATE':'/wEPDwUJOTI2MTk1Mzg4D2QWAgIBD2QWBAIlD2QWBGYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPZBYCZg8PFgIeB1Zpc2libGVoZBYGAgIPZBYIZg9kFgJmDxAPFggeCkRhdGFNZW1iZXIFCUVkdV9Pcmdhbh4NRGF0YVRleHRGaWVsZAURQ29sbGVnZURlcGFydG1lbnQeDkRhdGFWYWx1ZUZpZWxkBQJOTx4LXyFEYXRhQm91bmRnZBAVNwnkuI3pgbjmk4cW6Kit6KiI5a246ZmiLeW7uuevieezuyLoqK3oqIjlrbjpmaIt5Ym15oSP6Kit6KiI5a245aOr54+tHOioreioiOWtuOmZoi3oqK3oqIjnoJTnqbbmiYAW6Kit6KiI5a246ZmiLeioreioiOezuyvoqK3oqIjlrbjpmaIt5Ym15oSP6Kit6KiI5a245aOr5a245L2N5a2456iLMeaHieeUqOenkeaKgOWtuOmZoi3mh4nnlKjnp5HmioDlrbjlo6vlrbjkvY3lrbjnqIsx5oeJ55So56eR5oqA5a246ZmiLemGq+WtuOW3peeoi+WtuOWjq+WtuOS9jeWtuOeoiyjmh4nnlKjnp5HmioDlrbjpmaIt6Yar5a245bel56iL56CU56m25omAMeaHieeUqOenkeaKgOWtuOmZoi3oibLlvanoiIfnhafmmI7np5HmioDnoJTnqbbmiYBA5oeJ55So56eR5oqA5a246ZmiLeiJsuW9qeW9seWDj+iIh+eFp+aYjuenkeaKgOWtuOWjq+WtuOS9jeWtuOeoiyjmh4nnlKjnp5HmioDlrbjpmaIt5oeJ55So56eR5oqA56CU56m25omAJeaHieeUqOenkeaKgOWtuOmZoi3kuI3liIbns7vlrbjlo6vnj6005oeJ55So56eR5oqA5a246ZmiLeaZuuaFp+iyoeeUouasiuWtuOWjq+WtuOS9jeWtuOeoizrmh4nnlKjnp5HmioDlrbjpmaIt5oeJ55So56eR5oqA56CU56m25omA5p2Q5paZ56eR5oqA5a2456iLIuaHieeUqOenkeaKgOWtuOmZoi3lsIjliKnnoJTnqbbmiYAc6Zu76LOH5a246ZmiLeizh+ioiuW3peeoi+ezuxzpm7vos4flrbjpmaIt6Zu76LOH5a245aOr54+tHOmbu+izh+WtuOmZoi3pm7vmqZ/lt6XnqIvns7si6Zu76LOH5a246ZmiLeWFiembu+W3peeoi+eglOeptuaJgBzpm7vos4flrbjpmaIt6Zu75a2Q5bel56iL57O7JeS6uuaWh+ekvuacg+WtuOmZoi3kurrmlofnpL7mnIPlrbjnp5El5Lq65paH56S+5pyD5a246ZmiLeW4q+izh+WfueiCsuS4reW/gyLkurrmlofnpL7mnIPlrbjpmaIt5oeJ55So5aSW6Kqe57O7H+S6uuaWh+ekvuacg+WtuOmZoi3pgJrorZjlrbjnp5Ec5Lq65paH56S+5pyD5a246ZmiLemrlOiCsuWupDHkurrmlofnpL7mnIPlrbjpmaIt5pW45L2N5a2457+S6IiH5pWZ6IKy56CU56m25omANOaZuuaFp+iyoeeUouWtuOmZoi3mmbrmhafosqHnlKLmrIrlrbjlo6vlrbjkvY3lrbjnqIsi5pm65oWn6LKh55Si5a246ZmiLeWwiOWIqeeglOeptuaJgDHmmbrmhafosqHnlKLlrbjpmaIt56eR5oqA566h55CG5a245aOr5a245L2N5a2456iLKOaZuuaFp+iyoeeUouWtuOmZoi3np5HmioDnrqHnkIbnoJTnqbbmiYAc566h55CG5a246ZmiLeS8gealreeuoeeQhuezuyvnrqHnkIblrbjpmaIt6LKh5YuZ6YeR6J6N5a245aOr5a245L2N5a2456iLIueuoeeQhuWtuOmZoi3osqHli5nph5Hono3noJTnqbbmiYAc566h55CG5a246ZmiLeW3pealreeuoeeQhuezuxDnrqHnkIblrbjpmaItTUJBHOeuoeeQhuWtuOmZoi3nrqHnkIblrbjlo6vnj60c566h55CG5a246ZmiLeeuoeeQhueglOeptuaJgBznrqHnkIblrbjpmaIt6LOH6KiK566h55CG57O7LueuoeeQhuWtuOmZoi3mlrDliqDlnaHnrqHnkIbnoqnlo6vlnKjogbflsIjnj60r566h55CG5a246ZmiLeenkeaKgOeuoeeQhuWtuOWjq+WtuOS9jeWtuOeoiyLnrqHnkIblrbjpmaIt56eR5oqA566h55CG56CU56m25omAKOW3peeoi+WtuOmZoi3oh6rli5XljJblj4rmjqfliLbnoJTnqbbmiYAc5bel56iL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LeWFiembu+W3peeoi+eglOeptuaJgBzpm7vos4flrbjpmaIt6Zu75a2Q5bel56iL57O7JeS6uuaWh+ekvuacg+WtuOmZoi3kurrmlofnpL7mnIPlrbjnp5El5Lq65paH56S+5pyD5a246ZmiLeW4q+izh+WfueiCsuS4reW/gyLkurrmlofnpL7mnIPlrbjpmaIt5oeJ55So5aSW6Kqe57O7H+S6uuaWh+ekvuacg+WtuOmZoi3pgJrorZjlrbjnp5Ec5Lq65paH56S+5pyD5a246ZmiLemrlOiCsuWupDHkurrmlofnpL7mnIPlrbjpmaIt5pW45L2N5a2457+S6IiH5pWZ6IKy56CU56m25omANOaZuuaFp+iyoeeUouWtuOmZoi3mmbrmhafosqHnlKLmrIrlrbjlo6vlrbjkvY3lrbjnqIsi5pm65oWn6LKh55Si5a246ZmiLeWwiOWIqeeglOeptuaJgDHmmbrmhafosqHnlKLlrbjpmaIt56eR5oqA566h55CG5a245aOr5a245L2N5a2456iLKOaZuuaFp+iyoeeUouWtuOmZoi3np5HmioDnrqHnkIbnoJTnqbbmiYAc566h55CG5a246ZmiLeS8gealreeuoeeQhuezuyvnrqHnkIblrbjpmaIt6LKh5YuZ6YeR6J6N5a245aOr5a245L2N5a2456iLIueuoeeQhuWtuOmZoi3osqHli5nph5Hono3noJTnqbbmiYAc566h55CG5a246ZmiLeW3pealreeuoeeQhuezuxDnrqHnkIblrbjpmaItTUJBHOeuoeeQhuWtuOmZoi3nrqHnkIblrbjlo6vnj60c566h55CG5a246ZmiLeeuoeeQhueglOeptuaJgBznrqHnkIblrbjpmaIt6LOH6KiK566h55CG57O7LueuoeeQhuWtuOmZoi3mlrDliqDlnaHnrqHnkIbnoqnlo6vlnKjogbflsIjnj60r566h55CG5a246ZmiLeenkeaKgOeuoeeQhuWtuOWjq+WtuOS9jeWtuOeoiyLnrqHnkIblrbjpmaIt56eR5oqA566h55CG56CU56m25omAKOW3peeoi+WtuOmZoi3oh6rli5XljJblj4rmjqfliLbnoJTnqbbmiYAc5bel56iL5a246ZmiLeW3peeoi+WtuOWjq+ePrRzlt6XnqIvlrbjpmaIt5YyW5a245bel56iL57O7HOW3peeoi+WtuOmZoi3nh5/lu7rlt6XnqIvns7s35bel56iL5a246ZmiLee2oOiDveeUoualreapn+mbu+W3peeoi+WtuOWjq+WtuOS9jeWtuOeoixzlt6XnqIvlrbjpmaIt5qmf5qKw5bel56iL57O7IuW3peeoi+WtuOmZoi3mnZDmlpnnp5HmioDnoJTnqbbmiYAx5bel56iL5a246ZmiLemrmOmajuenkeaKgOeglOeZvOeiqeWjq+WtuOS9jeWtuOeoixzlt6XnqIvlrbjpmaIt6Leo57O75omA5a2456iLNOW3peeoi+WtuOmZoi3lhYjpgLLnp5HmioDlhajoi7Hoqp7lpJblnIvlrbjnlJ/lsIjnj6065bel56iL5a246ZmiLeW3peeoi+aKgOihk+eglOeptuaJgOaKgOiBt+WwiOalreeZvOWxleWtuOeoiyXlt6XnqIvlrbjpmaIt5p2Q5paZ56eR5a246IiH5bel56iL57O7A0FMTBU3BE5VTEwENC1BRAQ0LUNEBDQtREUENC1EVAQ0LURYBDAtQVQEMC1CQgQwLUJFBDAtQ0kEMC1DWAQwLUVOBDAtSEMEMC1JQgQwLU1TBDAtUEEEMi1DUwQyLUVDBDItRUUEMi1FTwQyLUVUBDUtQ0MENS1FUAQ1LUZMBDUtR0UENS1QRQQ1LVZFBDYtSUIENi1QQQQ2LVRCBDYtVE0EMy1CQQQzLUZCBDMtRk4EMy1JTQQzLU1BBDMtTUIEMy1NRwQzLU1JBDMtU0cEMy1UQgQzLVRNBDEtQUMEMS1DRQQxLUNIBDEtQ1QEMS1HWAQxLU1FBDEtTVMEMS1SRAQxLVJTBDEtVEUEMS1UVgQxLVRYAV8UKwM3Z2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBZmQCAQ9kFgJmDxAPFggfAQUJRWR1X09yZ2FuHwIFBlBlcmlvZB8DBQJOTx8EZ2QQFQEJ5LiN6YG45pOHFQEETlVMTBQrAwFnFgFmZAICD2QWAmYPEA8WCB8BBQlFZHVfT3JnYW4fAgUFZ3JhZGUfAwUCTk8fBGdkEBUBCeS4jemBuOaThxUBBE5VTEwUKwMBZxYBZmQCAw9kFgJmDxAPFggfAQUJRWR1X09yZ2FuHwIFBUNsYXNzHwMFAk5PHwRnZBAVAQnkuI3pgbjmk4cVAQROVUxMFCsDAWcWAWZkAgQPZBYIZg9kFgJmDxAPFggfAQUJRWR1X09yZ2FuHwIFEUNvbGxlZ2VEZXBhcnRtZW50HwMFAk5PHwRnZBAVNwnkuI3pgbjmk4cW6Kit6KiI5a246ZmiLeW7uuevieezuyLoqK3oqIjlrbjpmaIt5Ym15oSP6Kit6KiI5a245aOr54+tHOioreioiOWtuOmZoi3oqK3oqIjnoJTnqbbmiYAW6Kit6KiI5a246ZmiLeioreioiOezuyvoqK3oqIjlrbjpmaIt5Ym15oSP6Kit6KiI5a245aOr5a245L2N5a2456iLMeaHieeUqOenkeaKgOWtuOmZoi3mh4nnlKjnp5HmioDlrbjlo6vlrbjkvY3lrbjnqIsx5oeJ55So56eR5oqA5a246ZmiLemGq+WtuOW3peeoi+WtuOWjq+WtuOS9jeWtuOeoiyjmh4nnlKjnp5HmioDlrbjpmaIt6Yar5a245bel56iL56CU56m25omAMeaHieeUqOenkeaKgOWtuOmZoi3oibLlvanoiIfnhafmmI7np5HmioDnoJTnqbbmiYBA5oeJ55So56eR5oqA5a246ZmiLeiJsuW9qeW9seWDj+iIh+eFp+aYjuenkeaKgOWtuOWjq+WtuOS9jeWtuOeoiyjmh4nnlKjnp5HmioDlrbjpmaIt5oeJ55So56eR5oqA56CU56m25omAJeaHieeUqOenkeaKgOWtuOmZoi3kuI3liIbns7vlrbjlo6vnj6005oeJ55So56eR5oqA5a246ZmiLeaZuuaFp+iyoeeUouasiuWtuOWjq+WtuOS9jeWtuOeoizrmh4nnlKjnp5HmioDlrbjpmaIt5oeJ55So56eR5oqA56CU56m25omA5p2Q5paZ56eR5oqA5a2456iLIuaHieeUqOenkeaKgOWtuOmZoi3lsIjliKnnoJTnqbbmiYAc6Zu76LOH5a246ZmiLeizh+ioiuW3peeoi+ezuxzpm7vos4flrbjpmaIt6Zu76LOH5a245aOr54+tHOmbu+izh+WtuOmZoi3pm7vmqZ/lt6XnqIvns7si6Zu76LOH5a246ZmiLeWFiembu+W3peeoi+eglOeptuaJgBzpm7vos4flrbjpmaIt6Zu75a2Q5bel56iL57O7JeS6uuaWh+ekvuacg+WtuOmZoi3kurrmlofnpL7mnIPlrbjnp5El5Lq65paH56S+5pyD5a246ZmiLeW4q+izh+WfueiCsuS4reW/gyLkurrmlofnpL7mnIPlrbjpmaIt5oeJ55So5aSW6Kqe57O7H+S6uuaWh+ekvuacg+WtuOmZoi3pgJrorZjlrbjnp5Ec5Lq65paH56S+5pyD5a246ZmiLemrlOiCsuWupDHkurrmlofnpL7mnIPlrbjpmaIt5pW45L2N5a2457+S6IiH5pWZ6IKy56CU56m25omANOaZuuaFp+iyoeeUouWtuOmZoi3mmbrmhafosqHnlKLmrIrlrbjlo6vlrbjkvY3lrbjnqIsi5pm65oWn6LKh55Si5a246ZmiLeWwiOWIqeeglOeptuaJgDHmmbrmhafosqHnlKLlrbjpmaIt56eR5oqA566h55CG5a245aOr5a245L2N5a2456iLKOaZuuaFp+iyoeeUouWtuOmZoi3np5HmioDnrqHnkIbnoJTnqbbmiYAc566h55CG5a246ZmiLeS8gealreeuoeeQhuezuyvnrqHnkIblrbjpmaIt6LKh5YuZ6YeR6J6N5a245aOr5a245L2N5a2456iLIueuoeeQhuWtuOmZoi3osqHli5nph5Hono3noJTnqbbmiYAc566h55CG5a246ZmiLeW3pealreeuoeeQhuezuxDnrqHnkIblrbjpmaItTUJBHOeuoeeQhuWtuOmZoi3nrqHnkIblrbjlo6vnj60c566h55CG5a246ZmiLeeuoeeQhueglOeptuaJgBznrqHnkIblrbjpmaIt6LOH6KiK566h55CG57O7LueuoeeQhuWtuOmZoi3mlrDliqDlnaHnrqHnkIbnoqnlo6vlnKjogbflsIjnj60r566h55CG5a246ZmiLeenkeaKgOeuoeeQhuWtuOWjq+WtuOS9jeWtuOeoiyLnrqHnkIblrbjpmaIt56eR5oqA566h55CG56CU56m25omAKOW3peeoi+WtuOmZoi3oh6rli5XljJblj4rmjqfliLbnoJTnqbbmiYAc5bel56iL5a246ZmiLeW3peeoi+WtuOWjq+ePrRzlt6XnqIvlrbjpmaIt5YyW5a245bel56iL57O7HOW3peeoi+WtuOmZoi3nh5/lu7rlt6XnqIvns7s35bel56iL5a246ZmiLee2oOiDveeUoualreapn+mbu+W3peeoi+WtuOWjq+WtuOS9jeWtuOeoixzlt6XnqIvlrbjpmaIt5qmf5qKw5bel56iL57O7IuW3peeoi+WtuOmZoi3mnZDmlpnnp5HmioDnoJTnqbbmiYAx5bel56iL5a246ZmiLemrmOmajuenkeaKgOeglOeZvOeiqeWjq+WtuOS9jeWtuOeoixzlt6XnqIvlrbjpmaIt6Leo57O75omA5a2456iLNOW3peeoi+WtuOmZoi3lhYjpgLLnp5HmioDlhajoi7Hoqp7lpJblnIvlrbjnlJ/lsIjnj6065bel56iL5a246ZmiLeW3peeoi+aKgOihk+eglOeptuaJgOaKgOiBt+WwiOalreeZvOWxleWtuOeoiyXlt6XnqIvlrbjpmaIt5p2Q5paZ56eR5a246IiH5bel56iL57O7A0FMTBU3BE5VTEwENC1BRAQ0LUNEBDQtREUENC1EVAQ0LURYBDAtQVQEMC1CQgQwLUJFBDAtQ0kEMC1DWAQwLUVOBDAtSEMEMC1JQgQwLU1TBDAtUEEEMi1DUwQyLUVDBDItRUUEMi1FTwQyLUVUBDUtQ0MENS1FUAQ1LUZMBDUtR0UENS1QRQQ1LVZFBDYtSUIENi1QQQQ2LVRCBDYtVE0EMy1CQQQzLUZCBDMtRk4EMy1JTQQzLU1BBDMtTUIEMy1NRwQzLU1JBDMtU0cEMy1UQgQzLVRNBDEtQUMEMS1DRQQxLUNIBDEtQ1QEMS1HWAQxLU1FBDEtTVMEMS1SRAQxLVJTBDEtVEUEMS1UVgQxLVRYAV8UKwM3Z2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBZmQCAQ9kFgJmDxAPFggfAQUJRWR1X09yZ2FuHwIFBlBlcmlvZB8DBQJOTx8EZ2QQFQEJ5LiN6YG45pOHFQEETlVMTBQrAwFnFgFmZAICD2QWAmYPEA8WCB8BBQlFZHVfT3JnYW4fAgUFZ3JhZGUfAwUCTk8fBGdkEBUBCeS4jemBuOaThxUBBE5VTEwUKwMBZxYBZmQCAw9kFgJmDxAPFggfAQUJRWR1X09yZ2FuHwIFBUNsYXNzHwMFAk5PHwRnZBAVAQnkuI3pgbjmk4cVAQROVUxMFCsDAWcWAWZkAgEPZBYCZg9kFgJmD2QWAgIBD2QWAmYPZBYCZg8PFgIfAGhkZAItD2QWAmYPZBYCZg9kFgQCAQ8QZGQWAGQCAw8QZGQWAGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgcFB0FjYjAxMDEFB0FjYjYxMDEFB0FjYjYxMDIFB0JDSDAxMDEFCUNoZWNrYm94MwUKQ2hlY2tib3hfRwUKQ2hlY2tib3hfQ5sbK3SoM58/syF/UYuCHV0/Ozec',
                '__VIEWSTATEGENERATOR':'E915CB73',
                '__EVENTVALIDATION':'/wEWIwLm3uqGBQL2q8D8CgLM9PumDwLbwqJnArfcr5MMAtvWyYkGArGS9rMFAoqms9AKAr6QrdYMAr/MoaAHAq6dkvUKAtLd/qAJAruMlvkDAur23IwNArbvmZUJAoD+udsJAqOG6aIDAu/woqsPAqzat7gCAo22OQLg4fq/BgL/oILYBwLUrJXtBQL/oIrXCgKaiqjsBAKO29LaCAKo/pC1DAK9oL7oBwK6oL7oBwK7oL7oBwKA5NfcCQKU4+PeCQKU49PeCQLYm+qMCwLFounGCNEmKKj2lC5oy8WQBzrTc28SrSEp',
                'Acb0101':'on',
                'BCH0101':'on',
                'Checkbox_G':'on',
                'QuerySend':'送出查詢'
            }
            res = requests.post('http://140.118.31.215/querycourse/ChCourseQuery/QueryCondition.aspx', data=payload)
            #dataframe 分析區
            dfs = pandas.read_html(res.text)
            class1 = dfs[1]
            col = [3,5,6,10,12,13]
            for x in col:
                del class1[x]
            class1.columns = [u'課程代碼',u'通識向度',u'課程名稱',u'學分',u'授課老師',u'上課時間',u'教室',u'選課人數',u'限制人數']
            class1.drop(class1.index[[0]],inplace=True)
            class1[u'限制人數'] = class1[u'限制人數'].str.extract(u'(\d+)')
            class1[u'選課率'] = (class1[u'選課人數'].astype(int) / class1[u'限制人數'].astype(int)).round(3)
            #篩選區
            import os
            import sqlite3
            with sqlite3.connect(os.path.join(os.environ['USERPROFILE'], u'Documents\\class.sqlite')) as db:
                class1.to_sql('class1', con = db, if_exists='replace', index = False)
            with sqlite3.connect(os.path.join(os.environ['USERPROFILE'], u'Documents\\class.sqlite')) as db:
                want = ['']
                ws = ''
                for w in want:
                    ws += u"上課時間 LIKE '%" + w + "%'"
                    if w != want[-1]:
                        ws += " or "
                #left = u"select * from class1 where 課程代碼 is not null and 選課人數 < 限制人數 and Length (選課人數) <= Length (限制人數) and ("
                #left = u"select * from class1 where 課程代碼 is not null and 選課人數 > 限制人數 and Length (選課人數) >= Length (限制人數) and ("
                left = u"select * from class1 where 課程代碼 is not null and ("
                right = u")"
                total = u''
                total = left + ws + right
                df = pandas.read_sql_query(total, con = db)
                df.to_sql('class1', con = db, if_exists='replace')
            #輸出第一次html檔案
            df.to_html(os.path.join(os.environ['USERPROFILE'], u'Documents\\台科選課小釣手.html'))
            #寫檔
            with open(os.path.join(os.environ['USERPROFILE'], u'Documents\\台科選課小釣手.html'), 'w') as f:   
                #寫入區(檔案前面)
                f.write('<!DOCTYPE HTML>\n')
                f.write('<html>\n')
                f.write('<head>\n')
                f.write('<title>Welcome to Room 408</title>\n')
                f.write('<meta charset="utf-8" />\n')
                f.write('<meta name="viewport" content="width=device-width, initial-scale=1" />\n')
                f.write('<!--[if lte IE 8]><script src="assets/js/html5shiv.js"></script><![endif]-->\n')
                f.write('<link rel="stylesheet" href="assets/css/main.css" />\n')
                f.write('<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->\n')
                f.write('<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->\n')
                f.write('<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>\n')
                f.write('<link rel="Shortcut Icon" type="image/x-icon" href="favicon.ico" />\n')
                f.write('<script src="assets/js/jquery.min.js"></script>\n')
                f.write('<script src="assets/js/tablesort.js"></script>\n')
                f.write('<script src="assets/js/tablesearch.js"></script>\n')
                f.write('<script src="assets/js/load.js"></script>\n')
                f.write('<script src="assets/js/gotop.js"></script>')
                f.write('</head>\n')
                f.write('<body class="is-loading">\n')
                f.write('<div id="wrapper">\n')
                f.write('<section id="main" class="grade">\n')
                f.write('<header>\n')
                f.write('<span class="avatar"><img src="images/avatar.jpg" alt="Iori Moe" width="250" /></span>\n')
                f.write('<h1>台科選課小釣手-看來是位缺學分的朋友呢</h1>\n')
                f.write('<h3 align="right">最後更新時間: ' + time.strftime("%Y/%m/%d %H:%M:%S") + '</h3>\n')
                f.write('</header>\n')
                f.write('<div class="Content">\n')
                f.write('<select name="selection" id="selectInput">\n')
                f.write('  <option value="-1">搜尋全部</option>\n')
                f.write('　<option value="0">課程代碼</option>\n')
                f.write('　<option value="1">通識向度</option>\n')
                f.write('　<option value="2">課程名稱</option>\n')
                f.write('　<option value="3">學分</option>\n')
                f.write('  <option value="4">授課老師</option>\n')
                f.write('  <option value="5">上課時間</option>\n')
                f.write('  <option value="6">教室</option>\n')
                f.write('  <option value="7">選課人數</option>\n')
                f.write('  <option value="8">限制人數</option>\n')
                f.write('  <option value="9">選課率</option>\n')
                f.write('</select>\n')
                f.write('<input type="text" id="myInput" onkeyup="tablesearch()" placeholder="輸入你想查詢的字符!">\n')
                df.to_html(f)
            with open(os.path.join(os.environ['USERPROFILE'], u'Documents\\台科選課小釣手.html'), 'a') as f:
                #寫入區(檔案後面)
                f.write('\n')
                f.write('</div>\n')
                f.write('<hr />\n')
                f.write('<footer id="footer">\n')
                f.write('<ul class="icons">\n')
                f.write('<li><a href="index.html" class="fa-home"></a></li>\n')
                f.write('</ul>\n')
                f.write('</footer>\n')
                f.write('</section>\n')
                f.write('<footer id="footer">\n')
                f.write('<ul class="copyright">\n')
                f.write('<li>&copy; 408 Room</li>\n')
                f.write('</ul>\n')
                f.write('</footer>\n')
                f.write('</div>\n')
                f.write('<div id="gotop">')
                f.write('<ul class="icons">\n')
                f.write('<li><a class="fa fa-arrow-up"></i></a></li>\n')
                f.write('</ul>\n')
                f.write('</div>\n')
                f.write('<!--[if lte IE 8]><script src="assets/js/respond.min.js"></script><![endif]-->\n')
                f.write('</body>\n')
                f.write('</html>\n')
                f.close()
            # 先讀
            with open(os.path.join(os.environ['USERPROFILE'], u'Documents\\台科選課小釣手.html'), 'r') as file :
                filedata = file.read()
            # 取代
            filedata = filedata.replace('<tr style="text-align: right;">','<tr>')
            filedata = filedata.replace('<table border="1" class="dataframe">', '<table id="myTable2">')
            filedata = filedata.replace('<th></th>','<th onclick="sortTable(0)"></th>')
            filedata = filedata.replace('<th>課程代碼','<th onclick="sortTable(0)">課程代碼<i class="fa fa-sort-asc"></i>')
            filedata = filedata.replace('<th>通識向度','<th onclick="sortTable(1)">通識向度<i class="fa fa-sort"></i>')
            filedata = filedata.replace('<th>課程名稱','<th onclick="sortTable(2)">課程名稱<i class="fa fa-sort"></i>')
            filedata = filedata.replace('<th>學分','<th onclick="sortTable(3)">學分<i class="fa fa-sort"></i>')
            filedata = filedata.replace('<th>授課老師','<th onclick="sortTable(4)">授課老師<i class="fa fa-sort"></i>')
            filedata = filedata.replace('<th>上課時間','<th onclick="sortTable(5)">上課時間<i class="fa fa-sort"></i>')
            filedata = filedata.replace('<th>教室','<th onclick="sortTable(6)">教室<i class="fa fa-sort"></i>')
            filedata = filedata.replace('<th>選課人數','<th onclick="sortTable(7)">選課人數<i class="fa fa-sort"></i>')
            filedata = filedata.replace('<th>限制人數','<th onclick="sortTable(8)">限制人數<i class="fa fa-sort"></i>')
            filedata = filedata.replace('<th>選課率','<th onclick="sortTable(9)">選課率<i class="fa fa-sort"></i>')
            # 重寫
            with open(os.path.join(os.environ['USERPROFILE'], u'Documents\\台科選課小釣手.html'), 'w') as file:
                file.write(filedata)
            # 複製
            from shutil import copyfile
            copyfile(os.path.join(os.environ['USERPROFILE'], u'Documents\\台科選課小釣手.html'),u'C:\\inetpub\\wwwroot\\grade.html')
            time.sleep(57)
        except:
            print(sys.exc_info())


# In[33]:


# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup as bs
rs = requests.Session()
res = requests.get('http://moodle.ntust.edu.tw/user/profile.php?id=26697', headers = hd)


# In[2]:


# -*- coding: utf8 -*-
import requests
import urllib
from bs4 import BeautifulSoup as bs
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
rs = requests.Session()
def search(text):
    try:
        if (len(text.decode('utf-8')) > 32):
            return (u'輸入內容過長!')
            #raise Exception(u'輸入內容過長!') 
        else:    
            searchText = urllib.quote(text)
            prefix = 'https://www.google.com.tw/search?rlz=1C1CHZL_zh-TWTW736TW736&ei=BGo7WuLwHMe10gT-lIWoDA&q='
            suffix = '+site%3Ahttps%3A%2F%2Fwww.ptt.cc%2Fbbs%2FAOE%2F'
            res = requests.get(prefix + searchText + suffix, headers=headers)
            #print (prefix + searchText + suffix) #爬取的網址
            soup = bs(res.text,'lxml')
            return (soup.find('cite').text)
    except AttributeError:
        return (u'找不到相關的資料!')
        #針對網址做資料分析
        #res = requests.get(soup.find('cite').text, headers=headers) #爬出第一筆 (最相關) 的資料網址
        #soup = bs(res.text,'lxml')
        #print (soup.prettify())
print (search('種族'))

