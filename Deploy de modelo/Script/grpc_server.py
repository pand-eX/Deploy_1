# Cria o servidor gRPC

# Imports
import os
import grpc
import time
import joblib
from concurrent import futures
from pprint import pprint

# Import dos módulos gerados a partir da compilação do arquivo proto
import iris_pb2
import iris_pb2_grpc

# Variável para definir o número de segundos por dia
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# Cria uma classe carregar o modelo
class IrisPredictor(iris_pb2_grpc.IrisPredictorServicer):
    _model = None

    @classmethod

    # Obtém o modelo de ML
    def get_model(cls):
        if cls._model is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modeloml1.pickle')
            cls._model = joblib.load(path)
        return cls._model

    # Função para fazer as previsões
    def PredictIrisSpecies(self, request):
        model = self.__class__.get_model()
        sepal_length = request.sepal_length
        sepal_width = request.sepal_width
        petal_length = request.petal_length
        petal_width = request.petal_width
        
        # Previsão do modelo
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        
        return iris_pb2.IrisPredictReply(species=result[0])

# Função para servir o modelo na porta 50052
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iris_pb2_grpc.add_IrisPredictorServicer_to_server(IrisPredictor(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

# Execução do programa
if __name__ == '__main__':
    serve()


