# -*- coding: utf-8 -*-


class InstallAppRes(object):
    def __init__(self):
        self.apk_name = "weiyun.apk"
        self.search_box_id="com.google.android.googlequicksearchbox:id/search_box"
        self.search_icon_id="com.google.android.apps.nexuslauncher:id/g_icon"
        self.validate_text_id="com.google.android.googlequicksearchbox:id/suggestions_strip_container"


        # file_operater
        self.txt_search="com.google.android.googlequicksearchbox:id/launcher_search_button"
        self.app_name = u"百度网盘"
        self.upload = False
        self.down_files_name = u"python-2.7.13.amd64.msi"
        self.upload_id="com.baidu.netdisk:id/navigation_bar_upload"
        self.upload_type=u"图片"
        self.download_id="com.baidu.netdisk:id/btn_to_download"
        self.ok="com.qihoo.yunpan:id/btnOK"
        self.transfer_list="com.baidu.netdisk:id/navigation_bar_transfer_list"
        self.upload_list=u"上传列表"
        self.down_file_path="com.baidu.netdisk:id/transfer_download_path"
        self.download_task_list="com.baidu.netdisk:id/download_task_list_view"