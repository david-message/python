# # encoding:utf-8
import requests
import os
import time
import http.cookies as cookie

fileData = {
    "fileSize": -1  # 文件总大小
}


def getLocalFileSize(local_path):
    try:
        lsize = os.stat(local_path).st_size
    except:
        lsize = 0
    return lsize


def getDownLoadSize(webPage):
    r = webPage.headers['Content-Range']
    return int(r[r.find('/')+1:])

def httpRequest(down_link, offset, cookies):
    headers = {
        # 'Host': 'pan.baidu.com',
        # 'Upgrade-Insecure-Requests': 1,
        'Referer': 'https://pan.baidu.com/disk/home',
        'Range': 'bytes=%d-' % offset,
        'User-Agent': 'Mozilla / 5.0(Macintosh; Intel Mac OS X 10_12_6) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 62.0 .3202 .94 Safari / 537.36'
    }

    webPage = None
    try:
        webPage = requests.get(down_link, stream=True, headers=headers, timeout=120, verify=False, cookies=cookies)
        status_code = webPage.status_code
        if status_code in [200, 206]:
            # 需要下载的数据
            fileData["fileSize"] = getDownLoadSize(webPage)
            # 设置Cookies
            print(webPage.cookies.values())

            print(u"FileSize:%d" %fileData["fileSize"])
        elif status_code == 416:
            print(u"%s文件数据请求区间错误,status_code:%s" % (down_link, status_code))
        else:
            print(u"%s链接有误,status_code:%s" % (down_link, status_code))
    except Exception as e:
        print(u"无法链接:%s,e:%s" % (down_link, e))
    finally:
        return webPage


def download(down_link,local_path,cookies):
    tryCount = 0
    while True:
        lsize = getLocalFileSize(local_path)
        if fileData["fileSize"] >0 and lsize >= fileData["fileSize"] or tryCount > 5:
            break

        webPage = httpRequest(down_link, lsize, cookies)

        try:
            file_obj = open(local_path, 'ab+')
        except Exception as e:
            print(u"打开文件:%s失败" % local_path)
            break

        try:
            t = time.time()
            size = 50
            for chunk in webPage.iter_content(chunk_size=size * 1024):
                lsize = lsize+len(chunk)
                now = time.time()
                print("time:%f,speed:%f,total:%d,load:%d,p:%f" %(now-t,size*1024/(now-t),fileData["fileSize"],lsize,(1.0*lsize / fileData["fileSize"])))
                t=now
                if chunk:
                    file_obj.write(chunk)
                else:
                    break
            tryCount = 0
        except Exception as e:
            tryCount=tryCount+1
            time.sleep(5)

        file_obj.close()
        webPage.close()

        # end loop

if __name__ == '__main__':
    resURL= 'http://d.pcs.baidu.com/file/8fe7d5d3b2cbc52bf57d139e7ce88e7f'
    savePath = '/pythonDownload/(额外补充)词嵌入word embedding.avi'
    cookiesData = 'cookie'

    c = cookie.SimpleCookie()
    c.load(cookiesData)
    dict={}
    for k in c:
        # print k,c[k].value
        dict[k] = c[k].value

    download(resURL,savePath,dict)