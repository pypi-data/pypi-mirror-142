from dkist_processing_common.tasks import AssembleMovie
from PIL import ImageDraw

from dkist_processing_visp.models.constants import VispConstants
from dkist_processing_visp.parsers.visp_l0_fits_access import VispL0FitsAccess
from dkist_processing_visp.parsers.visp_l1_fits_access import VispL1FitsAccess


class AssembleVispMovie(AssembleMovie):
    @property
    def constants_model_class(self):
        return VispConstants

    @property
    def fits_parsing_class(self):
        return VispL1FitsAccess

    def write_overlay(self, draw: ImageDraw, fits_obj: VispL0FitsAccess) -> None:
        self.write_line(
            draw=draw,
            text=f"INSTRUMENT: {self.constants.instrument}",
            line=3,
            column="right",
            font=self.font_36,
        )
        self.write_line(
            draw=draw,
            text=f"WAVELENGTH: {fits_obj.wavelength} nm",
            line=2,
            column="right",
            font=self.font_36,
        )
        self.write_line(
            draw=draw,
            text=f"OBS TIME: {fits_obj.time_obs}",
            line=1,
            column="right",
            font=self.font_36,
        )

        if self.constants.correct_for_polarization:
            # The `line` on which an item is drawn is a multiple of the height of that line.
            # The "Q" character is slightly taller than the rest and so n units of the "I   Q"
            # line are taller than n units of the "U   V" line.
            self.write_line(draw=draw, text="I   Q", line=17, column="middle", font=self.font_36)
            self.write_line(draw=draw, text="U   V", line=17, column="middle", font=self.font_36)
