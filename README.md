
# Happy3boy

### 文件说明

训练集 data/BoP2017-DBQA.train.txt

验证集 data/BoP2017-DBQA.dev.txt

https://pan.baidu.com/s/1eSlAFPC 提取码 6acs

词向量结果文本文件 vector_train.txt 和 vector_dev.txt

词向量结果二进制文件 vector_train.bin 和 vector_dev.bin

更新：**vector.bin**，question_document.txt生成

分词结果 segmentation_results_train.txt 和 segmentation_results_train.txt

### 数据预处理

1. 分词
2. word2vec

### 问题答案匹配

### 已更新分词结果 在压缩文件内
segmentation.rar

### 文本处理代码与处理结果
链接: http://pan.baidu.com/s/1nuGos33 密码: 86bw

github有毒，传不了大文件

处理文件的代码已上传


### 资格赛任务题评价指标

Mean Reciprocal Rank(MRR)
 
|Q|表示评比数据集中问题的总数量，也是文档的总数量。

ranki表示对于第i个问题Qi，Qi的最优回答在答案集合Ci[2]中对应的实数值所排的顺序位。

例如表格2中，Q1“中国第一所职业学校成立的时间？”的最优回答是第3个句子，在表格3的

提交结果中第3个句子的实数值是1.2384834，它排在C1中第1位，因此 rank1=1。

以此类推第i个问题的ranki。特别的，如果Ci没有覆盖标注的答案，那么1/ranki=0。

### Baseline 已完成  代码已更新  数据已上传

baseline数据地址：

链接: https://pan.baidu.com/s/1c3ZKzO 密码: ctab

工作流：

文本处理包括：

1） 分割问题与文章 ， 去除 【0】【1】 label

2） 根据1） 的问题和文章内容构建vector表， 

### 建model

大致思想源头来自：

http://cs.umd.edu/~miyyer/pubs/2014_qb_rnn.pdf

http://cs.umd.edu/~miyyer/data/deepqa.pdf

https://github.com/miyyer/dan

上面的文章，代码都讲了 问答系统， quiz bowl 测试

和我们要做的东西很像，我觉得方向大致也是这样的

主要的思路是：

1） 先分好对应的文章与问题（本步已完成）

2） 然后把文章处理一遍（主要是文本里面的代词全都用名词换回去）

3） 然后建立一个像知识库一样的东西

4） 再按照上面文章里写的建一个table（关联度）

5） 从表中查询每句文章与问题的关联性即预测结果

我先看代码 。。

新发现：

https://medium.com/@devnag/pointer-networks-in-tensorflow-with-sample-code-14645063f264
