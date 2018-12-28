# 网页版设计

### 接口设计

1. 登录
    - 接口地址： idiomgamelogin
    - 请求方式： POST
    - 参数：  
        - username: 用户名
        - password: 密码
    - 调用成功： 跳转到 idiomgamestart
    - 备注： 无
    - 网页： 登录网页
    
2. 主游戏界面
    - 接口地址： idiomgamestart
    - 请求方式： GET
    - 参数： 无，通过session跟踪用户
    - 调用成功： 无操作
    - 备注： 返回的网页中包含关卡数据，前端JS代码使用此数据初始化关卡
    - 网页： 游戏网页

3. 获取关卡数据
    - 接口地址： idiomgamerounddata
    - 请求方式： GET
    - 参数： 
        - roundnum: 关卡序号
    - 调用成功： 返回关卡JSON数据，前端使用此数据刷新界面
    - 备注： 无
    - 网页： 无

4. 更新用户通关数
    - 接口地址： idiomgameupdatauserrnd
    - 请求方式： POST
    - 参数： 
        - roundnum: 已完成关卡序号
    - 调用成功： 返回成功码 UPDATA_OK
    - 备注： 参数中不包含用户信息，使用session跟踪
    - 网页： 无

### 错误码
- 通用
    1. 任务成功 TASK_SUCCESS 101
    2. 任务失败 TASK_FAIL -101
    
