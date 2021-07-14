import tensorflow as tf
import sys
import os

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf


def analyse(imageObj):
    # Read the image_data
    image_data = tf.gfile.FastGFile(imageObj, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                        in tf.io.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.compat.v1.Session() as sess:
        # Alimentez image_data en entrée du graphique et obtenez la première prédiction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})

        # Trier pour afficher les étiquettes de la première prédiction par ordre de confiance


        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        obj = {}
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            obj[human_string] = float(score)

        for key, value in list(obj.items())[:1]:
            return key,value
            #print("we think this is a {0} with a certainty of {1} %".format(key, value * 100))