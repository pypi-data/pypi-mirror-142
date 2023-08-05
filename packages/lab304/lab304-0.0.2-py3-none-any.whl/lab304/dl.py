import os
import re
import time
import random

from matplotlib import pyplot as plt


def isrepeated(path, mark='-dup'):
    """ 假如保存的文件重名，则在名字后面增加 “-dup” """
    while os.path.exists(path):
        dir_ = re.findall("(.*)\.", path)
        file_type = re.findall("(\.[a-z].*)", path)
        path = os.path.join(dir_[0] + mark + file_type[0])
    return path


def grid_search(trainer, param, test=False):
    """
    网格搜索，trainer: 需要运行的文件名， param: 指定的超参数范围
    示例：
        param = {'lr': [0.01, 0.001, 0.0001]}
        grid_search('main.py', param)
    """
    trainer = 'python ' + trainer
    keys, trainers, midtrainers = [], [], [trainer]
    dim = 1
    for key in param.keys():
        keys.append(key)
        dim *= len(param[key])
    for trainer in midtrainers:
        reset = trainer
        for key in param.keys():
            for i in param[key]:
                trainer += f' --{key} {i}'
                cond = re.findall('--(.*?) ', trainer)
                if cond == keys:
                    trainers.append(trainer)
                    if test is False:
                        os.system(trainer)
                if len(trainers) == dim:
                    with open(isrepeated('../runs/grid_research.txt'), 'w') as f:
                        f.write(f'number of param set: {len(trainers)}\n')
                        f.write('parameters:\n')
                        for l in trainers:
                            f.write(f'{l}\n')
                    # sys.exit()
                    break
                midtrainers.append(trainer)
                trainer = reset
            if len(trainers) == dim:
                break
        # time.sleep(1)
        # print("no break")
        if len(trainers) == dim:
            break


def random_search(trainer, param, limit):
    """
    随机搜索， trainer: 需要运行的文件名， param: 指定的超参数范围，limit: 随机搜索的时长，单位为秒
    示例：
        param = {'lr': [0.01, 0.001, 0.0001]}
        random_search('main.py', param, 6000)
    """
    end = time.time()
    trainer = 'python ' + trainer
    reset = trainer
    trainers = []
    while (time.time() - end) < limit:
        for key in param.keys():
            if isinstance(param[key], list):
                trainer += f' --{key} {random.choice(param[key])}'
            if isinstance(param[key], tuple) and len(param[key]) == 2:
                trainer += f' --{key} {random.uniform(param[key][0], param[key][1])}'
        if trainer not in trainers:
            trainers.append(trainer)
            # time.sleep(1)
            os.system(trainer)
        trainer = reset
    with open(isrepeated('../runs/random_research.txt'), 'w') as f:
        f.write(f'number of param set: {len(trainers)}\n')
        f.write('parameters:\n')
        for l in trainers:
            f.write(f'{l}\n')


# 绘图
def plot(X, Y=None, xlabel=None, ylabel=None, figsize=(10, 5),
         xscale='linear', yscale='linear', legend=None,
         xlim=None, ylim=None, grid=True, lw=1):
    """
    多层多维数据绘制
    示例：
        plot([np.random.random(50), 2 * np.random.random(50)])
    """
    plt.figure(figsize=figsize)

    # Return True if `X` (tensor or list) has 1 axis
    def has_one_axis(X):
        return (hasattr(X, "ndim") and X.ndim == 1 or
                isinstance(X, list) and not hasattr(X[0], "__len__"))
    if has_one_axis(X):
        X = [X]
    if Y is None:
        X, Y = [[]] * len(X), X
    elif has_one_axis(Y):
        Y = [Y]
    if len(X) != len(Y):
        X = X * len(Y)
    for x, y in zip(X, Y):
        if len(x):
            plt.plot(x, y, lw=lw)
        else:
            plt.plot(y, lw=lw)
    set_axes(xlabel, ylabel, xlim, ylim, xscale, yscale, legend, grid)
    plt.tight_layout()
    plt.show()


def set_axes(xlabel, ylabel, xlim, ylim, xscale, yscale, legend, grid):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.xlim(xlim)
    plt.ylim(ylim)
    if legend:
        plt.legend(legend)
    plt.grid(grid)
