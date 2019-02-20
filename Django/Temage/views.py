from django.shortcuts import render
from Temage.models import User
from Temage.models import Profile
from Temage.models import Product
from Temage.models import Card
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Theme
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.contrib.auth import authenticate, login
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.files import File
import jwt
import random
import requests


result_html = '<!DOCTYPE html><html><head>    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">    <meta http-equiv="X-UA-Compatible" content="IE=edge">    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0,viewport-fit=cover">    <meta name="apple-mobile-web-app-capable" content="yes">    <meta name="apple-mobile-web-app-status-bar-style" content="black">    <meta name="format-detection" content="telephone=no">    <title>        阿根廷主帅：梅西2019年会回归 暂时封存10号球衣    </title>    <style>.radius_avatar{display:inline-block;background-color:#fff;padding:3px;border-radius:50%;-moz-border-radius:50%;-webkit-border-radius:50%;overflow:hidden;vertical-align:middle}.radius_avatar img{display:block;width:100%;height:100%;border-radius:50%;-moz-border-radius:50%;-webkit-border-radius:50%;background-color:#eee}.rich_media_inner{word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.rich_media_area_primary{padding:20px 16px 12px;background-color:#fafafa}.rich_media_area_primary.voice{padding-top:66px}.rich_media_area_primary .weui-loadmore_line .weui-loadmore__tips{color:rgba(0,0,0,0.3);background-color:#fafafa}.rich_media_area_extra{padding:0 16px 24px}.rich_media_extra{padding-top:30px}.mpda_bottom_container .rich_media_extra{padding-top:24px}html{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;line-height:1.6}body{-webkit-touch-callout:none;font-family:-apple-system-font,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif;color:#333;background-color:#f2f2f2;letter-spacing:.034em}h1,h2,h3,h4,h5,h6{font-weight:400;font-size:16px}*{margin:0;padding:0}a{color:#576b95;text-decoration:none;-webkit-tap-highlight-color:rgba(0,0,0,0)}.rich_media_title{font-size:22px;line-height:1.4;margin-bottom:14px}@supports(-webkit-overflow-scrolling:touch){.rich_media_title{font-weight:700}}.rich_media_meta_list{margin-bottom:22px;line-height:20px;font-size:0;word-wrap:break-word;word-break:break-all}.rich_media_meta_list em{font-style:normal}.rich_media_meta{display:inline-block;vertical-align:middle;margin:0 10px 10px 0;font-size:15px;-webkit-tap-highlight-color:rgba(0,0,0,0)}.rich_media_meta.icon_appmsg_tag{margin-right:4px}.rich_media_meta.meta_tag_text{margin-right:0}.rich_media_meta_primary{display:block;margin-bottom:10px;font-size:15px}.meta_original_tag{padding:0 .5em;font-size:12px;line-height:1.4;background-color:#f2f2f2;color:#888}.meta_enterprise_tag img{width:30px;height:30px!important;display:block;position:relative;margin-top:-3px;border:0}.rich_media_meta_link{color:#576b95}.rich_media_meta_text{color:rgba(0,0,0,0.3)}.rich_media_meta_text.rich_media_meta_split{padding-left:10px}.rich_media_meta_text.rich_media_meta_split:before{position:absolute;top:50%;left:0;margin-top:-6px;content:\' \';display:block;border-left:1px solid #888;width:200%;height:130%;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:0 0;transform-origin:0 0}.rich_media_meta_text.article_modify_tag{position:relative}.rich_media_meta_nickname{position:relative}.rich_media_thumb_wrp{margin-bottom:6px}.rich_media_thumb_wrp .original_img_wrp{display:block}.rich_media_thumb{display:block;width:100%}.rich_media_content{overflow:hidden;color:#333;font-size:17px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto;text-align:justify}.rich_media_content *{max-width:100%!important;box-sizing:border-box!important;-webkit-box-sizing:border-box!important;word-wrap:break-word!important}.rich_media_content p{clear:both;min-height:1em}.rich_media_content em{font-style:italic}.rich_media_content fieldset{min-width:0}.rich_media_content .list-paddingleft-2{padding-left:2.2em}.rich_media_content .list-paddingleft-2 .list-paddingleft-2{padding-left:30px}.rich_media_content blockquote{margin:0;padding-left:10px;border-left:3px solid #dbdbdb}.weui-mask{position:fixed;z-index:1000;top:0;right:0;left:0;bottom:0;background:rgba(0,0,0,0.6)}.weui-dialog{position:fixed;z-index:5000;width:80%;max-width:300px;top:50%;left:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);background-color:#fff;text-align:center;border-radius:3px;overflow:hidden}.weui-dialog__hd{padding:1.3em 1.6em .5em}.weui-dialog__title{font-weight:400;font-size:18px}.weui-dialog__bd{padding:0 1.6em .8em;min-height:40px;font-size:15px;line-height:1.3;word-wrap:break-word;word-break:break-all;color:#999}.weui-dialog__bd:first-child{padding:2.7em 20px 1.7em;color:#353535}.weui-dialog__ft{position:relative;line-height:48px;font-size:18px;display:-webkit-box;display:-webkit-flex;display:flex}.weui-dialog__ft:after{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid #d5d5d6;color:#d5d5d6;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.weui-dialog__btn{display:block;-webkit-box-flex:1;-webkit-flex:1;flex:1;color:#3cc51f;text-decoration:none;-webkit-tap-highlight-color:rgba(0,0,0,0);position:relative}.weui-dialog__btn:active{background-color:#eee}.weui-dialog__btn:after{content:" ";position:absolute;left:0;top:0;width:1px;bottom:0;border-left:1px solid #d5d5d6;color:#d5d5d6;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleX(0.5);transform:scaleX(0.5)}.weui-dialog__btn:first-child:after{display:none}.weui-dialog__btn_default{color:#353535}.weui-dialog__btn_primary{color:#0bb20c}img{height:auto!important}@media only screen and (device-width:375px) and (device-height:812px) and (-webkit-device-pixel-ratio:3) and (orientation:portrait){.rich_media_area_extra{padding-bottom:34px}}@media only screen and (device-width:375px) and (device-height:812px) and (-webkit-device-pixel-ratio:3) and (orientation:landscape){.rich_media_area_primary{padding:20px 60px 15px 60px}.rich_media_area_extra{padding:0 60px 21px 60px}}@media screen and (min-width:1024px){.rich_media_area_primary_inner,.rich_media_area_extra_inner{max-width:677px;margin-left:auto;margin-right:auto}.rich_media_area_primary{padding-top:32px}}.appmsg_share_notice{font-size:16px;color:#888;position:relative;padding:1.25em 0;margin-bottom:1.75em}.appmsg_share_notice:before{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid #dfdfdf;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.appmsg_share_notice:after{content:" ";position:absolute;left:0;bottom:0;right:0;height:1px;border-bottom:1px solid #dfdfdf;-webkit-transform-origin:0 100%;transform-origin:0 100%;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.appmsg_share_notice_hd{font-weight:700;padding-bottom:.2em}.cell{padding:.8em 0;display:block;position:relative}.cell_hd,.cell_bd,.cell_ft{display:table-cell;vertical-align:middle;word-wrap:break-word;word-break:break-all;white-space:nowrap}.cell_primary{width:2000px;white-space:normal}.flex_cell{padding:10px 0;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-ms-flex-align:center;align-items:center}.flex_cell_primary{width:100%;-webkit-box-flex:1;-webkit-flex:1;-ms-flex:1;box-flex:1;flex:1}.original_tool_area{display:block;padding:.75em 1em 0;-webkit-tap-highlight-color:rgba(0,0,0,0);color:#333;border:1px solid #eaeaea;margin:20px 0}.original_tool_area .tips_global{position:relative;padding-bottom:.5em;font-size:15px}.original_tool_area .tips_global:after{content:" ";position:absolute;left:0;bottom:0;right:0;height:1px;border-bottom:1px solid #dbdbdb;-webkit-transform-origin:0 100%;transform-origin:0 100%;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.original_tool_area .radius_avatar{width:27px;height:27px;padding:0;margin-right:.5em}.original_tool_area .radius_avatar img{height:100%!important}.original_tool_area .flex_cell_bd{width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal}.original_tool_area .flex_cell_ft{font-size:14px;color:#888;padding-left:1em;white-space:nowrap}.original_tool_area .icon_access:after{content:" ";display:inline-block;height:8px;width:8px;border-width:1px 1px 0 0;border-color:#cbcad0;border-style:solid;transform:matrix(0.71,0.71,-0.71,0.71,0,0);-ms-transform:matrix(0.71,0.71,-0.71,0.71,0,0);-webkit-transform:matrix(0.71,0.71,-0.71,0.71,0,0);position:relative;top:-2px;top:-1px}.rich_media_global_msg{position:fixed;top:0;left:0;right:0;padding:.85em 35px .85em 15px;z-index:2;background-color:#c6e0f8;color:#888;font-size:12px}.rich_media_global_msg .icon_closed{position:absolute;right:15px;top:50%;margin-top:-5px;line-height:300px;overflow:hidden;-webkit-tap-highlight-color:rgba(0,0,0,0);background:transparent url(//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/icon_appmsg_msg_closed_sprite.2x2eb52b.png) no-repeat 0 0;width:11px;height:11px;vertical-align:middle;display:inline-block;-webkit-background-size:100% auto;background-size:100% auto}.rich_media_global_msg .icon_closed:active{background-position:0 -17px}.rich_media_global_msg.voice{color:#1aad19;background-color:#e8f6e8;padding-left:43.3px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.rich_media_global_msg.voice .ic_voice{position:absolute;top:50%;margin-top:-10px;left:15px;display:inline-block;width:13.3px;height:18.3px;background:url(data:image/png;base64,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) no-repeat center;background-size:contain}.rich_media_global_msg.voice .icon_more{position:absolute;right:15px;top:50%;margin-top:-6.5px;width:8px;height:13px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAmCAYAAADeB1slAAAAAXNSR0IArs4c6QAAA49JREFUSA2tVk1IVFEUPveOmhQk1ibfvLFZSJtACqJIIpCIoB+imcFV2Z9ZUVnRomgRGFn2i6mFf5XVotCZMYmgIMhlq6BFENFiwjfPAosgFzXOvNu5o3fmeue98Y16F3PP+c453/fu/xCQmvZSWwwJaC0G6P8WND9IoTmbVFRycpqAdgBWkwRo94V960RsPn1aoPpN9RI6CR0WsDWcjAErtUiqTR/S18+HnNcSTv5zYrwDSatVMgLkH6aciwfj79WYW5+OT4xfsyPnBIgvwt872qBW45ZQzaMlJXCfMPJbDQgfRUoIhduVUW2TwArpaWyX+bnYU9JAAH44FaJIccqCW76Ib7NTjhOOvFPN/8q/IvE3cR+npFJgao9rkiSUXjD2GCNqzMnPbNPYjth3mqINlJAvTsk4kiJmWa3eQe8WpxwVzwjwgFFn/CorL29EkY9qovC5CFDrKq7JVoHl6zNTJCf53/lLk78SN/FcbJRx2cZCixC4ZATGXsu4as8YgQjGamN/q5atOotn4K3A1J4BUMbgsh7Wt6sx2bcV4AkjtSPJxkDjRQL0hVwg21zEglSzN+rdKeOybTtFcgK39ajWZDFWr+IZHxfGQ8mV0YA5nMGmDVcCPNcb8R5gYJ1UCWQfp6PFCI4NyZhrAV6EIiHGrPOAB0ImkW2c0la8u8ICc0wUCWrvC1dsw+3TnN6uanDaJ4zeiIfiA9wtWIAX8XspxeA6iuBlaN88hNzCNXk+JwFOuXJYW5tMQmc+EcqgzXGb2n9XFk1NstX5yKczl89JAF+6vRaBM1m5XAu//qkRGrtb8BThTtqH2/V0LmUWwbvsiREw8X0vcJHxxNbjNm3KUuVaMjmPFuWm2CPesHc/kp+yj06hFMhj/PIOOcfVFLk6xZT0G3vMTpmc27MusityZk/OBfKOwA05MPLIDJn3OJldcxTQotpBYOyEXVEWIw/NoInvuHOznSJfVDs0GzneNw9mI+eyOSPQI9phfCqPO38TFhHaFw/Eu/LliNiMESB5w6zkzD05F8mMYJr8mFC263Fa+vAadvXloj4toEcrjlgMjgrQrseHpBcfkm67WD6M6MN6lTWZeoZjyYxGLcB57MGnsEfF3fjU2G189QBpcUqmBLrnSs4504s8GjLxrwm5qYrg3dKFf6x6VbwQ3yOS/wz8+bS0ruwfELaBY2nyoNkn4gvW65GKRn4WForwP+dONHDaOHeZAAAAAElFTkSuQmCC) no-repeat center;background-size:contain}.preview_appmsg .rich_media_title{margin-top:2.3em}@media screen and (min-width:1024px){.rich_media_global_msg{position:relative;margin-bottom:32px}.preview_appmsg .rich_media_title.rich_media_title{margin-top:0}}.pages_reset{color:#333;line-height:1.6;font-size:16px;font-weight:400;font-style:normal;text-indent:0;letter-spacing:normal;text-align:left;text-decoration:none;white-space:normal}.weapp_element,.weapp_display_element,.mp-miniprogram{display:block;margin:1em 0}.share_audio_context{margin:16px 0}.weapp_text_link{font-size:17px}.weapp_text_link:before{content:\'\';display:inline-block;line-height:1;background-size:contain;background-repeat:no-repeat;background-image:url(\'data:image/png;base64,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\');vertical-align:middle;font-size:11px;color:#888;margin-right:6px;margin-top:-3px;background-position:center;height:20px;width:20px}.flex_context{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.flex_bd{-webkit-box-flex:1;-webkit-flex:1;flex:1;word-wrap:break-word;word-break:break-all}.original_page{background-color:#fff;font-size:16px}.account_info{padding:0 0 20px}.account_info .flex_bd{padding-left:.85em}.radius_avatar.account_avatar{width:40px;height:40px;padding:0}.account_nickname{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:1;line-height:1.2;color:#576b95;font-size:14px}.account_nickname_inner{font-weight:400;vertical-align:top}.account_desc{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:1;color:#b2b2b2;font-size:13px;line-height:1.2;padding-top:.3em}.account_desc_inner{display:inline;vertical-align:top}.share_notice{margin-bottom:20px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.share_media{padding-bottom:18px}.original_panel{padding:20px;background-color:#fcfcfc;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto;overflow:hidden;position:relative}.original_panel:after{content:" ";border:1px solid #d8d8d8;border-radius:4px;-moz-border-radius:4px;-webkit-border-radius:4px;position:absolute;top:0;left:0;width:200%;height:200%;-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:0 0;transform-origin:0 0;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}.original_panel .original_account{margin-bottom:18px;position:relative;z-index:1}.original_panel .original_account_avatar{width:28px;height:28px;padding:0}.original_panel .original_account_nickname{padding-left:.85em;font-size:15px;color:#576b95}.original_panel_title{font-size:23px;color:#000;margin:0 0 16px}.original_panel_content{color:#333}.original_panel_tool{padding-top:20px;position:relative;z-index:1}.original_cell_nickname{display:inline-block;vertical-align:middle;font-weight:400;width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal;max-width:8em;color:#000}.original_tool_area{padding:1.17em 0;border-width:0;position:relative}.original_tool_area:before{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid #dfdfdf;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.original_tool_area:after{content:" ";position:absolute;left:0;bottom:0;right:0;height:1px;border-bottom:1px solid #dfdfdf;-webkit-transform-origin:0 100%;transform-origin:0 100%;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.original_tool_area .radius_avatar{width:20px;height:20px;margin-right:.2em}.original_tool_area .flex_cell{padding:0;font-size:14px}.original_tool_area .icon_access:after{margin-right:4px;top:0}.preview_appmsg .rich_media_title{margin-top:1.5em}.preview_appmsg .account_info{padding-top:3em}.original_page{background-color:transparent}.account_info{-webkit-tap-highlight-color:rgba(0,0,0,0);outline:0;padding-bottom:20px;font-size:14px}.account_info.appmsg_account_info{padding-bottom:32px}.account_info .radius_avatar img{background-color:transparent}.share_notice{font-size:16px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.original_panel{background-color:#fafafa}.original_panel:after{border-color:#e6e6e6}.original_panel .original_account_avatar{width:30px;height:30px}.original_panel_tool{font-size:14px}.original_panel_tool a{color:#576b95}.original_panel_content{font-size:17px}.share_media{padding-bottom:30px}.icon_appmsg_tag{display:inline-block;vertical-align:middle;padding:0 .5em;font-size:12px;line-height:1.5;background-color:#c3c3c3;color:#fff;border-radius:2px;-moz-border-radius:2px;-webkit-border-radius:2px;width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal;max-width:70%}.icon_appmsg_tag.primary{color:#3bb638;padding:4px .78em;background-color:rgba(9,187,7,0.08);font-size:12px;border-top-left-radius:.95em 50%;-moz-border-radius-topleft:.95em 50%;-webkit-border-top-left-radius:.95em 50%;border-top-right-radius:.95em 50%;-moz-border-radius-topright:.95em 50%;-webkit-border-top-right-radius:.95em 50%;border-bottom-left-radius:.95em 50%;-moz-border-radius-bottomleft:.95em 50%;-webkit-border-bottom-left-radius:.95em 50%;border-bottom-right-radius:.95em 50%;-moz-border-radius-bottomright:.95em 50%;-webkit-border-bottom-right-radius:.95em 50%}.icon_appmsg_tag.default{border:1px solid rgba(0,0,0,0.1);color:rgba(0,0,0,0.3);background-color:transparent;padding:0 .54em;font-size:15px;line-height:1.3;border-top-left-radius:.67em 50%;-moz-border-radius-topleft:.67em 50%;-webkit-border-top-left-radius:.67em 50%;border-top-right-radius:.67em 50%;-moz-border-radius-topright:.67em 50%;-webkit-border-top-right-radius:.67em 50%;border-bottom-left-radius:.67em 50%;-moz-border-radius-bottomleft:.67em 50%;-webkit-border-bottom-left-radius:.67em 50%;border-bottom-right-radius:.67em 50%;-moz-border-radius-bottomright:.67em 50%;-webkit-border-bottom-right-radius:.67em 50%}.rich_media_meta_list .icon_appmsg_tag.default{margin-top:-1px}.icon_appmsg_tag.title_tag{background-color:#d04b4e}.icon_global_tag_wrp{text-align:right;padding-bottom:12px}.icon_global_tag{background-color:rgba(118,118,118,0.16);color:rgba(0,0,0,0.41);line-height:2.2;border-top-left-radius:1em 50%;-moz-border-radius-topleft:1em 50%;-webkit-border-top-left-radius:1em 50%;border-bottom-left-radius:1em 50%;-moz-border-radius-bottomleft:1em 50%;-webkit-border-bottom-left-radius:1em 50%;padding:0 1.8em 0 1.34em;font-size:12px;margin-right:-24px;display:inline-block;vertical-align:top}.global_plain_btn{display:inline-block;vertical-align:middle;padding:0 1em;line-height:2;font-size:14px;-webkit-tap-highlight-color:rgba(0,0,0,0);border-radius:5px;-moz-border-radius:5px;-webkit-border-radius:5px}.global_plain_btn.primary{color:#1aad19;border:1px solid currentColor}.global_plain_btn.primary:active{color:rgba(26,173,25,0.6)}.wx_video_context{color:#fefefe;position:relative;background-color:#000}.wx_video_thumb,.wx_video_thumb_primary{position:absolute;left:0;width:100%;height:100%!important;top:0}.wx_video_thumb_primary{-webkit-background-size:cover;background-size:cover;background-position:50% 50%;background-repeat:no-repeat}.wx_video_play_btn{position:absolute;top:50%;left:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);margin-top:-2px;font-size:0;border-width:0;background-color:transparent;padding:0;outline:0;z-index:2}.wx_video_play_btn:before{content:" ";display:inline-block;width:0;height:0;border-width:14px 0 14px 25px;border-color:transparent transparent transparent #fff;border-style:dotted dotted dotted solid}.wx_video_mask{position:absolute;top:0;left:0;right:0;bottom:0;z-index:1;background-color:rgba(0,0,0,0.5)}.place_audio_area{min-height:100px;background-color:#fdfdfd;display:block;margin:16px 0}.place_music_area{min-height:68px;background-color:#fdfdfd;display:block;margin:17px 0 16px}.rich_media_empty_extra{background-color:#fafafa}.appmsg_skin_default.rich_media_empty_extra{background-color:#fff}.appmsg_skin_default .rich_media_area_primary{background-color:#fff}.appmsg_skin_default .rich_media_area_primary .weui-loadmore_line .weui-loadmore__tips{background-color:#fff}.appmsg_style_default .rich_media_tool{padding-top:15px}.rich_media_title_ios{font-weight:700}</style></head><body id="activity-detail" class="zh_CN mm_appmsg  appmsg_skin_default appmsg_style_default">    <div id="js_article" class="rich_media">        <div id="js_top_ad_area" class="top_banner"></div>        <div class="rich_media_inner">            <div id="page-content" class="rich_media_area_primary">                <div class="rich_media_area_primary_inner">                    <div id="img-content">                        <h2 class="rich_media_title" id="activity-name" style=\'text-align: center;font-size: 28px;\'>                            阿根廷主帅：梅西2019年会回归 暂时封存10号球衣                        </h2>                        <div class="rich_media_content " id="js_content">                            <p class="p1"><span style="font-size: 16px;"></span></p>                            <p class="p1"><span style="font-size: 16px;"> &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 阿根廷将连续两次对阵墨西哥，在周四进行的赛前新闻发布会上，阿根廷主帅斯卡罗尼透露梅西会在2019年回归蓝白军团，“他会再次为阿根廷出场”。</span></p>                            <p><br /></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;前阿根廷主帅斯卡罗尼在记者会上表示：</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <blockquote>                                <p><span style="font-size: 16px;">“他会再次为阿根廷出场！” &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ——斯卡罗尼</span></p>                            </blockquote>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p style="text-align: center;"><img src="http://106.15.225.249:8170/641.jpg"                                    style="width: 100%;height: auto;"/>梅西2019年将回归国家队</p>                            <br><br>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="font-size: 18px;">俄世界杯后</span></strong></span></p>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="color: rgb(0, 119, 181);font-size: 18px;">梅西未曾效力</span></strong></span></p>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="color: rgb(0, 119, 181);font-size: 18px;"><br /></span></strong></span></p>                            <p style="text-align: center;"><img src="http://106.15.225.249:8170/smpl.jpg"                                style="width: 100%;height: auto;"/>俄罗斯世界杯上的梅西</p>                            <br><br>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;自俄罗斯世界杯之后，梅西就再也没有为阿根廷国家队出场。斯卡罗尼透露，“现在还没有梅西回归的日期，他不会在2018年年底之前回到国家队。我相信在2019年，他会再次为阿根廷出场。”斯卡罗尼透露自己与梅西交流过，但没有谈及梅西是否会从国家队退役的话题，“我没有和梅西谈过他是否会踢美洲杯，我们谈论了足球，但我们并没有谈及未来会发生什么这个话题。我估计、希望也相信他会回到国家队。我们这次还是不会有球员身穿10号球衣。”</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <blockquote>                                    <p><span style="font-size: 16px;">“我没有和梅西谈过他是否会踢美洲杯，我们谈论了足球，但我们并没有谈及未来会发生什么这个话题。我估计、希望也相信他会回到国家队。我们这次还是不会有球员身穿10号球衣。”</span></p>                            </blockquote>                            <br>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果没有意外的话，那么对墨西哥的两场比赛将是斯卡罗尼执教阿根廷的最后两战。在被问及自己执教蓝白军团的目标时，斯卡罗尼透露：</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <blockquote>                                <p><span style="font-size: 16px;">“我的主要目标是确定阵容，第二个目标则是确定我们的踢球方式，不过有时候不会如愿。如果梅西能够回归，那么我们必须确保我们的战术会让他感到舒服。”</span></p>                            </blockquote>                            <br><br>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="font-size: 18px;">阿根廷主帅</span></strong></span></p>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="color: rgb(0, 119, 181);font-size: 18px;">卡斯罗尼</span></strong></span></p>                            <p style="text-align: center;"><span style="color: rgb(0, 119, 181);"><strong><span style="color: rgb(0, 119, 181);font-size: 18px;"><br /></span></strong></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在执教的前四场比赛里，斯卡罗尼取得了2胜1平1负的成绩，而且仅丢1球。阿根廷主帅指出，“现在的成绩并不重要，这是毫无意义的，我们需要让球员们找到默契，每一名球员都可以出场，还有一些球员没有在我手下得到出场机会，尤其是一些非常年轻的球员，但你很难做到这一点，我们开出了一份33到34人的名单，有23到24名球员来到了这里。”</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p style="text-align: center;"><img src="http://106.15.225.249:8170/coche.jpg"                                style="width: 100%;height: auto;"/>阿根廷主教练 斯卡洛尼</p>                            <br><br>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;斯卡罗尼强调，“担任国家队主帅最艰巨的任务在于找到平衡，除了一些无法来到国家队的球员之外，我们希望给所有人机会。所有来到国家队的球员都非常积极，都有着训练、出场的强烈愿望。”</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在被问及阿自己的未来时，斯卡罗尼指出，“我们考虑的是下一场比赛，我执教之后有六场比赛，我们会考虑以后，我们专注于周五和下周二的比赛。我们不会只有一套主力阵容，我们一直在说，我们必须给年轻球员机会。” </span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;阿根廷四天之内将连续两次对阵墨西哥，斯卡罗尼透露了此役的首发阵容，唯一一个疑问则是热刺中卫福伊特是否会首发出场，“我们遇到了麻烦，福伊特在训练中受伤，我们不得不等等看他能否出场。”斯卡罗尼还透露，伊卡尔迪会在对墨西哥的第二战出场，“下周二，其他球员会出场。” </span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在被问及自己是否会转正时，斯卡罗尼表示，“我不能指望任何不存在的东西，这些都是假设。最让我兴奋的是周五的比赛以及南美青年锦标赛。我很高兴去执教这支球队，我很像看看未来会发生什么。有很多事情是我不知道的，唯一确认的只有我从12月10日会开始执教U20青年队。” </span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 尽管斯卡罗尼不过是救火主帅，但赢得了众多球员的支持，罗梅罗、伊卡尔迪等球员都表达了对斯卡罗尼的支持。阿根廷主帅表示，“我要感谢球员们，是他们让一切变得更加轻松。球员们总是要关注一切，帮助我们前进。我们知道球员们的想法，我们的关系非常好。这不是一件容易的事情，但在我的位置上，每个人都会这么去做。”                                </span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                                                        <p><span style="font-size: 16px; text-align: center"><strong>阿根廷vs墨西哥首发阵容：</strong></span></p>                            <p><span style="font-size: 16px;">&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;马尔凯辛/萨拉维亚、福伊特（梅尔卡多）、莫里、塔利亚费科/洛塞尔索、帕雷德斯、阿库尼亚/迪巴拉、劳塔罗-马丁内斯、科雷亚</span></p>                            <p><span style="font-size: 16px;"><br /></span></p>                            <br><br>                            <p line="gnrw" class="ql-long-12490592" style="white-space: normal;"><strong><span style="font-size: 16px;"><br /></span></strong></p>                            <p line="gnrw" class="ql-long-12490592" style="white-space: normal;text-align: justify;"><strong><span                                        style="font-size: 16px;">本文引用腾讯体育新闻，仅作为学习交流和Temage项目展示使用</span></strong></p>                            <p style="white-space: normal;text-align: justify;line-height: normal;"><span style="color: rgb(136, 136, 136);font-family: inherit;font-weight: inherit;letter-spacing: 0.5px;text-decoration: inherit;font-size: 10px;">Temage最终呈现的效果可视为上文呈现效果，即纯文本的格式化，图片自动插入位置和描述</span><br /></p>                            <fieldset class="" style="font-family: inherit;font-size: 1em;font-weight: inherit;white-space: normal;text-decoration: inherit;line-height: 25.6px;max-width: 100%;box-sizing: border-box;min-width: 0px;border-width: 0px;border-style: none;text-align: justify;color: rgb(160, 160, 160);background-color: rgb(255, 255, 255);overflow-wrap: break-word !important;">                                <p style="line-height: normal;"><span style="color: rgb(136, 136, 136);letter-spacing: 0.5px;font-size: 10px;">本页面由Temage队员手动排版完成，旨在模拟Temage的呈现效果</span></p>                                <p style="line-height: normal;"><span style="color: rgb(136, 136, 136);letter-spacing: 0.5px;font-size: 10px;">©2018                                        3107小队 保留所有权利</span></p>                            </fieldset>                            <fieldset class="" style="font-family: inherit;font-size: 1em;font-weight: inherit;white-space: normal;text-decoration: inherit;line-height: 25.6px;max-width: 100%;box-sizing: border-box;min-width: 0px;border-width: 0px;border-style: none;text-align: justify;color: rgb(160, 160, 160);background-color: rgb(255, 255, 255);overflow-wrap: break-word !important;">                                <p style="max-width: 100%;min-height: 1em;color: rgb(62, 62, 62);font-size: 18px;line-height: normal;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span                                        style="max-width: 100%;color: rgb(136, 136, 136);font-family: inherit;font-weight: inherit;text-decoration: inherit;letter-spacing: 0.5px;font-size: 16px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><img                                            class="" data-copyright="0" data-ratio="0.47" data-src="Users/Miao/Desktop/641.jpg=gif"                                            data-type="gif" data-w="400" data-before-oversubscription-url="Users/Miao/Desktop/641.jpg=gif"                                            data-backw="558" data-backh="262" style="width: 558px;" /></span></p>                            </fieldset>                        </div>                        <div class="ct_mpda_wrp" id="js_sponsor_ad_area" style="display:none;"></div>                    </div>                    <ul id="js_hotspot_area" class="article_extend_area"></ul>                </div>            </div>            <div class="rich_media_area_primary sougou" id="sg_tj" style="display:none"></div>            <div class="rich_media_area_extra">                <div class="rich_media_area_extra_inner">                    <div id="js_share_appmsg">                    </div>                    <div class="mpda_bottom_container" id="js_bottom_ad_area"></div>                    <div id="js_iframetest" style="display:none;"></div>                    <div class="rich_media_extra rich_media_extra_discuss" id="js_cmt_container" style="display:none">                        <div class="discuss_mod" id="js_friend_cmt_area" style="display:none">                        </div>                        <div class="discuss_mod" id="js_cmt_area" style="display:none">                        </div>                    </div>                </div>            </div>        </div>    </div>    <div id="js_pc_weapp_code" class="weui-desktop-popover weui-desktop-popover_pos-up-center weui-desktop-popover_img-text"        style="display: none;">        <div class="weui-desktop-popover__content">            <div class="weui-desktop-popover__desc">                <img id="js_pc_weapp_code_img">                微信扫一扫<br>使用小程序<span id="js_pc_weapp_code_des"></span> </div>        </div>    </div>    <div id="js_minipro_dialog" style="display:none;">        <div class="weui-mask"></div>        <div class="weui-dialog">            <div class="weui-dialog__bd">即将打开"<span id="js_minipro_dialog_name"></span>"小程序</div>            <div class="weui-dialog__ft">                <a id="js_minipro_dialog_cancel" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_default">取消</a>                <a id="js_minipro_dialog_ok" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_primary">打开</a>            </div>        </div>    </div></body></html>'

