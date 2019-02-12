#coding=utf-8
from django.test import TestCase
from Temage.models import User
from Temage.models import Profile
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Product
from Temage.models import Theme
from Temage.models import Card
from django.contrib.auth import authenticate
from django.core.files import File
import jwt
import json

# Create your tests here.
class ModelTest(TestCase):
# Test Set Up
    def setUp(self):
        img1 = open("../test_file/img/good.jpg", "rb")
        img2 = open("../test_file/img/bad.jpg", "rb")
        img3 = open("../test_file/img/cold.jpg", "rb")
        img4 = open("../test_file/img/hot.jpg", "rb")
        avator1 = open("../test_file/img/girl.jpg", "rb")
        avator2 = open("../test_file/img/boy.jpg", "rb")
        User.objects.create_user(id=1,username=1234, is_superuser=True, email='1234@qq.com', password="1234")
        user1 = User.objects.create_user(username="qxy", password="123", id=2)
        user2 = User.objects.create_user(username="wxm", password="123")
        style1 = Style.objects.create(name="style_1")
        style2 = Style.objects.create(name="style_2")
        style3 = Style.objects.create(name="style_4")
        style4 = Style.objects.create(name="style_5")
        style5 = Style.objects.create(name="style_6")
        style6 = Style.objects.create(name="style_7")
        style7 = Style.objects.create(name="style_8")
        style8 = Style.objects.create(name="style_9")
        style9 = Style.objects.create(name="style_a")
        style10 = Style.objects.create(name="style_b")
        style11 = Style.objects.create(name="style_c")
        style12 = Style.objects.create(name="style_d")
        style13 = Style.objects.create(name="style_e")
        style14 = Style.objects.create(name="style_f")
        style15 = Style.objects.create(name="style_g")
        style16 = Style.objects.create(name="style_h")
        style17 = Style.objects.create(name="style_i")
        style18 = Style.objects.create(name="style_j")
        style19 = Style.objects.create(name="style_k")
        style20 = Style.objects.create(name="style_l")
        theme1 = Theme.objects.create(name="Sport", id=1)
        theme2 = Theme.objects.create(name="Art", id=2)
        theme3 = Theme.objects.create(name="Tech", id=3)
        theme4 = Theme.objects.create(name="Movie", id=4)                      
        theme5 = Theme.objects.create(name="Porn", id=5)
        theme6 = Theme.objects.create(name="Celebrity", id=6)
        profile1 = Profile.objects.create(user = user1)
        profile2 = Profile.objects.create(user = user2)
        profile1.avator.save('girl.jpg', File(avator1), save=True)
        profile2.avator.save('boy.jpg', File(avator2), save=True)
        profile1.theme.add(theme1)
        profile1.theme.add(theme2)
        profile1.theme.add(theme3)
        htmlmecy = '<!DOCTYPE html><html><head>    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">    <meta http-equiv="X-UA-Compatible" content="IE=edge">    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0,viewport-fit=cover">    <meta name="apple-mobile-web-app-capable" content="yes">    <meta name="apple-mobile-web-app-status-bar-style" content="black">    <meta name="format-detection" content="telephone=no">    <title>        阿根廷主帅：梅西2019年会回归 暂时封存10号球衣    </title>    <style>.radius_avatar{display:inline-block;background-color:#fff;padding:3px;border-radius:50%;-moz-border-radius:50%;-webkit-border-radius:50%;overflow:hidden;vertical-align:middle}.radius_avatar img{display:block;width:100%;height:100%;border-radius:50%;-moz-border-radius:50%;-webkit-border-radius:50%;background-color:#eee}.rich_media_inner{word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.rich_media_area_primary{padding:20px 16px 12px;background-color:#fafafa}.rich_media_area_primary.voice{padding-top:66px}.rich_media_area_primary .weui-loadmore_line .weui-loadmore__tips{color:rgba(0,0,0,0.3);background-color:#fafafa}.rich_media_area_extra{padding:0 16px 24px}.rich_media_extra{padding-top:30px}.mpda_bottom_container .rich_media_extra{padding-top:24px}html{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;line-height:1.6}body{-webkit-touch-callout:none;font-family:-apple-system-font,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif;color:#333;background-color:#f2f2f2;letter-spacing:.034em}h1,h2,h3,h4,h5,h6{font-weight:400;font-size:16px}*{margin:0;padding:0}a{color:#576b95;text-decoration:none;-webkit-tap-highlight-color:rgba(0,0,0,0)}.rich_media_title{font-size:22px;line-height:1.4;margin-bottom:14px}@supports(-webkit-overflow-scrolling:touch){.rich_media_title{font-weight:700}}.rich_media_meta_list{margin-bottom:22px;line-height:20px;font-size:0;word-wrap:break-word;word-break:break-all}.rich_media_meta_list em{font-style:normal}.rich_media_meta{display:inline-block;vertical-align:middle;margin:0 10px 10px 0;font-size:15px;-webkit-tap-highlight-color:rgba(0,0,0,0)}.rich_media_meta.icon_appmsg_tag{margin-right:4px}.rich_media_meta.meta_tag_text{margin-right:0}.rich_media_meta_primary{display:block;margin-bottom:10px;font-size:15px}.meta_original_tag{padding:0 .5em;font-size:12px;line-height:1.4;background-color:#f2f2f2;color:#888}.meta_enterprise_tag img{width:30px;height:30px!important;display:block;position:relative;margin-top:-3px;border:0}.rich_media_meta_link{color:#576b95}.rich_media_meta_text{color:rgba(0,0,0,0.3)}.rich_media_meta_text.rich_media_meta_split{padding-left:10px}.rich_media_meta_text.rich_media_meta_split:before{position:absolute;top:50%;left:0;margin-top:-6px;content:\' \';display:block;border-left:1px solid #888;width:200%;height:130%;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:0 0;transform-origin:0 0}.rich_media_meta_text.article_modify_tag{position:relative}.rich_media_meta_nickname{position:relative}.rich_media_thumb_wrp{margin-bottom:6px}.rich_media_thumb_wrp .original_img_wrp{display:block}.rich_media_thumb{display:block;width:100%}.rich_media_content{overflow:hidden;color:#333;font-size:17px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto;text-align:justify}.rich_media_content *{max-width:100%!important;box-sizing:border-box!important;-webkit-box-sizing:border-box!important;word-wrap:break-word!important}.rich_media_content p{clear:both;min-height:1em}.rich_media_content em{font-style:italic}.rich_media_content fieldset{min-width:0}.rich_media_content .list-paddingleft-2{padding-left:2.2em}.rich_media_content .list-paddingleft-2 .list-paddingleft-2{padding-left:30px}.rich_media_content blockquote{margin:0;padding-left:10px;border-left:3px solid #dbdbdb}.weui-mask{position:fixed;z-index:1000;top:0;right:0;left:0;bottom:0;background:rgba(0,0,0,0.6)}.weui-dialog{position:fixed;z-index:5000;width:80%;max-width:300px;top:50%;left:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);background-color:#fff;text-align:center;border-radius:3px;overflow:hidden}.weui-dialog__hd{padding:1.3em 1.6em .5em}.weui-dialog__title{font-weight:400;font-size:18px}.weui-dialog__bd{padding:0 1.6em .8em;min-height:40px;font-size:15px;line-height:1.3;word-wrap:break-word;word-break:break-all;color:#999}.weui-dialog__bd:first-child{padding:2.7em 20px 1.7em;color:#353535}.weui-dialog__ft{position:relative;line-height:48px;font-size:18px;display:-webkit-box;display:-webkit-flex;display:flex}.weui-dialog__ft:after{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid #d5d5d6;color:#d5d5d6;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.weui-dialog__btn{display:block;-webkit-box-flex:1;-webkit-flex:1;flex:1;color:#3cc51f;text-decoration:none;-webkit-tap-highlight-color:rgba(0,0,0,0);position:relative}.weui-dialog__btn:active{background-color:#eee}.weui-dialog__btn:after{content:" ";position:absolute;left:0;top:0;width:1px;bottom:0;border-left:1px solid #d5d5d6;color:#d5d5d6;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleX(0.5);transform:scaleX(0.5)}.weui-dialog__btn:first-child:after{display:none}.weui-dialog__btn_default{color:#353535}.weui-dialog__btn_primary{color:#0bb20c}img{height:auto!important}@media only screen and (device-width:375px) and (device-height:812px) and (-webkit-device-pixel-ratio:3) and (orientation:portrait){.rich_media_area_extra{padding-bottom:34px}}@media only screen and (device-width:375px) and (device-height:812px) and (-webkit-device-pixel-ratio:3) and (orientation:landscape){.rich_media_area_primary{padding:20px 60px 15px 60px}.rich_media_area_extra{padding:0 60px 21px 60px}}@media screen and (min-width:1024px){.rich_media_area_primary_inner,.rich_media_area_extra_inner{max-width:677px;margin-left:auto;margin-right:auto}.rich_media_area_primary{padding-top:32px}}.appmsg_share_notice{font-size:16px;color:#888;position:relative;padding:1.25em 0;margin-bottom:1.75em}.appmsg_share_notice:before{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid #dfdfdf;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.appmsg_share_notice:after{content:" ";position:absolute;left:0;bottom:0;right:0;height:1px;border-bottom:1px solid #dfdfdf;-webkit-transform-origin:0 100%;transform-origin:0 100%;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.appmsg_share_notice_hd{font-weight:700;padding-bottom:.2em}.cell{padding:.8em 0;display:block;position:relative}.cell_hd,.cell_bd,.cell_ft{display:table-cell;vertical-align:middle;word-wrap:break-word;word-break:break-all;white-space:nowrap}.cell_primary{width:2000px;white-space:normal}.flex_cell{padding:10px 0;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-ms-flex-align:center;align-items:center}.flex_cell_primary{width:100%;-webkit-box-flex:1;-webkit-flex:1;-ms-flex:1;box-flex:1;flex:1}.original_tool_area{display:block;padding:.75em 1em 0;-webkit-tap-highlight-color:rgba(0,0,0,0);color:#333;border:1px solid #eaeaea;margin:20px 0}.original_tool_area .tips_global{position:relative;padding-bottom:.5em;font-size:15px}.original_tool_area .tips_global:after{content:" ";position:absolute;left:0;bottom:0;right:0;height:1px;border-bottom:1px solid #dbdbdb;-webkit-transform-origin:0 100%;transform-origin:0 100%;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.original_tool_area .radius_avatar{width:27px;height:27px;padding:0;margin-right:.5em}.original_tool_area .radius_avatar img{height:100%!important}.original_tool_area .flex_cell_bd{width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal}.original_tool_area .flex_cell_ft{font-size:14px;color:#888;padding-left:1em;white-space:nowrap}.original_tool_area .icon_access:after{content:" ";display:inline-block;height:8px;width:8px;border-width:1px 1px 0 0;border-color:#cbcad0;border-style:solid;transform:matrix(0.71,0.71,-0.71,0.71,0,0);-ms-transform:matrix(0.71,0.71,-0.71,0.71,0,0);-webkit-transform:matrix(0.71,0.71,-0.71,0.71,0,0);position:relative;top:-2px;top:-1px}.rich_media_global_msg{position:fixed;top:0;left:0;right:0;padding:.85em 35px .85em 15px;z-index:2;background-color:#c6e0f8;color:#888;font-size:12px}.rich_media_global_msg .icon_closed{position:absolute;right:15px;top:50%;margin-top:-5px;line-height:300px;overflow:hidden;-webkit-tap-highlight-color:rgba(0,0,0,0);background:transparent url(//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/icon_appmsg_msg_closed_sprite.2x2eb52b.png) no-repeat 0 0;width:11px;height:11px;vertical-align:middle;display:inline-block;-webkit-background-size:100% auto;background-size:100% auto}.rich_media_global_msg .icon_closed:active{background-position:0 -17px}.rich_media_global_msg.voice{color:#1aad19;background-color:#e8f6e8;padding-left:43.3px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.rich_media_global_msg.voice .ic_voice{position:absolute;top:50%;margin-top:-10px;left:15px;display:inline-block;width:13.3px;height:18.3px;background:url(data:image/png;base64,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) no-repeat center;background-size:contain}.rich_media_global_msg.voice .icon_more{position:absolute;right:15px;top:50%;margin-top:-6.5px;width:8px;height:13px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAmCAYAAADeB1slAAAAAXNSR0IArs4c6QAAA49JREFUSA2tVk1IVFEUPveOmhQk1ibfvLFZSJtACqJIIpCIoB+imcFV2Z9ZUVnRomgRGFn2i6mFf5XVotCZMYmgIMhlq6BFENFiwjfPAosgFzXOvNu5o3fmeue98Y16F3PP+c453/fu/xCQmvZSWwwJaC0G6P8WND9IoTmbVFRycpqAdgBWkwRo94V960RsPn1aoPpN9RI6CR0WsDWcjAErtUiqTR/S18+HnNcSTv5zYrwDSatVMgLkH6aciwfj79WYW5+OT4xfsyPnBIgvwt872qBW45ZQzaMlJXCfMPJbDQgfRUoIhduVUW2TwArpaWyX+bnYU9JAAH44FaJIccqCW76Ib7NTjhOOvFPN/8q/IvE3cR+npFJgao9rkiSUXjD2GCNqzMnPbNPYjth3mqINlJAvTsk4kiJmWa3eQe8WpxwVzwjwgFFn/CorL29EkY9qovC5CFDrKq7JVoHl6zNTJCf53/lLk78SN/FcbJRx2cZCixC4ZATGXsu4as8YgQjGamN/q5atOotn4K3A1J4BUMbgsh7Wt6sx2bcV4AkjtSPJxkDjRQL0hVwg21zEglSzN+rdKeOybTtFcgK39ajWZDFWr+IZHxfGQ8mV0YA5nMGmDVcCPNcb8R5gYJ1UCWQfp6PFCI4NyZhrAV6EIiHGrPOAB0ImkW2c0la8u8ICc0wUCWrvC1dsw+3TnN6uanDaJ4zeiIfiA9wtWIAX8XspxeA6iuBlaN88hNzCNXk+JwFOuXJYW5tMQmc+EcqgzXGb2n9XFk1NstX5yKczl89JAF+6vRaBM1m5XAu//qkRGrtb8BThTtqH2/V0LmUWwbvsiREw8X0vcJHxxNbjNm3KUuVaMjmPFuWm2CPesHc/kp+yj06hFMhj/PIOOcfVFLk6xZT0G3vMTpmc27MusityZk/OBfKOwA05MPLIDJn3OJldcxTQotpBYOyEXVEWIw/NoInvuHOznSJfVDs0GzneNw9mI+eyOSPQI9phfCqPO38TFhHaFw/Eu/LliNiMESB5w6zkzD05F8mMYJr8mFC263Fa+vAadvXloj4toEcrjlgMjgrQrseHpBcfkm67WD6M6MN6lTWZeoZjyYxGLcB57MGnsEfF3fjU2G189QBpcUqmBLrnSs4504s8GjLxrwm5qYrg3dKFf6x6VbwQ3yOS/wz8+bS0ruwfELaBY2nyoNkn4gvW65GKRn4WForwP+dONHDaOHeZAAAAAElFTkSuQmCC) no-repeat center;background-size:contain}.preview_appmsg .rich_media_title{margin-top:2.3em}@media screen and (min-width:1024px){.rich_media_global_msg{position:relative;margin-bottom:32px}.preview_appmsg .rich_media_title.rich_media_title{margin-top:0}}.pages_reset{color:#333;line-height:1.6;font-size:16px;font-weight:400;font-style:normal;text-indent:0;letter-spacing:normal;text-align:left;text-decoration:none;white-space:normal}.weapp_element,.weapp_display_element,.mp-miniprogram{display:block;margin:1em 0}.share_audio_context{margin:16px 0}.weapp_text_link{font-size:17px}.weapp_text_link:before{content:\'\';display:inline-block;line-height:1;background-size:contain;background-repeat:no-repeat;background-image:url(\'data:image/png;base64,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\');vertical-align:middle;font-size:11px;color:#888;margin-right:6px;margin-top:-3px;background-position:center;height:20px;width:20px}.flex_context{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.flex_bd{-webkit-box-flex:1;-webkit-flex:1;flex:1;word-wrap:break-word;word-break:break-all}.original_page{background-color:#fff;font-size:16px}.account_info{padding:0 0 20px}.account_info .flex_bd{padding-left:.85em}.radius_avatar.account_avatar{width:40px;height:40px;padding:0}.account_nickname{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:1;line-height:1.2;color:#576b95;font-size:14px}.account_nickname_inner{font-weight:400;vertical-align:top}.account_desc{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:1;color:#b2b2b2;font-size:13px;line-height:1.2;padding-top:.3em}.account_desc_inner{display:inline;vertical-align:top}.share_notice{margin-bottom:20px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.share_media{padding-bottom:18px}.original_panel{padding:20px;background-color:#fcfcfc;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto;overflow:hidden;position:relative}.original_panel:after{content:" ";border:1px solid #d8d8d8;border-radius:4px;-moz-border-radius:4px;-webkit-border-radius:4px;position:absolute;top:0;left:0;width:200%;height:200%;-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:0 0;transform-origin:0 0;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}.original_panel .original_account{margin-bottom:18px;position:relative;z-index:1}.original_panel .original_account_avatar{width:28px;height:28px;padding:0}.original_panel .original_account_nickname{padding-left:.85em;font-size:15px;color:#576b95}.original_panel_title{font-size:23px;color:#000;margin:0 0 16px}.original_panel_content{color:#333}.original_panel_tool{padding-top:20px;position:relative;z-index:1}.original_cell_nickname{display:inline-block;vertical-align:middle;font-weight:400;width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal;max-width:8em;color:#000}.original_tool_area{padding:1.17em 0;border-width:0;position:relative}.original_tool_area:before{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid #dfdfdf;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.original_tool_area:after{content:" ";position:absolute;left:0;bottom:0;right:0;height:1px;border-bottom:1px solid #dfdfdf;-webkit-transform-origin:0 100%;transform-origin:0 100%;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.original_tool_area .radius_avatar{width:20px;height:20px;margin-right:.2em}.original_tool_area .flex_cell{padding:0;font-size:14px}.original_tool_area .icon_access:after{margin-right:4px;top:0}.preview_appmsg .rich_media_title{margin-top:1.5em}.preview_appmsg .account_info{padding-top:3em}.original_page{background-color:transparent}.account_info{-webkit-tap-highlight-color:rgba(0,0,0,0);outline:0;padding-bottom:20px;font-size:14px}.account_info.appmsg_account_info{padding-bottom:32px}.account_info .radius_avatar img{background-color:transparent}.share_notice{font-size:16px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.original_panel{background-color:#fafafa}.original_panel:after{border-color:#e6e6e6}.original_panel .original_account_avatar{width:30px;height:30px}.original_panel_tool{font-size:14px}.original_panel_tool a{color:#576b95}.original_panel_content{font-size:17px}.share_media{padding-bottom:30px}.icon_appmsg_tag{display:inline-block;vertical-align:middle;padding:0 .5em;font-size:12px;line-height:1.5;background-color:#c3c3c3;color:#fff;border-radius:2px;-moz-border-radius:2px;-webkit-border-radius:2px;width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal;max-width:70%}.icon_appmsg_tag.primary{color:#3bb638;padding:4px .78em;background-color:rgba(9,187,7,0.08);font-size:12px;border-top-left-radius:.95em 50%;-moz-border-radius-topleft:.95em 50%;-webkit-border-top-left-radius:.95em 50%;border-top-right-radius:.95em 50%;-moz-border-radius-topright:.95em 50%;-webkit-border-top-right-radius:.95em 50%;border-bottom-left-radius:.95em 50%;-moz-border-radius-bottomleft:.95em 50%;-webkit-border-bottom-left-radius:.95em 50%;border-bottom-right-radius:.95em 50%;-moz-border-radius-bottomright:.95em 50%;-webkit-border-bottom-right-radius:.95em 50%}.icon_appmsg_tag.default{border:1px solid rgba(0,0,0,0.1);color:rgba(0,0,0,0.3);background-color:transparent;padding:0 .54em;font-size:15px;line-height:1.3;border-top-left-radius:.67em 50%;-moz-border-radius-topleft:.67em 50%;-webkit-border-top-left-radius:.67em 50%;border-top-right-radius:.67em 50%;-moz-border-radius-topright:.67em 50%;-webkit-border-top-right-radius:.67em 50%;border-bottom-left-radius:.67em 50%;-moz-border-radius-bottomleft:.67em 50%;-webkit-border-bottom-left-radius:.67em 50%;border-bottom-right-radius:.67em 50%;-moz-border-radius-bottomright:.67em 50%;-webkit-border-bottom-right-radius:.67em 50%}.rich_media_meta_list .icon_appmsg_tag.default{margin-top:-1px}.icon_appmsg_tag.title_tag{background-color:#d04b4e}.icon_global_tag_wrp{text-align:right;padding-bottom:12px}.icon_global_tag{background-color:rgba(118,118,118,0.16);color:rgba(0,0,0,0.41);line-height:2.2;border-top-left-radius:1em 50%;-moz-border-radius-topleft:1em 50%;-webkit-border-top-left-radius:1em 50%;border-bottom-left-radius:1em 50%;-moz-border-radius-bottomleft:1em 50%;-webkit-border-bottom-left-radius:1em 50%;padding:0 1.8em 0 1.34em;font-size:12px;margin-right:-24px;display:inline-block;vertical-align:top}.global_plain_btn{display:inline-block;vertical-align:middle;padding:0 1em;line-height:2;font-size:14px;-webkit-tap-highlight-color:rgba(0,0,0,0);border-radius:5px;-moz-border-radius:5px;-webkit-border-radius:5px}.global_plain_btn.primary{color:#1aad19;border:1px solid currentColor}.global_plain_btn.primary:active{color:rgba(26,173,25,0.6)}.wx_video_context{color:#fefefe;position:relative;background-color:#000}.wx_video_thumb,.wx_video_thumb_primary{position:absolute;left:0;width:100%;height:100%!important;top:0}.wx_video_thumb_primary{-webkit-background-size:cover;background-size:cover;background-position:50% 50%;background-repeat:no-repeat}.wx_video_play_btn{position:absolute;top:50%;left:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);margin-top:-2px;font-size:0;border-width:0;background-color:transparent;padding:0;outline:0;z-index:2}.wx_video_play_btn:before{content:" ";display:inline-block;width:0;height:0;border-width:14px 0 14px 25px;border-color:transparent transparent transparent #fff;border-style:dotted dotted dotted solid}.wx_video_mask{position:absolute;top:0;left:0;right:0;bottom:0;z-index:1;background-color:rgba(0,0,0,0.5)}.place_audio_area{min-height:100px;background-color:#fdfdfd;display:block;margin:16px 0}.place_music_area{min-height:68px;background-color:#fdfdfd;display:block;margin:17px 0 16px}.rich_media_empty_extra{background-color:#fafafa}.appmsg_skin_default.rich_media_empty_extra{background-color:#fff}.appmsg_skin_default .rich_media_area_primary{background-color:#fff}.appmsg_skin_default .rich_media_area_primary .weui-loadmore_line .weui-loadmore__tips{background-color:#fff}.appmsg_style_default .rich_media_tool{padding-top:15px}.rich_media_title_ios{font-weight:700}</style></head><body id="activity-detail" class="zh_CN mm_appmsg  appmsg_skin_default appmsg_style_default">    <div id="js_article" class="rich_media">        <div id="js_top_ad_area" class="top_banner"></div>        <div class="rich_media_inner">            <div id="page-content" class="rich_media_area_primary">                <div class="rich_media_area_primary_inner">                    <div id="img-content">                        <h2 class="rich_media_title" id="activity-name" style=\'text-align: center;font-size: 28px;\'>                            阿根廷主帅：梅西2019年会回归 暂时封存10号球衣                        </h2>                        <div class="rich_media_content " id="js_content">                            <p class="p1"><span style="font-size: 16px;"></span></p>                            <p class="p1"><span style="font-size: 16px;"> &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 阿根廷将连续两次对阵墨西哥，在周四进行的赛前新闻发布会上，阿根廷主帅斯卡罗尼透露梅西会在2019年回归蓝白军团，“他会再次为阿根廷出场”。</span></p>                            <p><br /></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;前阿根廷主帅斯卡罗尼在记者会上表示：</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <blockquote>                                <p><span style="font-size: 16px;">“他会再次为阿根廷出场！” &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ——斯卡罗尼</span></p>                            </blockquote>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p style="text-align: center;"><img src="http://106.15.225.249:8170/641.jpg"                                    style="width: 100%;height: auto;"/>梅西2019年将回归国家队</p>                            <br><br>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="font-size: 18px;">俄世界杯后</span></strong></span></p>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="color: rgb(0, 119, 181);font-size: 18px;">梅西未曾效力</span></strong></span></p>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="color: rgb(0, 119, 181);font-size: 18px;"><br /></span></strong></span></p>                            <p style="text-align: center;"><img src="http://106.15.225.249:8170/smpl.jpg"                                style="width: 100%;height: auto;"/>俄罗斯世界杯上的梅西</p>                            <br><br>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;自俄罗斯世界杯之后，梅西就再也没有为阿根廷国家队出场。斯卡罗尼透露，“现在还没有梅西回归的日期，他不会在2018年年底之前回到国家队。我相信在2019年，他会再次为阿根廷出场。”斯卡罗尼透露自己与梅西交流过，但没有谈及梅西是否会从国家队退役的话题，“我没有和梅西谈过他是否会踢美洲杯，我们谈论了足球，但我们并没有谈及未来会发生什么这个话题。我估计、希望也相信他会回到国家队。我们这次还是不会有球员身穿10号球衣。”</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <blockquote>                                    <p><span style="font-size: 16px;">“我没有和梅西谈过他是否会踢美洲杯，我们谈论了足球，但我们并没有谈及未来会发生什么这个话题。我估计、希望也相信他会回到国家队。我们这次还是不会有球员身穿10号球衣。”</span></p>                            </blockquote>                            <br>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果没有意外的话，那么对墨西哥的两场比赛将是斯卡罗尼执教阿根廷的最后两战。在被问及自己执教蓝白军团的目标时，斯卡罗尼透露：</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <blockquote>                                <p><span style="font-size: 16px;">“我的主要目标是确定阵容，第二个目标则是确定我们的踢球方式，不过有时候不会如愿。如果梅西能够回归，那么我们必须确保我们的战术会让他感到舒服。”</span></p>                            </blockquote>                            <br><br>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="font-size: 18px;">阿根廷主帅</span></strong></span></p>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="color: rgb(0, 119, 181);font-size: 18px;">卡斯罗尼</span></strong></span></p>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="color: rgb(0, 119, 181);font-size: 18px;"><br /></span></strong></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在执教的前四场比赛里，斯卡罗尼取得了2胜1平1负的成绩，而且仅丢1球。阿根廷主帅指出，“现在的成绩并不重要，这是毫无意义的，我们需要让球员们找到默契，每一名球员都可以出场，还有一些球员没有在我手下得到出场机会，尤其是一些非常年轻的球员，但你很难做到这一点，我们开出了一份33到34人的名单，有23到24名球员来到了这里。”</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p style="text-align: center;"><img src="http://106.15.225.249:8170/coche.jpg"                                style="width: 100%;height: auto;"/>阿根廷主教练 斯卡洛尼</p>                            <br><br>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;斯卡罗尼强调，“担任国家队主帅最艰巨的任务在于找到平衡，除了一些无法来到国家队的球员之外，我们希望给所有人机会。所有来到国家队的球员都非常积极，都有着训练、出场的强烈愿望。”</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在被问及阿自己的未来时，斯卡罗尼指出，“我们考虑的是下一场比赛，我执教之后有六场比赛，我们会考虑以后，我们专注于周五和下周二的比赛。我们不会只有一套主力阵容，我们一直在说，我们必须给年轻球员机会。” </span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;阿根廷四天之内将连续两次对阵墨西哥，斯卡罗尼透露了此役的首发阵容，唯一一个疑问则是热刺中卫福伊特是否会首发出场，“我们遇到了麻烦，福伊特在训练中受伤，我们不得不等等看他能否出场。”斯卡罗尼还透露，伊卡尔迪会在对墨西哥的第二战出场，“下周二，其他球员会出场。” </span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在被问及自己是否会转正时，斯卡罗尼表示，“我不能指望任何不存在的东西，这些都是假设。最让我兴奋的是周五的比赛以及南美青年锦标赛。我很高兴去执教这支球队，我很像看看未来会发生什么。有很多事情是我不知道的，唯一确认的只有我从12月10日会开始执教U20青年队。” </span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 尽管斯卡罗尼不过是救火主帅，但赢得了众多球员的支持，罗梅罗、伊卡尔迪等球员都表达了对斯卡罗尼的支持。阿根廷主帅表示，“我要感谢球员们，是他们让一切变得更加轻松。球员们总是要关注一切，帮助我们前进。我们知道球员们的想法，我们的关系非常好。这不是一件容易的事情，但在我的位置上，每个人都会这么去做。”                                </span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                                                        <p><span style="font-size: 16px; text-align: center"><strong>阿根廷vs墨西哥首发阵容：</strong></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;马尔凯辛/萨拉维亚、福伊特（梅尔卡多）、莫里、塔利亚费科/洛塞尔索、帕雷德斯、阿库尼亚/迪巴拉、劳塔罗-马丁内斯、科雷亚</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <br><br>                            <p line="gnrw" class="ql-long-12490592" style="white-space: normal;"><strong><span style="font-size: 16px;"><br /></span></strong></p>                            <p line="gnrw" class="ql-long-12490592" style="white-space: normal;text-align: justify;"><strong><span                                        style="font-size: 16px;">本文引用腾讯体育新闻，仅作为学习交流和Temage项目展示使用</span></strong></p>                            <p style="white-space: normal;text-align: justify;line-height: normal;"><span style="color: rgb(136, 136, 136);font-family: inherit;font-weight: inherit;letter-spacing: 0.5px;text-decoration: inherit;font-size: 10px;">Temage最终呈现的效果可视为上文呈现效果，即纯文本的格式化，图片自动插入位置和描述</span><br /></p>                            <fieldset class="" style="font-family: inherit;font-size: 1em;font-weight: inherit;white-space: normal;text-decoration: inherit;line-height: 25.6px;max-width: 100%;box-sizing: border-box;min-width: 0px;border-width: 0px;border-style: none;text-align: justify;color: rgb(160, 160, 160);background-color: rgb(255, 255, 255);overflow-wrap: break-word !important;">                                <p style="line-height: normal;"><span style="color: rgb(136, 136, 136);letter-spacing: 0.5px;font-size: 10px;">本页面由Temage队员手动排版完成，旨在模拟Temage的呈现效果</span></p>                                <p style="line-height: normal;"><span style="color: rgb(136, 136, 136);letter-spacing: 0.5px;font-size: 10px;">©2018                                        3107小队 保留所有权利</span></p>                            </fieldset>                            <fieldset class="" style="font-family: inherit;font-size: 1em;font-weight: inherit;white-space: normal;text-decoration: inherit;line-height: 25.6px;max-width: 100%;box-sizing: border-box;min-width: 0px;border-width: 0px;border-style: none;text-align: justify;color: rgb(160, 160, 160);background-color: rgb(255, 255, 255);overflow-wrap: break-word !important;">                                <p style="max-width: 100%;min-height: 1em;color: rgb(62, 62, 62);font-size: 18px;line-height: normal;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span                                        style="max-width: 100%;color: rgb(136, 136, 136);font-family: inherit;font-weight: inherit;text-decoration: inherit;letter-spacing: 0.5px;font-size: 16px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><img                                            class="" data-copyright="0" data-ratio="0.47" data-src="Users/Miao/Desktop/641.jpg=gif"                                            data-type="gif" data-w="400" data-before-oversubscription-url="Users/Miao/Desktop/641.jpg=gif"                                            data-backw="558" data-backh="262" style="width: 558px;" /></span></p>                            </fieldset>                        </div>                        <div class="ct_mpda_wrp" id="js_sponsor_ad_area" style="display:none;"></div>                    </div>                    <ul id="js_hotspot_area" class="article_extend_area"></ul>                </div>            </div>            <div class="rich_media_area_primary sougou" id="sg_tj" style="display:none"></div>            <div class="rich_media_area_extra">                <div class="rich_media_area_extra_inner">                    <div id="js_share_appmsg">                    </div>                    <div class="mpda_bottom_container" id="js_bottom_ad_area"></div>                    <div id="js_iframetest" style="display:none;"></div>                    <div class="rich_media_extra rich_media_extra_discuss" id="js_cmt_container" style="display:none">                        <div class="discuss_mod" id="js_friend_cmt_area" style="display:none">                        </div>                        <div class="discuss_mod" id="js_cmt_area" style="display:none">                        </div>                    </div>                </div>            </div>        </div>    </div>    <div id="js_pc_weapp_code" class="weui-desktop-popover weui-desktop-popover_pos-up-center weui-desktop-popover_img-text"        style="display: none;">        <div class="weui-desktop-popover__content">            <div class="weui-desktop-popover__desc">                <img id="js_pc_weapp_code_img">                微信扫一扫<br>使用小程序<span id="js_pc_weapp_code_des"></span> </div>        </div>    </div>    <div id="js_minipro_dialog" style="display:none;">        <div class="weui-mask"></div>        <div class="weui-dialog">            <div class="weui-dialog__bd">即将打开"<span id="js_minipro_dialog_name"></span>"小程序</div>            <div class="weui-dialog__ft">                <a id="js_minipro_dialog_cancel" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_default">取消</a>                <a id="js_minipro_dialog_ok" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_primary">打开</a>            </div>        </div>    </div></body></html>'
        product1 = Product.objects.create(title="product_1", html="<p>good day</p>", creator=profile1,style=style1, score=0.1, id=11)
        product2 = Product.objects.create(title="product_2", html="<p>bad day</p>", creator=profile1,style=style2, score=0.9, id=12)
        product3 = Product.objects.create(title="product_3", html="<p>cold day</p>", creator=profile1,style=style4, score=0.8, id=13)
        product4 = Product.objects.create(title="product_4", html="<p>hot day</p>", creator=profile1,style=style5, score=0.7, id=14)
        product5 = Product.objects.create(title="product_5", html="<p>hot day</p>", creator=profile1,style=style6, score=0.7, id=15)
        product6 = Product.objects.create(title="product_6", html="<p>hot day</p>", creator=profile1,style=style7, score=0.7, id=16)
        product7 = Product.objects.create(title="product_7", html="<p>hot day</p>", creator=profile1,style=style8, score=0.7, id=17)
        product8 = Product.objects.create(title="梅西重返赛场", html = htmlmecy, creator=profile1,style=style10, score=0.9, id = 18)
        product1.imagesrc.save('good.jpg', File(img1), save=True)
        product2.imagesrc.save('bad.jpg', File(img2), save=True)
        product3.imagesrc.save('cold.jpg', File(img3), save=True)
        product4.imagesrc.save('hot.jpg', File(img4), save=True)
        product5.imagesrc.save('hot.jpg', File(img4), save=True)
        product6.imagesrc.save('hot.jpg', File(img4), save=True)
        product7.imagesrc.save('hot.jpg', File(img4), save=True)
        product8.imagesrc.save('hot.jpg', File(img4), save=True)
        product1.theme.add(theme1)
        product1.theme.add(theme2)
        product2.theme.add(theme2)
        product8.theme.add(theme1)
        product8.theme.add(theme6)
        card1 = Card.objects.create(creator=profile1, product=product1, title="positive", prompt="A positive people said...", head="head content", foottext="foot content", id=1)
        card2 = Card.objects.create(creator=profile1, product=product2, title="negative", prompt="A negative people said...", head="head content", foottext="foot content")
        card3 = Card.objects.create(creator=profile1, product=product3, title="cold", prompt="A cold people said...", head="head content", foottext="foot content")
        card4 = Card.objects.create(creator=profile1, product=product4, title="hot", prompt="A hot people said...", head="head content", foottext="foot content")
        card5 = Card.objects.create(creator=profile1, product=product5, title="hot", prompt="A hot people said...", head="head content", foottext="foot content")
        card6 = Card.objects.create(creator=profile1, product=product6, title="hot", prompt="A hot people said...", head="head content", foottext="foot content")
        card7 = Card.objects.create(creator=profile1, product=product7, title="hot", prompt="A hot people said...", head="head content", foottext="foot content")
        card8 = Card.objects.create(creator=profile1, product=product8, title = "梅西重返赛场", prompt="反赛场啊反赛场", head="head content", foottext="foot content", id=10086)
        collection1 = Collection.objects.create(name = "quote", user=profile1)
        collection1.cards.add(card1)
        collection1.cards.add(card2)
        collection1.cards.add(card3)
        collection1.cards.add(card4)
        collection2 = Collection.objects.create(name="requote", user=profile1)
        collection2.cards.add(card1)
    

