#%% [markdown]
# ## 結果の可視化
#
# ここのコメントはMarkdown形式で保存できます

#%%
import matplotlib.pyplot as plt
import numpy as np

#%%
# 等間隔の数値リストを生成
x=np.linspace(0,20,100)
# sin値を用いたプロットの表示
plt.plot(x, np.sin(x))
# プロットの表示
plt.show()
# %%