# Create your views here.

####################################################################
# Interfaces for get data from database and send theme to front-end
####################################################################

def homepage_data(request):
    """
    This is function that gets data for the homepage.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required homepage data in json-string form.
    """
    identity = jwt.decode(request.META.get("HTTP_AUTHORIZATION"), "Temage")['id']
    user = Profile.objects.get(user__id=identity)
    recentpic = user.cards.all()[:2]
    reclist = []
    for card in recentpic:
        card_info = {}
        card_info['title'] = card.product.title
        card_info['imgsrc'] = str(card.product.image_src)
        card_info['promt'] = card.prompt
        card_info['id'] = card.product.id
        reclist.append(card_info)
    collection = user.collection
    cards = collection.cards.all()
    cards_info = []
    for card in cards:
        card_info = {}
        card_info['title'] = card.product.title
        card_info['imgsrc'] = str(card.product.image_src)
        card_info['prompt'] = card.prompt
        card_info['id'] = card.product.id
        cards_info.append(card_info)
    intrests = list(user.theme.all().values('id'))
    cards = Card.objects.filter(product__theme__id=intrests[0]['id'])[:2]
    gallist = []
    for card in cards:
        card_info = {}
        card_info['title'] = card.product.title
        card_info['imgsrc'] = str(card.product.image_src)
        card_info['promt'] = card.prompt
        card_info['id'] = card.product.id
        gallist.append(card_info)
    user_info = {}
    user_info['username'] = user.user.username
    user_info['id'] = user.user.id
    user_info['avator'] = str(user.avator)
    relist = {}
    relist['recent_pics'] = reclist
    relist['collect_pics'] = cards_info
    relist['gallery_pics'] = gallist
    relist['user_info'] = user_info
    return HttpResponse(json.dumps(relist), content_type="application/json")

