



import pickle
import numpy as np
#Text Preprocessing

from keras.models import load_model
from .References import References
from .Preprocess import Preprocessing
from .WordEmbedding import WordEmbedding
from .ModelStruct import ModelStruct

class BinaryInference(References):

      def __init__(self):
          self.preprocess = Preprocessing()
          self.embedding = WordEmbedding()
          self.model_struct = ModelStruct()
          self.load_models()


      def load_models(self):
          """ Loading trained models"""
          with open(self.ROOT_DIR+self.OUTPUT+'model_binaryclass/tokenizerBinaryClassification.pickle', 'rb') as handle:
              self.tokenizer = pickle.load(handle)
          self.model=load_model(self.ROOT_DIR+self.OUTPUT+"model_binaryclass/binaryClassificationModel.h5")

      def predict_complaint(self, text):
          """ Predicting Complain Main"""

          #Preprocess text
          text = self.preprocess.clean_text(text)

          # vectorizing the tweet by the pre-fitted tokenizer instance
          twt = self.embedding.infer_embedding(text, self.tokenizer)

          # Predicting
          complain = self.model.predict(twt,batch_size=1,verbose = 0)[0]

          # Returning Results
          if(np.argmax(complain) == 0):
              print("negative")
              return True
          elif (np.argmax(complain) == 1):
              print("positive")
              return False
