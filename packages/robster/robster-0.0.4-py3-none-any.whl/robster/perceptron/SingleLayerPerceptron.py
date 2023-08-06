# robster/perceptron.py SingleLayerPerceptron
from robster.model import LinearModel

class SingleLayerPerceptron:
  def __init__(self, epochs, mini_batch, MODEL = LinearModel,learning_rate = 0.001, report = 1):
    self.epochs = epochs; self.mini_batch = mini_batch, self.learning_rate = learning_rate; self.report=report
    self.repo = ""; self.MODEL = MODEL


  def fit(self, X, y):
    steps = int(X.shape[0])//self.mini_batch # 미니배치가 가능한 갯수
    self.model = self.MODEL(int(X.shape[1]), self.learning_rate)

    for epoch in range(self.epochs):
      losses, accs = [], []
      # 매 epoch 마다 데이터를 섞어서 진행한다.
      shuffle_map = np.arrange(X.shape[0])
      for step in range(steps):
        if step == 0: np.random.shuffle(shuffle_map)
        X_train = X[shuffle_map[self.mini_batch*step : self.mini_batch(step + 1)]]
        y_train = y[shuffle_map[self.mini_batch*step : self.mini_batch(step + 1)]]
        
        output, aux_nn = self.model.forward(X_train)
        loss, aux_pp = self.model.forward_postproc(output, y_train)
        acc = self.model.eval_accuracy(output, y_train)
        losses.append(loss); accs.append(acc)

        #
        G_loss = 1
        G_output = self.model.back_postproc(G_loss, aux_pp)
        self.model.back(G_output, aux_nn)

      if self.report > 0 and (epoch + 1)%self.report ==0:
        print(f"[Epoch {epoch}] loss = {np.mean(losses)} , accuracy = {np.mean(accs)}/{acc}")

    print(f"\n[Final] loss = {np.mean(losses)} , accuracy = {np.mean(accs)}")

  def predict(self, X):
    return self.model.forward(X)
  
