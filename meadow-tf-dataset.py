# coding=utf-8
# Based on TF Datasets

"""Meadow dataset."""

import os

import tensorflow as tf

import tensorflow_datasets.public_api as tfds


#images_path_dir = "Z:/Unreal_Datasets/Meadow1/Images_Categorical/"
#annotations_path_dir = "Z:/Unreal_Datasets/Meadow1/Labels_Categorical/"

_DESCRIPTION = """\
Meadow images from Unreal Engine
"""


_CITATION = """\
@InProceedings{parkhi12a,
  author       = "",
  title        = "",
  booktitle    = "",
  year         = "2019",
}
"""

_NUM_SHARDS = 1

_BASE_URL = ""

_LABEL_CLASSES = [
    "Sky", "Ground", "Blueberry", "Groundwood", "Rock", "Groundplant", "Tree", "Water"
]


class UnrealMeadow(tfds.core.GeneratorBasedBuilder):
  """Meadow Unreal Dataset"""

  VERSION = tfds.core.Version("1.2.0",
                              experiments={tfds.core.Experiment.S3: False})
  SUPPORTED_VERSIONS = [
      tfds.core.Version(
          "1.0.0", ("")),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names=_LABEL_CLASSES),
            "file_name": tfds.features.Text(),
            "segmentation_mask": tfds.features.Image(shape=(None, None, 1))
        }),
        supervised_keys=("image", "label"),
        homepage="",
        citation=_CITATION,
    )

  def _split_generators(self):
    """Returns splits."""
    # Download images and annotations that come in separate archives.
    # Note, that the extension of archives is .tar.gz even though the actual
    # archives format is uncompressed tar.
    #dl_paths = dl_manager.download_and_extract({
    #    "images": tfds.download.Resource(
    #        url=_BASE_URL + "/images.tar.gz",
    #        extract_method=tfds.download.ExtractMethod.TAR),
    #    "annotations": tfds.download.Resource(
    #        url=_BASE_URL + "/annotations.tar.gz",
    #        extract_method=tfds.download.ExtractMethod.TAR)
    #})

    #images_path_dir = os.path.join(dl_paths["images"], "images")
    #annotations_path_dir = os.path.join(dl_paths["annotations"], "annotations")
    images_path_dir = "Z:/Unreal_Datasets/Meadow1/Images_Categorical/"
    annotations_path_dir = "Z:/Unreal_Datasets/Meadow1/Labels_Categorical/"

    # Setup train and test splits
    train_split = tfds.core.SplitGenerator(
        name="train",
        num_shards=_NUM_SHARDS,
        gen_kwargs={
            "images_dir_path": images_path_dir,
            "annotations_dir_path": annotations_path_dir,
            "images_list_file": os.path.join(annotations_path_dir,
                                             "trainval.txt"),
            },
        )
    test_split = tfds.core.SplitGenerator(
        name="test",
        num_shards=_NUM_SHARDS,
        gen_kwargs={
            "images_dir_path": images_path_dir,
            "annotations_dir_path": annotations_path_dir,
            "images_list_file": os.path.join(annotations_path_dir,
                                             "test.txt")
            },
        )

    return [train_split, test_split]

  def _generate_examples(self, images_dir_path, annotations_dir_path,
                         images_list_file):
    with tf.io.gfile.GFile(images_list_file, "r") as images_list:
      for line in images_list:
        image_name = line

        trimaps_dir_path = os.path.join(annotations_dir_path, "trimaps")

        trimap_name = image_name + ".png"
        image_name += ".jpg"

        record = {
            "image": os.path.join(images_dir_path, image_name),
            "file_name": image_name,
            "segmentation_mask": os.path.join(trimaps_dir_path, trimap_name)
        }
        yield image_name, record