def work_data(request, work_id):
    """
    This is function that gets data for the work space.
    Parameters:
        work_id - this is a request to data from the front-end.
    Returns:
        required homepage data in json-string form.
    """
    # guess data here
    work = Product.objects.get(id=work_id).html
    allstyle = Style.objects.all().values('name')
    work_data = {}
    work_data['guess_style'] = [{'name' : 'sport','possibility': '80%'},{'name' : 'art','possibility' : '45%'},{'name' : 'history','possibility': '25%'}]
    work_data['style'] = ['style_1','style_2','style_4','style_5','style_6','style_7','style_8','style_9','style_a','style_b','style_c','style_d','style_e','style_f','style_g','style_h','style_i','style_j','style_k','style_l']
    work_data['temage'] = "<html><head> </head> <body> <h1>Hello, Temage!</h1> </body> </html>"
    return HttpResponse(json.dumps(work_data), content_type="application/json")

def gallery_data(request):
    """
    This is function that gets data for the work space.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required homepage data in json-string form.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    cards = Card.objects.all()
    cards_info = []
    if cards.count() > 7:
        cards = cards[:7]

    for card in cards:
        card_info = {}
        user_info = {}
        user_info['username'] = card.creator.user.username
        user_info['id'] = card.creator.user.id
        user_info['avator'] = str(card.creator.avator)
        card_info['id'] = card.product.id
        card_info['creator'] = user_info
        card_info['title'] = card.title
        card_info['imagesrc'] = str(card.product.image_src)
        card_info['head'] = card.head
        card_info['maintext'] = card.prompt
        card_info['foottext'] = card.foot_text
        cards_info.append(card_info)
    return HttpResponse(json.dumps(cards_info), content_type="application/json")

def gallery_more_cards(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    cards = Card.objects.order_by('?')[:4]
    cards_info = []
    for card in cards:
        card_info = {}
        user_info = {}
        user_info['username'] = card.creator.user.username
        user_info['id'] = card.creator.user.id
        user_info['avator'] = str(card.creator.avator)
        card_info['id'] = card.product.id
        card_info['creator'] = user_info
        card_info['imagesrc'] = str(card.product.image_src)
        card_info['title'] = card.title
        card_info['head'] = card.head
        card_info['maintext'] = card.prompt
        card_info['foottext'] = card.foot_text
        cards_info.append(card_info)
    return HttpResponse(json.dumps(cards_info), content_type="application/json")

def post_search(request):
    keywords = json.loads(request.body)['keywords']
    data = {"size": 10, "query": { "bool":{  "should":[{"terms":{"style":keywords.split()}},{"match":{"title": keywords}}]} }}
    response = requests.post(settings.ES_SEARCH_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    ids = []
    res_data = json.loads(response.text)
    for hit in res_data['hits']['hits']:
        ids.append(hit['_source']['ID'])
    cards = Card.objects.filter(id__in = ids)
    cards_info = []
    for card in cards:
        card_info = {}
        user_info = {}
        user_info['username'] = card.creator.user.username
        user_info['id'] = card.creator.user.id
        user_info['avator'] = str(card.creator.avator)
        card_info['id'] = card.product.id
        card_info['creator'] = user_info
        card_info['imagesrc'] = str(card.product.image_src)
        card_info['title'] = card.title
        card_info['head'] = card.head
        card_info['maintext'] = card.prompt
        card_info['foottext'] = card.foot_text
        cards_info.append(card_info)
    return HttpResponse(json.dumps({"cards":cards_info}), content_type="application/json")
    

def collection_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    collection = Profile.objects.get(user__id=identity).collection
    cards = collection.cards.all()
    cards_info = []
    for card in cards:
        user_info = {}
        card_info = {}
        user_info['username'] = card.creator.user.username
        user_info['id'] = card.creator.user.id
        user_info['avator'] = str(card.creator.avator)
        card_info['name'] = card.product.title
        card_info['imagesrc'] = str(card.product.image_src)
        card_info['prompt'] = card.prompt
        card_info['id'] = card.product.id
        card_info['creator'] = user_info
        card_info['title'] = card.title
        cards_info.append(card_info)
    return HttpResponse(json.dumps(cards_info), content_type="application/json")

def recent_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    recentpic = Profile.objects.get(user__id=identity).cards.all()[:4]
    reclist = []
    for pic in recentpic:
        picinfo = {}
        picinfo['title'] = pic.product.title
        picinfo['img_url'] = str(pic.product.image_src)
        picinfo['promt'] = pic.prompt
        picinfo['id'] = pic.product.id
        reclist.append(picinfo)
    return HttpResponse(json.dumps(reclist), content_type="application/json")

def text(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_AUTHORIZATION")
        payload = jwt.decode(token, "Temage")
        identity = payload['id']
        product_id = json.loads(request.body)['id']
        product = Product.objects.get(id=product_id)
        content = {}
        userInfo = {}
        userInfo['username'] = product.creator.user.username
        userInfo['id'] = product.creator.user.id
        userInfo['avator'] = str(product.creator.avator)
        if product.creator.user.id == identity:
            content['can_be_delete'] = 1
        else:
            content['can_be_delete'] = 0
        user = Profile.objects.get(user__id=identity)
        collect = user.collections.get(id=1)
        been_owned = collect.cards.filter(product_id = product_id)
        if been_owned:
            content['has_been_colleted'] = 1
        else:
            content['has_been_collected'] = 0
        content['id'] = product_id
        content['text'] = product.html
        content['creator'] = product.creator
        content['title'] = product.title
        themes = product.theme.all()
        themelist = []
        for theme in themes:
            themelist.append(theme.name)
        content['style'] = themelist
        return HttpResponse(json.dumps(content), content_type="application/json")

def collect(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_AUTHORIZATION")
        payload = jwt.decode(token, "Temage")
        identity = payload['id']
        post_body = json.loads(request.body)
        card_id = post_body['id']
        try:
            user = Profile.objects.get(user__id=identity)
            card = Card.objects.get(product__id=card_id)
            collection = user.collection
            collection.cards.add(card)
            return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")
        except:
            return HttpResponse(json.dumps("failed"), status=400, content_type="application/json")

def delete_product(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        work_id = post_body['workID']
        try:
            product = Product.objects.get(id = work_id)
            product.delete()
            # ES delete start
            # response = requests.post(settings.ES_DELETE_URL, data=json.loads({"query":{"match":{"ID": work_id}}}), headers={"content-type":"application/json"})
            # if response.status_code != 200:
            #     raise RuntimeError('Index has not been deleted!')
            # ES delete end
            return HttpResponse(json.dumps("succeed"), status = 200, content_type = "application/json")
        except:
            return HttpResponse(json.dumps("error"), status = 400, content_type = "application/json")

def cancel_collect(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_AUTHORIZATION")
        payload = jwt.decode(token, "Temage")
        identity = payload['id']

        user = Profile.objects.get(user__id=identity)

        post_body = json.loads(request.body)
        work_id = post_body['id']
        try:
            card = Card.objects.get(product__id=work_id)
            collection = user.collection
            if (collection.cards.filter(product__id=work_id).count() == 0):
                return HttpResponse(json.dumps("This work has already been removed!"), status = 402, content_type = "application/json")
            else:
                card.collections.remove(collection)
                return HttpResponse(json.dumps("Succeed"), status=200, content_type = "application/json")
        except:
            return HttpResponse(json.dumps("Something wrong"), status = 400, content_type="application/json")

####################################################################
# Interfaces for register and login, and also identity authenticate
####################################################################

def login_submit(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        username = post_body['username']
        password = post_body['password']
        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            return HttpResponse(status=400)
        if user:
            payload = {
                'id': user.id,
                'name': user.username,
            }
            return HttpResponse(jwt.encode(payload, "Temage"),
                                status=200,
                                content_type="application/json"
                                )

def JWTauthenticate(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        payload = jwt.decode(post_body['token'], "Temage")
        try:
            user = User.objects.get(id=payload['id'])
        except:
            return HttpResponse(status=400)
        else:
            return HttpResponse(
                json.dumps({"username":user.username}),
                status=200,
                content_type="application/json"
                )

def register(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        user = Profile.objects.filter(user__username=post_body['username'])
        if user.count() == 0:
            password = post_body['password']
            username = post_body['username']
            interests = post_body['interest']
            user = User.objects.create_user(username=username, password=password)
            profile = Profile.objects.create(user=user)
            for interest in interests:
                theme = Theme.objects.get(name=interest)
                profile.theme.add(theme)

            avator = open("../test_file/img/boy.jpg", "rb")
            profile.avator.save('boy.jpg', File(avator), save=True)
            return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")
        else:
            return HttpResponse(json.dumps("The username has been used"),
                                status=400,
                                content_type="application/json"
                                )

##########################
# Interface for workflow
##########################
def pic_post(request): # 需完善
    """
    Get pictures from users, and send them to the models.
    """
    
    return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")

def text_post(request): # 需完善
    """
    Get text content from users, and send it with the pictures
    """

    return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")

def ret_html(request): # 需完善
    # 会有styles需要接收
    content = {}
    content['html'] = result_html
    return HttpResponse(json.dumps(content), content_type="application/json")

def store_passage(request):
    if request.method == 'POST':
        # token = request.META.get("HTTP_AUTHORIZATION")
        # payload = jwt.decode(token, "Temage")
        # identity = payload['id']
        identity = 2
        post_body = json.loads(request.body)
        user = Profile.objects.get(user__id=identity)
        style_names = post_body['styles']
        html = post_body['res_html']
        title = post_body['title']
        width = post_body['t_width']
        score = 0
        # only for test
        style = Style.objects.get(name=style_names[0])
        product = Product.objects.create(title=title, html=html, creator=user, style=style, score=score, width=width)
        
        # for style_name in style_names:
        #     style = Theme.objects.get(name=style_name)
        #     product.theme.add(style)

        # store htmlfile
        file_name = "html_" + str(product.id) + ".html"
        product.html_file.save(file_name, ContentFile(html))

        content = {}
        content['ID'] = product.id
        
        # ES index create start
        index_data = {"title":title, "style":style_names, "ID": product.id}
        res = requests.post(settings.ES_CREATE_URL, 
                        headers = {'content-Type': 'application/json'},
                        data = json.dumps(index_data)
                    )
        if res.status_code != 201:
            raise RuntimeError("The ES index has not been updated, please start ES server or check the post data")
        # ES index create end

        return HttpResponse(json.dumps(content), status = 200, content_type = "application/json")

def finished_work(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        work_id = post_body['workID']
        work = Product.objects.get(id=work_id)
        width = work.width
        url = work.html_file.url
        content = {}
        content['url'] = url
        content['width'] = width
        return HttpResponse(json.dumps(content), content_type = "application/json")

def download(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        work_id = post_body['workID']
        # 生成长图
        img_name = "boy.jpg"
        url = "/media/img/pimg/" + str(img_name)
        content = {}
        content['url'] = url
        return HttpResponse(json.dumps(content), content_type = "application/json")

    return HttpResponse(json.dumps(""), content_type = "application/json")

def confirm_store(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        work_id = post_body['workID']
        stars = post_body['stars']
        try:
            product = Product.objects.get(id = work_id)
            product.is_finished = 1
            product.score = stars
            return HttpResponse(json.dumps("succeed"), status = 200, content_type = "application/json")
        except:
            return HttpResponse(json.dumps("error"), status = 400, content_type = "application/json")

