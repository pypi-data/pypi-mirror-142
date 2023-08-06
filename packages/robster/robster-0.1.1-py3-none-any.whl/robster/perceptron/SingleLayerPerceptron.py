# robster/perceptron.py SingleLayerPerceptron
from robster.model import LinearModel

class SingleLayerPerceptron:
  def __init__(self, epochs, mini_batch, learning_rate = 0.001, report = 1, MODEL = LinearModel):
    self.epochs_ = epochs
    self.mini_batch_ = mini_batch
    self.learning_rate_ = learning_rate
    self.report_=report
    self.MODEL_ = MODEL


  def fit(self, X, y):
    if str(type(X)) == "<class 'pandas.core.frame.DataFrame'>" : X = X.to_numpy()
    if str(type(y)) == "<class 'pandas.core.series.Series'>": y = y.to_numpy().reshape(-1,1)

    steps = int(X.shape[0])//self.mini_batch_ # 미니배치가 가능한 갯수
    self.model = self.MODEL_(int(X.shape[1]), self.learning_rate_)
    # self.model = LinearModel(int(X.shape[1]), self.learning_rate_)

    for epoch in range(self.epochs_):
      losses, accs = [], []
      # 매 epoch 마다 데이터를 섞어서 진행한다.
      shuffle_map = np.arange(X.shape[0])
      for step in range(steps):
        if step == 0: np.random.shuffle(shuffle_map)
        X_train = X[shuffle_map[self.mini_batch_*step : self.mini_batch_ * (step + 1)]]
        y_train = y[shuffle_map[self.mini_batch_*step : self.mini_batch_ * (step + 1)]]
        
        output, aux_nn = self.model.forward(X_train)
        loss, aux_pp = self.model.forward_postproc(output, y_train)
        acc = self.model.eval_accuracy(output, y_train)
        losses.append(loss)
        accs.append(acc)

        #
        G_loss = 1.0
        G_output = self.model.back_postproc(G_loss, aux_pp)
        self.model.back(G_output, aux_nn)

      if self.report_ > 0 and (epoch + 1)%self.report_ ==0:
        print(f"[Epoch {epoch}] loss = {np.mean(losses)} , accuracy = {np.mean(accs)}/{acc}")

    print(f"\n[Final] loss = {np.mean(losses)} , accuracy = {np.mean(accs)}")

  def predict(self, X):
    if str(type(X)) == "<class 'pandas.core.frame.DataFrame'>" : X = X.to_numpy()
    return self.model.forward(X)
  
