from framework_common.manshuo_draw.core.deal_img import *
import asyncio
import copy


async def manshuo_draw(json_img):
    json_img=copy.deepcopy(json_img)
    json_img=json_check(json_img)   #检查并补正输入的参数
    img_path=await deal_img(json_img)
    return img_path

if __name__ == '__main__':

    """
        定义一个json和内容文件，方便后续进行调试维护,并在此处阐明各个标签的用途
    :type:表示该组件的类型，如text表示文字，img表示图片，avatar表示头像
    :content:表示该组件的内容，如文本内容，图片地址，头像地址
    :font:表示字体类型，如default表示默认字体
    :color:表示字体颜色，如#000000表示黑色
    :size:表示字体大小，如24表示24号字体
    :padding_ahind:表示该组件与上一个组件之间的距离
    :padding_with:表示内容与内容之间的距离
    :img:表示图片地址，如https://i.imgur.com/5y9y95L.jpg
    :label:表示图片标签，如['标签1','标签2']
    :label_color:表示标签颜色，如#000000表示黑色
    :number_per_row:表示每行显示的图片数量，如1表示一行显示一个图片
    :is_crop:表示是否裁剪图片，如True表示裁剪图片为一个正方形
    """
    contents=[
        {'type': 'basic_set', 'debug': True},

        {'type': 'backdrop', 'subtype': 'gradient'},

        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg'],'upshift_extra':25,'layer':2,
         'content':[ {'name': '漫朔_manshuo', 'time': '2025年 05月27日 20:32'}] },

        {'type': 'img', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg'],
         'label': ['BiliBili', 'dy', 'manshuo'],'layer':3,},

        {'type': 'img', 'subtype': 'common_with_des_right', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg'],
         'content': ['这里是manshuo[title]！这部分是测manshuo！[/title]这manshuo！[des]这里是介绍[/des]'],'layer':4, },
    ]

    contents2=[
        {'type': 'basic_set', 'debug': True,'img_width':1500,'img_height':1000,},

        {'type': 'backdrop', 'subtype': 'gradient'},

        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg'],'upshift_extra':25,'layer':1,
         'content':[ f"[name]今日发言排行榜[/name]\n[time]2025年 05月27日 20:32[/time]"] },
        {'type': 'img', 'subtype': 'common_with_des_right', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg',
                                                        f"https://q1.qlogo.cn/g?b=qq&nk=1280433782&s=640",
                                                        f"https://q1.qlogo.cn/g?b=qq&nk=3552663628&s=640",
                                                        f"https://q1.qlogo.cn/g?b=qq&nk=2702495766&s=640",
                                                        f"https://q1.qlogo.cn/g?b=qq&nk=1687148274&s=640",
                                                        f"https://q1.qlogo.cn/g?b=qq&nk=1124901768&s=640",
                                                        f"https://q1.qlogo.cn/g?b=qq&nk=2319804644&s=640"],
         'content': [f"[title]漫朔_manshuo[/title]这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]这部分是测manshuo！",
                     f"[title]漫朔_manshuo[/title]这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]这部分是测manshuo！",
                     f"[title]漫朔_manshuo[/title]这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]这部分是测manshuo！",
                     f"[title]漫朔_manshuo[/title]这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]这部分是测manshuo！",
                     f"[title]漫朔_manshuo[/title]这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]这部分是测manshuo！",
                     f"[title]漫朔_manshuo[/title]这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]这部分是测manshuo！",
                     f"[title]漫朔_manshuo[/title]这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]这部分是测manshuo！",
                     ], 'number_per_row': 2,
         },
        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg',f"https://q1.qlogo.cn/g?b=qq&nk=1280433782&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=3552663628&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=2702495766&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=1687148274&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=1124901768&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=2319804644&s=640"],
         'content': [f"[name]漫朔_manshuo[/name]\n[time]发言次数：230次[/time]","[name]荔枝[/name]\n[time]发言次数：215次[/time]","[name]test[/name]\n[time]发言次数：205次[/time]","[name]荔枝[/name]\n[time]发言次数：215次[/time]","[name]荔枝[/name]\n[time]发言次数：215次[/time]","[name]荔枝[/name]\n[time]发言次数：215次[/time]","[name]荔枝[/name]\n[time]发言次数：215次[/time]","[name]荔枝[/name]\n[time]发言次数：215次[/time]"],'number_per_row':2,
         'background':['framework_common/manshuo_draw/data/cache/manshuo.jpg',f"https://q1.qlogo.cn/g?b=qq&nk=1280433782&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=3552663628&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=2702495766&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=1687148274&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=1124901768&s=640",f"https://q1.qlogo.cn/g?b=qq&nk=2319804644&s=640"],
         },

    ]

    contents_not=[{'type': 'basic_set', 'debug': True},
        'https://avatars.fastly.steamstatic.com/93947d71b3900b1bb1a5144d62a9af99a4338bba_full.jpg',
        'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1329410/capsule_184x69.jpg'
        ]


    contentsWithNoTag=[
        {'type': 'basic_set', 'debug': True,'img_width':1000,'img_height':980,'max_num_of_columns':4},
        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg'],'layer':1,
         'content': [f"[name]漫朔_manshuo[/name]\n[time]2025年 05月27日 20:32[/time]"]},
        '这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]',
        ['framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg',
         'framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg',
         'framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg',],
        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg'],
         'content': [f"[name]漫朔_manshuo[/name]\n[time]2025年 05月27日 20:32[/time]"]},
        ['framework_common/manshuo_draw/data/cache/manshuo.jpg', 'framework_common/manshuo_draw/data/cache/manshuo.jpg',
         'framework_common/manshuo_draw/data/cache/manshuo.jpg', ],
        '这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]',
        {'type': 'img', 'subtype': 'common_with_des_right','img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg'],'label':['BiliBili'],'layer':2,
         'content': ['这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]']},
        {'type': 'img', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg'],'layer':3,
         'content': ['葬送的芙莉莲\n5星','败犬女主太多啦\n4.5星',]
         },
        '这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]',
        {'type': 'img', 'subtype': 'common_with_des','img': ['https://gal.manshuo.ink/usr/uploads/2025/02/1709218403.png'], 'label': ['BiliBili'],'layer':5,
         'content': ['这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]']},
    ]

    games_content=[
        {'type': 'basic_set', 'debug': True, 'img_width': 1500,'img_height':1000},
        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg',
                                                      'https://gal.manshuo.ink/usr/uploads/2025/02/1709218403.png'],
         'content': [f"[name]漫朔_manshuo[/name]\n[time]2025年 05月27日 20:32[/time]",
                     f"[name]galgame[/name]\n[time]2025年 05月27日 20:32[/time]"],
         'background': ['framework_common/manshuo_draw/data/cache/manshuo.jpg',
                        'https://gal.manshuo.ink/usr/uploads/2025/02/1709218403.png'], },
        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg','framework_common/manshuo_draw/data/cache/manshuo.jpg'],
         'upshift_extra': 0,'layer':5,
         'content': [f"[name]漫朔_manshuo[/name]\n[time]2025年 05月27日 20:32[/time]",f"[name]漫朔_manshuo[/name]\n[time]2025年 05月27日 20:32[/time]"],
         'type_software': 'bilibili', },
        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg',
                                                        'https://gal.manshuo.ink/usr/uploads/2025/02/1709218403.png'],
         'content': [f"[name]漫朔_manshuo[/name]\n[time]2025年 05月27日 20:32[/time]",
                     f"[name]galgame[/name]\n[time]2025年 05月27日 20:32[/time]"],
         'background': ['framework_common/manshuo_draw/data/cache/manshuo.jpg',
                        'https://gal.manshuo.ink/usr/uploads/2025/02/1709218403.png'], },
        '这部分是测manshuo！\n这manshuo！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试！这里是测试\n[des]这里是介绍[/des]',
        {'type': 'avatar', 'subtype': 'common', 'img': ['framework_common/manshuo_draw/data/cache/manshuo.jpg',
                                                        'https://gal.manshuo.ink/usr/uploads/2025/02/1709218403.png'],
         'content': [f"[name]漫朔_manshuo[/name]\n[time]2025年 05月27日 20:32[/time]",
                     f"[name]galgame[/name]\n[time]2025年 05月27日 20:32[/time]"],
         'background': ['framework_common/manshuo_draw/data/cache/manshuo.jpg',
                        'https://gal.manshuo.ink/usr/uploads/2025/02/1709218403.png'], },
    ]




    asyncio.run(manshuo_draw(contents2))
    #asyncio.run(manshuo_draw(contents_not))