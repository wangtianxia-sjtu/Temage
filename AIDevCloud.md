# AI Devcloud
## 新建任务

```shell
touch your_task
vim your_task
# modify your_task as below

# 第一行一定要写 cd $PBS_O_WORKDIR
cd $PBS_O_WORKDIR
python wtx_textCNN.py
python ...
python ...
# an empty comment 最后一行一定要是注释

```

## 提交任务

```shell
qsub your_task -l walltime=24:00:00 -o <path_to_stdout_file> -e <path_to_stderr_file>
# -o -e redirect output and error (not neccessarily needed) default output in XXXX.o<任务号> error in XXXX.e<任务号>
```

## 查看任务
```shell
qstat
qstat -f
```
## 取消任务
```shell
qdel <任务号>
```

## 查看集群信息
```shell
pbsnodes
# 查看有多少节点free
pbsnodes | grep "state = free" | wc -l
```
