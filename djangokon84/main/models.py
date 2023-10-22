#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class bingren(BaseModel):
    __doc__ = u'''bingren'''
    __tablename__ = 'bingren'

    __loginUser__='bingrenzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='bingrenzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    bingrenzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='病人账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    bingrenxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='病人姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    bingrendianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='病人电话' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    '''
    bingrenzhanghao=VARCHAR
    mima=VARCHAR
    bingrenxingming=VARCHAR
    xingbie=VARCHAR
    bingrendianhua=VARCHAR
    touxiang=VARCHAR
    '''
    class Meta:
        db_table = 'bingren'
        verbose_name = verbose_name_plural = '病人'
class yisheng(BaseModel):
    __doc__ = u'''yisheng'''
    __tablename__ = 'yisheng'

    __loginUser__='yishengzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yishengzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yishengzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='医生账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yishengxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='医生姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    yishengdianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='医生电话' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    '''
    yishengzhanghao=VARCHAR
    mima=VARCHAR
    yishengxingming=VARCHAR
    xingbie=VARCHAR
    yishengdianhua=VARCHAR
    touxiang=VARCHAR
    '''
    class Meta:
        db_table = 'yisheng'
        verbose_name = verbose_name_plural = '医生'
class keshixinxi(BaseModel):
    __doc__ = u'''keshixinxi'''
    __tablename__ = 'keshixinxi'



    __authTables__={'yishengzhanghao':'yisheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yiyuanmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='医院名称' )
    keshibianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='科室编号' )
    keshileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='科室类型' )
    keshimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='科室名称' )
    keshijieshao=models.TextField   (  null=True, unique=False, verbose_name='科室介绍' )
    guahaofei=models.IntegerField  (  null=True, unique=False, verbose_name='挂号费' )
    tupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    yishengzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='医生账号' )
    yishengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='医生姓名' )
    paibanbiao=models.TextField   (  null=True, unique=False, verbose_name='排班表' )
    '''
    yiyuanmingcheng=VARCHAR
    keshibianhao=VARCHAR
    keshileixing=VARCHAR
    keshimingcheng=VARCHAR
    keshijieshao=Text
    guahaofei=Integer
    tupian=VARCHAR
    yishengzhanghao=VARCHAR
    yishengxingming=VARCHAR
    paibanbiao=Text
    '''
    class Meta:
        db_table = 'keshixinxi'
        verbose_name = verbose_name_plural = '科室信息'
class keshileixing(BaseModel):
    __doc__ = u'''keshileixing'''
    __tablename__ = 'keshileixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    keshileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='科室类型' )
    '''
    keshileixing=VARCHAR
    '''
    class Meta:
        db_table = 'keshileixing'
        verbose_name = verbose_name_plural = '科室类型'
class guahaoyuyue(BaseModel):
    __doc__ = u'''guahaoyuyue'''
    __tablename__ = 'guahaoyuyue'



    __authTables__={'yishengzhanghao':'yisheng','bingrenzhanghao':'bingren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    guahaobianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='挂号编号' )
    keshimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='科室名称' )
    keshileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='科室类型' )
    yishengzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='医生账号' )
    yishengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='医生姓名' )
    guahaofei=models.FloatField   (  null=True, unique=False, verbose_name='挂号费' )
    guahaoshijian=models.DateField   (  null=True, unique=False, verbose_name='挂号时间' )
    bingrenzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='病人账号' )
    bingrenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='病人姓名' )
    beizhu=models.TextField   (  null=True, unique=False, verbose_name='备注' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    guahaobianhao=VARCHAR
    keshimingcheng=VARCHAR
    keshileixing=VARCHAR
    yishengzhanghao=VARCHAR
    yishengxingming=VARCHAR
    guahaofei=Float
    guahaoshijian=Date
    bingrenzhanghao=VARCHAR
    bingrenxingming=VARCHAR
    beizhu=Text
    sfsh=VARCHAR
    shhf=Text
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'guahaoyuyue'
        verbose_name = verbose_name_plural = '挂号预约'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='收藏id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收藏名称' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收藏图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型(1:收藏,21:赞,22:踩)' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=VARCHAR
    type=VARCHAR
    inteltype=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告资讯'
