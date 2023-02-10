class NeuralNetwork:
    def __init__(self, n_layers):
        self.name = "NN"
        self.n_layers = n_layers
        self.model = None
    
    def train(self, dataset):
        self.model = train_model(dataset)

    def compute_accuracy(self, dataset):
        return self.model.compute_acc(dataset)

def train_model(dataset):

