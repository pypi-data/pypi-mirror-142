from nlu.pipe.pipe_component import SparkNLUComponent

class LabeledDependencyParser(SparkNLUComponent):
    def __init__(self, annotator_class='labeled_dependency_parser', language ='en', component_type='dependency_typed', get_default=True, nlp_ref='',  nlu_ref='', model=None,loaded_from_pretrained_pipe=False,is_licensed=False):


        if model != None : self.model = model
        else:
            if 'dep' in annotator_class:
                from nlu.components.dependency_typeds.labeled_dependency_parser.labeled_dependency_parser import \
                    LabeledDependencyParser
                if get_default : self.model = LabeledDependencyParser.get_default_model()
                else :self.model = LabeledDependencyParser.get_pretrained_model(nlp_ref, language)
        SparkNLUComponent.__init__(self, annotator_class, component_type, nlu_ref, nlp_ref, language,loaded_from_pretrained_pipe , is_licensed)
