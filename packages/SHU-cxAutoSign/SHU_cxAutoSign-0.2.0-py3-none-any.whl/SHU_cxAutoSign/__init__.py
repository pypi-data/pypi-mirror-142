# -*- encoding: utf-8 -*-
'''
@File    :   SHU-cxAutoSign.py
@Time    :   2022/03/08 10:21:21
@Author  :   XHLin
@Version :   1.0
@Contact :   xhaughearl@gmail.com
'''

import os
import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import parse_qs
import pickle
import json
from time import sleep

from .login import login

class_url = 'http://www.elearning.shu.edu.cn/courselist/coursedata?courseType=3&sectionId=7530'
# sectionId为学期的关键字，暂时先硬编码，后续再改
workDir = os.path.dirname(__file__)
#workDir下保存用户的信息与cookies



def deleteUser(user_qq):
    dataPath = os.path.join(workDir,"usersData.json")
    usersDataFile = open(dataPath)
    usersData = json.load(usersDataFile)
    if user_qq not in usersData.keys():
        return False
    del usersData[user_qq]
    with open(dataPath, 'w') as f:
        f.write(json.dumps(usersData))
        f.close()
    return True

def getUsersData():
    dataPath = os.path.join(workDir, "usersData.json")
    usersDataFile = open(dataPath)
    return json.load(usersDataFile)


class User():
    name = ''
    user_qq = 0
    course_dict = {}
    username = ''
    password = ''
    uid = 0
    session = requests.session()
    
    def __init__(self) -> None:
        if not os.path.exists(os.path.join(workDir,"usersData.json")):
            print("新建资料保存文件路径",os.path.join(workDir,"usersData.json"))
            usersData = {}
            with open(os.path.join(workDir,"usersData.json"),'w') as f:
                f.write(json.dumps(usersData))
        if not os.path.exists(os.path.join(workDir,"cookies")):
            os.makedirs(os.path.join(workDir,"cookies"))

    def login(self):
        self.name,self.uid,self.session = login(username=self.username, password=self.password)
        
        dataPath = os.path.join(os.path.dirname( __file__), "cookies", str(self.user_qq))
            # 本地保存cookie
        with open(dataPath, 'wb') as f:
            pickle.dump(self.session.cookies, f)
            self.isSolid = True
        return '登录成功'

    def loadUser(self, user_qq):
        usersData = getUsersData()
        if user_qq not in usersData.keys():
            return '账号不存在'
        self.user_qq = user_qq
        self.username = usersData[str(user_qq)]['username']
        self.password = usersData[str(user_qq)]['password']
        self.uid = usersData[str(user_qq)]['uid']
        self.name = usersData[str(user_qq)]['name']
        self.course_dict = usersData[str(user_qq)]['course_dict']
        dataPath = os.path.join(workDir, "cookies", user_qq)
        with open(dataPath, 'rb') as f:
            self.session.cookies.update(pickle.load(f))

    def getClass(self):
        klass = self.session.get(url=class_url).text
        klassSoup = BeautifulSoup(klass,'lxml')
        for s in klassSoup.find_all('li', class_='zmy_item'):
            cname = s['cname']
            
            courseId,classId = False,False
            try:
                link = s.find_all('a')[0]['href']
                parse_dict = parse_qs(link)
                courseId, classId = parse_dict['courseId'][0], parse_dict['clazzId'][0]
                # print(cname, courseId, classId)
                self.course_dict.update(
                    {
                        cname: {
                            "courseId": courseId,
                            "classId": classId,
                            "latitude": -1,
                            "longitude": -1,
                            "address": '中国上海市宝山区',
                            "events": {
                }}})
            except:
                print(cname,"出错,可能账号操作过于频繁")
    
    def getEvent(self):
        '''
        回传一个新事件list
        '''        
        newEvent = []
        for c in self.course_dict:
            if self.course_dict[c]["courseId"] == False:
                continue
            print(c)
            courseId = self.course_dict[c]["courseId"]
            classId = self.course_dict[c]["classId"]
            URL = f"http://mobilelearn.elearning.shu.edu.cn/widget/pcpick/stu/index?courseId={courseId}&jclassId={classId}"
            eventSoup = BeautifulSoup(self.session.get(URL).text,'lxml')
            sleep(0.3)
            # print(eventSoup)
            try:
                inSigning = eventSoup.find_all('div',class_='Maincon2')
                activities = inSigning[0].find_all('div',class_ = 'Mct')
                for activity in activities:
                    activeId = re.findall(r"\((.*?),",str(activity['onclick']))[0]
                    if activeId not in self.course_dict[c]["events"]:
                        print(activeId)
                        self.course_dict[c]["events"].update({
                                activeId: True
                            })
                        newEvent.append({
                                "course":c,
                                "activeId":activeId,
                                "courseId":courseId,
                                "classId":classId
                            })
                
            except:
                print(c,"可能未开课")
        return newEvent
    def getType(self, activeId, courseId, classId):
        url = f"http://mobilelearn.elearning.shu.edu.cn/widget/sign/pcStuSignController/preSign?activeId={activeId}&classId={classId}&courseId={courseId}"
        soup = BeautifulSoup(self.session.get(url).text,'lxml')
        eventType = soup.title.text
        if '签到成功' in eventType:
            return "普通签到，签到成功"
        if '学生端-签到' in eventType:
            return '拍照签到，咱解决不了'
        return "进行一个"+eventType+"的签"

    def gestureSign(self,activeId, courseId, classId):
        url = f'http://mobilelearn.elearning.shu.edu.cn/widget/sign/pcStuSignController/signIn?activeId={activeId}&classId={classId}&courseId={courseId}'
        res = self.session.get(url)
        if res == 'success':
            return False
        return True

    def locationSign(self,activeId,latitude,longtitude,address):
        params = {
                'name': self.name,
                'activeId': activeId,
                'address': address,
                'uid': self.uid,
                'clientip': '27.115.83.251',
                'latitude': latitude,
                'longitude': longtitude, #todo 各个课程加入各自的经纬度
                'fid': '209',
                'appType': '15',
                'ifTiJiao': '1'
            }
        res = self.session.get(
            url='https://mobilelearn.chaoxing.com/pptSign/stuSignajax',
            params=params
        )
        if res.text == 'success':
            return False
        return True
    
    def QRSign(self,activeId,enc):
        params = {
                'name': self.name,
                'activeId': activeId,
                'uid': self.uid,
                'clientip': '27.115.83.251',
                'appType': '15',
                'ifTiJiao': '1',
                'enc':enc
            }
        res = self.session.get(
            url='https://mobilelearn.chaoxing.com/pptSign/stuSignajax',
            params=params
        )
        if res.text == 'success':
            return False
        return True
    def saveData(self):
        dataPath = os.path.join(workDir,"usersData.json")
        usersDataFile = open(dataPath)
        usersData = json.load(usersDataFile)
        if self.user_qq in usersData.keys():
            usersData[str(self.user_qq)].update(
                    {
                        "username": self.username,
                        "password": self.password,
                        "uid" : self.uid,
                        "name": self.name,
                        "course_dict": self.course_dict
                    }
                )
            with open(dataPath, 'w') as f:
                f.write(json.dumps(usersData))
                f.close()
        else:
            newData = {self.user_qq: {
            "username": self.username,
            "password": self.password,
            "uid" : self.uid,
            "name" : self.name,
            "course_dict": self.course_dict
        }}
            usersData.update(newData)
            with open(dataPath, 'w') as f:
                f.write(json.dumps(usersData))
                f.close()
