
# robster/model.py LinearModel
class LinearModel:
  def __init__(self, feature_count, learning_rate, mean =0, std=0.003):
    import numpy as np
    self.weight = np.random.normal(mean, std, [feature_count, 1])
    self.bias = np.zeros([1])
    self.learning_rate_ = learning_rate
  

  def forward(self, X):
    return np.matmul(X, self.weight) + self.bias, X
  

  def back_postproc(self, G_loss, diff):
    shape = diff.shape

    g_loss_square = np.ones(shape)/np.prod(shape) # Loss 함수를 Square로 미분한 값. 이때는 그냥 샘플 갯수 만큼 나눈 것이므로, 샘플 갯수만큼의  
    g_square_diff = 2 * diff # Square이 diff를 제곱한 값이므로 각 diff에 대해서 미분하면 2가 앞으로 나온다
    g_diff_output = 1 # 각 diff에서 output은 1차항에 계수가 1
    
    return G_loss * g_loss_square * g_square_diff * g_diff_output
  
  def back(self, G_output, X):
    G_w = np.matmul(X.transpose(), G_output)
    G_b = np.sum(G_output, axis = 0)

    self.weight -= self.learning_rate_ * G_w
    self.bias -= self.learning_rate_ * G_b


  def forward_postproc(self, output, y):
    square = np.square(output- y)
    loss = np.mean(square)
    return loss, output- y


  def eval_accuracy(self, output, y):
    return 1 - np.mean(np.abs((output-y)/y))