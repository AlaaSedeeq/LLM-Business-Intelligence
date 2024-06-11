# base model for llm
from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self, model_path):
        """init model"""
        model_name = None
        self.model = None
        self.tokenizer = None
        self.is_model_loaded = False
    
    def load_model(self):
        if self.is_model_loaded:
            return
        self._load_model()
        self.is_model_loaded = True

    @abstractmethod
    def _load_model(self):
        """load model"""
        pass
    
    @abstractmethod
    def generate(self, **kwargs):
        """generate"""
        pass