#  用例编号: 001{前端} 101{后端}
#  测试单元描述: {{测试文件中文}}
#  用例目的: {{带数据实例的过程描述}}
#  前提条件: {{数据背景，环境要求}}
#  特殊的规程说明: {{无， or必须的流程}}
#  用例间的依赖关系: {{多个用例测试之间的关系}}
#  具体流程:
#     步骤1
#         输入:
# 		  期望输出:
# 		  实际输出:
# 		  备注:
#     步骤2
#         ······
#  测试结果综合分析及建议:
#  测试经验总结:

    def testSuperuser(self):
        super_user = User.objects.filter(is_superuser=True)
        self.assertEqual(len(super_user),1)


#  用例编号: 101
#  测试单元描述: 测试Models的多态多对多关系
#  用例目的: 测试model多态多对多关系能否正常工作
#  前提条件: 通过数据库操作创建相应的带有多态多对多关系的对象们
#  特殊的规程说明: Profile与Product的对象可以同时拥有同一个Theme，且它们分别与Theme成多对多关系
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: user和第一个product拥有同一个theme
# 		  实际输出: 两者的theme相等
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testPolymorphicManytomany(self):
        user = Profile.objects.get(user__username='qxy')
        themelist_of_user = user.theme.all().values('name')
        list1 = list(themelist_of_user)
        themelist_of_product = Product.objects.get(id=11).theme.all().values('name')
        list2 = list(themelist_of_product)
        self.assertEqual(list1[0]['name'], list2[0]['name'])


