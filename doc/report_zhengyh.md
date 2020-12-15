# 基于深度学习的通信领域应用
    
    了解到有个课题组在将 Model-driven DL 引入无线物理层收发机各个模块，我从他们的引用里我找到一些论文，总结如下：

        1. 传统的深度学习基于海量数据来训练，但是通信领域的数据并不是那么理想，所以就引入了专家系统和特征工程，以先验的知识来提升模型。

        我是觉得这样挺没劲的:( 
        之所以要用深度学习不就是为了让机器自己来提取特征就是不想做专家系统啊

        2. 自编码器
            用于 OFDM 的调制
            用来做数据压缩/降维

        3. 用于导频信号的处理，还没看的很明白
        
#### papers:
    [1] Z. Xu and J. Sun, “Model-Driven Deep-Learning,” National Sci. Rev., vol. 5, no. 1, 2018, pp. 22–24.
    [2] H. T. He, S. Jin, C.-K. Wen, F. Gao, G. Y. Li, and Z. Xu, “Model-driven deep learning for physical layer communications”, IEEE Wireless Communications, vol. 26, no. 5, pp. 77-83, Oct. 2019.
    [3] H. T. He, C.-K. Wen, S. Jin, and G. Y. Li, “Deep learning-based channel estimation for beamspace mmWave massive MIMO systems,” IEEE Wireless Commun. Lett, vol. 7, no. 5, pp. 852–855, Oct. 2018. 
    [4] H. T. He, R. Wang, S. Jin, C.-K. Wen and G. Y. Li, “Beamspace channel estimation in Terahertz communications: A model-driven unsupervised learning approach,” 2020, arXiv:2006.16628.
    [5] H. T. He, C.-K. Wen, S. Jin, and G. Y. Li, “Model-driven deep learning for MIMO detection,” IEEE Trans. Signal Process, vol. 68, pp. 1702–1715, Mar. 2020.
# MOOC数据集
    发觉用户历史数据和物联网的数据其实有共通之处，都由序列型的数据和分类数据组成，对于其中的序列型数据，可以采用循环神经网络如LSTM等处理，而对于分类数据采用其它网络。
    突然明白为什么那些人对于一个任务要堆砌各种各样的模型再加权出结果。
    因为一个现实的任务一般是复杂的，没有模型可以适应任意类型的数据。针对不同数据要采用合适的模型。

    对于mooc和物联网数据里的序列，我采用LSTM模型来预测后n个时刻的值，之前没有了解过序列模型，现在差不多看明白了，正在预处理的阶段。

    aaai那篇的源码 闫娜学姐正在调试
    
# 物联网数据日志
# 20201120
## 对 LSTM结构的进一步理解  
###    example： 
####        训练集 ：10篇文章
####        重复训练集次数： epoch = n_e
####        每次输入模型的词语数量： num_words = n_w
####        每次权重更新消耗的句子数量： batch_sizes = n_b
###    重点： 
#### 1. 每次输入模型的词语数量
    不同的场景下，上下文依赖程度不同，每次输入模型的词语数量要能准确表达句意,num_words 大小的选取是重点，否则每次模型都在 '断章取义'
#### 2. 反向传播
    全连接网络的权值是从最后一层隐含层向前一层的节点传递，但是像LSTM这样的循环神经网络，如果以相同的表述，本节点的上一层节点其实是上一时刻的本节点。

    导致循环神经网络反向传播的细节上和全连接网络不同，被称为backpropagation through time, BPTT。
    link: https://ilewseu.github.io/2017/12/30/RNN%E7%AE%80%E5%8D%95%E6%8E%A8%E5%AF%BC/

# 20201119
## 面向时间序列模型进行预处理
   
    序列网络的训练数据只包含告警序列，不包含设备位置等数据

## Question  CLOSED
    对于RNN LSTM等序列模型有一个问题待解决:

        Q：对于多序列的序列预测 在训练时同一时间上的多个序列是否会相互影响?
            会影响到训练数据的选择是否要保留设备id地理信息等数据
        answer:
            不保留
            对于网络来说，只是对输入的数据进行适应调整自身的权值，LSTM等序列网络是基于序列的历史行为的 区别在于对于历史的记忆强弱和记忆方式 
           
                
        solution： 
            1. 将多维序列输入网络 先试试这个
            2. 对于多维序列进行编码（类似embedding），降维到单变量序列，再对预测出的序列进行解码，还原多变量序列

# 20201115
    12-14日代码丢失 
    现在看来写的也是垃圾丢了就丢了 20201120

## 基于treelib库建立了区域层级的树结构
    预计区域的融合告警会基于树来实现
## 封包了几个基于本数据集的预处理class
    20% 