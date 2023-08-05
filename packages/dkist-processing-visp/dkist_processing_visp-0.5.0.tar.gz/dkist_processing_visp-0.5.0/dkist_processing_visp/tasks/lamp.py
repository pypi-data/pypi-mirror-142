import logging

import numpy as np
from dkist_processing_common.tasks.mixin.quality import QualityMixin
from dkist_processing_math.arithmetic import subtract_array_from_arrays
from dkist_processing_math.statistics import average_numpy_arrays

from dkist_processing_visp.models.tags import VispTag
from dkist_processing_visp.tasks.mixin.input_frame_loaders import InputFrameLoadersMixin
from dkist_processing_visp.tasks.mixin.intermediate_frame_helpers import (
    IntermediateFrameHelpersMixin,
)
from dkist_processing_visp.tasks.mixin.metadata import MetaDataMixin
from dkist_processing_visp.tasks.visp_base import VispTaskBase


class LampCalibration(
    VispTaskBase, IntermediateFrameHelpersMixin, InputFrameLoadersMixin, MetaDataMixin, QualityMixin
):
    """
    Task class for calculation of the averaged lamp gain frame for a VISP calibration run.

    Parameters
    ----------
    recipe_run_id : int
        id of the recipe run used to identify the workflow run this task is part of
    workflow_name : str
        name of the workflow to which this instance of the task belongs
    workflow_version : str
        version of the workflow to which this instance of the task belongs

    """

    record_provenance = True

    def run(self):
        with self.apm_step(f"Generate lamp gains for {self.constants.num_beams} beams"):
            for exp_time in self.constants.lamp_exposure_times:
                for beam in range(1, self.constants.num_beams + 1):
                    logging.info(f"Load dark for beam {beam}")
                    try:
                        dark_array = self.intermediate_frame_helpers_load_dark_array(
                            beam=beam, exposure_time=exp_time
                        )
                    except StopIteration:
                        raise ValueError(f"No matching dark found for {exp_time = } s")

                    for state_num in range(
                        1, self.constants.num_modstates + 1
                    ):  # modulator states go from 1 to n
                        logging.info(
                            f"Calculating average lamp gain for beam {beam}, modulator state {state_num}"
                        )
                        self.compute_and_write_master_lamp_gain_for_modstate(
                            modstate=state_num,
                            dark_array=dark_array,
                            beam=beam,
                            exp_time=exp_time,
                        )

        with self.apm_step("Finding number of input lamp gain frames."):
            no_of_raw_lamp_frames: int = self.metadata_count_after_beam_split(
                tags=[
                    VispTag.input(),
                    VispTag.frame(),
                    VispTag.task("LAMP_GAIN"),
                ],
            )

        with self.apm_step("Sending lamp gain frame count for quality metric storage"):
            self.quality_store_task_type_counts(
                task_type="LAMP_GAIN", total_frames=no_of_raw_lamp_frames
            )

    def compute_and_write_master_lamp_gain_for_modstate(
        self,
        modstate: int,
        dark_array: np.ndarray,
        beam: int,
        exp_time: float,
    ) -> None:
        """
        Parameters
        ----------
        modstate : the modulator state to calculate the master lamp gain for
        dark_array : the master dark to be subtracted from each lamp gain file
        beam : the number of the beam

        Returns
        -------
        None
        """
        # Get the input lamp gain arrays
        input_lamp_gain_arrays = self.input_frame_loaders_lamp_gain_array_generator(
            beam=beam, modstate=modstate, exposure_time=exp_time
        )
        # Calculate the average of the input gain arrays
        averaged_gain_data = average_numpy_arrays(input_lamp_gain_arrays)
        # subtract dark
        dark_corrected_gain_data = next(subtract_array_from_arrays(averaged_gain_data, dark_array))
        # normalize
        dark_normalized_gain_data = self.normalize_gain(
            dark_corrected_gain_data, pivot=self.parameters.beam_border
        )
        self.intermediate_frame_helpers_write_arrays(
            dark_normalized_gain_data,
            beam=beam,
            task="LAMP_GAIN",
            modstate=modstate,
        )

        # These lines are here to help debugging and can be removed if really necessary
        filename = next(
            self.read(
                tags=[
                    VispTag.intermediate(),
                    VispTag.frame(),
                    VispTag.beam(beam),
                    VispTag.modstate(modstate),
                    VispTag.task("LAMP_GAIN"),
                ]
            )
        )
        logging.info(f"Wrote lamp gain for {beam=} and {modstate=} to {filename}")

    @staticmethod
    def normalize_gain(gain_array: np.ndarray, pivot: int = 1000) -> np.ndarray:
        """
        Normalize gain data

        Parameters
        ----------
        gain_array: Dark corrected gain array for a single modulation state

        Returns
        -------
        gain_array: Dark corrected normalized gain array for a single modulation state

        """
        avg1 = np.mean(gain_array[:pivot, :])
        avg2 = np.mean(gain_array[pivot:, :])
        gain_array[:pivot, :] = gain_array[:pivot, :] / avg1
        gain_array[pivot:, :] = gain_array[pivot:, :] / avg2

        return gain_array