#  用例编号: 102
#  测试单元描述: 登录功能测试
#  用例目的: 测试login登录功能
#  前提条件: 数据库中已存在username="qxy", password="123"的用户
#  特殊的规程说明: 无
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: {username:"qxy", password:"123"}
# 		  期望输出: status_code = 200
# 		  实际输出: "200"
# 		  备注: 无
#  测试结果综合分析及建议: Succeed
#  测试经验总结: 无
    def testLogin(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        self.assertEqual(response.status_code, 200)

#  用例编号: 103
#  测试单元描述: 测试api接口
#  用例目的: 测试给前端/api返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 用户需要先登录才能获取这些信息
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 有三个元素的list
# 		  实际输出: 有三个元素的list
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApi(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList), 3)

#  用例编号: 104
#  测试单元描述: 测试/api/work接口
#  用例目的: 测试给前端/api/work返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 用户需要先登录才能获取这些信息
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request，work的id
# 		  期望输出: 所有的style的数据和该work的html内容
# 		  实际输出: 所有的style的数据和该work的html内容
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiWork(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/work/11', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList[0]), 20)
        self.assertGreater(len(responseList[1]), 0)

#  用例编号: 105
#  测试单元描述: 测试api接口
#  用例目的: 测试给前端/api/collection返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 用户需要先登录才能获取这些信息
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: collection的内容
# 		  实际输出: collection的内容
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiCollection(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/collection', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList[0]), 1)
        self.assertEqual(len(responseList[1]), 2)

#  用例编号: 106
#  测试单元描述: 测试api/recent接口
#  用例目的: 测试给前端/api/recent返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 用户需要先登录才能获取这些信息
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 七张card
# 		  实际输出: 七张card
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiRecent(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/recent', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList), 4)


#  用例编号: 107
#  测试单元描述: 测试register接口
#  用例目的: 测试用户注册功能
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 无
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 注册成功状态码“200”
# 		  实际输出: “200”
# 		  备注: 
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testRegister(self):
        response = self.client.post('/register',  {'password': '123', 'username': 'tmg','email': '123123@qq.com','interest': ['Porn','Sport'],'desc': 'love and peace'}, content_type="application/json")
        self.assertEqual(response.status_code, 200)

#  用例编号: 108
#  测试单元描述: 测试/api/gallery接口
#  用例目的: 测试/api/gallery返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 需登陆后操作
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 返回相应gallery数据
# 		  实际输出：返回了相应的gallery数据
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiGallery(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/gallery', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        print(responseList)
        self.assertEqual(len(responseList), 7)

#  用例编号: 109
#  测试单元描述: 测试/api/gallery/more_cards接口
#  用例目的: 测试/api/gallery/more_cards返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 需登陆后操作
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 随机返回4条gallery数据
# 		  实际输出: 随机返回4条gallery数据
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiGalleryMoreCard(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/gallery/more_cards', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList), 4)

#  用例编号: 110
#  测试单元描述: 测试/api/text接口
#  用例目的: 测试/api/text返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 需登陆后操作
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 返回所请求的card的信息
# 		  实际输出: 返回所请求的card的信息
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiText(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/text', {'id' : '10086'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        print(responseList)
        self.assertEqual(responseList['id'], 1)