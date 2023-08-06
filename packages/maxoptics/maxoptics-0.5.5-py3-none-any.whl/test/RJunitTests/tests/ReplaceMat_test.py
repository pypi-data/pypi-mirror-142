import unittest
from maxoptics.base import Material, Waveform

from .base import *


class ReplaceMaterialTestCase(unittest.TestCase):
    def test_MaterialDeletion(self):
        Mat1 = Material("rep", {1.55:[2,0]})
        Mat2 = Material("rep", {1.55:[3,0]})
        Base.cl.ensure_materials([Mat1, Mat2], "passive")
        print(Base.cl.user_materials["rep"]["table_data"])
        print(Base.cl.user_materials["rep_1"]["table_data"])

        changed = Base.cl.user_materials["rep_1"]
        changed["name"] = "rep"
        Base.cl.post("change_materials", **changed)

        with self.assertRaises(SystemExit):
            print(Base.cl.user_materials["rep"]["table_data"])

        Base.cl.user_materials.reload()

        self.assertNotIn("rep", Base.cl.user_materials.names)
        self.assertNotIn("rep1", Base.cl.user_materials.names)

    def test_WaveformDeletion(self):
        Wav1 = Waveform("rep", 1.3, 1.6, 2.0, 3.0, 4.1)
        Wav2 = Waveform("rep", 1.31, 1.61, 2.01, 3.01, 4.11)
        Base.cl.ensure_waveforms([Wav1, Wav2])
        print(Base.cl.user_waveforms["rep"])
        print(Base.cl.user_waveforms["rep_1"])

        changed = Base.cl.user_waveforms["rep_1"]
        changed["name"] = "rep"
        Base.cl.post("change_waveforms", **changed)

        with self.assertRaises(SystemExit):
            print(Base.cl.user_waveforms["rep"])

        Base.cl.user_waveforms.reload()

        self.assertNotIn("rep", Base.cl.user_waveforms.names)
        self.assertNotIn("rep1", Base.cl.user_waveforms.names)


if __name__ == '__main__':
    unittest.main()
