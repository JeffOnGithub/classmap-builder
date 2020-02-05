"""Minimal example showing how to generate TensorFlow TFRecord file."""
from os import listdir
import tensorflow as tf
#tf.enable_eager_execution()

INPUT_FOLDER = "Z:/Unreal_Datasets/unrealmeadow/Labels_Categorical/"

# All raw values should be converted to a type compatible with tf.Example. Use
# the following functions to do these convertions.
def _bytes_feature(value):
    """Returns a bytes_list from a string / byte."""
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _float_feature(value):
    """Returns a float_list from a float / double."""
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def _int64_feature(value):
    """Returns an int64_list from a bool / enum / int / uint."""
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def write_record(image):
    # Read image raw data, which will be embedded in the record file later.
    image_string = open(INPUT_FOLDER + image, 'rb').read()
    
    # Manually set the label to 0. This should be set according to your situation.
    label = 0
    
    # For each sample there are two features: image raw data, and label. Wrap them in a single dict.
    feature = {
        'label': _int64_feature(label),
        'image_raw': _bytes_feature(image_string),
    }
    
    # Create a `example` from the feature dict.
    tf_example = tf.train.Example(features=tf.train.Features(feature=feature))
  
    # Write the serialized example to a record file.
    with tf.compat.v1.python_io.TFRecordWriter(image + 'images.tfrecords') as writer:
        writer.write(tf_example.SerializeToString())


def read_record(image):
    # Use dataset API to import date directly from TFRecord file.
    raw_image_dataset = tf.data.TFRecordDataset(image + 'images.tfrecords')

    # Create a dictionary describing the features. The key of the dict should be the same with the key in writing function.
    image_feature_description = {
        'label': tf.io.FixedLenFeature([], tf.int64),
        'image_raw': tf.io.FixedLenFeature([], tf.string),
    }
    
    # Define the parse function to extract a single example as a dict.
    def _parse_image_function(example_proto):
        # Parse the input tf.Example proto using the dictionary above.
        return tf.compat.v1.parse_single_example(example_proto, image_feature_description)

    parsed_image_dataset = raw_image_dataset.map(_parse_image_function)
    
    # If there are more than one example, use a for loop to read them out.

    for image_features in parsed_image_dataset:
        image_raw = image_features['image_raw'].numpy()
        label = image_features['label'].numpy()
        
    return image_features

        
if __name__ == "__main__":
    
    list = listdir(INPUT_FOLDER)
    for file in list:
        try:
            write_record(file)
            read_record(file)
        except:
            print(file)