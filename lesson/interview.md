## 软件测试面试总结
- 这里提供的测试总结经验

 

## 一个网站怎么测试
- 第一阶段：
    - 需求分析：需求文档规格 产品原型图等
    - 测试计划：周期 功能模块划分
    - 测试策略：功能模块划分 单元测试|接口测试|自动化测试|性能测试的比例
    - 用例编写: 接着开始写测试用例 范围有功能测试 ui测试 专项测试：性能 安全 兼容性等
- 第二阶段：开展测试，记录bug，合理安排 
 
    - 功能测试：
      - 
    - 专项测试：
      - 数据库安全测试 sql注入|xss攻击
      - 性能测试
      - 压力测试
      - 兼容性测试

 
-  第三阶段测试评审和总结


## 数据库
 - mysqldump -p  -n 
 - DML:
    - select
    - update
    - delete
    - group by | having | order by
    - limit offset
    - left join | right join | inner join
 - DDL:
 - 存储引擎 : innodb | mysiam
 - binlog: 
 - 索引 二叉树 主键|联合 
 - 锁： 行锁 | 表锁
 - 视图：
 - mysql性能调优：sql语句 正确索引 
 - 分库分表：水平|垂直-分库分表
 - Nosql： memcache redis mongodb
 - 消息中间件： Kafka|RabbitMQ

 ## linux命令
  - 文件： cat find head less more tail 
  - 进程： ps aux/ef  | grep 
  - 网络： netstat lsof ping
  - 日志： less view tail head  
  - 三剑客：grep sed awk
  - 三剑客nginx的日志分析实战
  - bash编程 写一个抽奖程序实战
  -
    -读出文件
    -- #！/bin/bash
    random(){
       ##取出了所有的人
      local  seeds = `while read line;do echo $line; <$tmp.txt `
      local count = 0
      while [[ $count != 1 ]];do
        #从seeds中筛选一部分人出来
          seeds=`for seed in $seeds;do (($RANDOM%2)) && echo $seed;done`
          count=`echo "$seeds" | wc -l`
      done
      echo $seeds
    }

    result() {
      ####从随机的一个结果中遍历10个出来
      for i in {1..10};do
        tmp=`random`
        while [[ `is_repeat $tmp` == 0 ]];do
          tmp=`random`
          done
          arrs[$i]=$tmp
      done
      echo ${arrs[@]}
    }

    is_repeat(){
      for arr in ${arrs[@]};do
          if [[ $arr == $1 ]];then
            echo 0;
            return 0;
          fi
      done
      echo 1;
    }


  - 分析nginx日志文件
  - cat access.log | awk '{print $1}' | sort 排序 | uniq去重 -c | sort -nr 倒续 | head -3
  - cat access.log| grep -o '^[0-9]*.[0-9]*.[0-9]*.[0-9]*' | sort | uniq -c | sort -nr | head -3
  - cat access.log | awk '$9~/404|500/' | wc -l

  







