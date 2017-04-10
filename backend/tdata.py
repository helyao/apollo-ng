import hashlib

md = hashlib.md5()

def getmd5(passwd):
    md.update(passwd.encode('utf-8'))
    return md.hexdigest()

plane = [
    {
        'id': 'A001',
        'type': '4-axis',
        'load': 'Neo-X1',
        'lens': [
            {'type': 'IR'},
            {'type': 'Star'}
        ],
        'lng': 39.500000,
        'lat': 116.500000,
        'duration': 32,
        'own': '020'
    },
    {
        'id': 'F001',
        'type': 'fixed-wing',
        'load': 'Neo-2',
        'lens': [
            {'type': 'White'},
            {'type': 'IR'}
        ],
        'lng': 39.500000,
        'lat': 116.500000,
        'duration': 120,
        'own': '021'
    },
    {
        'id': 'F002',
        'type': 'fixed-wing',
        'load': 'Neo-1',
        'lens': [
            {'type': 'White'}
        ],
        'lng': 39.500000,
        'lat': 116.500000,
        'duration': 150,
        'own': '020'
    },
    {
        'id': 'A002',
        'type': '4-axis',
        'load': 'Neo-X1',
        'lens': [
            {'type': 'Star'}
        ],
        'lng': 39.500000,
        'lat': 116.500000,
        'duration': 42,
        'own': '020'
    },
    {
        'id': 'A003',
        'type': '6-axis',
        'load': 'Neo-2',
        'lens': [
            {'type': 'White'},
            {'type': 'IR'}
        ],
        'lng': 39.500000,
        'lat': 116.500000,
        'duration': 42,
        'own': '020'
    },
]

task = [
    {
        'id': 'T2017031601',
        'point': [
            {
                'lng': 39.800000,
                'lat': 116.800000
            },
            {
                'lng': 39.900000,
                'lat': 116.900000
            },
            {
                'lng': 39.700000,
                'lat': 116.700000
            }
        ],
        'plane': 'A001',
        'load': 'Neo-X1',
        'captain': '0303',
        'manager': '020',
        'state': 'finish',
        'record': '',
        'otime': '2017-03-16 10:25:26',
        'ftime': '2017-03-18 14:41:12'
    },
    {
        'id': 'T2017031601',
        'point': [
            {
                'lng': 39.800000,
                'lat': 116.800000
            },
            {
                'lng': 39.900000,
                'lat': 116.900000
            },
            {
                'lng': 39.700000,
                'lat': 116.700000
            }
        ],
        'plane': 'F001',
        'load': 'Neo-X1',
        'captain': '0301',
        'manager': '021',
        'state': 'going',
        'record': '',
        'otime': '2017-03-17 14:21:21',
        'ftime': ''
    }
]

person = [
    {
        'id': '010',
        'identity': 'admin',
        'username': 'helyao',
        'password': getmd5('welcome')
    },
    {
        'id': '020',
        'identity': 'manager',
        'username': 'jack',
        'password': getmd5('jack')
    },
    {
        'id': '021',
        'identity': 'manager',
        'username': 'lucy',
        'password': getmd5('lucy')
    },
    {
        'id': '0300',
        'identity': 'capiture',
        'username': 'anna',
        'password': getmd5('anna')
    },
    {
        'id': '0301',
        'identity': 'capiture',
        'username': 'mike',
        'password': getmd5('mike')
    },
    {
        'id': '0302',
        'identity': 'capiture',
        'username': 'tomas',
        'password': getmd5('tomas')
    },
    {
        'id': '0303',
        'identity': 'capiture',
        'username': 'lily',
        'password': getmd5('lily')
    }
]

image = [
    {
        'lng': 39.800000,       # 图片位置信息 lng - 纬度
        'lat': 116.800000,      # 图片位置信息 lat - 经度
        'time': '2017-03-18 14:36:32',  # 图片时间戳
        'task': 'T2017031601',  # 该照片所属的任务编号
        'plane': 'A001',    # 所使用的飞机型号
        'load': 'Neo-X1',   # 所使用的吊舱
        'lens': 'Star',     # 图片拍摄所使用的机芯
        'captain': '0303',  # 飞手编号
        'manager': '020',   # 负责人编号
        'image': 'history/T2017031601/1.jpg',   # 图片存放路径
        'remark': ''        # 备注
    },
    {
        'lng': 39.800000,
        'lat': 116.800000,
        'time': '2017-03-18 14:36:32',
        'task': 'T2017031601',
        'plane': 'A001',
        'load': 'Neo-X1',
        'lens': 'Star',
        'captain': '0303',
        'manager': '020',
        'image': 'history/T2017031601/2.jpg',
        'remark': ''
    },
    {
        'lng': 39.800000,
        'lat': 116.800000,
        'time': '2017-03-18 14:36:32',
        'task': 'T2017031601',
        'plane': 'A001',
        'load': 'Neo-X1',
        'lens': 'Star',
        'captain': '0303',
        'manager': '020',
        'image': 'history/T2017031601/3.jpg',
        'remark': ''
    },
    {
        'lng': 39.800000,
        'lat': 116.800000,
        'time': '2017-03-18 14:36:32',
        'task': 'T2017031601',
        'plane': 'A001',
        'load': 'Neo-X1',
        'lens': 'IR',
        'captain': '0303',
        'manager': '020',
        'image': 'history/T2017031601/4.jpg',
        'remark': ''
    },
    {
        'lng': 39.800000,
        'lat': 116.800000,
        'time': '2017-03-18 14:36:32',
        'task': 'T2017031601',
        'plane': 'A001',
        'load': 'Neo-X1',
        'lens': 'Star',
        'captain': '0303',
        'manager': '020',
        'image': 'history/T2017031601/5.jpg',
        'remark': ''
    }
]