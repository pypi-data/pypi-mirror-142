#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from urllib import parse
import requests
import platform
import time
import sys
import re
import os
if platform.system() == 'Windows':
    path_separator = '\\'
else:
    path_separator = '/'
headers_default = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}


def download(
        url,
        filename: str = None,  # 文件名
        suffix_name: str = None,  # 后缀名
        headers=None,
        path: str = "download",  # 下载到路径
        proxies=None,  # 代理
        size_limit=None,
        range_start=0,
        range_end=None,
):
    """
    实现文件下载功能，可指定url、文件名、后缀名、请求头、文件保存路径
    :param url:
    :param filename:文件名
    :param suffix_name:后缀名
    :param headers:请求头
    :param path:文件保存路径
    :param proxies:代理
    :param size_limit:尺寸限制
    :param range_start:开始位置
    :param range_end:结束位置
    :return:
    """
    if headers is None:
        headers_local = headers_default
    else:
        headers_local = headers

    # 参照：https://www.cnblogs.com/yizhenfeng168/p/7078480.html
    if range_start is None and range_end is None:
        range_start = 0
        range_info = None
    elif range_start is not None and range_end is None:
        range_info = 'bytes=%d-' % range_start  # 从这里向后
    elif range_start is None and range_end is not None:
        range_start = 0
        range_info = 'bytes=0-%d' % range_end
    else:
        range_info = 'bytes=%d-%d' % (range_start, range_end)

    # 参照：https://blog.csdn.net/Python_sn/article/details/109167016
    if range_info is None:
        pass
    else:
        headers_local['Range'] = range_info
    # 获取文件的基本信息
    response = requests.get(
        url=url,
        headers=headers_local,
        stream=True,
        proxies=proxies
    )
    total_length = response.headers.get('content-length')  # 文件大小
    content_type = response.headers.get('content-type')  # 文件类型
    content_disposition = response.headers.get('content-disposition')  # 文件名及类型
    try:
        # 尝试自动获取文件名
        filename_default = re.findall('filename="(.*?)";', content_disposition, re.S)[0]
        filename_default = parse.unquote(filename_default)
    except:
        # 无法自动获取到文件名的，将按照默认命名
        filename_default = 'unknown_' + str(time.time())

    if suffix_name is None:
        # 尝试自动获取文件后缀名
        suffix_name = content_type.split('/')[1]

    if filename is None:
        download_file_name = str(filename_default) + "." + str(suffix_name)
    else:
        download_file_name = str(filename) + "." + str(suffix_name)

    if path is None:
        path_local = download_file_name
    else:
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)
        path_local = path + path_separator + download_file_name

    if range_start is None:
        temp_size = 0  # 已经下载文件大小
    else:
        temp_size = range_start + 0  # 已经下载文件大小
    chunk_size = 1024  # 分割文件大小，字节B
    total_size = int(total_length)  # 文件总大小
    total_size_mb = round(total_size / (1024 * 1024), 2)  # 换算到MB的文件大小
    # 添加文件大小控制，跳过下载超大文件
    if size_limit is None:
        pass
    else:
        if total_size > size_limit:
            return
        else:
            pass

    time_start = time.time()  # 获取下载开始时间
    is_finish = False

    with open(path_local, "ab") as f:  # wb新建文件，a追加
        for chunk in response.iter_content(chunk_size=chunk_size):
            if not chunk:
                if temp_size >= total_size:
                    is_finish = True
                else:
                    is_finish = False
                break
            else:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                done = int(50 * temp_size / total_size)

                temp_time_now = time.time()  # 时间采样
                time_spend_total = temp_time_now - time_start
                if time_spend_total == 0:
                    total_speed = round((temp_size - range_start) / (1024 * 1024) / 0.001, 2)  # 计算速度：MB/s
                else:
                    total_speed = round((temp_size - range_start) / (1024 * 1024) / time_spend_total, 2)  # 计算速度：MB/s

                if total_speed == 0 or time_spend_total == 0:
                    time_left = 0
                else:
                    time_left = (total_size - temp_size) / total_speed / 1024 / 1024
                show_dict = {
                    'finish_mark': '█' * done,
                    'not_finish_mark': ' ' * (50 - done),
                    'total_size': total_size_mb,  # 换算到M
                    'total_percent': round(100 * temp_size / total_size, 4),
                    'total_speed': total_speed,
                    'finish_size': round(temp_size / (1024 * 1024), 2),
                    'time_spend_total': int(time_spend_total),
                    'time_left': int(time_left)
                }
                show_msg = "\r[%(finish_mark)s%(not_finish_mark)s] " \
                           "总大小:%(total_size)sMB " \
                           "总进度:%(total_percent)s%% " \
                           "平均速度:%(total_speed)sMB/s " \
                           "已下载:%(finish_size)sMB " \
                           "已耗时 %(time_spend_total)s 秒 " \
                           "预计剩余 %(time_left)s 秒" % show_dict
                sys.stdout.write(show_msg)
                sys.stdout.flush()
                if temp_size >= total_size:
                    is_finish = True
                else:
                    is_finish = False
    print("\n  ==> 文件已下载完成，保存位置:", path_local)
    res_dict = {
        'file_dir': path_local,
        'is_finish': is_finish,
        'temp_size': temp_size
    }
    return res_dict


def safe_download(
        url,
        filename=None,
        suffix_name=None,
        headers=None,
        path="download",
        proxies=None,
        size_limit=None,
        range_start=None,
        range_end=None
):
    while True:
        download_response = download(
            url=url,
            filename=filename,
            suffix_name=suffix_name,
            headers=headers,
            path=path,
            proxies=proxies,
            size_limit=size_limit,
            range_start=range_start,
            range_end=range_end
        )
        if download_response.get('is_finish') is True:
            local_file_dir = download_response.get('file_dir')
            return local_file_dir
        else:
            print(':( 下载中断')
            range_start = download_response.get('temp_size')
            time.sleep(1)
            print('将继续下载（断点续传）...')
