''' 
#设计trigger pipeline
example 命令
#全局变量, 可以用来拼接全局参数
env:
    is_debug=False
    skip_nir=False
    print=true      #如果为true,则只打印curl command 不execute
    
    --form variables[IS_DEBUG]=9999
    xx.sh projectName [otherparam: --branch=xx jobname=xx version=xx ]
---pipeline/job---
    xx.sh projectName [otherparam: --job=retry --jobId=xxx ]      #这里branch其实用不上, 可以作用replaceRegex 操作 移除branch参数的拼接

三种情况
1.trigger common
    number
2.trigger component
    job_name
3.trigger release
    target_relase
    version
    #其实用不到projectId, 但是需要projectName, 所以设计数组上必须,projectName命名必须和release的projectName一致.
必须参数:
    CI_JOB_NAME=scripts
    ref=NSI-r24.2
    token=projectToken
    
common参数:
    IS_DEBUG
    SKIP_NIR
    SKIP_CN_NIR
    PIPELINE_CANCELD
    CT_TEST
    FT_TEST
    

自定义参数:
    print   #only print but not excute curl command

---其他情况---
cancel job /retry job/cancel pipeline/delete pipelin
    必须参数: private-token, projectId, pipelineId, jobId, 

'''