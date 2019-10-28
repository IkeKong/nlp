import paddle.fluid as fluid



class transformer(fluid.dygraph.Layer):
    def __init__(self, name_scope):
        super(transformer, self).__init__(name_scope)

