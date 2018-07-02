# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..specialized import RobustStatisticsSegmenter


def test_RobustStatisticsSegmenter_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        curvatureWeight=dict(argstr='--curvatureWeight %f', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        expectedVolume=dict(argstr='--expectedVolume %f', ),
        intensityHomogeneity=dict(argstr='--intensityHomogeneity %f', ),
        labelImageFileName=dict(
            argstr='%s',
            position=-2,
        ),
        labelValue=dict(argstr='--labelValue %d', ),
        maxRunningTime=dict(argstr='--maxRunningTime %f', ),
        originalImageFileName=dict(
            argstr='%s',
            position=-3,
        ),
        segmentedImageFileName=dict(
            argstr='%s',
            hash_files=False,
            position=-1,
        ),
    )
    inputs = RobustStatisticsSegmenter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_RobustStatisticsSegmenter_outputs():
    output_map = dict(segmentedImageFileName=dict(position=-1, ), )
    outputs = RobustStatisticsSegmenter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
