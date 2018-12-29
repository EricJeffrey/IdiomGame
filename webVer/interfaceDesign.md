# 网页版设计

### 接口设计

1. 登录页面
    - 接口地址： idiomgamelogin
    - 请求方式： GET
    - 参数： 无
    - 成功操作： 返回登录网页
    - 备注： 无
    - 返回网页： 登录网页

1. 执行登录
    - 接口地址： idiomgamedologin
    - 请求方式： POST
    - 参数：  
        - username: 用户名
        - password: 密码
    - 成功操作： 返回成功码，前端跳转到 idiomgamestart
    - 备注： 无
    - 返回网页： 无

1. 注册页面
    - 接口地址： idiomgameregister
    - 请求方式： GET
    - 参数： 无
    - 成功操作： 返回注册网页
    - 备注： 无
    - 返回网页： 注册网页

1. 执行注册
    - 接口地址： idiomgamedoregister
    - 请求方式： POST
    - 参数： 
        - username: 用户名
        - password: 密码
    - 调用成功： 返回成功码，前端自动跳转登录
    - 备注： 无
    - 网页： 无

1. 主游戏界面
    - 接口地址： idiomgamestart
    - 请求方式： GET
    - 参数： 无，通过session跟踪用户
    - 成功操作： 无操作
    - 备注： 返回的网页中包含关卡数据，前端JS代码使用此数据初始化关卡
    - 返回网页： 游戏网页

1. 获取关卡数据
    - 接口地址： idiomgamerounddata
    - 请求方式： GET
    - 参数： 
        - roundnum: 关卡序号
    - 成功操作： 返回关卡JSON数据，前端使用此数据刷新界面
    - 备注： 无
    - 返回网页： 无

1. 更新用户通关数
    - 接口地址： idiomgameupdatauserrnd
    - 请求方式： POST
    - 参数： 
        - roundnum: 已完成关卡序号
    - 成功操作： 返回成功码 UPDATA_OK
    - 备注： 参数中不包含用户信息，使用session跟踪
    - 返回网页： 无


### 错误码
- 通用
    1. 任务成功 TASK_SUCCESS 101
    2. 任务失败 TASK_FAIL -101
    
